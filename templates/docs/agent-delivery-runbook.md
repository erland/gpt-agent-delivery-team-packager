# Agent Delivery Runbook

## Purpose

This runbook defines how to execute the development plan using either Codex CLI or the ChatGPT zip workflow.

## Active work setup

Before implementation:

1. Determine the selected team profile. Use `general-feature-delivery` if none is specified.
2. Read the selected profile under `docs/team-profiles/`.
3. Read `docs/active-work.md`.
4. If the user provided a plan in chat, store it in the appropriate active plan file before implementation.
5. If replacing an existing active plan, archive the old plan under `docs/work-history/<type>/`.
6. If the user asked only to create/store a plan, update docs and stop without implementation.

## Normal one-step delivery loop

1. Read `docs/agent-progress.md`.
2. Find the first incomplete step in the active plan referenced by `docs/active-work.md`, or in `docs/development-plan.md` when no active work is set.
3. Perform architect impact analysis.
4. Implement only the selected step.
5. Add or update tests when behavior changes.
6. Run the verification commands listed for the step, when possible.
7. Review the diff against:
   - `docs/functional-specification.md`
   - `docs/development-plan.md`
   - `docs/agent-review-checklist.md`
8. Update `docs/agent-progress.md`.
9. Stop after exactly one step.

## Codex CLI workflow

Use:

```bash
scripts/codex-next-step.sh
```

For multiple guarded iterations:

```bash
scripts/codex-run-plan.sh 3
```

The multi-step wrapper must still run one step at a time and stop if blocked or verification fails.

## ChatGPT zip workflow fallback

When the whole project/package is uploaded to ChatGPT as a zip and the user asks for an updated zip,
ChatGPT should use this fallback:

1. Read `AGENTS.md`.
2. Read `docs/functional-specification.md`.
3. Read `docs/development-plan.md`.
4. Read `docs/agent-progress.md`.
5. Read `docs/agent-review-checklist.md`.
6. Identify the first incomplete step.
7. Simulate the roles sequentially in one response:
   - Architect: impact analysis, affected files, risks, boundaries.
   - Implementer: scoped source changes.
   - Test engineer: add/update tests or document verification commands.
   - Reviewer: check diff against spec, plan, and checklist.
   - Documentation writer: update `docs/agent-progress.md`.
8. Return an updated zip.
9. If tests/builds cannot be run, document exact local verification commands.
10. Stop after exactly one step.

Note: `.codex/agents/*.toml` files are active custom agents for Codex CLI but only readable
reference instructions in ChatGPT zip workflows.

## Blocked work

If the next step cannot be completed safely, update `docs/agent-progress.md` with:

- blocked status,
- reason,
- files inspected,
- commands attempted,
- exact question or missing input required.
