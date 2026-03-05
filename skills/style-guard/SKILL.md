# Style Guard

## Metadata
- status: active
- owner: coding-standards
- review_cadence: monthly

## Purpose
Enforce the project-specific Go coding style profile before final review.

## Source of Truth
- `docs/CODING_STYLE.md`

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

## Output Contract
- Style compliance score (0-4)
- Violations with file/function references
- Required fixes before final review
- Explicit pass/fail for style gate
