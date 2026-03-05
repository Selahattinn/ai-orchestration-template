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
- [ ] File/package layout follows `docs/FILE_HIERARCHY.md`.
- [ ] Names follow `docs/NAMING_STANDARD.md` for package/type/method/file conventions.

### Logging
- [ ] Logging follows `docs/LOGGING_STANDARD.md`.
- [ ] `zap` + `SugaredLogger` is used in application layer code.
- [ ] Level usage is correct (`Debugw/Infow/Warnw/Errorw`).
- [ ] Structured keys are present and sensitive data is not leaked.

### Testing
- [ ] Testing approach follows `docs/TESTING_STANDARD.md`.
- [ ] Unit/integration scope is defined.
- [ ] Critical paths have test evidence or a clear gap note.
- [ ] Regression risks are documented.
- [ ] Test naming and structure are behavior-oriented.
- [ ] Flaky-test risks are explicitly addressed.

### Security and Safety
- [ ] No secrets or sensitive data leakage.
- [ ] Security policy checks were applied.
- [ ] High-risk actions include human approval points.

### Operability
- [ ] Assumptions and limitations are explicit.
- [ ] Rollback/mitigation notes exist for risky changes.
- [ ] Next actions are clear and prioritized.
- [ ] Architecture decisions align with `docs/PROJECT_PROFILE.md` and `docs/ARCHITECTURE_STYLE_GUIDE.md`.

### Architecture Discipline
- [ ] Architecture stage output includes the full contract from `skills/architecture/SKILL.md`.
- [ ] Selected architecture pattern is active in `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`.
- [ ] Pattern-specific skill output is present for the selected architecture.
- [ ] Dependency matrix explicitly lists allowed and forbidden directions.
- [ ] No circular dependency or core-to-adapter dependency exists.
- [ ] Data ownership and transaction boundaries are explicit.
- [ ] `google/wire` dependency injection plan exists and is limited to bootstrap layer, or an active waiver is documented.
- [ ] Manual wiring outside approved bootstrap locations is absent.

### Mandatory Enforcement
- [ ] `docs/MANDATORY_ENFORCEMENT_POLICY.md` is satisfied.
- [ ] No orchestration bypass occurred, or active waiver is documented.
- [ ] Rules mode is `mandatory_all` for this run.
- [ ] If waiver exists, owner/reason/expiry/affected_rules are documented.
- [ ] `workflows/STAGE_CONTRACT.md` stage order and artifact requirements are satisfied.
- [ ] `runs/latest/manifest.json` passes CI run-contract validation.

## Decision Rule

- `PASS`: all critical criteria satisfied.
- `REVISE`: non-critical gaps exist with clear remediation.
- `BLOCK`: critical correctness/security/testing failure.
