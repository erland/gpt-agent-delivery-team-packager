# Knowledge Bundle — Validation Checklists

Use this bundle as reference material for validating generated packages.



---

# Step 7 expected output checklist

Source: `fixtures/test-prompts/step-07-expected-output-checklist.md`

# Step 7 Expected Output Checklist

Use this checklist to evaluate the zip returned by the GPT.

## Original project files preserved

- [ ] `package.json`
- [ ] `README.md`
- [ ] `src/index.js`
- [ ] `docs/functional-specification.md`
- [ ] `docs/development-plan.md`

## Agent delivery package files added

- [ ] `AGENTS.md`
- [ ] `docs/agent-delivery-runbook.md`
- [ ] `docs/agent-progress.md`
- [ ] `docs/agent-review-checklist.md`
- [ ] `docs/chatgpt-zip-workflow.md`

## Codex custom agent files added

- [ ] `.codex/agents/architect.toml`
- [ ] `.codex/agents/implementer.toml`
- [ ] `.codex/agents/test-engineer.toml`
- [ ] `.codex/agents/reviewer.toml`
- [ ] `.codex/agents/documentation-writer.toml`
- [ ] `.codex/config.toml`

## Script files added

- [ ] `scripts/codex-next-step.sh`
- [ ] `scripts/codex-run-plan.sh`
- [ ] `scripts/zip-for-chatgpt.sh`
- [ ] `scripts/apply-chatgpt-zip.sh`

## Codex TOML validity

Each role TOML file includes:

- [ ] `name`
- [ ] `description`
- [ ] `developer_instructions`
- [ ] suitable `sandbox_mode`

## Safety and workflow

- [ ] No MCP server configuration is present by default.
- [ ] No plugin configuration is present by default.
- [ ] `.gitignore` includes `.chatgpt-zips/`.
- [ ] `.gitignore` includes `*.zip`.
- [ ] Zip workflow docs mention clean tree, upload, apply, inspect diff, verify, commit.
- [ ] The runbook says to stop after exactly one step.
- [ ] The runbook includes ChatGPT zip workflow fallback instructions.

## Structure

- [ ] No unwanted extra top-level directory was added.
- [ ] Build/cache folders were not included.




---

# Step 8 Codex TOML validation checklist

Source: `docs/step-08-validation-checklist.md`

# Step 8 Validation Checklist

Use this checklist on any generated agent delivery team package.

## Required files

- [ ] `.codex/agents/architect.toml`
- [ ] `.codex/agents/implementer.toml`
- [ ] `.codex/agents/test-engineer.toml`
- [ ] `.codex/agents/reviewer.toml`
- [ ] `.codex/agents/documentation-writer.toml`

## Required fields per role file

Each role file contains:

- [ ] `name`
- [ ] `description`
- [ ] `developer_instructions`
- [ ] `sandbox_mode`

## Developer instructions content

Each `developer_instructions` value describes:

- [ ] role behavior,
- [ ] objective,
- [ ] constraints,
- [ ] scope rules,
- [ ] whether the agent may edit files.

## Sandbox modes

- [ ] `architect.toml` uses `sandbox_mode = "read-only"`.
- [ ] `reviewer.toml` uses `sandbox_mode = "read-only"`.
- [ ] `implementer.toml` uses `sandbox_mode = "workspace-write"`.
- [ ] `test-engineer.toml` uses `sandbox_mode = "workspace-write"`.
- [ ] `documentation-writer.toml` uses `sandbox_mode = "workspace-write"`.

## Safety

- [ ] No MCP servers are configured by default.
- [ ] No plugins are enabled by default.
- [ ] `.codex/config.toml`, if present, contains only safe agent settings.
- [ ] `.codex/config.toml`, if present, contains no default MCP or plugin config.

## Script validation

Run:

```bash
python3 scripts/validate-codex-agent-toml.py
```

Expected output:

```text
Codex agent TOML validation passed.
```


## Config location

