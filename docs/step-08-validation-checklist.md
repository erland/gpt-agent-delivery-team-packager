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
