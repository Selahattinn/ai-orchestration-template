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
