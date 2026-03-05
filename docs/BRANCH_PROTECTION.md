# Branch Protection Standard

Required branch/ruleset settings for `main`.

## Required Checks

- `Docs Contract / validate-docs`
- `PR Body Contract / validate-pr-body`
- `Orchestration Contract / validate-run-contract`

## Required Pull Request Rules

- Require a pull request before merging.
- Require at least 1 approving review.
- Require conversation resolution before merge.
- Require branches to be up to date before merging.

## Restriction Rules

- Do not allow force pushes.
- Do not allow branch deletion.
- Restrict bypass to repository owner only.
- Enforce for administrators when possible.

## Setup Checklist

1. Go to repository settings -> Rules or Branch protection.
2. Target branch: `main`.
3. Enable required status checks and select the checks listed above.
4. Enable pull request and review requirements.
5. Save and test with a trial PR.

## Done Criteria

- Required checks are listed with exact workflow/job names.
- PR/review constraints are explicit.
- Bypass and destructive actions are restricted.
