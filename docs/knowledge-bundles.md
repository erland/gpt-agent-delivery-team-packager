# Knowledge Bundles for GPT Setup

The GPT editor may limit the number of files that can be uploaded as GPT knowledge.

Instead of uploading every file under `templates/` individually, upload the bundled files in this directory:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
knowledge/validation-checklists.md
knowledge/gpt-setup-reference.md
```

This keeps the knowledge upload below common file-count limits while preserving the important template content.

## Recommended upload set

Upload all five files from `knowledge/`.

## Minimal upload set

If you want the smallest useful setup, upload only:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
```

Then paste the main GPT instructions from:

```text
docs/step-02-gpt-instructions.md
```

directly into the GPT instruction field.

## Why bundles are preferred

Bundled knowledge files reduce the risk that:

- the GPT editor rejects the upload because there are too many files,
- an important template is accidentally omitted,
- Codex TOML requirements are split across too many separate files,
- later setup instructions become harder to follow.

## Important source-of-truth note

The GPT instructions field remains the primary behavior source for the GPT.

The knowledge files are reference templates. The GPT should adapt them to each project while preserving the core constraints:

- valid Codex role TOML with `developer_instructions`,
- no MCP servers or plugins by default,
- one-step-at-a-time delivery,
- ChatGPT zip workflow fallback,
- safe zip/apply scripts,
- `.gitignore` zip and build-output exclusions.
