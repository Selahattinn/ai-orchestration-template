# Agent Definition Template

## Identity
- name:
- owner:
- stage:

## Mission
- purpose:
- done_criteria:

## Model Configuration
- primary_model:
- fallback_model:
- temperature:
- max_output_tokens:
- latency_target:
- cost_tier:

## Behavior Contract
- inputs:
- outputs:
- guardrails:
- handoff_to:
- io_contract_ref: `workflows/AGENT_IO_CONTRACT.md`

## Skill Binding
- skill_file: `skills/<skill-name>/SKILL.md`
- style_profile_ref: `docs/CODING_STYLE.md`
