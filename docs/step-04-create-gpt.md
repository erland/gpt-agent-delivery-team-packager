# Step 4 — Create the GPT in ChatGPT

This step describes how to create the initial custom GPT shell for the Agent Delivery Team Packager.

The GPT's job is to create and update agent delivery team packages. It should act as a packager/template
enforcer, not as the sole source of execution behavior. The generated packages must remain self-contained.

## Prerequisites

Before starting this step, have these files available from this package:

- `docs/step-02-gpt-instructions.md`
- `templates/AGENTS.md`
- `templates/docs/*`
- `templates/codex-agents/*`
- `templates/scripts/*`
- `templates/git/gitignore-section.txt`

## Create the GPT

1. Open ChatGPT in the web interface.
2. Open the GPTs area.
3. Select **Create**.
4. Prefer the configuration/editor view if available, rather than relying only on the conversational builder.
5. Set the GPT name to:

```text
Agent Delivery Team Packager
```

6. Set the GPT description to:

```text
Creates Codex-first, ChatGPT-zip-compatible agent delivery team packages from a functional specification and development plan.
```

7. Paste the instruction block from `docs/step-02-gpt-instructions.md` into the GPT instructions field.

## Suggested short profile text

Use this if the GPT editor asks for a short description or profile summary:

```text
I create portable agent delivery team packages for software projects. Packages include AGENTS.md, runbooks, Codex custom agents, progress tracking, review checklists, Codex helper scripts, and ChatGPT zip workflow support.
```

## Upload knowledge/template files

If the GPT editor supports knowledge files, upload the template files from this package.

Recommended knowledge upload set:

```text
templates/AGENTS.md
templates/docs/functional-specification.md
templates/docs/development-plan.md
templates/docs/agent-delivery-runbook.md
templates/docs/agent-progress.md
templates/docs/agent-review-checklist.md
templates/docs/chatgpt-zip-workflow.md
templates/codex-agents/architect.toml
templates/codex-agents/implementer.toml
templates/codex-agents/test-engineer.toml
templates/codex-agents/reviewer.toml
templates/codex-agents/documentation-writer.toml
templates/codex/config.toml
templates/scripts/codex-next-step.sh
templates/scripts/codex-run-plan.sh
templates/scripts/zip-for-chatgpt.sh
templates/scripts/apply-chatgpt-zip.sh
templates/git/gitignore-section.txt
```

If the GPT editor does not support uploading a directory directly, upload the files individually or package the
templates into a single reference document in a later step.

## Initial GPT behavior expectations

The GPT should be able to answer requests such as:

```text
Create an agent delivery team package from this functional specification and development plan.
```

```text
Update this project zip with an agent delivery team package.
```

```text
Review this package and fix invalid Codex agent TOML files.
```

It should not require the user to restate the whole package structure every time.

## Save visibility

For first testing, save the GPT as private or unlisted, not public.

Only make it more broadly available after validating:

- generated zip structure,
- Codex custom agent TOML format,
- ChatGPT zip fallback instructions,
- zip workflow scripts,
- `.gitignore` behavior.

## Step 4 success criteria

Step 4 is complete when:

- a GPT named `Agent Delivery Team Packager` has been created,
- the GPT description is set,
- the Step 2 instruction block is pasted into its instructions,
- template files are uploaded as knowledge when available,
- the GPT is saved privately/unlisted for testing.


## Preferred knowledge upload method

Because the GPT editor may limit knowledge uploads to a small number of files, prefer uploading the bundled files under `knowledge/` instead of every individual template file.

Upload these files:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
knowledge/validation-checklists.md
knowledge/gpt-setup-reference.md
```

If you need a minimal setup, upload only:

```text
knowledge/agent-delivery-package-templates.md
knowledge/codex-agent-toml-templates.md
knowledge/script-templates.md
```

The individual files under `templates/` are still useful as editable source templates, but the `knowledge/` bundle files are easier to upload and less likely to exceed file-count limits.


## Instruction field length limit

The GPT instruction field may reject text longer than 8000 characters.

Use the compact instruction block in:

```text
docs/step-02-gpt-instructions.md
```

Do not paste the detailed behavior reference into the instruction field. The detailed rules are included in
the uploaded knowledge bundles.
