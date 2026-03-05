---
name: worktree-setup
description: Prepare and validate mandatory per-stage git worktree assignments for orchestration runs. Use when initializing or validating a run before stage execution.
---

# Worktree Setup Skill

Prepare a mandatory per-stage worktree plan and block execution on violations.

## Inputs

- `run_id`
- `stage_contract`
- `base_branch`
- `existing_worktree_list` (if available)

## Procedure

1. Parse ordered stages from `workflows/STAGE_CONTRACT.md`.
2. Build a one-to-one mapping between each stage and one worktree path.
3. Build a one-to-one mapping between each stage and one worktree branch.
4. Validate uniqueness for all worktree paths and branches.
5. Verify naming policy from `docs/WORKTREE_STANDARD.md`.
6. Produce `worktree_setup` artifact for handoff.

## Output Contract

Return these sections in the stage artifact:
- `summary`
- `stage_worktree_map`
- `branch_plan`
- `base_branch_plan`
- `validation_result`
- `risks`
- `verdict: PASS | REVISE | BLOCK`

## Block Rules

Return `BLOCK` when any condition occurs:
- A stage has no dedicated worktree path.
- A stage has no dedicated worktree branch.
- Path or branch collisions exist.
- Naming does not follow `docs/WORKTREE_STANDARD.md`.
