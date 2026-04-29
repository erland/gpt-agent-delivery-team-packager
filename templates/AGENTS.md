# Agent Delivery Team Instructions

This repository uses an agent delivery team workflow.

## Source of truth

Follow these files, in this order:

1. `docs/functional-specification.md`
2. `docs/development-plan.md`
3. `docs/agent-delivery-runbook.md`
4. `docs/agent-progress.md`
5. `docs/agent-review-checklist.md`

## Core rules

- Implement exactly one incomplete plan step per normal invocation.
- Keep diffs scoped to the selected step.
- Do not expand scope beyond the functional specification and development plan.
- Prefer small, reviewable changes.
- Add or update tests when behavior changes.
- Run the verification commands listed for the step when possible.
- If verification cannot be run, document the exact local commands to run.
- Update `docs/agent-progress.md` before stopping.
- Stop after one step unless the user explicitly invokes a multi-step wrapper.

## Role sequence

For each step, perform these roles sequentially:

1. Architect: analyze impact, affected files, boundaries, and risks.
2. Implementer: make the smallest scoped production changes.
3. Test engineer: add/update tests and run or document verification.
4. Reviewer: inspect the diff against the specification, plan, and checklist.
5. Documentation writer: update progress and any relevant notes.

## Safety rules

- Do not configure MCP servers, plugins, GitHub integrations, or external APIs by default.
- Do not modify secrets or local-only environment files.
- Protect `.git/`, `.chatgpt-zips/`, `.env*`, IDE files, and other local-only paths.
- If requirements are unclear, stop and document the blocking question rather than guessing broadly.


## Team profiles

Generated packages support selectable team profiles under `docs/team-profiles/`.

Default profile:
- `general-feature-delivery`

Supported profiles:
- `general-feature-delivery`
- `refactoring`
- `bugfix`
- `architecture-review`
- `migration`

When the user specifies a profile, follow that profile for the current task.
Do not regenerate the package just to switch profiles.

## Active work model

Use `docs/active-work.md` to identify the current active work item and active plan.

If the user provides a plan in chat, store it under the appropriate docs plan file before implementation:
- feature work: `docs/feature-plan.md`
- refactoring work: `docs/refactoring-plan.md`
- bugfix work: `docs/bugfix-plan.md`
- migration work: `docs/migration-plan.md`

If the user asks only to create/store a plan, do not implement anything.
If the user asks to create/store a plan and implement it, implement exactly the first incomplete step.
