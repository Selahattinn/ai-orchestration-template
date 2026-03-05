# Architecture Clean Layered

## Metadata
- status: active
- owner: platform-architecture
- review_cadence: monthly

## Purpose
Enforce clean layered architecture with strict layer transitions.

## Source of Truth
- `docs/ARCHITECTURE_STYLE_GUIDE.md`
- `docs/FILE_HIERARCHY.md`
- `docs/CODING_STYLE.md`

## Non-Negotiable Rules

If any rule fails, return `BLOCK`:

- Layer order must be explicit and unidirectional.
- Skip-layer dependencies are forbidden.
- Upper layers must not leak transport/framework concerns into core layers.
- Shared mutable state across layers without ownership is forbidden.
- `google/wire` is mandatory in bootstrap layer for dependency assembly.

## Required Output

1. Layer stack definition and allowed transitions.
2. Forbidden dependency list (including skip-layer paths).
3. Ownership map and transaction boundaries.
4. Failure/retry/idempotency strategy at layer boundaries.
5. Wire provider-set plan by layer.
6. Risks and final verdict: `PASS | REVISE | BLOCK`.
