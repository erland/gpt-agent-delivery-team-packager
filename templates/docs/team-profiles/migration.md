# Migration Team Profile

## Purpose

Use this profile for framework, language, platform, API, database, or UI migration work.

## Source of truth

Use, in order:

1. `docs/active-work.md`
2. `docs/migration-plan.md`
3. `docs/functional-specification.md`
4. `docs/development-plan.md`
5. `docs/agent-progress.md`
6. `docs/agent-review-checklist.md`

## Rules

- Preserve behavior and parity unless the migration plan explicitly changes it.
- Migrate incrementally.
- Keep rollback path clear where practical.
- Track old vs new behavior.
- Add/update tests that prove parity and compatibility.
- If the user provides a migration plan in chat, store it in `docs/migration-plan.md` before implementation.
- If a different active migration already exists, archive it under `docs/work-history/migration/` before replacing it.
- Implement exactly one incomplete migration step.
