# Eval Rubric

Use this rubric to score every orchestration run.

## Scoring Scale

- `0`: missing / invalid
- `1`: weak
- `2`: acceptable
- `3`: strong
- `4`: excellent

## Criteria

### Correctness
- Are claims technically sound?
- Are model/tool limits reflected correctly?

### Completeness
- Did the run produce all required artifacts?
- Are open questions and assumptions explicit?

### Consistency
- Are outputs aligned across stages and handoffs?
- Are terms and decisions stable between agents?

### Risk Awareness
- Are critical risks identified and prioritized?
- Are mitigations practical and actionable?

### Actionability
- Can the next agent (or human) execute immediately?
- Are outputs structured and decision-ready?

### Style Match
- Does output follow `docs/CODING_STYLE.md` rules?
- Are context usage, import ordering, comments, and ErrorBag rules applied?
- Are logging choices and levels aligned with `docs/LOGGING_STANDARD.md`?

## Final Grade

- `Pass`: no criterion below `2`, and average >= `2.6`
- `Borderline`: one criterion at `1`, average >= `2.3`
- `Fail`: any criterion at `0`, or average < `2.3`

## Required Eval Output

- Criteria table with scores
- 3 strongest points
- 3 highest-impact gaps
- Decision: `pass`, `revise`, or `block`
