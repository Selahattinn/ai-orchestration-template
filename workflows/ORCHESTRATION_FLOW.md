# Orchestration Flow

## Stage 1: API Scope
- Agent: `api_designer`
- Skill: `skills/api-design/SKILL.md`
- Output: endpoint map and contract draft

## Stage 2: Go Fit Check
- Agent: `go_idiom_guard`
- Skill: `skills/go-idioms/SKILL.md`
- Output: idiomatic Go recommendations and boundary checks

## Stage 3: Architecture
- Agent: `architect`
- Skill: `skills/architecture/SKILL.md`
- Output: component topology and dependency rules

## Stage 4: Testing Plan
- Agent: `test_strategist`
- Skill: `skills/testing-strategy/SKILL.md`
- Output: test matrix and acceptance criteria

## Stage 5: Style Gate
- Agent: `style_guard`
- Skill: `skills/style-guard/SKILL.md`
- Output: style compliance score, violations, and mandatory fixes

## Stage 6: Final Review
- Agent: `reviewer`
- Skill: `skills/code-review/SKILL.md`
- Output: quality gate decision + risks/actions

## Handoff Rules
- Every stage must produce a named artifact for the next stage.
- If fallback model is used, record reason and impact.
- `done` is allowed only after reviewer stage.
- Every stage output must follow `workflows/AGENT_IO_CONTRACT.md`.
- Every full run must be scored with `docs/EVAL_RUBRIC.md`.
- Every full run must be logged with `templates/RUN_LOG_TEMPLATE.md`.
- Orchestration bypass is prohibited under `docs/MANDATORY_ENFORCEMENT_POLICY.md`.
- Single-agent direct completion is invalid unless a documented waiver exists.
