# Operating Guide

## How to Fork and Reuse

1. Fork this repository.
2. Complete or confirm `docs/PROJECT_PROFILE.md` (use `docs/BOOTSTRAP_INTERVIEW.md` when needed).
3. Confirm architecture style in `docs/ARCHITECTURE_STYLE_GUIDE.md`.
4. Rename agents or keep defaults in `workflows/AGENT_REGISTRY.md`.
5. Update model choices based on your budget in `docs/MODEL_POLICY.md`.
6. Align stage budgets in `docs/COST_LATENCY_BUDGET.md`.
7. Customize `skills/*/SKILL.md` for your domain.
8. Define agent handoff contracts in `workflows/AGENT_IO_CONTRACT.md`.
9. Add project-specific scenarios to `examples/TASK_EXAMPLES.md`.
10. Validate with golden references under `examples/golden/`.
11. Configure personal style in `docs/CODING_STYLE.md`.
12. Configure logging policy in `docs/LOGGING_STANDARD.md`.
13. Configure project layout policy in `docs/FILE_HIERARCHY.md`.
14. Configure naming policy in `docs/NAMING_STANDARD.md`.
15. Configure testing policy in `docs/TESTING_STANDARD.md`.
16. Follow the rapid checklist in `docs/QUICK_ONBOARDING.md`.
17. Maintain active roadmap items in `docs/NOW_NEXT_LATER.md`.
18. Save each run using `templates/RUN_LOG_TEMPLATE.md`.

## Governance Rule

Any change to agent behavior must update both:
- agent entry in `workflows/AGENT_REGISTRY.md`
- referenced skill file in `skills/*/SKILL.md`

## Required Change Companions

When agent behavior changes, include at least one of:
- decision update in `docs/DECISIONS.md`
- eval criteria impact in `docs/EVAL_RUBRIC.md`
- security impact note in `docs/SECURITY_POLICY.md`
