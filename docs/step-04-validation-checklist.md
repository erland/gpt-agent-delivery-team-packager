# Step 4 Validation Checklist

Use this checklist after creating the GPT.

## Basic setup

- [ ] GPT name is `Agent Delivery Team Packager`.
- [ ] GPT description explains that it creates Codex-first, ChatGPT-zip-compatible agent delivery team packages.
- [ ] Instructions contain the full text from `docs/step-02-gpt-instructions.md`.
- [ ] GPT is saved privately or unlisted for initial testing.

## Knowledge/template files

- [ ] `templates/AGENTS.md` uploaded if knowledge upload is available.
- [ ] Documentation templates uploaded.
- [ ] Codex custom agent TOML templates uploaded.
- [ ] Script templates uploaded.
- [ ] `.gitignore` section template uploaded.

## First smoke prompt

Use this prompt in the GPT preview/test area:

```text
Summarize your role and list the files you will include when creating an agent delivery team package.
```

Expected answer should mention:

- `AGENTS.md`
- `docs/functional-specification.md`
- `docs/development-plan.md`
- `docs/agent-delivery-runbook.md`
- `docs/agent-progress.md`
- `docs/agent-review-checklist.md`
- `docs/chatgpt-zip-workflow.md`
- `.codex/agents/*.toml`
- scripts for Codex and ChatGPT zip workflow
- no default MCP/plugin configuration
- one-step-at-a-time delivery loop

## Failure indicators

The GPT setup needs adjustment if it:

- omits `developer_instructions` from Codex custom agent TOML files,
- configures MCP servers or plugins by default,
- says it should implement the whole plan in one uncontrolled run,
- does not mention ChatGPT zip workflow fallback,
- does not mention safe zip apply behavior,
- suggests adding an extra top-level directory when updating an existing project zip.
