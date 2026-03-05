# Operating Guide

## How to Fork and Reuse

1. Fork this repository.
2. Complete or confirm `docs/PROJECT_PROFILE.md` (use `docs/BOOTSTRAP_INTERVIEW.md` when needed).
3. Confirm architecture style in `docs/ARCHITECTURE_STYLE_GUIDE.md`.
4. Confirm strict policy in `docs/MANDATORY_ENFORCEMENT_POLICY.md`.
5. Rename agents or keep defaults in `workflows/AGENT_REGISTRY.md`.
6. Update model choices based on your budget in `docs/MODEL_POLICY.md`.
7. Align stage budgets in `docs/COST_LATENCY_BUDGET.md`.
8. Customize `skills/*/SKILL.md` for your domain.
9. Define agent handoff contracts in `workflows/AGENT_IO_CONTRACT.md`.
10. Keep stage definitions aligned in `workflows/STAGE_CONTRACT.md`.
11. Initialize run manifest with `python3 tools/stage_orchestrator.py init --run-dir runs/<run_id>`.
12. Complete stages in order using `python3 tools/stage_orchestrator.py complete`.
13. Add project-specific scenarios to `examples/TASK_EXAMPLES.md`.
14. Validate with golden references under `examples/golden/`.
15. Configure personal style in `docs/CODING_STYLE.md`.
16. Configure logging policy in `docs/LOGGING_STANDARD.md`.
17. Configure project layout policy in `docs/FILE_HIERARCHY.md`.
18. Configure naming policy in `docs/NAMING_STANDARD.md`.
19. Configure testing policy in `docs/TESTING_STANDARD.md`.
20. Follow the rapid checklist in `docs/QUICK_ONBOARDING.md`.
21. Maintain active roadmap items in `docs/NOW_NEXT_LATER.md`.
22. Save each run using `templates/RUN_LOG_TEMPLATE.md`.
23. Enforce branch rules from `docs/BRANCH_PROTECTION.md`.

## Governance Rule

Any change to agent behavior must update both:
- agent entry in `workflows/AGENT_REGISTRY.md`
- referenced skill file in `skills/*/SKILL.md`

## Required Change Companions

When agent behavior changes, include at least one of:
- decision update in `docs/DECISIONS.md`
- eval criteria impact in `docs/EVAL_RUBRIC.md`
- security impact note in `docs/SECURITY_POLICY.md`