- [ ] `.codex/agents/config.toml` does not exist.
- [ ] `.codex/config.toml` exists if agent fan-out settings are included.
- [ ] `.codex/config.toml` contains only safe `[agents]` settings by default.




---

# Step 9 zip workflow validation checklist

Source: `docs/step-09-validation-checklist.md`

# Step 9 Validation Checklist

Use this checklist on any generated agent delivery team package.

## Required files

- [ ] `scripts/zip-for-chatgpt.sh`
- [ ] `scripts/apply-chatgpt-zip.sh`
- [ ] `docs/chatgpt-zip-workflow.md`
- [ ] `.gitignore`

## Zip creation script

`zip-for-chatgpt.sh`:

- [ ] creates `.chatgpt-zips/outgoing/`,
- [ ] creates a timestamped zip,
- [ ] warns if the Git working tree is dirty,
- [ ] excludes `.git/`,
- [ ] excludes `.chatgpt-zips/`,
- [ ] excludes `node_modules/`,
- [ ] excludes `target/`,
- [ ] excludes `build/`,
- [ ] excludes `dist/`,
- [ ] excludes `coverage/`,
- [ ] excludes `*.zip`,
- [ ] excludes `*.tsbuildinfo`.

## Apply script

`apply-chatgpt-zip.sh`:

- [ ] requires a zip argument,
- [ ] refuses to run with dirty Git working tree,
- [ ] unpacks to a temp directory,
- [ ] protects `.git/`,
- [ ] protects `.chatgpt-zips/`,
- [ ] protects `.env` and `.env.*`,
- [ ] protects `.idea/` and `.vscode/`,
- [ ] does not delete missing files by default,
- [ ] supports explicit `--delete-missing`,
- [ ] shows `git status` after applying.

## Documentation

`docs/chatgpt-zip-workflow.md`:

- [ ] explains `.chatgpt-zips/outgoing/`,
- [ ] explains `.chatgpt-zips/incoming/`,
- [ ] explains `.chatgpt-zips/applied/`,
- [ ] explains upload flow,
- [ ] explains returned zip apply flow,
- [ ] tells the user to inspect `git diff`,
- [ ] tells the user to run verification,
- [ ] tells the user to commit after successful verification.

## Script validation

Run:

```bash
python3 scripts/validate-zip-workflow-scripts.py
```

Expected output:

```text
ChatGPT zip workflow script validation passed.
```




---

# Step 10 .gitignore validation checklist

Source: `docs/step-10-validation-checklist.md`

# Step 10 Validation Checklist

Use this checklist on any generated agent delivery team package.

## Required

- [ ] `.gitignore` exists.
- [ ] `.gitignore` includes `.chatgpt-zips/`.
- [ ] `.gitignore` includes `*.zip`.
- [ ] The agent delivery / ChatGPT zip section is clearly marked.

## Recommended

- [ ] `.gitignore` includes `node_modules/`.
- [ ] `.gitignore` includes `target/`.
- [ ] `.gitignore` includes `build/`.
- [ ] `.gitignore` includes `dist/`.
- [ ] `.gitignore` includes `coverage/`.
- [ ] `.gitignore` includes `.next/`.
- [ ] `.gitignore` includes `.vite/`.
- [ ] `.gitignore` includes `.gradle/`.
- [ ] `.gitignore` includes `out/`.
- [ ] `.gitignore` includes `*.tsbuildinfo`.
- [ ] `.gitignore` includes `.DS_Store`.

## Existing project update behavior

When updating an existing project:

- [ ] Existing `.gitignore` content was preserved.
- [ ] Required entries were appended if missing.
- [ ] The GPT did not replace project-specific ignore rules.
- [ ] Duplicate entries were avoided where practical.

## Script validation

Run:

```bash
python3 scripts/validate-gitignore-convention.py
```

Expected output:

```text
.gitignore convention validation passed.
```

Warnings about recommended language/framework-specific entries may be acceptable if the project does not use those tools.




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


