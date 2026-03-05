# AGENTS

This is a markdown-only AI orchestration template.
It defines roles, models, skills, and handoffs without shipping runtime code.

## Required Files

- `workflows/AGENT_REGISTRY.md`
- `workflows/AGENT_IO_CONTRACT.md`
- `workflows/ORCHESTRATION_FLOW.md`
- `workflows/STAGE_CONTRACT.md`
- `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`
- `docs/MODEL_POLICY.md`
- `docs/COST_LATENCY_BUDGET.md`
- `docs/EVAL_RUBRIC.md`
- `docs/SECURITY_POLICY.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/RUN_LOG_STANDARD.md`
- `docs/DECISIONS.md`
- `docs/IMPLEMENTATION_PROTOCOL.md`
- `docs/QUALITY_GATE.md`
- `docs/NOW_NEXT_LATER.md`
- `docs/QUICK_ONBOARDING.md`
- `docs/PROJECT_PROFILE.md`
- `docs/BOOTSTRAP_INTERVIEW.md`
- `docs/ARCHITECTURE_STYLE_GUIDE.md`
- `docs/HEXAGONAL_BOUNDARY_STANDARD.md`
- `docs/MANDATORY_ENFORCEMENT_POLICY.md`
- `docs/BRANCH_PROTECTION.md`
- `docs/WORKTREE_STANDARD.md`
- `docs/CODING_STYLE.md`
- `docs/LOGGING_STANDARD.md`
- `docs/FILE_HIERARCHY.md`
- `docs/NAMING_STANDARD.md`
- `docs/TESTING_STANDARD.md`
- `skills/worktree-setup/SKILL.md`
- `skills/*/SKILL.md`
- `examples/TASK_EXAMPLES.md`
- `examples/golden/*`
- `examples/style/*`
- `examples/structure/*`
- `examples/naming/*`
- `examples/testing/*`
- `runs/latest/manifest.json`
- `tools/stage_orchestrator.py`
- `tools/validate_run.py`

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
- Worktree Setup
- Architecture Router
- Architecture Hexagonal
- Architecture Clean Layered
- Architecture Service Layered
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
- `Validation` must never be empty or placeholder text.
- Before opening or updating a PR, generate draft body and wait for user approval.
- When creating/updating PR bodies via CLI, use `--body-file` only (do not use inline `--body`).
- CI enforcement is defined in `.github/workflows/pr-body-contract.yml`.
- Docs contract CI enforcement is defined in `.github/workflows/docs-contract.yml`.
- Run contract CI enforcement is defined in `.github/workflows/orchestration-contract.yml`.

## Profile-Driven Startup

- Repository language is always English.
- On first run, if `docs/PROJECT_PROFILE.md` is incomplete, run `docs/BOOTSTRAP_INTERVIEW.md`.
- Persist answers in `docs/PROJECT_PROFILE.md` and do not re-ask the same questions.
- In later runs, ask only for missing fields or explicit user-requested changes.

## Mandatory Mode

- Rules mode is `mandatory_all` (no optional standards).
- Agent orchestration mode is `mandatory` (no single-agent bypass).
- Worktree mode is `mandatory` with `per_stage` strategy.
- All agents must execute in dedicated stage worktrees per `docs/WORKTREE_STANDARD.md`.
- Any exception requires a documented waiver per `docs/MANDATORY_ENFORCEMENT_POLICY.md`.
