# Step 8 — Validate Codex TOML Files

This step adds validation guidance and a helper script for checking generated Codex custom agent TOML files.

The main problem this step prevents is Codex ignoring role files with warnings like:

```text
Ignoring malformed agent role definition: agent role file ... must define `developer_instructions`
```

## Required Codex role files

A generated agent delivery team package should contain these role files:

```text
.codex/agents/architect.toml
.codex/agents/implementer.toml
.codex/agents/test-engineer.toml
.codex/agents/reviewer.toml
.codex/agents/documentation-writer.toml
```

Optionally, it may contain:

```text
.codex/config.toml
```

## Required fields

Every role file must include these top-level fields:

```toml
name = "..."
description = "..."
sandbox_mode = "read-only" # or "workspace-write"

developer_instructions = """
...
"""
```

`developer_instructions` must be a TOML multiline string containing:

- role behavior,
- role objective,
- constraints,
- scope rules,
- whether the agent may edit files.

## Sandbox expectations

Use:

```toml
sandbox_mode = "read-only"
```

for:

```text
architect.toml
reviewer.toml
```

Use:

```toml
sandbox_mode = "workspace-write"
```

for:

```text
implementer.toml
test-engineer.toml
documentation-writer.toml
```

## Invalid pattern to avoid

Do not generate role files that only contain fields like:

```toml
role = "architect"
prompt = "..."
objective = "..."
instructions = "..."
```

Codex requires `developer_instructions`.

## MCP and plugin rule

Generated packages must not configure MCP servers or plugins by default.

Avoid this by default:

```toml
[mcp_servers.some_server]
...
```

Avoid this by default:

```toml
[plugins."github@openai-curated"]
enabled = true
```

MCP servers or plugins should only be added when explicitly requested for a real workflow dependency.

## Validation script

This step adds:

```text
scripts/validate-codex-agent-toml.py
templates/scripts/validate-codex-agent-toml.py
```

Run it from an unpacked/generated package root:

```bash
python3 scripts/validate-codex-agent-toml.py
```

Or point it at a package/project directory:

```bash
python3 scripts/validate-codex-agent-toml.py path/to/project
```

## What the script checks

The script checks:

- required role files exist,
- role TOML files parse,
- `name` exists,
- `description` exists,
- `developer_instructions` exists,
- `sandbox_mode` matches the expected role type,
- role files do not use deprecated/invalid top-level `role`, `prompt`, `objective`, or `instructions` fields instead of `developer_instructions`,
- default config files do not configure MCP servers or plugins.

## Step 8 success criteria

Step 8 is complete when:

- Codex TOML validation rules are documented,
- a validation script exists,
- the script can be added to generated packages,
- the GPT instructions/templates make malformed role files less likely.


## Config location rule

Do not create:

```text
.codex/agents/config.toml
```

Codex treats every `.toml` file under `.codex/agents/` as a custom agent role definition.
Configuration belongs here instead:

```text
.codex/config.toml
```

The validation script must fail if `.codex/agents/config.toml` exists.
