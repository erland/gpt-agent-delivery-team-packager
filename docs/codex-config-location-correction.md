# Codex Config Location Correction

Codex treats every `.toml` file under `.codex/agents/` as a custom agent role definition.
Therefore, generated packages must not contain:

```text
.codex/agents/config.toml
```

Use this instead:

```text
.codex/config.toml
```

For safe default agent fan-out settings, `.codex/config.toml` may contain only:

```toml
[agents]
max_threads = 6
max_depth = 1
```

Do not configure MCP servers, plugins, GitHub integrations, CI systems, deployment systems, or external APIs by default.

## Files updated in this package

- `docs/step-02-gpt-instructions.md`
- `docs/step-08-validate-codex-toml.md`
- `docs/step-08-validation-checklist.md`
- `templates/codex/config.toml`
- `knowledge/codex-agent-toml-templates.md`
- `knowledge/gpt-setup-reference.md`
- `scripts/validate-codex-agent-toml.py`
- `templates/scripts/validate-codex-agent-toml.py`

## What to replace in the GPT

In the GPT builder, replace:

1. The GPT instructions with the corrected instruction block from:
   - `docs/step-02-gpt-instructions.md`

2. The uploaded knowledge files with the regenerated files in:
   - `knowledge/agent-delivery-package-templates.md`
   - `knowledge/codex-agent-toml-templates.md`
   - `knowledge/script-templates.md`
   - `knowledge/validation-checklists.md`
   - `knowledge/gpt-setup-reference.md`

At minimum, replace:
- `knowledge/codex-agent-toml-templates.md`
- `knowledge/gpt-setup-reference.md`

Recommended: replace all five knowledge bundle files to avoid drift.
