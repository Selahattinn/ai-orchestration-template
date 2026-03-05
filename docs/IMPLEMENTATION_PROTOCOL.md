# Implementation Protocol

Standard process for generating production-grade code from this markdown orchestration template.

## Goal

Produce code that is correct, testable, and reviewable with explicit artifacts.

## Required Inputs

- Project brief: `templates/PROJECT_BRIEF.md`
- Agent definitions: `workflows/AGENT_REGISTRY.md`
- Agent I/O contract: `workflows/AGENT_IO_CONTRACT.md`
- Model and budget policy: `docs/MODEL_POLICY.md`, `docs/COST_LATENCY_BUDGET.md`
- Coding style profile: `docs/CODING_STYLE.md`
- Logging policy: `docs/LOGGING_STANDARD.md`
- File hierarchy policy: `docs/FILE_HIERARCHY.md`

## Execution Flow

1. Scope and assumptions
- Clarify constraints, non-goals, and acceptance criteria.
- Mark unknowns explicitly.

2. Design output
- Produce API/design artifacts first.
- Resolve handoff artifacts before coding starts.

3. Implementation output
- Generate code with file-level intent and change rationale.
- Prefer small, reviewable increments.

4. Verification output
- Define and run unit/integration checks where applicable.
- Record untested areas and residual risks.
- Validate logging level and structured-field usage.

5. Style gate output
- Validate generated code against `docs/CODING_STYLE.md`.
- Produce explicit style score and violation list.

6. Final review output
- Produce severity-ranked findings.
- Return ship/hold decision with next actions.

## Mandatory Artifacts Per Run

- Implementation plan
- Code change summary
- Test plan and test evidence
- Risk list
- Final review findings
- Run log (using `templates/RUN_LOG_TEMPLATE.md`)

## Stop Conditions

- Missing critical input data
- Conflicting requirements unresolved
- Security policy violation risk
- Quality gate failure (see `docs/QUALITY_GATE.md`)
