# Architecture Style Guide

Architecture decision guide for template consumers.

## Default Recommendation

Use **Hexagonal Architecture (Ports and Adapters)** by default.

Why default:
- Keeps business core independent from frameworks and providers.
- Works well with AI-generated iterative changes.
- Improves testability through interface-driven boundaries.

## Alternative Styles

### Clean Layered
- Useful when teams prefer strict layer transitions.
- Good for monoliths with predictable domain boundaries.

### Service Layered
- Useful for simpler products with lower domain complexity.
- May be faster early, but needs stronger boundary discipline later.

## Pattern Guidance

### Hexagonal (Primary)
- `domain` and use-case logic in `internal/` core packages.
- Ports as interfaces at boundaries.
- Adapters in `internal/platform` and `internal/transport`.

### Factory Pattern (Supporting)
- Use factories for composition and dependency assembly.
- Typical places: `cmd/<service>/main.go`, `internal/app/bootstrap`.
- Do not use factory as a replacement for architecture boundaries.

## Selection Rules

- If long-term maintainability and testability dominate: choose `hexagonal`.
- If team already runs layered conventions successfully: choose `clean_layered`.
- If project is small and speed-focused: choose `service_layered` with strict migration notes.

## Mapping to File Hierarchy

- Follow `docs/FILE_HIERARCHY.md` and align architecture choice to package layout.
- Keep adapters and transport concerns outside core business logic.

## Done Criteria

- `architecture_preference` is set in `docs/PROJECT_PROFILE.md`.
- Architecture rationale is documented for chosen style.
- Factory usage is limited to composition/bootstrap concerns.
