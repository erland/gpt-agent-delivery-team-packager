# Knowledge Bundle — Agent Delivery Package Templates

Use this bundle as reference material for generating the standard package files.



---

# AGENTS.md template

Source: `templates/AGENTS.md`

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




---

# Functional specification template

Source: `templates/docs/functional-specification.md`

# Functional Specification

## Status

Placeholder. Replace this file with the project-specific functional specification.

## Required behavior

TBD

## In scope

TBD

## Out of scope

TBD

## Actors

TBD

## Inputs and outputs

TBD

## Behavior rules

TBD

## Validation and error handling

TBD

## Edge cases

TBD

## Assumptions

TBD




---

# Development plan template

Source: `templates/docs/development-plan.md`

# Development Plan

## Status

Placeholder. Replace this file with the project-specific development plan.

## Execution rule

Each step should be small enough to implement, verify, and review independently.

## Steps

### Step 1 — Replace with first implementation step

Status: Not started

Objective:
- TBD

Expected changes:
- TBD

Verification:
```bash
# Add project-specific verification commands here
```

Completion criteria:
- TBD




---

# Active work template

Source: `templates/docs/active-work.md`

# Active Work

Type: none
Team profile: general-feature-delivery
Active plan: none
Status: No active work
Created from: n/a
Created at: n/a

## Current execution rule

No active work has been selected yet.

When a user provides or requests a work plan in chat, store the active plan under `docs/` before implementation,
update this file to point to the active plan, and then implement exactly one step if implementation was requested.

## Supported work types

- feature
- refactoring
- bugfix
- migration
- architecture-review

## Active work rules

- Only one active work item is assumed at a time.
- If a new active plan replaces an existing one, archive the previous plan under `docs/work-history/<type>/`.
- Do not implement from a chat-only plan until the plan has been stored in `docs/`.
- If the user asks only to create/store a plan, do not implement anything.
- If the user asks to create/store a plan and implement it, implement exactly the first incomplete step.




---

# Feature plan template

Source: `templates/docs/feature-plan.md`

# Active Feature Plan

Source: n/a
Status: No active feature plan

## Objective

TBD

## Constraints

- Keep changes scoped and reviewable.
- Update tests and verification guidance where practical.

## Steps

### Feature Step 1 — TBD

Status: Not started

Objective:
- TBD

Expected changes:
- TBD

Verification:
```bash
# Add project-specific verification commands here
```

Completion criteria:
- TBD




---

# Refactoring plan template

Source: `templates/docs/refactoring-plan.md`

# Active Refactoring Plan

Source: n/a
Status: No active refactoring plan

## Objective

TBD

## Constraints

- Keep changes scoped and reviewable.
- Update tests and verification guidance where practical.

## Steps

### Refactoring Step 1 — TBD

Status: Not started

Objective:
- TBD

Expected changes:
- TBD

Verification:
```bash
# Add project-specific verification commands here
```

Completion criteria:
- TBD




---

# Bugfix plan template

Source: `templates/docs/bugfix-plan.md`

# Active Bugfix Plan

Source: n/a
Status: No active bugfix plan

## Objective

TBD

## Constraints

- Keep changes scoped and reviewable.
- Update tests and verification guidance where practical.

## Steps

### Bugfix Step 1 — TBD

Status: Not started

Objective:
- TBD

Expected changes:
- TBD

Verification:
```bash
# Add project-specific verification commands here
```

Completion criteria:
- TBD




---

# Migration plan template

Source: `templates/docs/migration-plan.md`

# Active Migration Plan

Source: n/a
Status: No active migration plan

## Objective

TBD

## Constraints

- Keep changes scoped and reviewable.
- Update tests and verification guidance where practical.

## Steps

### Migration Step 1 — TBD

Status: Not started

Objective:
- TBD

Expected changes:
- TBD

Verification:
```bash
# Add project-specific verification commands here
```

Completion criteria:
- TBD




---

# Agent delivery runbook template

Source: `templates/docs/agent-delivery-runbook.md`

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




---

# Agent progress template

Source: `templates/docs/agent-progress.md`

# Agent Progress

## Current status

No steps completed yet.

## Step history

### Step 1 — Replace with plan step title

Status: Not started

Executor:
- TBD

Changed files:
- TBD

Verification:
- TBD

Result:
- TBD

Notes:
- TBD




---

# Agent review checklist template

Source: `templates/docs/agent-review-checklist.md`

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




---

# ChatGPT zip workflow template

Source: `templates/docs/chatgpt-zip-workflow.md`

# ChatGPT Zip Workflow

## Purpose

This document describes how to exchange project zips with ChatGPT while keeping the repository clean and reviewable.

## Directory convention

Use:

```text
.chatgpt-zips/
  outgoing/
  incoming/
  applied/
```

