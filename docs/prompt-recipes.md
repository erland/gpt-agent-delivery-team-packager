# Prompt Recipes

Use these ready-to-copy prompts when working with the Agent Delivery Team Packager GPT from the ChatGPT client.

## How to use this file

Pick the scenario that matches what you want to do, copy the prompt, and replace placeholders such as:

```text
[ATTACH PROJECT ZIP]
[ATTACH SPEC FILE]
[ATTACH PLAN FILE]
[PASTE PLAN HERE]
[PASTE ERROR HERE]
```

## 1. Store a functional specification and development plan only

Use when you want to set up the package and active work, but not implement anything yet.

```text
Use the general-feature-delivery team profile.

I have uploaded:
- the current project zip
- a functional specification
- a development plan

Add or update the agent delivery team package in the project zip.

Store the uploaded functional specification as:
docs/functional-specification.md

Store the uploaded development plan as:
docs/development-plan.md

Set docs/active-work.md to:
- Type: feature
- Team profile: general-feature-delivery
- Active plan: docs/development-plan.md
- Status: In progress

Do not implement anything yet.

Return an updated project zip.
```

## 2. Store a functional specification/development plan and implement first step

```text
Use the general-feature-delivery team profile.

I have uploaded:
- the current project zip
- a functional specification
- a development plan

Add or update the agent delivery team package in the project zip.

Store the uploaded functional specification as:
docs/functional-specification.md

Store the uploaded development plan as:
docs/development-plan.md

Set docs/active-work.md to:
- Type: feature
- Team profile: general-feature-delivery
- Active plan: docs/development-plan.md
- Status: In progress

Then implement exactly the first incomplete step from docs/development-plan.md.

Follow the agent delivery runbook:
- keep the diff scoped,
- update or add tests where appropriate,
- update docs/agent-progress.md,
- document exact local verification commands if you cannot run them,
- stop after exactly one step.

Return an updated project zip.
```

## 3. Store a refactoring plan only

Use when you have a refactoring plan in chat or uploaded as a file, but want no implementation yet.

```text
Use the refactoring team profile.

I have uploaded or pasted a refactoring plan.

Store it as:
docs/refactoring-plan.md

Set docs/active-work.md to:
- Type: refactoring
- Team profile: refactoring
- Active plan: docs/refactoring-plan.md
- Status: In progress

If an active refactoring plan already exists and this is a new plan, archive the old one under:
docs/work-history/refactoring/

Do not implement anything yet.

Return an updated project zip.

[PASTE PLAN HERE IF NOT UPLOADED AS A FILE]
```

## 4. Store a refactoring plan and implement first step

```text
Use the refactoring team profile.

I have uploaded or pasted a refactoring plan.

Store it as:
docs/refactoring-plan.md

Set docs/active-work.md to:
- Type: refactoring
- Team profile: refactoring
- Active plan: docs/refactoring-plan.md
- Status: In progress

If an active refactoring plan already exists and this is a new plan, archive the old one under:
docs/work-history/refactoring/

Then implement exactly the first incomplete step from docs/refactoring-plan.md.

Refactoring rules:
- preserve externally visible behavior unless the plan explicitly changes it,
- do not add features,
- keep the diff small and reversible,
- add or preserve regression coverage where practical,
- update docs/agent-progress.md,
- document exact local verification commands if tests/builds cannot be run,
- stop after exactly one step.

Return an updated project zip.

[PASTE PLAN HERE IF NOT UPLOADED AS A FILE]
```

## 5. Store a feature implementation plan only

```text
Use the general-feature-delivery team profile.

I have uploaded or pasted a step-by-step feature implementation plan.

Store it as:
docs/feature-plan.md

Set docs/active-work.md to:
- Type: feature
- Team profile: general-feature-delivery
- Active plan: docs/feature-plan.md
- Status: In progress

If an active feature plan already exists and this is a new feature, archive the old one under:
docs/work-history/feature/

Do not implement anything yet.

Return an updated project zip.

[PASTE PLAN HERE IF NOT UPLOADED AS A FILE]
```

## 6. Store a feature implementation plan and implement first step

```text
Use the general-feature-delivery team profile.

I have uploaded or pasted a step-by-step feature implementation plan.

Store it as:
docs/feature-plan.md

Set docs/active-work.md to:
- Type: feature
- Team profile: general-feature-delivery
- Active plan: docs/feature-plan.md
- Status: In progress

If an active feature plan already exists and this is a new feature, archive the old one under:
docs/work-history/feature/

Then implement exactly the first incomplete step from docs/feature-plan.md.

Follow the agent delivery runbook:
- keep the diff scoped,
- update or add tests where appropriate,
- update docs/agent-progress.md,
- document exact local verification commands if tests/builds cannot be run,
- stop after exactly one step.

Return an updated project zip.

[PASTE PLAN HERE IF NOT UPLOADED AS A FILE]
```

