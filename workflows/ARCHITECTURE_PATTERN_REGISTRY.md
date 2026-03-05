# Architecture Pattern Registry

Single source of truth for supported architecture patterns and their skills.

## Registry Fields

- `pattern_id`: stable identifier used by `docs/PROJECT_PROFILE.md`
- `skill_file`: pattern-specific architecture skill path
- `status`: `active` | `deprecated` | `experimental`
- `default`: whether this pattern is the default selection

## Active Patterns

| pattern_id | skill_file | status | default | notes |
|---|---|---|---|---|
| `hexagonal` | `skills/architecture-hexagonal/SKILL.md` | `active` | `yes` | Preferred default for maintainability and testability. |
| `clean_layered` | `skills/architecture-clean-layered/SKILL.md` | `active` | `no` | Strict layer transitions and bounded dependencies. |
| `service_layered` | `skills/architecture-service-layered/SKILL.md` | `active` | `no` | Simpler structure with migration triggers for growth. |

## Selection Contract

- `docs/PROJECT_PROFILE.md` -> `architecture_preference` must match an `active` `pattern_id`.
- Routing is executed by `skills/architecture/SKILL.md`.
- Unknown or non-active patterns must return `BLOCK` unless an explicit waiver exists.

## Extension Contract (Adding New Patterns)

When adding a new pattern:

1. Create `skills/architecture-<pattern>/SKILL.md`.
2. Add one row to this registry with stable `pattern_id`.
3. Define pattern-level `BLOCK` conditions, dependency rules, and DI rules.
4. Define testing expectations and migration triggers for the pattern.
5. Update docs contract checks if new mandatory fields are introduced.

## Deprecation Contract

- Set `status: deprecated` instead of deleting registry rows.
- Deprecated patterns require migration notes in architecture output.
- Removing a registry row is allowed only after all dependent profiles are migrated.

## Done Criteria

- Registry includes all supported architecture patterns.
- Every active pattern maps to an existing skill file.
- Selection, extension, and deprecation rules are explicit.
