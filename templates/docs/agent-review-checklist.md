# Agent Review Checklist

Use this checklist before marking any step complete.

## Scope

- [ ] The change implements exactly one development-plan step.
- [ ] No unrelated features or refactors were added.
- [ ] The implementation matches the functional specification.

## Code quality

- [ ] Changes are small and reviewable.
- [ ] Responsibilities remain clearly separated.
- [ ] No obvious duplication or avoidable complexity was introduced.
- [ ] No secrets, generated files, build outputs, or local-only files were committed.

## Tests and verification

- [ ] Relevant tests were added or updated.
- [ ] Verification commands were run when possible.
- [ ] Any commands that could not be run are documented exactly.
- [ ] Failures are documented as related, unrelated, or blocking.

## Documentation and progress

- [ ] `docs/agent-progress.md` is updated.
- [ ] Any important assumptions or follow-up risks are recorded.
- [ ] The executor stopped after exactly one step.
