# Run Log Standard

Every orchestration run should produce one run log entry.

## Required Fields

- run_id
- date_utc
- project_context
- input_summary
- stages_executed
- agent_sequence
- model_usage
- fallback_events
- rules_mode
- orchestration_mode
- orchestration_bypassed
- waiver_id
- waiver_owner
- waiver_reason
- waiver_expiry_utc
- eval_score
- style_score
- style_violations
- final_decision
- open_risks
- next_actions

## Minimal Rules

- Use one markdown file per run.
- Keep stage order identical to actual execution.
- Include fallback reason and impact when fallback occurs.
- Include links to generated artifacts.
- Explicitly record mandatory-mode compliance and bypass status.

## Done Criteria

- Required run-log fields are listed and stable.
- Fallback and artifact-link recording rules are explicit.
- The standard is aligned with `templates/RUN_LOG_TEMPLATE.md`.
