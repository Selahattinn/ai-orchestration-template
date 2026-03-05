# Go Idioms

## Metadata
- status: active
- owner: backend-go-team
- review_cadence: monthly

## Purpose
Evaluate whether design/output aligns with idiomatic Go practices.

## Source of Truth
- `docs/CODING_STYLE.md`

## Use When
- Proposals include package structures or API boundaries.
- Naming/interfaces/error handling decisions are needed.

## Checklist
- Package names are short, clear, and lowercase.
- Interfaces are consumer-driven and minimal.
- Errors are wrapped and contextualized correctly.
- Context propagation and cancellation are explicit.
- Concurrency patterns avoid hidden shared-state risk.
- Constructor and handler patterns match the interface-first preference.
- Import ordering is stdlib -> third-party -> internal.
- Top-level function comments exist where required.
- TDD-first evidence is visible in plan or artifacts.

## Output Contract
- Idiom compliance notes
- Refactoring recommendations
- Risky anti-patterns to avoid
