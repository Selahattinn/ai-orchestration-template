# Project Profile

Persistent project context for profile-driven orchestration.

## Profile Metadata

- profile_version: 1
- profile_status: bootstrap_pending
- last_updated_utc:

## Fixed Repository Rules

- repository_language: English

## Core Project Inputs

- domain:
- critical_flows:
- integrations:
- priority_mode: safety_correctness | speed_cost | balanced
- architecture_preference: active `pattern_id` from `workflows/ARCHITECTURE_PATTERN_REGISTRY.md` (aliases `clean-layered` and `service-layered` normalize to underscore form)
- architecture_notes:

## Optional Inputs

- compliance_constraints:
- deployment_context:
- runtime_limits:

## Profile-Driven Behavior Contract

- If mandatory fields are missing, run `docs/BOOTSTRAP_INTERVIEW.md` once.
- After profile completion, do not re-ask the same questions.
- Ask only for newly missing fields or explicit user changes.
- Any profile update must revise `last_updated_utc`.

## Change Log

| Date (UTC) | Updated By | Change Summary |
|---|---|---|

## Done Criteria

- Repository language is explicitly fixed to English.
- Mandatory fields are filled with non-placeholder values.
- `architecture_preference` maps to an active pattern in registry.
- Interview rerun is not required for unchanged fields.
