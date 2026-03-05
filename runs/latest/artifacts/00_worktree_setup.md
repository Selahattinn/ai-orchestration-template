# Stage 0 Artifact: Worktree Setup

## Summary
Per-stage mandatory worktree mapping is prepared and validated.

## Stage Worktree Map
- worktree_setup -> path: `worktrees/latest/00_worktree_setup`, branch: `codex/latest-worktree-setup`, base: `main`
- api_scope -> path: `worktrees/latest/01_api_scope`, branch: `codex/latest-api-scope`, base: `main`
- go_fit_check -> path: `worktrees/latest/02_go_fit_check`, branch: `codex/latest-go-fit-check`, base: `main`
- architecture -> path: `worktrees/latest/03_architecture`, branch: `codex/latest-architecture`, base: `main`
- testing_plan -> path: `worktrees/latest/04_testing_plan`, branch: `codex/latest-testing-plan`, base: `main`
- style_gate -> path: `worktrees/latest/05_style_gate`, branch: `codex/latest-style-gate`, base: `main`
- final_review -> path: `worktrees/latest/06_final_review`, branch: `codex/latest-final-review`, base: `main`

## Validation Result
- path uniqueness: pass
- branch uniqueness: pass
- naming policy: pass
- verdict: PASS
