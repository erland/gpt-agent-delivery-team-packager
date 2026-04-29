# Agent Delivery Team Packager GPT

This package is the starting point for creating a reusable custom GPT that generates and updates
agent delivery team packages.

Current status: Step 1 through Step 10 complete.

Completed:
- Step 1: GPT scope defined.
- Step 2: GPT instruction text prepared.
- Step 3: optional knowledge/template files prepared.
- Step 4: GPT creation instructions prepared.
- Step 5: GPT capability configuration documented.
- Step 6: conversation starters finalized.
- Step 7: minimal fake project test fixture added.
- Step 8: Codex TOML validation guidance and script added.
- Step 9: zip workflow validation guidance and script added.
- Step 10: `.gitignore` convention guidance and validation script added.

Later steps can add:
- ChatGPT fallback validation
- Codex CLI validation
- package examples
- post-test instruction improvements


## Knowledge bundles

This version includes `knowledge/` bundle files for GPT setup. Use these bundled files as GPT knowledge uploads
instead of uploading every individual template file under `templates/`.

Recommended upload set:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
knowledge/validation-checklists.md
knowledge/gpt-setup-reference.md
```


## Corrected GPT instructions update

`docs/step-02-gpt-instructions.md` has been updated to make `.gitignore`, validation scripts,
the no-default-MCP/no-default-plugin rule, and package summary expectations explicit.


## Codex config location correction

This version fixes the Codex config location rule:

- Use `.codex/config.toml`
- Do not generate `.codex/agents/config.toml`

Codex treats TOML files under `.codex/agents/` as custom agent role files, so a config file there causes malformed-agent warnings.
See `docs/codex-config-location-correction.md`.


## Active work and team profiles

This version adds support for selectable team profiles and active work items.

Generated packages should include:
- `docs/active-work.md`
- `docs/feature-plan.md`
- `docs/refactoring-plan.md`
- `docs/bugfix-plan.md`
- `docs/migration-plan.md`
- `docs/team-profiles/*.md`
- `docs/work-history/.gitkeep`
- `scripts/validate-active-work-profiles.py`

See `docs/team-profiles-and-active-work-update.md`.


## Short GPT instruction version

This version updates `docs/step-02-gpt-instructions.md` with a compact instruction block that fits the GPT instruction field limit.
Detailed behavior remains in `docs/detailed-gpt-behavior-reference.md` and the knowledge bundles.


## Prompt helper support

This version adds ready-to-copy prompt recipes.

New files:
- `docs/prompt-recipes.md`
- `knowledge/prompt-recipes.md`

Upload `knowledge/prompt-recipes.md` as an additional GPT knowledge file.
