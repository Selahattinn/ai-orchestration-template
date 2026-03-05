# Bootstrap Interview

One-time discovery protocol for collecting initial project context.

## Trigger Condition

Run this interview only when `docs/PROJECT_PROFILE.md` has missing mandatory fields.

## Mandatory Questions

1. What is the project domain?
2. What are the top 3 critical flows for first release?
3. Which integrations are required (DB, cache, queue, external APIs)?
4. What is the priority mode: safety/correctness, speed/cost, or balanced?
5. Which architecture preference is expected (hexagonal, clean-layered, service-layered)?

## Optional Questions

1. Are there compliance or policy constraints?
2. Are there deployment/runtime limitations?

## Persistence Rules

- Write all answers into `docs/PROJECT_PROFILE.md`.
- Set `profile_status` to `active` after required fields are complete.
- Never ask already-answered questions unless user asks to revise profile.
- For partial profiles, ask only missing fields.

## Output Contract

- Updated project profile file
- Summary of captured decisions
- Explicit list of remaining unknowns (if any)

## Done Criteria

- All mandatory questions are answered and persisted.
- `profile_status` is `active` when required fields are complete.
- Follow-up questions (if any) are only for missing values.
