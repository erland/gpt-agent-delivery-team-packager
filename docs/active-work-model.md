# Active Work Model

The agent delivery package supports an active work model so the user can discuss work in chat first, then have
the GPT store the active plan in the repository before execution.

## Core files

```text
docs/active-work.md
docs/feature-plan.md
docs/refactoring-plan.md
docs/bugfix-plan.md
docs/migration-plan.md
docs/work-history/
docs/team-profiles/
```

## Rules

- Assume only one active work item at a time.
- The active work item is recorded in `docs/active-work.md`.
- Chat-provided plans must be stored in `docs/` before implementation.
- If replacing an existing active plan, archive the previous plan under `docs/work-history/<type>/`.
- If the user asks only to create or store a plan, do not implement anything.
- If the user asks to create/store a plan and implement it, implement exactly the first incomplete step.
- If the user asks to continue, use the active plan referenced by `docs/active-work.md`.
