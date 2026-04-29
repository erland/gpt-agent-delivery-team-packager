# Step 6 — Add Conversation Starters

This step finalizes the recommended conversation starters for the Agent Delivery Team Packager GPT.

The starters should make the GPT easy to use in the common workflows:

1. create a new package from a functional specification and development plan,
2. add package files to an existing project zip,
3. repair an existing package,
4. add ChatGPT zip workflow support,
5. validate Codex custom agent files.

## Recommended GPT conversation starters

Use these in the GPT editor.

### Starter 1 — Create a package from planning docs

```text
Create an agent delivery team package from this functional specification and development plan.
```

Use when:
- the functional specification and development plan are already written,
- the user wants a standalone package zip or package files to add to a repo,
- no source project zip is required.

Expected GPT behavior:
- ask for missing spec/plan only if not provided,
- generate the standard package structure,
- include Codex agent TOML files,
- include ChatGPT zip workflow support,
- return a downloadable zip.

### Starter 2 — Add package to an existing project zip

```text
Update this project zip with an agent delivery team package based on the included or provided functional specification and development plan.
```

Use when:
- the user uploads a project zip,
- the GPT should add package files to the project,
- the result should preserve the project structure.

Expected GPT behavior:
- inspect the uploaded zip,
- avoid adding an extra top-level directory,
- add or update package files,
- append `.gitignore` entries safely,
- preserve existing source files,
- return an updated project zip.

### Starter 3 — Repair or validate an existing package

```text
Review this uploaded agent delivery team package and fix any invalid Codex agent TOML files.
```

Use when:
- Codex reports malformed agent definitions,
- the package has old or invalid `.codex/agents/*.toml` files,
- the user wants a corrected package.

Expected GPT behavior:
- verify every role TOML file includes `name`, `description`, and `developer_instructions`,
- ensure `developer_instructions` is a TOML multiline string,
- avoid MCP/plugin configuration by default,
- return a corrected zip.

### Starter 4 — Add ChatGPT zip workflow support

```text
Add ChatGPT zip workflow support scripts and documentation to this agent delivery team package.
```

Use when:
- a package exists but lacks upload/apply scripts,
- the user wants hybrid ChatGPT/Codex workflows.

Expected GPT behavior:
- add `docs/chatgpt-zip-workflow.md`,
- add `scripts/zip-for-chatgpt.sh`,
- add `scripts/apply-chatgpt-zip.sh`,
- update `.gitignore`,
- update `docs/agent-delivery-runbook.md` with fallback instructions.

### Starter 5 — Create a specialized delivery team

```text
Create a specialized agent delivery team package for this task type: refactoring, bugfix, feature delivery, architecture review, or ops/environment mapping.
```

Use when:
- the user wants a different team composition,
- the package should still follow the same core structure,
- role instructions need a specific emphasis.

Expected GPT behavior:
- preserve the standard package contract,
- adapt role behavior and review checklist to the task type,
- still stop after one step by default,
- still include ChatGPT zip workflow fallback.

## Shorter starter set

If the GPT editor only supports a small number of starters, use these four:

```text
Create an agent delivery team package from this functional specification and development plan.
```

```text
Update this project zip with an agent delivery team package based on the included or provided functional specification and development plan.
```

```text
Review this uploaded agent delivery team package and fix any invalid Codex agent TOML files.
```

```text
Add ChatGPT zip workflow support scripts and documentation to this agent delivery team package.
```

## Step 6 success criteria

Step 6 is complete when:

- final conversation starters are documented,
- each starter has a purpose,
- each starter has expected GPT behavior,
- a shorter starter set is available for GPT editors with limited starter slots.
