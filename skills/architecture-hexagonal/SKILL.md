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
- `docs/CODING_STYLE.md`

## Non-Negotiable Rules

If any rule fails, return `BLOCK`:

- Core domain/use-case packages must not import transport/framework/platform adapter implementations.
- Every external dependency crossing must be behind explicit ports (interfaces).
- Adapter code must stay outside core business logic packages.
- Circular dependency is forbidden.
- `google/wire` is mandatory for bootstrap dependency graph assembly.

## Required Output

1. Port definitions (inbound/outbound).
2. Adapter mapping to each port.
3. Dependency matrix (allowed/forbidden imports).
4. Data ownership and transaction boundaries.
5. Wire provider-set plan and bootstrap location.
6. Risks and final verdict: `PASS | REVISE | BLOCK`.