These directories are local exchange artifacts and should be ignored by Git.

## Upload workflow

1. Start from a clean Git working tree.
2. Run:

```bash
scripts/zip-for-chatgpt.sh
```

3. Upload the generated zip from `.chatgpt-zips/outgoing/`.
4. Ask ChatGPT:

```text
Use the agent delivery team package instructions.
Implement exactly the next incomplete step.
Return an updated zip.
```

## Apply returned zip

1. Save the returned zip under `.chatgpt-zips/incoming/`.
2. Apply it:

```bash
scripts/apply-chatgpt-zip.sh .chatgpt-zips/incoming/<returned-file>.zip
```

3. Inspect:

```bash
git status
git diff
```

4. Run verification commands.
5. Commit if the change is good.

## Delete behavior

The apply script should be conservative by default. It should not delete missing files unless explicitly invoked with:

```bash
scripts/apply-chatgpt-zip.sh .chatgpt-zips/incoming/<returned-file>.zip --delete-missing
```

Protected paths must never be deleted by the script:

```text
.git/
.chatgpt-zips/
.env
.env.*
.idea/
.vscode/
```


## Optional validation

Generated packages may include:

```bash
python3 scripts/validate-zip-workflow-scripts.py
```

Use it to check that zip workflow scripts and documentation include the expected safety behavior.


## `.gitignore` validation

Generated packages may include:

```bash
python3 scripts/validate-gitignore-convention.py
```

Use it to confirm `.chatgpt-zips/`, `*.zip`, and common build/cache outputs are ignored.




---

# General feature delivery team profile

Source: `templates/docs/team-profiles/general-feature-delivery.md`

# General Feature Delivery Team Profile

## Purpose

Use this profile for planned feature implementation and ordinary development-plan work.

## Source of truth

Use, in order:

1. `docs/active-work.md`
2. `docs/feature-plan.md` if active work type is `feature`
3. `docs/functional-specification.md`
4. `docs/development-plan.md`
5. `docs/agent-progress.md`
6. `docs/agent-review-checklist.md`

## Rules

- Implement exactly one incomplete feature/development step.
- Keep diffs scoped to the selected step.
- Add or update tests for changed behavior.
- Preserve existing behavior unless the plan explicitly changes it.
- If the user provides only a feature discussion in chat, create and store a step-by-step plan in `docs/feature-plan.md` before implementation.
- If the user asks only to create the plan, do not implement anything.
- If the user asks to create the plan and implement it, implement exactly the first incomplete step.




---

# Refactoring team profile

Source: `templates/docs/team-profiles/refactoring.md`

# Refactoring Team Profile

## Purpose

Use this profile for step-by-step refactoring plans and behavior-preserving structural improvements.

## Source of truth

Use, in order:

1. `docs/active-work.md`
2. `docs/refactoring-plan.md`
3. `docs/agent-progress.md`
4. `docs/agent-review-checklist.md`
5. `docs/functional-specification.md`, if present, to understand externally visible behavior

## Rules

- Preserve externally visible behavior unless the plan explicitly requires a behavior change.
- Do not add features.
- Prefer small, reversible changes.
- Reduce complexity, improve boundaries, or improve maintainability according to the selected step.
- Add or preserve regression tests where practical.
- Stop if behavior change seems necessary but is not documented.
- If the user provides a refactoring plan in chat, store it in `docs/refactoring-plan.md` before implementation.
- If a different active refactoring already exists, archive it under `docs/work-history/refactoring/` before replacing it.
- Implement exactly one incomplete refactoring step.




---

# Bugfix team profile

Source: `templates/docs/team-profiles/bugfix.md`

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




---

# Architecture review team profile

Source: `templates/docs/team-profiles/architecture-review.md`

# Architecture Review Team Profile

## Purpose

Use this profile for source-code analysis, architecture review, dependency mapping, risk review, and plan creation.

## Source of truth

Use, in order:

1. The user's review question or analysis request
2. Existing architecture rules or documentation
3. Source code and configuration files
4. `docs/agent-review-checklist.md`

## Rules

- Read-only by default.
- Do not edit source code unless the user explicitly asks for implementation.
- Produce findings, reports, diagrams, or implementation/refactoring plans.
- Prefer concrete file/module references and prioritized recommendations.
- If implementation is requested after the review, first store a plan under `docs/feature-plan.md`, `docs/refactoring-plan.md`, or another active plan file.




---

# Migration team profile

Source: `templates/docs/team-profiles/migration.md`

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




---

# .gitignore section template

Source: `templates/git/gitignore-section.txt`

# Agent delivery / ChatGPT zip exchange artifacts
.chatgpt-zips/
*.zip

# Common build/cache outputs
node_modules/
target/
build/
dist/
coverage/
.next/
.vite/
.gradle/
out/
*.tsbuildinfo
.DS_Store


