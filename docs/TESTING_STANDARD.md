# Testing Standard

Canonical testing policy for Go services in this template.

## Core Principles

- Default workflow is TDD: `red -> green -> refactor`.
- Tests validate behavior, not implementation details.
- Keep tests deterministic and isolated.
- Prefer risk-based depth over chasing arbitrary global coverage.

## Test Layers

### Unit Tests
- Scope: pure business logic and small component behavior.
- Fast, deterministic, no external I/O.
- Use table-driven tests when multiple input/output combinations exist.

### Integration Tests
- Scope: DB, queue, cache, HTTP client/server boundaries.
- Validate adapter behavior and wiring assumptions.
- Use controlled test environment and explicit fixtures.

### Contract Tests
- Scope: API request/response contracts and error semantics.
- Validate schema-level compatibility and error code mapping.

### End-to-End Tests
- Scope: critical user journeys and cross-boundary flows.
- Keep suite small and focused on highest-risk business paths.

## Naming and Structure

- Test function names should be behavior-oriented:
- `TestCreateUser_WhenRepositoryFails_ReturnsError`
- Use `_test.go` files near target package when possible.
- Use `testdata/` for fixture files.
- Keep test doubles under `mocks/` with explicit contract names.

## TDD Workflow Rules

1. Write a failing test for expected behavior.
2. Implement minimal code to pass.
3. Refactor while preserving green status.
4. Record uncovered risk if behavior cannot be tested yet.

## Mocking Rules

- Prefer generated mocks for interfaces.
- Mock only external boundaries, not simple value objects.
- Keep expectations minimal and behavior-focused.
- Avoid brittle call-order assertions unless order is business-critical.

## Context, Time, and Concurrency

- Use explicit context timeouts in integration/e2e tests.
- Avoid `time.Sleep` as synchronization strategy.
- For concurrency tests, enforce deterministic completion and assertions.

## Coverage Policy

- No fixed global percentage gate by default.
- Require high coverage on critical paths:
- authentication/authorization
- payment/billing/business-critical writes
- error mapping and retry/fallback behavior
- If a critical path is not covered, add explicit risk note.

## Flaky Test Policy

- Flaky tests are treated as defects.
- Quarantine temporarily only with linked follow-up action.
- Do not merge with known flaky tests on critical paths.

## CI Expectations

- Unit tests should run on every PR.
- Integration/e2e tests should run at least on merge queue or protected branch checks.
- Test output should include failing scenario context, not only stack traces.

## Anti-Patterns

- Snapshot-style assertions for unstable outputs without normalization.
- Asserting private internals instead of public behavior.
- Long, multi-behavior tests with unclear failure cause.
- Skipping tests silently without traceable reason.
