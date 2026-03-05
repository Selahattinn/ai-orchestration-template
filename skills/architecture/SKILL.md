# Architecture

## Metadata
- status: active
- owner: platform-architecture
- review_cadence: monthly

## Purpose
Define and enforce service boundaries, dependency direction, and orchestration topology.

## Source of Truth
- `docs/PROJECT_PROFILE.md`
- `docs/ARCHITECTURE_STYLE_GUIDE.md`
- `docs/FILE_HIERARCHY.md`
- `docs/CODING_STYLE.md`

## Use When
- Multi-agent flow or service decomposition is being designed.
- Ownership and integration points are unclear.
- New package/module boundaries are introduced.
- Dependency injection and bootstrap strategy are being defined.

## Non-Negotiable Rules

If any rule below fails, return `BLOCK`:

- Core business logic (`internal/domain`, `internal/service`, use-case layer) must not import transport, framework, or platform adapter packages.
- Dependency direction must be one-way and explicit; circular dependencies are forbidden.
- Data ownership per aggregate/resource must be explicit; shared mutable ownership is forbidden.
- Boundary crossings must happen via interfaces (ports) and adapters.
- Architecture choice must match `docs/PROJECT_PROFILE.md` and `docs/ARCHITECTURE_STYLE_GUIDE.md`.
- Factory pattern must be limited to composition/bootstrap.
- `google/wire` is required for dependency assembly at bootstrap; manual wiring outside documented exceptions is forbidden.

## Required Checks

- Components and responsibilities are separated with clear bounded contexts.
- Sync vs async boundaries are justified with latency/failure trade-offs.
- Failure modes, retry policy, timeout policy, and idempotency stance are documented.
- Transaction boundary and consistency model are explicit.
- External dependencies are isolated behind adapter interfaces.
- Package placement follows `docs/FILE_HIERARCHY.md`.

## Output Contract

Architecture stage output must include all sections:

1. `Architecture Decision`
- Selected style (`hexagonal`, `clean_layered`, or `service_layered`) and rationale.

2. `Component Boundaries`
- Component list with responsibilities.
- In-scope and out-of-scope per component.

3. `Dependency Matrix`
- Allowed dependency directions.
- Forbidden dependency directions.
- Circular dependency check result.

4. `Data Ownership and Consistency`
- Owner component for each domain resource.
- Transaction boundaries and consistency approach.

5. `Runtime Boundaries`
- Sync/async interaction map.
- Timeout, retry, and idempotency policy per boundary.

6. `Dependency Injection Plan`
- `google/wire` set definitions and provider grouping.
- Bootstrap location (`cmd/<service>/main.go`, `internal/app/bootstrap`).
- No-manual-wiring statement for core graph.

7. `Risks and Decision`
- Top architecture risks and mitigations.
- Final decision: `PASS`, `REVISE`, or `BLOCK`.
