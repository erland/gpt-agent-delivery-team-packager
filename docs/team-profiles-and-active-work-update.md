# Team Profiles and Active Work Update

This update extends the agent delivery package model with selectable team profiles and active work items.

## Team profiles included by default

Generated packages should include:

```text
docs/team-profiles/general-feature-delivery.md
docs/team-profiles/refactoring.md
docs/team-profiles/bugfix.md
docs/team-profiles/architecture-review.md
docs/team-profiles/migration.md
```

The user can switch team behavior by prompt, without regenerating the package.

## Active work files included by default

Generated packages should include:

```text
docs/active-work.md
docs/feature-plan.md
docs/refactoring-plan.md
docs/bugfix-plan.md
docs/migration-plan.md
docs/work-history/.gitkeep
```

## Chat-provided plan workflow

If a plan exists only in chat, the team should store it in the repository package before implementation.

Examples:

- New functionality discussion → create/store `docs/feature-plan.md`
- Refactoring plan from chat → create/store `docs/refactoring-plan.md`
- Bugfix/build failure plan → create/store `docs/bugfix-plan.md`
- Migration plan → create/store `docs/migration-plan.md`

`docs/active-work.md` must point to the active plan.

## One active work item

Assume only one active work item at a time. If replacing an active plan, archive the previous one under:

```text
docs/work-history/<type>/
```

## GPT configuration update

Replace GPT instructions with `docs/step-02-gpt-instructions.md`.

Replace all five knowledge bundles after this update.
