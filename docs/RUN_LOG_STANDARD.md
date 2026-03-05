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
