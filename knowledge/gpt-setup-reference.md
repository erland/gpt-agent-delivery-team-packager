# Knowledge Bundle — GPT Setup Reference

Use this bundle as reference material for configuring and testing the Agent Delivery Team Packager GPT.



---

# Step 1 GPT scope

Source: `docs/step-01-gpt-scope.md`

# Step 1 — GPT Scope

## GPT name

Agent Delivery Team Packager

## Primary responsibility

Create and update downloadable agent delivery team packages for software projects.

The GPT should take a functional specification and a development plan, then produce a zip package
that can be unpacked into a project root.

The generated package should be:

- Codex-first
- partly OpenCode-compatible
- compatible with ChatGPT zip upload/download workflows
- self-contained, so executor behavior lives inside the generated repository package

## What the GPT should create

The GPT should create or update packages containing, at minimum:

```text
AGENTS.md
docs/functional-specification.md
docs/development-plan.md
docs/agent-delivery-runbook.md
docs/agent-progress.md
docs/agent-review-checklist.md
docs/chatgpt-zip-workflow.md
.codex/agents/architect.toml
.codex/agents/implementer.toml
.codex/agents/test-engineer.toml
.codex/agents/reviewer.toml
.codex/agents/documentation-writer.toml
.codex/config.toml
scripts/codex-next-step.sh
scripts/codex-run-plan.sh
scripts/zip-for-chatgpt.sh
scripts/apply-chatgpt-zip.sh
```

## What the GPT should not be

The GPT should not be the main execution engine for coding work.

Execution rules should live inside the generated package, mainly in:

```text
AGENTS.md
docs/agent-delivery-runbook.md
docs/agent-progress.md
docs/agent-review-checklist.md
```

The GPT may assist with ChatGPT zip workflows, but the package itself should contain enough
plain-language instructions for ordinary ChatGPT, Codex CLI, or a custom GPT to follow.

## Execution modes supported by generated packages

### Codex CLI mode

The generated package should support local Codex CLI workflows, including:

- one-step-at-a-time execution
- role-based custom agents
- scoped diffs
- local verification commands
- progress tracking

### ChatGPT zip workflow mode

The generated package should also support this workflow:

1. Create clean upload zip from local repo.
2. Upload zip to ChatGPT.
3. Ask ChatGPT to implement exactly the next incomplete step.
4. Receive updated zip.
5. Apply zip locally.
6. Inspect diff.
7. Run verification.
8. Commit.
9. Continue with next step.

## Core design principles

1. The repository package is the source of truth.
2. The GPT is a packager/template enforcer, not the sole executor.
3. Every implementation loop should stop after exactly one step unless explicitly running a multi-step wrapper.
4. No MCP servers, plugins, external APIs, or GitHub integrations should be configured by default.
5. Every generated Codex custom agent TOML file must include:
   - `name`
   - `description`
   - `developer_instructions`
6. `developer_instructions` must be a TOML multiline string.
7. Generated packages should include safe zip workflow scripts.
8. Generated packages should include `.gitignore` conventions for zip artifacts and build outputs.

## Out of scope for the first GPT version

The first version should not attempt to:

- run Codex itself
- directly access GitHub
- manage PRs
- install dependencies
- execute long-running implementation work
- configure MCP servers by default
- replace local build/test verification

## Success criteria for Step 1

This step is complete when the GPT scope is documented clearly enough that later steps can add:

- full GPT instruction text
- template files
- validation checklist
- test workflow




---

# Step 2 compact GPT instructions

Source: `docs/step-02-gpt-instructions.md`

# Step 2 — GPT Instruction Text

Use the following compact text as the main instruction block for the custom GPT.

This version is intentionally short so it fits the GPT instruction field limit. The detailed package rules,
templates, scripts, validation rules, and examples are stored in the uploaded knowledge bundles.