## 7. Create a feature plan from a chat discussion only

Use when you have discussed the feature but do not yet have a step-by-step plan.

```text
Use the general-feature-delivery team profile.

Based on the functionality we discussed in this chat, create a step-by-step implementation plan.

Store it as:
docs/feature-plan.md

Set docs/active-work.md to:
- Type: feature
- Team profile: general-feature-delivery
- Active plan: docs/feature-plan.md
- Status: In progress

Do not implement anything yet.

Return an updated project zip.
```

## 8. Create a feature plan from chat and implement first step

```text
Use the general-feature-delivery team profile.

Based on the functionality we discussed in this chat, create a step-by-step implementation plan.

Store it as:
docs/feature-plan.md

Set docs/active-work.md to:
- Type: feature
- Team profile: general-feature-delivery
- Active plan: docs/feature-plan.md
- Status: In progress

Then implement exactly the first incomplete step.

Follow the agent delivery runbook.
Update docs/agent-progress.md.
Document exact local verification commands if tests/builds cannot be run.
Stop after exactly one step.

Return an updated project zip.
```

## 9. Continue the active plan

Use after the project already contains docs/active-work.md and an active plan.

```text
Use the active team profile from docs/active-work.md.

Continue the active plan and implement exactly the next incomplete step.

Follow docs/agent-delivery-runbook.md.
Update docs/agent-progress.md.
Document exact local verification commands if tests/builds cannot be run.
Stop after exactly one step.

Return an updated project zip.
```

## 10. Fix build/test errors using the bugfix profile

```text
Use the bugfix team profile.

The latest returned zip has the following build/test error.

Fix only the error related to the current active step.
Add or update regression coverage if appropriate.
Update docs/agent-progress.md.
Document the exact verification command.
Stop after exactly one bugfix step.

Return an updated project zip.

[PASTE ERROR HERE]
```

## 11. Store a bugfix plan only

```text
Use the bugfix team profile.

I have uploaded or pasted a bugfix plan or failure analysis.

Store it as:
docs/bugfix-plan.md

Set docs/active-work.md to:
- Type: bugfix
- Team profile: bugfix
- Active plan: docs/bugfix-plan.md
- Status: In progress

If an active bugfix plan already exists and this is a new bugfix, archive the old one under:
docs/work-history/bugfix/

Do not implement anything yet.

Return an updated project zip.

[PASTE BUGFIX PLAN OR FAILURE ANALYSIS HERE IF NOT UPLOADED AS A FILE]
```

## 12. Architecture review only

```text
Use the architecture-review team profile.

Review the uploaded project zip according to the request below.
Do not edit source code.
Do not implement anything.

Produce the requested analysis or plan.
If a plan is created, store it under the appropriate docs/*-plan.md file and update docs/active-work.md only if I explicitly ask for it.

Return an updated zip only if documentation files are added or changed.

[DESCRIBE REVIEW REQUEST HERE]
```

## 13. Migration plan only

```text
Use the migration team profile.

I have uploaded or pasted a migration plan.

Store it as:
docs/migration-plan.md

Set docs/active-work.md to:
- Type: migration
- Team profile: migration
- Active plan: docs/migration-plan.md
- Status: In progress

If an active migration plan already exists and this is a new migration, archive the old one under:
docs/work-history/migration/

Do not implement anything yet.

Return an updated project zip.

[PASTE MIGRATION PLAN HERE IF NOT UPLOADED AS A FILE]
```

## 14. Migration plan and first step

```text
Use the migration team profile.

I have uploaded or pasted a migration plan.

Store it as:
docs/migration-plan.md

Set docs/active-work.md to:
- Type: migration
- Team profile: migration
- Active plan: docs/migration-plan.md
- Status: In progress

Then implement exactly the first incomplete step from docs/migration-plan.md.

Migration rules:
- preserve behavior and parity unless the plan explicitly changes it,
- migrate incrementally,
- keep rollback path clear where practical,
- add/update tests that prove parity and compatibility,
- update docs/agent-progress.md,
- document exact local verification commands if tests/builds cannot be run,
- stop after exactly one step.

Return an updated project zip.

[PASTE MIGRATION PLAN HERE IF NOT UPLOADED AS A FILE]
```
