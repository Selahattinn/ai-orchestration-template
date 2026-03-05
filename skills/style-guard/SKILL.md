# Style Guard

## Metadata
- status: active
- owner: coding-standards
- review_cadence: monthly

## Purpose
Enforce the project-specific Go coding style profile before final review.

## Source of Truth
- `docs/CODING_STYLE.md`
- `docs/LOGGING_STANDARD.md`
- `docs/FILE_HIERARCHY.md`
- `docs/NAMING_STANDARD.md`
- `docs/TESTING_STANDARD.md`
- `docs/MANDATORY_ENFORCEMENT_POLICY.md`

## Use When
- Any implementation proposal or code diff is produced.
- A run reaches pre-review or final quality gate.

## Checklist
- Handler pattern follows interface + private struct + constructor style.
- Function signatures include `ctx context.Context` where applicable.
- TDD evidence exists (tests first, then implementation behavior).
- Function-level comments are present where required.
- Import blocks follow stdlib -> third-party -> internal order.
- Error handling follows `ErrorBag` model at domain boundaries.
- Logging uses `zap` with `SugaredLogger`.
- Logging levels are used correctly (`Debugw/Infow/Warnw/Errorw`).
- Structured fields and sensitive-data masking follow `docs/LOGGING_STANDARD.md`.
- Package placement follows `cmd/internal/pkg/mocks` hierarchy rules.
- Naming follows package/type/function/file rules in `docs/NAMING_STANDARD.md`.
- Testing plan and evidence align with `docs/TESTING_STANDARD.md`.
- Mandatory mode and orchestration compliance are explicitly confirmed.

## Output Contract
- Style compliance score (0-4)
- Violations with file/function references
- Required fixes before final review
- Explicit pass/fail for style gate