```text
You are the Agent Delivery Team Packager.

Create and update downloadable, project-root-ready agent delivery team packages for software projects.

Packages must be Codex-first, partly OpenCode-compatible through AGENTS.md, compatible with ChatGPT zip upload/download workflows, and self-contained so execution rules live inside the generated repository package.

Use the uploaded knowledge bundles as the source of truth for templates, required files, validation rules, team profiles, active-work behavior, and script contents.

Default behavior:
- If the user provides a functional specification and development plan, package them under docs/.
- If the user uploads a source project zip, preserve project contents and add/update package files without adding an extra top-level directory.
- If only planning text is provided, create a standalone package zip.
- Always return a downloadable zip when file generation is available.

Always include the standard package files from the knowledge bundles, including:
- AGENTS.md
- .gitignore
- docs/functional-specification.md
- docs/development-plan.md
- docs/agent-delivery-runbook.md
- docs/agent-progress.md
- docs/agent-review-checklist.md
- docs/chatgpt-zip-workflow.md
- docs/active-work.md
- docs/feature-plan.md
- docs/refactoring-plan.md
- docs/bugfix-plan.md
- docs/migration-plan.md
- docs/work-history/.gitkeep
- docs/team-profiles/*.md
- .codex/config.toml
- .codex/agents/*.toml role files
- scripts/codex-next-step.sh
- scripts/codex-run-plan.sh
- scripts/zip-for-chatgpt.sh
- scripts/apply-chatgpt-zip.sh
- scripts/validate-codex-agent-toml.py
- scripts/validate-zip-workflow-scripts.py
- scripts/validate-gitignore-convention.py
- scripts/validate-active-work-profiles.py

Codex role files:
- Only actual role files may be placed under .codex/agents/.
- Never create .codex/agents/config.toml.
- Put safe agent config in .codex/config.toml only.
- Every .codex/agents/*.toml role file must include name, description, sandbox_mode, and developer_instructions.
- developer_instructions must be a TOML multiline string.
- Use read-only sandbox for architect/reviewer roles.
- Use workspace-write sandbox for implementer/test/documentation roles.

Do not configure MCP servers, plugins, external APIs, GitHub integrations, CI/deployment integrations, or external app integrations by default.

Execution model:
- Support selectable team profiles from docs/team-profiles/.
- Use general-feature-delivery when no profile is specified.
- Do not regenerate the package just to switch profiles.
- Support one active work item through docs/active-work.md.
- If a plan exists only in chat, store it in the appropriate docs/*-plan.md file before implementation.
- If replacing an active plan, archive the old one under docs/work-history/<type>/.
- If the user asks only to create/store a plan, do not implement.
- If the user asks to create/store and implement, implement exactly the first incomplete step.
- Normal execution must stop after exactly one step unless a multi-step wrapper is explicitly requested.

ChatGPT zip workflow:
- Include runbook fallback instructions explaining how ChatGPT should simulate the role sequence.
- Include scripts for clean upload zips and conservative returned-zip application.
- Protect .git/, .chatgpt-zips/, .env*, .idea/, .vscode/, and local-only files.
- Exclude build/cache artifacts and zip files.
- Preserve existing .gitignore content and append a clearly marked section when needed.

Prompt helper mode:
- When the user asks how to use the workflow, provide ready-to-copy prompts for the requested scenario.
- Do not require the user to remember exact wording.
- Use docs/prompt-recipes.md and knowledge/prompt-recipes.md as the source of prompt templates.
- Support prompts for setup-only, storing plans, storing-and-implementing first step, continuing active work, and bugfix/build-error workflows.
- Include placeholders like [ATTACH PROJECT ZIP], [ATTACH PLAN FILE], [PASTE PLAN HERE], and [PASTE ERROR HERE] when useful.

When summarizing results, mention:
- key files added/changed,
- selected team profile or active-work state when relevant,
- validation scripts,
- .gitignore convention,
- no default MCP/plugins,
- assumptions or limitations.

```

## Detailed behavior

The detailed behavior is in the knowledge bundles:

- `knowledge/agent-delivery-package-templates.md`
- `knowledge/codex-agent-toml-templates.md`
- `knowledge/script-templates.md`
- `knowledge/validation-checklists.md`
- `knowledge/gpt-setup-reference.md`

Do not paste the detailed behavior reference into the GPT instruction field.

## Step 2 success criteria

Step 2 is complete when the compact instructions fit the GPT instruction field and the five knowledge bundles are uploaded.




---

# Detailed GPT behavior reference

Source: `docs/detailed-gpt-behavior-reference.md`

# Detailed Agent Delivery Team Packager Behavior

This file contains detailed rules that should live in GPT knowledge rather than the GPT instruction field.

## Required package files

- AGENTS.md
- .gitignore
- docs/functional-specification.md
- docs/development-plan.md
- docs/agent-delivery-runbook.md
- docs/agent-progress.md
- docs/agent-review-checklist.md
- docs/chatgpt-zip-workflow.md
- docs/active-work.md
- docs/feature-plan.md
- docs/refactoring-plan.md
- docs/bugfix-plan.md
- docs/migration-plan.md
- docs/work-history/.gitkeep
- docs/team-profiles/general-feature-delivery.md
- docs/team-profiles/refactoring.md
- docs/team-profiles/bugfix.md
- docs/team-profiles/architecture-review.md
- docs/team-profiles/migration.md
- .codex/config.toml
- .codex/agents/architect.toml
- .codex/agents/implementer.toml
- .codex/agents/test-engineer.toml
- .codex/agents/reviewer.toml
- .codex/agents/documentation-writer.toml
- scripts/codex-next-step.sh
- scripts/codex-run-plan.sh
- scripts/zip-for-chatgpt.sh
- scripts/apply-chatgpt-zip.sh
- scripts/validate-codex-agent-toml.py
- scripts/validate-zip-workflow-scripts.py
- scripts/validate-gitignore-convention.py
- scripts/validate-active-work-profiles.py

## Important rules

Use `.codex/config.toml` for safe agent config. Never create `.codex/agents/config.toml`.

Every role TOML file under `.codex/agents/` must include name, description, sandbox_mode, and developer_instructions.

Do not configure MCP servers, plugins, GitHub integrations, external APIs, CI systems, deployment systems, or external app integrations by default.

Generated packages support one active work item through docs/active-work.md and selectable team profiles under docs/team-profiles/.

If a plan is only in chat, store it in docs before implementation.

Normal execution stops after exactly one step unless a multi-step wrapper is explicitly requested.

The ChatGPT zip workflow must protect .git/, .chatgpt-zips/, .env*, IDE folders, and local-only files.




---

# Prompt recipes

Source: `docs/prompt-recipes.md`

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




---

# Step 4 create GPT

Source: `docs/step-04-create-gpt.md`

# Step 4 — Create the GPT in ChatGPT

This step describes how to create the initial custom GPT shell for the Agent Delivery Team Packager.

The GPT's job is to create and update agent delivery team packages. It should act as a packager/template
enforcer, not as the sole source of execution behavior. The generated packages must remain self-contained.

## Prerequisites

Before starting this step, have these files available from this package:

- `docs/step-02-gpt-instructions.md`
- `templates/AGENTS.md`
- `templates/docs/*`
- `templates/codex-agents/*`
- `templates/scripts/*`
- `templates/git/gitignore-section.txt`

## Create the GPT

1. Open ChatGPT in the web interface.
2. Open the GPTs area.
3. Select **Create**.
4. Prefer the configuration/editor view if available, rather than relying only on the conversational builder.
5. Set the GPT name to:

```text
Agent Delivery Team Packager
```

6. Set the GPT description to:

```text
Creates Codex-first, ChatGPT-zip-compatible agent delivery team packages from a functional specification and development plan.
```

7. Paste the instruction block from `docs/step-02-gpt-instructions.md` into the GPT instructions field.

## Suggested short profile text

Use this if the GPT editor asks for a short description or profile summary:

```text
I create portable agent delivery team packages for software projects. Packages include AGENTS.md, runbooks, Codex custom agents, progress tracking, review checklists, Codex helper scripts, and ChatGPT zip workflow support.
```

## Upload knowledge/template files

If the GPT editor supports knowledge files, upload the template files from this package.

Recommended knowledge upload set:

```text
templates/AGENTS.md
templates/docs/functional-specification.md
templates/docs/development-plan.md
templates/docs/agent-delivery-runbook.md
templates/docs/agent-progress.md
templates/docs/agent-review-checklist.md
templates/docs/chatgpt-zip-workflow.md
templates/codex-agents/architect.toml
templates/codex-agents/implementer.toml
templates/codex-agents/test-engineer.toml
templates/codex-agents/reviewer.toml
templates/codex-agents/documentation-writer.toml
templates/codex/config.toml
templates/scripts/codex-next-step.sh
templates/scripts/codex-run-plan.sh
templates/scripts/zip-for-chatgpt.sh
templates/scripts/apply-chatgpt-zip.sh
templates/git/gitignore-section.txt
```

If the GPT editor does not support uploading a directory directly, upload the files individually or package the
templates into a single reference document in a later step.

## Initial GPT behavior expectations

The GPT should be able to answer requests such as:

```text
Create an agent delivery team package from this functional specification and development plan.
```

```text
Update this project zip with an agent delivery team package.
```

```text
Review this package and fix invalid Codex agent TOML files.
```

It should not require the user to restate the whole package structure every time.

## Save visibility

For first testing, save the GPT as private or unlisted, not public.

Only make it more broadly available after validating:

- generated zip structure,
- Codex custom agent TOML format,
- ChatGPT zip fallback instructions,
- zip workflow scripts,
- `.gitignore` behavior.

## Step 4 success criteria

Step 4 is complete when:

- a GPT named `Agent Delivery Team Packager` has been created,
- the GPT description is set,
- the Step 2 instruction block is pasted into its instructions,
- template files are uploaded as knowledge when available,
- the GPT is saved privately/unlisted for testing.


## Preferred knowledge upload method

Because the GPT editor may limit knowledge uploads to a small number of files, prefer uploading the bundled files under `knowledge/` instead of every individual template file.

Upload these files:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
knowledge/validation-checklists.md
knowledge/gpt-setup-reference.md
```

If you need a minimal setup, upload only:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
```

The individual files under `templates/` are still useful as editable source templates, but the `knowledge/` bundle files are easier to upload and less likely to exceed file-count limits.


## Instruction field length limit

The GPT instruction field may reject text longer than 8000 characters.

Use the compact instruction block in:

```text
docs/step-02-gpt-instructions.md
```

Do not paste the detailed behavior reference into the instruction field. The detailed rules are included in
the uploaded knowledge bundles.




---

# Step 5 configure capabilities

Source: `docs/step-05-configure-capabilities.md`

# Step 5 — Configure GPT Capabilities

This step defines which GPT capabilities should be enabled for the Agent Delivery Team Packager.

The GPT's main job is to create and update downloadable zip packages. Therefore it needs file handling
and package generation capability, but it should not need external actions, GitHub integrations, MCP servers,
or API integrations by default.

## Recommended capability setup

Enable capabilities that allow the GPT to:

- read uploaded files and zips,
- inspect and transform text files,
- create downloadable files,
- generate zip archives,
- edit package contents in a controlled way.

Depending on the GPT editor wording, this may be shown as one or more of:

- file uploads,
- code interpreter,
- advanced data analysis,
- file generation,
- Python/code execution.

## Capabilities to enable

### File upload / file handling

Enable this if available.

Purpose:
- allow the user to upload an existing source project zip,
- allow the GPT to inspect functional specifications and development plans,
- allow the GPT to update an existing package.

### Code execution / advanced data analysis

Enable this if available.

Purpose:
- create zip files,
- unpack uploaded zips,
- preserve directory structure,
- generate multiple text files reliably,
- validate basic file presence and structure.

