# Agent Registry

Single source of truth for orchestration agents and model selections.

## Agent Template

```md
### <agent_name>
- purpose:
- primary_model:
- fallback_model:
- temperature:
- max_output_tokens:
- latency_target:
- cost_tier: (low|medium|high)
- skill_file: skills/<skill-name>/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to:
- done_criteria:
```

## Default Agents

### worktree_manager
- purpose: prepares mandatory per-stage git worktree mapping and blocks invalid setup
- primary_model: gpt-5-mini
- fallback_model: gpt-5-nano
- temperature: 0.1
- max_output_tokens: 900
- latency_target: fast
- cost_tier: low
- skill_file: skills/worktree-setup/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to: api_designer
- done_criteria: stage-to-worktree map and branch plan are complete and valid

### api_designer
- purpose: defines API boundaries, endpoint contracts, and versioning
- primary_model: gpt-5
- fallback_model: gpt-5-mini
- temperature: 0.2
- max_output_tokens: 1800
- latency_target: medium
- cost_tier: medium
- skill_file: skills/api-design/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to: go_idiom_guard
- done_criteria: endpoint list, schema summary, and error model are complete

### go_idiom_guard
- purpose: enforces Go idioms, package boundaries, and error-handling norms
- primary_model: gpt-5
- fallback_model: gpt-5-mini
- temperature: 0.1
- max_output_tokens: 1200
- latency_target: medium
- cost_tier: medium
- skill_file: skills/go-idioms/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to: architect
- done_criteria: naming, interfaces, and package recommendations are clear

### architect
- purpose: defines service boundaries and orchestration topology
- primary_model: gpt-5
- fallback_model: gpt-5-mini
- temperature: 0.2
- max_output_tokens: 1600
- latency_target: medium
- cost_tier: medium
- skill_file: skills/architecture/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to: test_strategist
- done_criteria: components, dependencies, and handoff points are explicit

### test_strategist
- purpose: defines testing strategy and acceptance criteria
- primary_model: gpt-5-mini
- fallback_model: gpt-5-nano
- temperature: 0.2
- max_output_tokens: 1400
- latency_target: fast
- cost_tier: low
- skill_file: skills/testing-strategy/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to: style_guard
- done_criteria: unit/integration/e2e coverage map is complete

### style_guard
- purpose: enforces project-specific style profile before final review
- primary_model: gpt-5-mini
- fallback_model: gpt-5-nano
- temperature: 0.1
- max_output_tokens: 1000
- latency_target: fast
- cost_tier: low
- skill_file: skills/style-guard/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to: reviewer
- done_criteria: style compliance score and required fixes are explicit

### reviewer
- purpose: performs final quality gate before completion
- primary_model: gpt-5
- fallback_model: gpt-5-mini
- temperature: 0.1
- max_output_tokens: 1000
- latency_target: medium
- cost_tier: medium
- skill_file: skills/code-review/SKILL.md
- io_contract_ref: workflows/AGENT_IO_CONTRACT.md
- handoff_to: done
- done_criteria: no critical issues or a clear action list exists
