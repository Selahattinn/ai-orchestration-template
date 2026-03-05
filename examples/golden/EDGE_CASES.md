# Golden Example: Edge Cases

## Edge Case List

- Conflicting requirements from stakeholders
- Missing input fields at stage boundary
- Tight latency budget with high quality requirement
- Security-sensitive prompt content
- Large scope with incomplete domain context

## Expected Behavior

- Return `blocked` when mandatory input is absent
- Escalate model only with explicit reason
- Flag unresolved contradictions before final review
- Require human check for security-sensitive decisions
