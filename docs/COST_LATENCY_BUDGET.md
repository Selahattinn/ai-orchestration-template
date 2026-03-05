# Cost and Latency Budget

Default budget policy per orchestration stage.

## Budget Matrix

| Stage | Preferred Model | Fallback | Max Calls | Latency Target | Cost Tier |
|---|---|---|---:|---|---|
| API Scope | gpt-5 | gpt-5-mini | 2 | medium | medium |
| Go Fit Check | gpt-5 | gpt-5-mini | 1 | medium | medium |
| Architecture | gpt-5 | gpt-5-mini | 2 | medium | medium |
| Testing Plan | gpt-5-mini | gpt-5-nano | 2 | fast | low |
| Style Gate | gpt-5-mini | gpt-5-nano | 1 | fast | low |
| Final Review | gpt-5 | gpt-5-mini | 1 | medium | medium |

## Escalation Rules

- Escalate to a stronger model only if the stage is blocked by ambiguity.
- Escalate to a stronger model only if a high-risk decision is unresolved.
- Escalate to a stronger model only if final review flags a correctness issue.

## Hard Limits

- No more than `10` model calls per run unless explicitly approved.
- No repeated retry loops with the same prompt over `2` attempts.
- Record any escalation in the run log.

## Done Criteria

- Every orchestration stage has a budget row.
- Escalation and hard-limit rules are explicit.
- Budget policy is aligned with current agent flow.
