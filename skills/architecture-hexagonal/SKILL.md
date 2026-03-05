# Architecture Hexagonal

## Metadata
- status: active
- owner: platform-architecture
- review_cadence: monthly

## Purpose
Enforce hexagonal (ports and adapters) architecture for backend services.

## Source of Truth
- `docs/ARCHITECTURE_STYLE_GUIDE.md`
- `docs/FILE_HIERARCHY.md`
- `docs/HEXAGONAL_BOUNDARY_STANDARD.md`
- `docs/CODING_STYLE.md`

## Non-Negotiable Rules

If any rule fails, return `BLOCK`:

- Core domain/use-case packages must not import transport/framework/platform adapter implementations.
- Every external dependency crossing must be behind explicit ports (interfaces).
- Adapter code must stay outside core business logic packages.
- Inbound and outbound ports must be separated and explicitly mapped.
- Circular dependency is forbidden.
- `google/wire` is mandatory for bootstrap dependency graph assembly, unless an active waiver is explicitly documented.

## Required Output

1. Canonical hierarchy mapping (packages to hexagonal roles).
2. Inbound port definitions and owning use cases.
3. Outbound port definitions and adapter mappings.
4. Dependency matrix (allowed/forbidden imports).
5. Inbound -> use case -> outbound interaction map.
6. Data ownership and transaction boundaries.
7. Wire provider-set plan and bootstrap location.
8. Risks and final verdict: `PASS | REVISE | BLOCK`.
