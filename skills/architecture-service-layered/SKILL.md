# Architecture Service Layered

## Metadata
- status: active
- owner: platform-architecture
- review_cadence: monthly

## Purpose
Enforce service-layered architecture for simpler products with explicit growth triggers.

## Source of Truth
- `docs/ARCHITECTURE_STYLE_GUIDE.md`
- `docs/FILE_HIERARCHY.md`
- `docs/CODING_STYLE.md`

## Non-Negotiable Rules

If any rule fails, return `BLOCK`:

- Handlers must stay thin; business logic belongs in service layer.
- Repository contracts must be explicit; direct transport-to-storage coupling is forbidden.
- Service layer must not depend on transport implementations.
- Data ownership and write boundaries must be explicit.
- `google/wire` is mandatory in bootstrap for dependency injection, unless an active waiver is explicitly documented.

## Migration Triggers

If any trigger is observed, return `REVISE` with migration plan:

- Cross-service/domain rules become hard to isolate.
- Service methods exceed cohesion boundaries.
- Repeated adapter leakage into service logic appears.

## Required Output

1. Handler/service/repository boundary map.
2. Allowed/forbidden dependency matrix.
3. Migration trigger assessment.
4. Data ownership and consistency boundaries.
5. Wire provider-set plan.
6. Risks and final verdict: `PASS | REVISE | BLOCK`.
