# Quick Onboarding (15 Minutes)

Use this guide to bootstrap a new fork quickly.

## Minute 0-3: Fork and Baseline

1. Fork repository.
2. Confirm required docs are present.
3. Read `README.md` and `AGENTS.md` once end-to-end.

## Minute 3-7: Project Configuration

1. Complete `docs/PROJECT_PROFILE.md` (run `docs/BOOTSTRAP_INTERVIEW.md` if incomplete).
2. Fill `templates/PROJECT_BRIEF.md`.
3. Update `workflows/AGENT_REGISTRY.md` for your agents/models.
4. Confirm `workflows/ORCHESTRATION_FLOW.md` handoff order.

## Minute 7-11: Standards Alignment

1. Tailor `docs/CODING_STYLE.md`.
2. Tailor `docs/LOGGING_STANDARD.md`.
3. Tailor `docs/FILE_HIERARCHY.md`, `docs/NAMING_STANDARD.md`, and `docs/TESTING_STANDARD.md`.
4. Confirm architecture choice in `docs/ARCHITECTURE_STYLE_GUIDE.md`.

## Minute 11-13: Example Calibration

1. Add one domain scenario to `examples/TASK_EXAMPLES.md`.
2. Compare expected outputs against `examples/golden/*` and style/testing examples.

## Minute 13-15: Governance Check

1. Ensure PR template is in place (`.github/pull_request_template.md`).
2. Ensure `Breaking Changes`, `Migration Notes`, and `Validation` are non-empty in PRs.
3. Add first follow-up items to `docs/NOW_NEXT_LATER.md`.

## Done Criteria

- Project brief, agent registry, and flow are customized.
- Project profile is active and reusable for future runs.
- Standards docs reflect project constraints.
- At least one scenario and one run-log entry can be produced.
