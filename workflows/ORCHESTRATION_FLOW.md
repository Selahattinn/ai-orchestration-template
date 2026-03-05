# Orchestration Flow

## Stage 0: Worktree Setup (`worktree_setup`)
- Agent: `worktree_manager`
- Skill: `skills/worktree-setup/SKILL.md`
- Output: stage-to-worktree mapping, branch plan, and setup validation

## Stage 1: API Scope (`api_scope`)
- Agent: `api_designer`
- Skill: `skills/api-design/SKILL.md`
- Output: endpoint map and contract draft

## Stage 2: Go Fit Check (`go_fit_check`)
- Agent: `go_idiom_guard`
- Skill: `skills/go-idioms/SKILL.md`
- Output: idiomatic Go recommendations and boundary checks

## Stage 3: Architecture (`architecture`)
- Agent: `architect`
- Skill: `skills/architecture/SKILL.md`
- Output: routed architecture artifact (selected pattern, pattern-specific report, dependency matrix, data ownership, DI plan via `google/wire`, risks, verdict)

## Stage 4: Testing Plan (`testing_plan`)
- Agent: `test_strategist`
- Skill: `skills/testing-strategy/SKILL.md`
- Output: test matrix and acceptance criteria

## Stage 5: Style Gate (`style_gate`)
- Agent: `style_guard`
- Skill: `skills/style-guard/SKILL.md`
- Output: style compliance score, violations, and mandatory fixes

## Stage 6: Final Review (`final_review`)
- Agent: `reviewer`
- Skill: `skills/code-review/SKILL.md`
- Output: quality gate decision + risks/actions

## Handoff Rules
- Every stage must produce a named artifact for the next stage.
- Every stage must run in its dedicated git worktree from the Stage 0 mapping.
- If fallback model is used, record reason and impact.
- `done` is allowed only after reviewer stage.
- Every stage output must follow `workflows/AGENT_IO_CONTRACT.md`.
- Every stage must satisfy `workflows/STAGE_CONTRACT.md` before advancing.
- Architecture stage must resolve pattern from `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`.
- If selected pattern is `hexagonal`, architecture output must satisfy `docs/HEXAGONAL_BOUNDARY_STANDARD.md`.
- Every full run must be scored with `docs/EVAL_RUBRIC.md`.
- Every full run must be logged with `templates/RUN_LOG_TEMPLATE.md`.
- Orchestration bypass is prohibited under `docs/MANDATORY_ENFORCEMENT_POLICY.md`.
- Single-agent direct completion is invalid unless a documented waiver exists.
