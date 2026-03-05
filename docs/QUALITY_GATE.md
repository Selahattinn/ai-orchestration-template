# Quality Gate

Use this checklist before accepting generated code output.

## Gate Criteria

### Correctness
- [ ] Requirements are implemented as specified.
- [ ] No known logical contradictions remain.
- [ ] Edge cases are addressed or explicitly deferred.

### Go and API Quality
- [ ] Output aligns with Go idioms and package boundaries.
- [ ] API contracts are consistent and versioning-safe.
- [ ] Error handling is explicit and contextual.

### Style Adherence
- [ ] Interface + constructor pattern follows `docs/CODING_STYLE.md`.
- [ ] `ctx context.Context` is present where applicable.
- [ ] Import groups follow stdlib -> third-party -> internal order.
- [ ] Function-level comments are present where required.
- [ ] `ErrorBag` usage is consistent at domain boundaries.

### Testing
- [ ] Unit/integration scope is defined.
- [ ] Critical paths have test evidence or a clear gap note.
- [ ] Regression risks are documented.

### Security and Safety
- [ ] No secrets or sensitive data leakage.
- [ ] Security policy checks were applied.
- [ ] High-risk actions include human approval points.

### Operability
- [ ] Assumptions and limitations are explicit.
- [ ] Rollback/mitigation notes exist for risky changes.
- [ ] Next actions are clear and prioritized.

## Decision Rule

- `PASS`: all critical criteria satisfied.
- `REVISE`: non-critical gaps exist with clear remediation.
- `BLOCK`: critical correctness/security/testing failure.
