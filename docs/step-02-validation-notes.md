# Step 2 Validation Notes

When testing the future GPT, verify that it follows these Step 2 rules:

## Required file set

The generated agent delivery team package must include:

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

## Codex custom agent TOML validation

Every `.codex/agents/*.toml` role file must include:

```toml
name = "..."
description = "..."
sandbox_mode = "read-only" # or "workspace-write"

developer_instructions = """
...
"""
```

The GPT must not generate invalid agent files that only contain fields like:

```toml
role = "..."
prompt = "..."
objective = "..."
instructions = "..."
```

without `developer_instructions`.

## MCP/plugin validation

The generated package must not configure MCP servers or plugins by default.

Avoid generating:

```toml
[mcp_servers.some_server]
...
```

unless the user explicitly asks for it.

## Execution behavior validation

The generated package must make one-step-at-a-time execution the default.

The runbook must explicitly say that the executor stops after exactly one step unless the user invokes
a multi-step wrapper.
