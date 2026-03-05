# Agent I/O Contracts

Standard input/output rules to reduce ambiguity between handoffs.

## Shared Input Envelope

- `task_id`
- `stage`
- `goal`
- `constraints`
- `required_artifacts`
- `previous_stage_output`

## Shared Output Envelope

- `summary`
- `decisions`
- `assumptions`
- `risks`
- `next_handoff_artifact`
- `done_criteria_check`
- `style_notes` (required for implementation-related stages)

## Contract Rules

- If required input is missing, agent must return `blocked` with missing fields.
- Output must include at least one explicit assumption.
- Handoff artifact names must be stable and unique per stage.
