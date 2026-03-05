# Architecture

## Metadata
- status: active
- owner: platform-architecture
- review_cadence: monthly

## Purpose
Define service boundaries, dependencies, and orchestration topology.

## Source of Truth
- `docs/PROJECT_PROFILE.md`
- `docs/ARCHITECTURE_STYLE_GUIDE.md`
- `docs/FILE_HIERARCHY.md`

## Use When
- Multi-agent flow or service decomposition is being designed.
- Ownership and integration points are unclear.

## Checklist
- Components and responsibilities are separated clearly.
- Dependency direction is explicit.
- Data ownership is documented.
- Sync vs async boundaries are justified.
- Failure modes and retry points are identified.
- Architecture choice aligns with project profile (`hexagonal` preferred by default).
- Factory usage is limited to composition/bootstrap concerns.

## Output Contract
- Component map (textual)
- Dependency rules
- Handoff and integration points
- Architecture risks
