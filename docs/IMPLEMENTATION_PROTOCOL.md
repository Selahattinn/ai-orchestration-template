# Implementation Protocol

Standard process for generating production-grade code from this markdown orchestration template.

## Goal

Produce code that is correct, testable, and reviewable with explicit artifacts.

## Required Inputs

- Project profile: `docs/PROJECT_PROFILE.md`
- Project brief: `templates/PROJECT_BRIEF.md`
- Agent definitions: `workflows/AGENT_REGISTRY.md`
- Agent I/O contract: `workflows/AGENT_IO_CONTRACT.md`
- Stage contract: `workflows/STAGE_CONTRACT.md`
- Architecture pattern registry: `workflows/ARCHITECTURE_PATTERN_REGISTRY.md`
- Model and budget policy: `docs/MODEL_POLICY.md`, `docs/COST_LATENCY_BUDGET.md`
- Architecture style guide: `docs/ARCHITECTURE_STYLE_GUIDE.md`
- Mandatory enforcement policy: `docs/MANDATORY_ENFORCEMENT_POLICY.md`
- Worktree policy: `docs/WORKTREE_STANDARD.md`
- Coding style profile: `docs/CODING_STYLE.md`
- Logging policy: `docs/LOGGING_STANDARD.md`
- File hierarchy policy: `docs/FILE_HIERARCHY.md`
- Naming policy: `docs/NAMING_STANDARD.md`
- Testing policy: `docs/TESTING_STANDARD.md`
- Branch protection policy: `docs/BRANCH_PROTECTION.md`

## Execution Flow

0. Worktree setup
- Complete Stage 0 (`worktree_setup`) first.
- Assign one dedicated worktree path and branch per stage.
- Fail fast if worktree mapping is incomplete or duplicated.

1. Scope and assumptions
- If project profile is incomplete, run `docs/BOOTSTRAP_INTERVIEW.md` first.
- Clarify constraints, non-goals, and acceptance criteria.
- Mark unknowns explicitly.
- Confirm strict mode (`rules_mode: mandatory_all`, `orchestration_mode: mandatory`).
- Confirm worktree strict mode (`worktree_mode: mandatory`, `worktree_strategy: per_stage`).

2. Design output
- Produce API/design artifacts first.
- Resolve handoff artifacts before coding starts.
- Mark Stage 1 artifact complete before Stage 2 starts.
- For architecture, route to the selected pattern skill via `skills/architecture/SKILL.md`.

3. Implementation output
- Generate code with file-level intent and change rationale.
- Prefer small, reviewable increments.
- Follow TDD sequence for behavior-critical changes.

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
- Final stage completion requires non-empty final review artifact.

## Orchestrator Commands

- Initialize: `python3 tools/stage_orchestrator.py init --run-dir runs/<run_id>`
- Complete next stage: `python3 tools/stage_orchestrator.py complete --run-dir runs/<run_id> --stage-id <stage_id>`
- Validate complete run: `python3 tools/stage_orchestrator.py finish --run-dir runs/<run_id>`
- CI validator: `python3 tools/validate_run.py --run-dir runs/latest`

## Mandatory Artifacts Per Run

- Implementation plan
- Stage manifest (`manifest.json`) aligned with `workflows/STAGE_CONTRACT.md`
- Worktree setup artifact (`artifacts/00_worktree_setup.md`)
- Stage artifacts for each ordered stage
- Code change summary
- Test plan and test evidence
- Risk list
- Final review findings
- Run log (using `templates/RUN_LOG_TEMPLATE.md`)

## Stop Conditions

- Missing critical input data
- Missing required stage artifact
- Stage order violation
- Conflicting requirements unresolved
- Security policy violation risk
- Quality gate failure (see `docs/QUALITY_GATE.md`)
- Orchestration bypass without active waiver
