# Worktree Standard

Mandatory git worktree policy for all orchestrated runs.

## Mandatory Rules

- Every run must use `worktree_mode: mandatory`.
- Worktree strategy must be `per_stage`.
- Every stage must execute in its own dedicated git worktree.
- A stage cannot start unless its worktree is prepared and assigned.
- Worktree branch naming must follow `codex/<normalized-run-id>-<normalized-stage-id>`.
- Worktree path naming must follow `worktrees/<normalized-run-id>/<order>_<stage-id>`.
- Reusing one worktree for multiple stages is prohibited.

`normalized-*` means lowercase slug format (`[a-z0-9-]`) used by `tools/stage_orchestrator.py`.

## Stage 0 Requirement

- `worktree_setup` is required as the first stage in `workflows/STAGE_CONTRACT.md`.
- `worktree_setup` must generate a non-empty artifact that includes:
- planned stage-to-worktree mapping
- worktree branch list
- base branch for each worktree

## Validation Rules

- `tools/stage_orchestrator.py` must fail validation if worktree mode/strategy is missing or invalid.
- Validation must fail when any stage record has empty `worktree_path` or `worktree_branch`.
- Validation must fail when stage worktree paths are duplicated.
- Validation must fail when stage worktree branches are duplicated.

## Block Conditions

Return `BLOCK` when any condition occurs:
- Worktree mode is not mandatory.
- Stage worktree mapping is missing or ambiguous.
- Stage execution is reported without a dedicated worktree assignment.
- Orchestration attempts to proceed without `worktree_setup` artifact.

## Done Criteria

- Mandatory worktree rules are explicit and unambiguous.
- Stage 0 worktree requirement is defined and enforceable.
- Validation behavior is aligned with orchestration tooling and contracts.
