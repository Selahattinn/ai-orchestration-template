# Architecture and Orchestration Decisions

Record key decisions and why they changed.

## Decision Template

### DEC-<number>: <title>
- Date:
- Status: proposed | accepted | superseded
- Context:
- Decision:
- Consequences:
- Supersedes:
- Links:

## Initial Decisions

### DEC-001: Markdown-Only Template
- Date: 2026-03-04
- Status: accepted
- Context: Team needs a forkable orchestration template without runtime lock-in.
- Decision: Keep repository markdown-first with no required runtime code.
- Consequences: Faster adoption, lower setup cost, clearer governance docs.
- Supersedes: none
- Links: README.md

### DEC-002: Personal Style Gate
- Date: 2026-03-05
- Status: accepted
- Context: Team wants generated code to match a specific Go coding style.
- Decision: Introduce `docs/CODING_STYLE.md` and `skills/style-guard/SKILL.md` as mandatory quality inputs.
- Consequences: Stronger consistency, fewer style regressions, explicit style scoring in run logs.
- Supersedes: none
- Links: docs/CODING_STYLE.md, workflows/AGENT_REGISTRY.md

### DEC-003: zap SugaredLogger Logging Standard
- Date: 2026-03-05
- Status: accepted
- Context: Team wants structured logging with simple ergonomics and explicit level policy.
- Decision: Standardize on `zap` with `SugaredLogger` and enforce level rules via quality/style gates.
- Consequences: Better consistency for operational logs, easier review of logging behavior, and clearer incident diagnostics.
- Supersedes: none
- Links: docs/LOGGING_STANDARD.md, docs/QUALITY_GATE.md

### DEC-004: File Hierarchy Contract
- Date: 2026-03-05
- Status: accepted
- Context: Team wants predictable package boundaries and test-double placement.
- Decision: Adopt `cmd/internal/pkg/mocks` hierarchy with clear placement rules and anti-patterns.
- Consequences: Better codebase navigation, cleaner boundaries, and fewer architecture drifts.
- Supersedes: none
- Links: docs/FILE_HIERARCHY.md, docs/CODING_STYLE.md
