# Step 3 — Optional Knowledge and Template Files

Step 3 prepares reusable template files that can be uploaded as GPT knowledge or used as reference material
when configuring the Agent Delivery Team Packager GPT.

## Purpose

The GPT should not have to recreate the agent delivery package format from memory every time. These templates
provide concrete examples for the files the GPT should generate or update.

## Template groups

### Root package template

- `templates/AGENTS.md`

### Documentation templates

- `templates/docs/functional-specification.md`
- `templates/docs/development-plan.md`
- `templates/docs/agent-delivery-runbook.md`
- `templates/docs/agent-progress.md`
- `templates/docs/agent-review-checklist.md`
- `templates/docs/chatgpt-zip-workflow.md`

### Codex custom agent templates

- `templates/codex-agents/architect.toml`
- `templates/codex-agents/implementer.toml`
- `templates/codex-agents/test-engineer.toml`
- `templates/codex-agents/reviewer.toml`
- `templates/codex-agents/documentation-writer.toml`
- `templates/codex/config.toml`

### Script templates

- `templates/scripts/codex-next-step.sh`
- `templates/scripts/codex-run-plan.sh`
- `templates/scripts/zip-for-chatgpt.sh`
- `templates/scripts/apply-chatgpt-zip.sh`

### Git ignore template

- `templates/git/gitignore-section.txt`

## GPT knowledge recommendation

When creating the GPT, upload these templates as knowledge files if available.

The GPT should treat them as reusable examples, not immutable files. It may adapt content to the user's project,
but it must preserve the core constraints:

- Codex agent TOML files must include `name`, `description`, and `developer_instructions`.
- `developer_instructions` must be a TOML multiline string.
- MCP servers and plugins must not be configured by default.
- The runbook must include ChatGPT zip workflow fallback instructions.
- The normal delivery loop must stop after exactly one step.
- Zip scripts must protect `.git/`, `.chatgpt-zips/`, `.env*`, and local IDE files.

## Step 3 success criteria

Step 3 is complete when the package contains reusable templates for:

- package instructions,
- project docs,
- Codex custom agents,
- Codex helper scripts,
- ChatGPT zip workflow scripts,
- `.gitignore` additions.


## Knowledge upload file-count limit

The GPT editor may limit how many knowledge files can be uploaded. Do not upload every individual template file if that would exceed the limit.

Use the bundled knowledge files instead:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
knowledge/validation-checklists.md
knowledge/gpt-setup-reference.md
```

The individual `templates/` files remain useful as source templates, but `knowledge/` is the preferred upload set for GPT configuration.
