# Operating Guide

## How to Fork and Reuse

1. Fork this repository.
2. Rename agents or keep defaults in `workflows/AGENT_REGISTRY.md`.
3. Update model choices based on your budget in `docs/MODEL_POLICY.md`.
4. Align stage budgets in `docs/COST_LATENCY_BUDGET.md`.
5. Customize `skills/*/SKILL.md` for your domain.
6. Define agent handoff contracts in `workflows/AGENT_IO_CONTRACT.md`.
7. Add project-specific scenarios to `examples/TASK_EXAMPLES.md`.
8. Validate with golden references under `examples/golden/`.
9. Configure personal style in `docs/CODING_STYLE.md`.
10. Configure logging policy in `docs/LOGGING_STANDARD.md`.
11. Configure project layout policy in `docs/FILE_HIERARCHY.md`.
12. Save each run using `templates/RUN_LOG_TEMPLATE.md`.

## Governance Rule

Any change to agent behavior must update both:
- agent entry in `workflows/AGENT_REGISTRY.md`
- referenced skill file in `skills/*/SKILL.md`

## Required Change Companions

When agent behavior changes, include at least one of:
- decision update in `docs/DECISIONS.md`
- eval criteria impact in `docs/EVAL_RUBRIC.md`
- security impact note in `docs/SECURITY_POLICY.md`
