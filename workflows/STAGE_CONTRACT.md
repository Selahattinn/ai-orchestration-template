# Stage Contract

Machine-checked contract for stage order and artifact requirements.

## Ordered Stages

- stage_id: api_scope
  stage_name: API Scope
  artifact: artifacts/01_api_scope.md
- stage_id: go_fit_check
  stage_name: Go Fit Check
  artifact: artifacts/02_go_fit_check.md
- stage_id: architecture
  stage_name: Architecture
  artifact: artifacts/03_architecture.md
- stage_id: testing_plan
  stage_name: Testing Plan
  artifact: artifacts/04_testing_plan.md
- stage_id: style_gate
  stage_name: Style Gate
  artifact: artifacts/05_style_gate.md
- stage_id: final_review
  stage_name: Final Review
  artifact: artifacts/06_final_review.md

## Transition Rules

- Stages must be completed exactly in the declared order.
- A stage is complete only when its artifact file exists and is non-empty.
- Next stage cannot start until previous stage is complete.
- `final_review` cannot be completed before all earlier stages are complete.

## Waiver Rules

- Orchestration bypass is prohibited by default.
- If `orchestration_bypassed: true`, waiver fields must be present:
- `waiver_id`
- `waiver_owner`
- `waiver_reason`
- `waiver_expiry_utc`
- `affected_rules`
- Waiver expiry must be in the future at validation time.

## CI Contract

- CI validates `runs/latest/manifest.json` against this stage contract.
- CI fails when stage order, artifact presence, or waiver rules are violated.

## Done Criteria

- Stage order is explicit and machine-checkable.
- Every stage defines exactly one required artifact.
- Transition and waiver rules are strict and unambiguous.
