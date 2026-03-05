# Architecture

## Metadata
- status: active
- owner: platform-architecture
- review_cadence: monthly

## Purpose
Route architecture evaluation to the selected pattern-specific skill and enforce shared architecture gates.

## Source of Truth
- `docs/PROJECT_PROFILE.md`
- `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`
- `docs/ARCHITECTURE_STYLE_GUIDE.md`
- `docs/FILE_HIERARCHY.md`
- `docs/CODING_STYLE.md`

## Use When
- Stage 3 architecture decisions are being produced.
- Architecture pattern must be selected, validated, or changed.
- Dependency injection and boundary rules need strict validation.

## Routing Contract

1. Read `architecture_preference` from `docs/PROJECT_PROFILE.md`.
2. Resolve the pattern in `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`.
3. If pattern is missing or not `active`, return `BLOCK` unless an explicit waiver exists.
4. Load the mapped pattern skill file and execute its rules.
5. Return final decision with both router-level and pattern-level checks.

## Shared Non-Negotiable Rules

If any rule fails, return `BLOCK`:

- Core business logic must not depend on transport/framework/platform implementation packages.
- Dependency direction must be explicit and acyclic.
- Data ownership must be explicit for each domain resource.
- Boundary crossings must use explicit interfaces.
- `google/wire` must be used for bootstrap dependency graph assembly, unless an active waiver is explicitly documented (`waiver_id`, `waiver_owner`, `waiver_reason`, `waiver_expiry_utc`, `affected_rules`).

## Output Contract

Architecture stage output must include:

1. `Selected Pattern`
- `pattern_id`
- `skill_file`
- `status`

2. `Router Checks`
- Shared-rule validation results.
- Profile-to-registry consistency check.
- Waiver applicability check when DI exception is used.

3. `Pattern Report`
- Full report from the selected pattern skill.

4. `Final Verdict`
- `PASS`, `REVISE`, or `BLOCK`.
- Blocking reasons list when not `PASS`.
