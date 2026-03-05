# Model Policy

This file standardizes model usage for all agents.

## Selection Guidelines

- `gpt-5`: high-stakes design, architecture, and final review
- `gpt-5-mini`: routine planning and structured outputs
- `gpt-5-nano`: low-cost drafting or repetitive transformations

## Fallback Policy

- `gpt-5` -> `gpt-5-mini`
- `gpt-5-mini` -> `gpt-5-nano`
- On fallback, note: trigger reason, expected quality impact, and retry condition.

## Parameter Guidelines

- `temperature`
- 0.1-0.2: review, risk analysis, consistency checks
- 0.2-0.3: planning and design proposals
- 0.4+: optional ideation only

- `max_output_tokens`
- 800-1200: focused review tasks
- 1200-1800: planning/architecture tasks

## Cost/Latency Guardrails

- Use one expensive step per stage unless escalation is justified.
- Prefer mini-first draft and high-model final validation for long tasks.

## Done Criteria

- Model selection, fallback, and parameter rules are explicitly documented.
- At least one cost/latency guardrail is defined.
- No unresolved TBD placeholders remain.
