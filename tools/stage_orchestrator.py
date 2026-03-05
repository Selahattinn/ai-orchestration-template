#!/usr/bin/env python3
"""Stage-based orchestration helper for markdown-only runs."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REQUIRED_MANIFEST_FIELDS = [
    "run_id",
    "date_utc",
    "rules_mode",
    "orchestration_mode",
    "worktree_mode",
    "worktree_strategy",
    "orchestration_bypassed",
    "waiver",
    "stage_order",
    "stages",
    "run_log_path",
]

WAIVER_FIELDS = [
    "waiver_id",
    "waiver_owner",
    "waiver_reason",
    "waiver_expiry_utc",
    "affected_rules",
]


class ContractError(Exception):
    pass


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_utc(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timezone offset is required")
    return parsed.astimezone(timezone.utc)


def slugify(value: str) -> str:
    chars: list[str] = []
    prev_dash = False
    for ch in value.strip().lower():
        if ch.isalnum():
            chars.append(ch)
            prev_dash = False
            continue
        if not prev_dash:
            chars.append("-")
            prev_dash = True
    slug = "".join(chars).strip("-")
    return slug or "run"


def parse_stage_contract(contract_path: Path) -> list[dict[str, str]]:
    if not contract_path.exists():
        raise ContractError(f"missing stage contract: {contract_path}")

    stages: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw in contract_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("- stage_id:"):
            if current is not None:
                if "artifact" not in current:
                    raise ContractError(f"stage missing artifact: {current['stage_id']}")
                stages.append(current)
            current = {"stage_id": line.split(":", 1)[1].strip()}
            continue

        if current is None:
            continue

        if line.startswith("artifact:"):
            current["artifact"] = line.split(":", 1)[1].strip()

    if current is not None:
        if "artifact" not in current:
            raise ContractError(f"stage missing artifact: {current['stage_id']}")
        stages.append(current)

    if not stages:
        raise ContractError("no stages parsed from stage contract")

    return stages


def default_manifest(run_id: str, stages: list[dict[str, str]]) -> dict[str, Any]:
    safe_run_id = slugify(run_id)
    return {
        "run_id": run_id,
        "date_utc": utc_now_iso(),
        "rules_mode": "mandatory_all",
        "orchestration_mode": "mandatory",
        "worktree_mode": "mandatory",
        "worktree_strategy": "per_stage",
        "orchestration_bypassed": False,
        "waiver": {
            "waiver_id": "",
            "waiver_owner": "",
            "waiver_reason": "",
            "waiver_expiry_utc": "",
            "affected_rules": [],
        },
        "stage_order": [stage["stage_id"] for stage in stages],
        "stages": [
            {
                "stage_id": stage["stage_id"],
                "status": "pending",
                "artifact": stage["artifact"],
                "worktree_path": f"worktrees/{safe_run_id}/{idx:02d}_{stage['stage_id']}",
                "worktree_branch": (
                    f"codex/{safe_run_id}-{slugify(stage['stage_id'])}"
                ),
                "completed_at_utc": "",
            }
            for idx, stage in enumerate(stages)
        ],
        "run_log_path": "run_log.md",
    }


def load_manifest(manifest_path: Path) -> dict[str, Any]:
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def save_manifest(manifest_path: Path, manifest: dict[str, Any]) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def resolve_under(base_dir: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = base_dir / path
    return path.resolve()


def non_empty_file(path: Path) -> bool:
    return path.exists() and path.is_file() and path.stat().st_size > 0


def display_path(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def is_within_dir(path: Path, base_dir: Path) -> bool:
    try:
        path.relative_to(base_dir)
        return True
    except ValueError:
        return False


def validate_manifest(
    *,
    repo_root: Path,
    run_dir: Path,
    manifest: dict[str, Any],
    stages: list[dict[str, str]],
    require_complete: bool,
) -> list[str]:
    errors: list[str] = []

    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest:
            errors.append(f"manifest missing field: {field}")

    if manifest.get("rules_mode") != "mandatory_all":
        errors.append("rules_mode must be mandatory_all")

    if manifest.get("orchestration_mode") != "mandatory":
        errors.append("orchestration_mode must be mandatory")

    if manifest.get("worktree_mode") != "mandatory":
        errors.append("worktree_mode must be mandatory")

    if manifest.get("worktree_strategy") != "per_stage":
        errors.append("worktree_strategy must be per_stage")

    expected_order = [stage["stage_id"] for stage in stages]
    if manifest.get("stage_order") != expected_order:
        errors.append("stage_order does not match stage contract")

    stage_records = manifest.get("stages")
    if not isinstance(stage_records, list):
        errors.append("stages must be a list")
        stage_records = []

    if len(stage_records) != len(stages):
        errors.append("stages length does not match stage contract")

    seen_worktree_paths: set[str] = set()
    seen_worktree_branches: set[str] = set()
    seen_pending = False
    for idx, stage in enumerate(stages):
        if idx >= len(stage_records):
            continue

        record = stage_records[idx]
        if not isinstance(record, dict):
            errors.append(f"stage position {idx+1} record must be an object")
            continue

        if record.get("stage_id") != stage["stage_id"]:
            errors.append(f"stage position {idx+1} expected {stage['stage_id']}")
            continue

        expected_artifact = stage["artifact"]
        if record.get("artifact") != expected_artifact:
            errors.append(f"stage {stage['stage_id']} artifact must be {expected_artifact}")

        worktree_path_raw = record.get("worktree_path")
        if not isinstance(worktree_path_raw, str) or not worktree_path_raw.strip():
            errors.append(f"stage {stage['stage_id']} missing worktree_path")
            worktree_path_raw = ""
        else:
            if not worktree_path_raw.startswith("worktrees/"):
                errors.append(
                    f"stage {stage['stage_id']} worktree_path must start with worktrees/"
                )
            resolved_worktree = resolve_under(repo_root, worktree_path_raw)
            if not is_within_dir(resolved_worktree, repo_root):
                errors.append(
                    f"stage {stage['stage_id']} worktree_path escapes repo: {worktree_path_raw}"
                )
            else:
                normalized_worktree_path = resolved_worktree.relative_to(repo_root).as_posix()
                if not normalized_worktree_path.startswith("worktrees/"):
                    errors.append(
                        "stage "
                        f"{stage['stage_id']} worktree_path must resolve under worktrees/: "
                        f"{normalized_worktree_path}"
                    )
                if normalized_worktree_path in seen_worktree_paths:
                    errors.append(f"duplicate worktree_path: {normalized_worktree_path}")
                seen_worktree_paths.add(normalized_worktree_path)

        worktree_branch = record.get("worktree_branch")
        if not isinstance(worktree_branch, str) or not worktree_branch.strip():
            errors.append(f"stage {stage['stage_id']} missing worktree_branch")
            worktree_branch = ""
        else:
            if worktree_branch in seen_worktree_branches:
                errors.append(f"duplicate worktree_branch: {worktree_branch}")
            seen_worktree_branches.add(worktree_branch)

            if not worktree_branch.startswith("codex/"):
                errors.append(
                    f"stage {stage['stage_id']} worktree_branch must start with codex/"
                )

        status = record.get("status")
        if status not in {"pending", "completed"}:
            errors.append(f"stage {stage['stage_id']} has invalid status: {status}")
            continue

        if seen_pending and status == "completed":
            errors.append(
                f"stage order violation: {stage['stage_id']} is completed after a pending stage"
            )
        if status == "pending":
            seen_pending = True

        if require_complete and status != "completed":
            errors.append(f"stage {stage['stage_id']} status must be completed")

        artifact_path = resolve_under(run_dir, expected_artifact)
        if not is_within_dir(artifact_path, run_dir):
            errors.append(f"stage artifact path escapes run dir: {expected_artifact}")
        elif status == "completed" and not non_empty_file(artifact_path):
            errors.append(
                f"stage artifact missing or empty: {display_path(artifact_path, repo_root)}"
            )

    run_log_path = manifest.get("run_log_path", "")
    if not isinstance(run_log_path, str) or not run_log_path.strip():
        errors.append("run_log_path must be a non-empty string")
    else:
        resolved_log = resolve_under(run_dir, run_log_path)
        if not is_within_dir(resolved_log, run_dir):
            errors.append("run_log_path must stay under the run directory")
        elif require_complete and not non_empty_file(resolved_log):
            errors.append(f"run log missing or empty: {display_path(resolved_log, repo_root)}")

    bypassed = bool(manifest.get("orchestration_bypassed"))
    waiver = manifest.get("waiver", {})
    if not isinstance(waiver, dict):
        errors.append("waiver must be an object")
        waiver = {}

    if bypassed:
        for field in WAIVER_FIELDS:
            value = waiver.get(field)
            if field == "affected_rules":
                if not isinstance(value, list) or not value:
                    errors.append("waiver.affected_rules must be a non-empty list when bypassed")
            elif not isinstance(value, str) or not value.strip():
                errors.append(f"waiver.{field} is required when bypassed")

        expiry = waiver.get("waiver_expiry_utc", "")
        if isinstance(expiry, str) and expiry.strip():
            try:
                expiry_dt = parse_utc(expiry)
                if expiry_dt <= datetime.now(timezone.utc):
                    errors.append("waiver_expiry_utc must be in the future")
            except ValueError:
                errors.append("waiver_expiry_utc must be ISO-8601 UTC timestamp")

    return errors


def next_pending_stage(manifest: dict[str, Any]) -> dict[str, Any] | None:
    for stage in manifest.get("stages", []):
        if stage.get("status") != "completed":
            return stage
    return None


def cmd_init(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    contract_path = repo_root / args.contract
    stages = parse_stage_contract(contract_path)

    run_dir = (repo_root / args.run_dir).resolve()
    manifest_path = run_dir / "manifest.json"

    if manifest_path.exists() and not args.force:
        print(f"error: manifest already exists: {manifest_path}", file=sys.stderr)
        return 1

    run_id = args.run_id or run_dir.name
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "artifacts").mkdir(parents=True, exist_ok=True)

    manifest = default_manifest(run_id, stages)
    save_manifest(manifest_path, manifest)

    print(f"initialized run manifest: {display_path(manifest_path, repo_root)}")
    return 0


def cmd_complete(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    run_dir = (repo_root / args.run_dir).resolve()
    manifest_path = run_dir / "manifest.json"

    manifest = load_manifest(manifest_path)
    pending = next_pending_stage(manifest)
    if pending is None:
        print("all stages already completed", file=sys.stderr)
        return 1

    if args.stage_id != pending.get("stage_id"):
        print(
            f"error: stage order violation. expected {pending.get('stage_id')}, got {args.stage_id}",
            file=sys.stderr,
        )
        return 1

    artifact = args.artifact or pending.get("artifact", "")
    artifact_path = resolve_under(run_dir, artifact)
    if not non_empty_file(artifact_path):
        print(f"error: artifact missing or empty: {artifact_path}", file=sys.stderr)
        return 1

    pending["status"] = "completed"
    pending["artifact"] = artifact_path.relative_to(run_dir).as_posix()
    pending["completed_at_utc"] = utc_now_iso()
    save_manifest(manifest_path, manifest)

    print(f"completed stage: {args.stage_id}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    run_dir = (repo_root / args.run_dir).resolve()
    manifest = load_manifest(run_dir / "manifest.json")

    print(f"run_id: {manifest.get('run_id')}")
    print(f"rules_mode: {manifest.get('rules_mode')}")
    print(f"orchestration_mode: {manifest.get('orchestration_mode')}")
    print(f"worktree_mode: {manifest.get('worktree_mode')}")
    print(f"worktree_strategy: {manifest.get('worktree_strategy')}")
    print(f"orchestration_bypassed: {manifest.get('orchestration_bypassed')}")
    print("stages:")
    for stage in manifest.get("stages", []):
        print(
            f"- {stage.get('stage_id')}: {stage.get('status')} "
            f"({stage.get('artifact')}) "
            f"[{stage.get('worktree_path')} @ {stage.get('worktree_branch')}]"
        )

    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    run_dir = (repo_root / args.run_dir).resolve()

    contract_path = repo_root / args.contract
    stages = parse_stage_contract(contract_path)
    manifest = load_manifest(run_dir / "manifest.json")

    errors = validate_manifest(
        repo_root=repo_root,
        run_dir=run_dir,
        manifest=manifest,
        stages=stages,
        require_complete=args.require_complete,
    )

    if errors:
        print("run validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("run validation passed")
    return 0


def cmd_finish(args: argparse.Namespace) -> int:
    args.require_complete = True
    code = cmd_validate(args)
    if code != 0:
        return code

    print("run is complete and valid")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Stage orchestration helper")
    parser.set_defaults(func=None)

    parser.add_argument("--repo-root", default=".", help="Repository root path")

    sub = parser.add_subparsers(dest="command")

    init_cmd = sub.add_parser("init", help="Initialize a run manifest")
    init_cmd.add_argument("--run-dir", required=True, help="Run directory path")
    init_cmd.add_argument("--run-id", default="", help="Run identifier")
    init_cmd.add_argument(
        "--contract",
        default="workflows/STAGE_CONTRACT.md",
        help="Stage contract path",
    )
    init_cmd.add_argument("--force", action="store_true", help="Overwrite existing manifest")
    init_cmd.set_defaults(func=cmd_init)

    complete_cmd = sub.add_parser("complete", help="Complete the next stage")
    complete_cmd.add_argument("--run-dir", required=True, help="Run directory path")
    complete_cmd.add_argument("--stage-id", required=True, help="Stage identifier")
    complete_cmd.add_argument("--artifact", default="", help="Artifact path (optional)")
    complete_cmd.set_defaults(func=cmd_complete)

    status_cmd = sub.add_parser("status", help="Show run status")
    status_cmd.add_argument("--run-dir", required=True, help="Run directory path")
    status_cmd.set_defaults(func=cmd_status)

    validate_cmd = sub.add_parser("validate", help="Validate run manifest and artifacts")
    validate_cmd.add_argument("--run-dir", required=True, help="Run directory path")
    validate_cmd.add_argument(
        "--contract",
        default="workflows/STAGE_CONTRACT.md",
        help="Stage contract path",
    )
    validate_cmd.add_argument(
        "--require-complete",
        action="store_true",
        help="Require all stages and run log to be complete",
    )
    validate_cmd.set_defaults(func=cmd_validate)

    finish_cmd = sub.add_parser("finish", help="Require a fully complete and valid run")
    finish_cmd.add_argument("--run-dir", required=True, help="Run directory path")
    finish_cmd.add_argument(
        "--contract",
        default="workflows/STAGE_CONTRACT.md",
        help="Stage contract path",
    )
    finish_cmd.set_defaults(func=cmd_finish)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.func is None:
        parser.print_help()
        return 1

    try:
        return args.func(args)
    except (ContractError, FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
