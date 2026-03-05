# Orchestration Flow

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
- Output: strict architecture artifact (decision, boundaries, dependency matrix, data ownership, DI plan via `google/wire`, risks, verdict)

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
- If fallback model is used, record reason and impact.
- `done` is allowed only after reviewer stage.
- Every stage output must follow `workflows/AGENT_IO_CONTRACT.md`.
- Every stage must satisfy `workflows/STAGE_CONTRACT.md` before advancing.
- Every full run must be scored with `docs/EVAL_RUBRIC.md`.
- Every full run must be logged with `templates/RUN_LOG_TEMPLATE.md`.
- Orchestration bypass is prohibited under `docs/MANDATORY_ENFORCEMENT_POLICY.md`.
- Single-agent direct completion is invalid unless a documented waiver exists.
