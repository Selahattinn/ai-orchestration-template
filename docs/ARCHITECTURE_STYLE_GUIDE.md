# Architecture Style Guide

Architecture decision guide for template consumers.

Pattern support is registry-driven via `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`.

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
- Dependency flow remains inward toward the core.
- Pattern skill: `skills/architecture-hexagonal/SKILL.md`
- Boundary standard: `docs/HEXAGONAL_BOUNDARY_STANDARD.md`

### Clean Layered
- Use explicit layers with strict transition order.
- No skip-layer dependencies.
- Pattern skill: `skills/architecture-clean-layered/SKILL.md`

### Service Layered
- Keep handlers thin and service layer cohesive.
- Enforce migration triggers when complexity grows.
- Pattern skill: `skills/architecture-service-layered/SKILL.md`

### Factory Pattern (Supporting)
- Use factories for composition and dependency assembly.
- Typical places: `cmd/<service>/main.go`, `internal/bootstrap`.
- Do not use factory as a replacement for architecture boundaries.

### Google Wire (Required for DI)
- Use [`google/wire`](https://github.com/google/wire) for compile-time dependency injection.
- Keep provider sets grouped by boundary (for example `transportSet`, `serviceSet`, `platformSet`).
- Generate wiring only in bootstrap/composition layer.
- Do not expose `wire` concerns to domain code.

## Non-Negotiable Rules

- Core packages must not depend on transport/framework/platform implementation packages.
- Circular dependencies are `BLOCK`.
- Boundary crossings without port interfaces are `BLOCK`.
- Data ownership ambiguity for the same resource is `BLOCK`.
- Manual dependency graph assembly in non-bootstrap packages is `BLOCK`.
- `google/wire` is mandatory unless an explicit waiver exists.

## Selection Rules

- If long-term maintainability and testability dominate: choose `hexagonal`.
- If team already runs layered conventions successfully: choose `clean_layered`.
- If project is small and speed-focused: choose `service_layered` with strict migration notes.
- Selected value must be an active `pattern_id` in `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`.
- Pattern-specific checks must run through `skills/architecture/SKILL.md` router.

## Mapping to File Hierarchy

- Follow `docs/FILE_HIERARCHY.md` and align architecture choice to package layout.
- Keep adapters and transport concerns outside core business logic.
- Keep DI files under bootstrap-oriented locations (for example `internal/bootstrap/wire.go`).
- When `architecture_preference=hexagonal`, enforce `docs/HEXAGONAL_BOUNDARY_STANDARD.md`.

## Done Criteria

- `architecture_preference` is set in `docs/PROJECT_PROFILE.md`.
- Architecture rationale is documented for chosen style.
- Factory usage is limited to composition/bootstrap concerns.
- `google/wire` usage and provider-set strategy are documented.
- Non-negotiable boundary rules are explicitly listed.
- Pattern-to-skill mapping is defined in `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`.
- Hexagonal boundary rules are documented in `docs/HEXAGONAL_BOUNDARY_STANDARD.md`.
