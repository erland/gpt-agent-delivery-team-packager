# Bugfix Team Profile

## Purpose

Use this profile for build failures, test failures, runtime bugs, and small corrective changes.

## Source of truth

Use, in order:

1. The user's reported error or failing command from the current chat
2. `docs/active-work.md`
3. `docs/bugfix-plan.md`, if present
4. `docs/agent-progress.md`
5. Relevant source/test files

## Rules

- Reproduce or understand the failure before changing code when possible.
- Make the smallest safe fix.
- Prefer adding or updating a regression test.
- Run the failing command or document the exact command to run locally.
- Do not refactor unrelated code.
- If the bugfix requires multiple steps, store a bugfix plan in `docs/bugfix-plan.md`.
- If a different active bugfix already exists, archive it under `docs/work-history/bugfix/` before replacing it.
