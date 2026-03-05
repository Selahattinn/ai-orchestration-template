#!/usr/bin/env python3
"""CI entrypoint for validating orchestration run outputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import stage_orchestrator as orchestrator  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate run output contract")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--run-dir", default="runs/latest", help="Run directory")
    parser.add_argument(
        "--contract",
        default="workflows/STAGE_CONTRACT.md",
        help="Stage contract path",
    )
    parser.add_argument(
        "--allow-incomplete",
        action="store_true",
        help="Allow incomplete stage runs",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    run_dir = (repo_root / args.run_dir).resolve()

    contract_path = repo_root / args.contract
    manifest_path = run_dir / "manifest.json"

    try:
        stages = orchestrator.parse_stage_contract(contract_path)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        print(f"run validation failed: {exc}", file=sys.stderr)
        return 1
    except (orchestrator.ContractError, json.JSONDecodeError) as exc:
        print(f"run validation failed: {exc}", file=sys.stderr)
        return 1

    errors = orchestrator.validate_manifest(
        repo_root=repo_root,
        run_dir=run_dir,
        manifest=manifest,
        stages=stages,
        require_complete=not args.allow_incomplete,
    )

    if errors:
        print("run validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("run validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
