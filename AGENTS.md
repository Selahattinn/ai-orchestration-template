# AGENTS

This is a markdown-only AI orchestration template.
It defines roles, models, skills, and handoffs without shipping runtime code.

## Required Files

- `workflows/AGENT_REGISTRY.md`
- `workflows/AGENT_IO_CONTRACT.md`
- `workflows/ORCHESTRATION_FLOW.md`
- `docs/MODEL_POLICY.md`
- `docs/COST_LATENCY_BUDGET.md`
- `docs/EVAL_RUBRIC.md`
- `docs/SECURITY_POLICY.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/RUN_LOG_STANDARD.md`
- `docs/DECISIONS.md`
- `docs/IMPLEMENTATION_PROTOCOL.md`
- `docs/QUALITY_GATE.md`
- `docs/CODING_STYLE.md`
- `skills/*/SKILL.md`
- `examples/TASK_EXAMPLES.md`
- `examples/golden/*`
- `examples/style/*`

## Agent Record Schema

Each agent entry must include:
- `name`
- `purpose`
- `primary_model`
- `fallback_model`
- `temperature`
- `max_output_tokens`
- `latency_target`
- `cost_tier`
- `skill_file`
- `io_contract_ref`
- `handoff_to`
- `done_criteria`

## Default Skill Set

- API Design
- Go Idioms
- Architecture
- Testing Strategy
- Style Guard
- Code Review

## PR Description Rules

- Default language is English unless user explicitly requests another language.
- Use technical narrative style, not short generic bullet dumps.
- Target length is 180-300 words for medium-size changes.
- Required sections:
1. Context
2. What Changed
3. Why It Matters
4. Risks and Trade-offs
5. Breaking Changes
6. Migration Notes
7. Validation
8. Follow-ups
- Before opening or updating a PR, generate draft body and wait for user approval.
