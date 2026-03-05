# Mandatory Enforcement Policy

Global execution policy for all template-driven runs.

## Policy Flags

- rules_mode: mandatory_all
- orchestration_mode: mandatory
- bypass_policy: prohibited
- exception_policy: explicit_waiver_only

## Core Rules

- All standards under `docs/` are mandatory inputs, not optional guidance.
- Every run must execute through defined orchestration stages from `workflows/ORCHESTRATION_FLOW.md`.
- Direct single-agent bypass output is not allowed.
- Any exception requires a documented waiver with owner, reason, and expiry date.

## Waiver Contract

If a waiver is used, include all fields:
- `waiver_id`
- `waiver_owner`
- `waiver_reason`
- `waiver_expiry_utc`
- `affected_rules`

Waivers are temporary and must be removed after expiry.

## Run-Level Requirements

- Run log must explicitly state ruleset mode and orchestration compliance.
- Run manifest must satisfy `workflows/STAGE_CONTRACT.md`.
- Final review must fail when orchestration is bypassed without an active waiver.
- Missing mandatory standards => `BLOCK`.

## Done Criteria

- Policy flags are present and unchanged.
- Bypass prohibition is explicit.
- Waiver mechanism is documented and time-bounded.
