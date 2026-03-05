# Architecture

## Metadata
- status: active
- owner: platform-architecture
- review_cadence: monthly

## Purpose
Define service boundaries, dependencies, and orchestration topology.

## Use When
- Multi-agent flow or service decomposition is being designed.
- Ownership and integration points are unclear.

## Checklist
- Components and responsibilities are separated clearly.
- Dependency direction is explicit.
- Data ownership is documented.
- Sync vs async boundaries are justified.
- Failure modes and retry points are identified.

## Output Contract
- Component map (textual)
- Dependency rules
- Handoff and integration points
- Architecture risks
