# AI Orchestration Template (Markdown-Only)

This repository is a **non-code template** for AI orchestration experiments.
It is intentionally markdown-first so you can fork it and adapt agent behavior quickly.

## What This Template Contains

- Agent definitions with model settings
- Skill files for specialized tasks (`api-design`, `go-idioms`, etc.)
- Orchestration flow and handoff rules
- Project and agent definition templates
- Task examples and output contracts
- Eval rubric, golden examples, and edge-case references
- Security, cost/latency, skill lifecycle, and run-log standards
- Personal coding style profile and style-gate skill
- `zap` SugaredLogger logging standard with level policy
- Go file hierarchy contract (`cmd/internal/pkg/mocks`)
- Go naming contract for packages, types, methods, files, and mocks
- Testing contract for TDD, test layers, mocks, and CI expectations
- Now/Next/Later backlog for incremental roadmap tracking
- 15-minute onboarding guide for new forks
- Project profile memory (ask once, persist, reuse)
- Architecture style decision guide (hexagonal default, factory as supporting pattern)
- Mandatory enforcement mode for all standards and orchestration
- Stage-based orchestrator tool with artifact gating
- CI run-contract checks for stage order, artifact presence, and waiver validity
- Branch protection baseline for mandatory checks

## Core Principle

No runtime implementation is required here.
The repo is a planning and governance layer for orchestration.

## Quick Start

1. Fill [`templates/PROJECT_BRIEF.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/templates/PROJECT_BRIEF.md)
2. Update [`workflows/AGENT_REGISTRY.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/workflows/AGENT_REGISTRY.md)
3. Customize skill files under `skills/*/SKILL.md`
4. Align contracts in [`workflows/AGENT_IO_CONTRACT.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/workflows/AGENT_IO_CONTRACT.md)
5. Adapt [`workflows/ORCHESTRATION_FLOW.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/workflows/ORCHESTRATION_FLOW.md)
6. Set budgets in [`docs/COST_LATENCY_BUDGET.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/COST_LATENCY_BUDGET.md)
7. Add real use cases in [`examples/TASK_EXAMPLES.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/examples/TASK_EXAMPLES.md)
8. Benchmark outputs against golden refs in [`examples/golden/GOOD_OUTPUT.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/examples/golden/GOOD_OUTPUT.md) and [`examples/golden/BAD_OUTPUT.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/examples/golden/BAD_OUTPUT.md)
9. Apply implementation process in [`docs/IMPLEMENTATION_PROTOCOL.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/IMPLEMENTATION_PROTOCOL.md)
10. Validate acceptance via [`docs/QUALITY_GATE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/QUALITY_GATE.md)
11. Apply style profile from [`docs/CODING_STYLE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/CODING_STYLE.md)
12. Apply logging policy from [`docs/LOGGING_STANDARD.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/LOGGING_STANDARD.md)
13. Apply file hierarchy policy from [`docs/FILE_HIERARCHY.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/FILE_HIERARCHY.md)
14. Apply naming policy from [`docs/NAMING_STANDARD.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/NAMING_STANDARD.md)
15. Apply testing policy from [`docs/TESTING_STANDARD.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/TESTING_STANDARD.md)
16. Review quick setup in [`docs/QUICK_ONBOARDING.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/QUICK_ONBOARDING.md)
17. Bootstrap or update [`docs/PROJECT_PROFILE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/PROJECT_PROFILE.md) via [`docs/BOOTSTRAP_INTERVIEW.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/BOOTSTRAP_INTERVIEW.md)
18. Confirm architecture choice via [`docs/ARCHITECTURE_STYLE_GUIDE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/ARCHITECTURE_STYLE_GUIDE.md)
19. Enforce strict policy via [`docs/MANDATORY_ENFORCEMENT_POLICY.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/MANDATORY_ENFORCEMENT_POLICY.md)
20. Track roadmap items in [`docs/NOW_NEXT_LATER.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/NOW_NEXT_LATER.md)
21. Record each run with [`templates/RUN_LOG_TEMPLATE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/templates/RUN_LOG_TEMPLATE.md)
22. Define stage artifacts in [`workflows/STAGE_CONTRACT.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/workflows/STAGE_CONTRACT.md)
23. Initialize/advance runs with `python3 tools/stage_orchestrator.py`
24. Enforce required checks from [`docs/BRANCH_PROTECTION.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/BRANCH_PROTECTION.md)

## Governance Stack

- Eval rules: [`docs/EVAL_RUBRIC.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/EVAL_RUBRIC.md)
- Model policy: [`docs/MODEL_POLICY.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/MODEL_POLICY.md)
- Security checks: [`docs/SECURITY_POLICY.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/SECURITY_POLICY.md)
- Skill lifecycle: [`docs/SKILL_LIFECYCLE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/SKILL_LIFECYCLE.md)
- Decision log (ADR-style): [`docs/DECISIONS.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/DECISIONS.md)
- Run log format: [`docs/RUN_LOG_STANDARD.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/RUN_LOG_STANDARD.md)
- Implementation process: [`docs/IMPLEMENTATION_PROTOCOL.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/IMPLEMENTATION_PROTOCOL.md)
- Quality gate: [`docs/QUALITY_GATE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/QUALITY_GATE.md)
- Coding style profile: [`docs/CODING_STYLE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/CODING_STYLE.md)
- Logging standard: [`docs/LOGGING_STANDARD.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/LOGGING_STANDARD.md)
- File hierarchy standard: [`docs/FILE_HIERARCHY.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/FILE_HIERARCHY.md)
- Naming standard: [`docs/NAMING_STANDARD.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/NAMING_STANDARD.md)
- Testing standard: [`docs/TESTING_STANDARD.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/TESTING_STANDARD.md)
- Quick onboarding: [`docs/QUICK_ONBOARDING.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/QUICK_ONBOARDING.md)
- Rolling roadmap: [`docs/NOW_NEXT_LATER.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/NOW_NEXT_LATER.md)
- Project profile: [`docs/PROJECT_PROFILE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/PROJECT_PROFILE.md)
- Bootstrap interview: [`docs/BOOTSTRAP_INTERVIEW.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/BOOTSTRAP_INTERVIEW.md)
- Architecture style guide: [`docs/ARCHITECTURE_STYLE_GUIDE.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/ARCHITECTURE_STYLE_GUIDE.md)
- Mandatory enforcement policy: [`docs/MANDATORY_ENFORCEMENT_POLICY.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/MANDATORY_ENFORCEMENT_POLICY.md)
- Stage contract: [`workflows/STAGE_CONTRACT.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/workflows/STAGE_CONTRACT.md)
- Branch protection standard: [`docs/BRANCH_PROTECTION.md`](/Users/selahattinceylan/Documents/personal/projects/ai-orchestration-template/docs/BRANCH_PROTECTION.md)
