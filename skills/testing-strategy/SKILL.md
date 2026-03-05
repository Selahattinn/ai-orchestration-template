# Testing Strategy

## Metadata
- status: active
- owner: qa-engineering
- review_cadence: monthly

## Purpose
Define a practical, risk-based testing plan.

## Source of Truth
- `docs/TESTING_STANDARD.md`

## Use When
- Scope is known and behavior must be validated.
- Release readiness or regression risk must be assessed.

## Checklist
- Unit test targets are identified.
- Integration boundaries are listed.
- End-to-end acceptance criteria are explicit.
- Critical negative/error paths are included.
- Observability and diagnostics needs are noted.
- TDD sequence is explicit for behavior-critical paths.
- Flaky-test risks and mitigation are documented.

## Output Contract
- Test matrix (unit/integration/e2e)
- Priority tiers
- Acceptance criteria list
- Regression watchlist