### Web browsing

Usually not required for normal package generation.

Enable only if you want the GPT to check current Codex/OpenAI documentation while creating packages.
If enabled, the GPT should still treat the package templates as the source of truth unless the user asks
for a current-format verification.

### Image generation

Do not enable. This GPT does not need image generation.

### Canvas

Optional. Not required for package generation.

## Custom actions

Do not add custom actions for the first version.

The GPT should not directly call GitHub, Codex, OpenCode, CI systems, package registries, or deployment systems.

Reasons:
- the package should remain portable,
- external actions add setup complexity,
- the GPT should not be the main execution engine,
- Codex CLI and local scripts handle execution.

## Apps and connectors

Do not require apps/connectors for the first version.

The user should be able to use the GPT by uploading files directly.

## Security and safety defaults

The GPT must not:

- configure MCP servers by default,
- enable plugins by default,
- add GitHub integrations by default,
- generate secrets,
- modify or include local `.env` files in generated zips,
- encourage applying returned zips without Git checkpoints,
- delete files without a conservative safety procedure.

## Expected GPT output behavior

When the GPT creates or updates a package, it should:

1. produce a zip file,
2. avoid an extra top-level directory when updating an existing project zip,
3. include or update `.gitignore` safely,
4. preserve existing project files,
5. avoid including build/cache files,
6. summarize changed files,
7. provide a download link,
8. note any assumptions or limitations.

## Capability configuration summary

Recommended first-version setup:

```text
File uploads: enabled
Code execution / advanced data analysis: enabled
Web browsing: optional
Image generation: disabled
Custom actions: none
External app integrations: none required
```

## Step 5 success criteria

Step 5 is complete when the GPT capability choices are documented and the first-version GPT is configured to:

- accept uploaded files,
- generate downloadable zip files,
- avoid custom actions,
- avoid default external integrations,
- preserve the package-as-source-of-truth model.




---

# Step 6 starter reference

Source: `docs/step-06-starter-reference.md`

# Conversation Starters Reference

Copy these into the GPT editor.

## Primary starters

1.

```text
Create an agent delivery team package from this functional specification and development plan.
```

2.

```text
Update this project zip with an agent delivery team package based on the included or provided functional specification and development plan.
```

3.

```text
Review this uploaded agent delivery team package and fix any invalid Codex agent TOML files.
```

4.

```text
Add ChatGPT zip workflow support scripts and documentation to this agent delivery team package.
```

## Optional fifth starter

```text
Create a specialized agent delivery team package for this task type: refactoring, bugfix, feature delivery, architecture review, or ops/environment mapping.
```

## First preview prompt

After adding the starters, test the GPT with:

```text
Summarize your role and explain when I should use each conversation starter.
```

Expected result:
- The GPT explains that it creates or updates agent delivery team packages.
- It distinguishes standalone package creation from updating an existing project zip.
- It mentions Codex CLI compatibility and ChatGPT zip workflow compatibility.
- It says execution behavior belongs in the generated package.


## Active work / team profile starters

```text
Use the general feature delivery team profile. Based on the functionality we discussed in this chat, create a step-by-step implementation plan, store it as docs/feature-plan.md, update docs/active-work.md, and return an updated zip. Do not implement anything yet.
```

```text
Use the refactoring team profile. Store the refactoring plan from this chat as docs/refactoring-plan.md, update docs/active-work.md, and return an updated zip. Do not implement anything yet.
```

```text
Use the bugfix team profile. Create or update docs/bugfix-plan.md from the failing command output in this chat, implement exactly the first incomplete bugfix step, update progress, and return an updated zip.
```

```text
Use the active team profile from docs/active-work.md. Continue the active plan and implement exactly the next incomplete step. Return an updated zip.
```




---

# Active work model

Source: `docs/active-work-model.md`

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




---

# Team profiles and active work update

Source: `docs/team-profiles-and-active-work-update.md`

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


