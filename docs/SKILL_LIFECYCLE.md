# Skill Lifecycle

How skills are proposed, approved, maintained, and retired.

## States

- `draft`: skill exists but not approved
- `active`: approved for normal use
- `deprecated`: avoid new usage
- `retired`: archived and replaced

## Add a New Skill

1. Create `skills/<name>/SKILL.md`
2. Define trigger conditions and output contract
3. Add owner and review cadence
4. Register usage in relevant workflow docs

## Review Cadence

- Monthly quick review for active skills
- Immediate review after major failures
- Deprecate if overlap is high or quality is low

## Deprecation Policy

- Mark skill as deprecated in its file header
- Add replacement skill reference
- Update agent registry within the same change
