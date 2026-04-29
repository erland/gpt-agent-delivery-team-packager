# Step 7 — Test with a Minimal Fake Project

This step adds a tiny test project fixture and defines how to validate the Agent Delivery Team Packager GPT
before using it on real projects.

The goal is to prove that the GPT can take a small project zip with a functional specification and development
plan, then return an updated project zip containing the agent delivery team package files.

## Fixture

This package includes:

```text
fixtures/minimal-fake-project/
fixtures/minimal-fake-project.zip
```

The fake project is intentionally small:

```text
package.json
README.md
src/index.js
docs/functional-specification.md
docs/development-plan.md
```

## Test objective

Use the GPT to update the fake project zip with an agent delivery team package.

The GPT should:

- preserve the existing fake project files,
- avoid adding an extra top-level directory,
- add the standard agent delivery team package files,
- include valid Codex custom agent TOML files,
- include ChatGPT zip workflow support,
- include safe zip scripts,
- update or create `.gitignore` with zip/build-output exclusions,
- return a downloadable updated zip.

## Test prompt

Upload `fixtures/minimal-fake-project.zip` to the GPT and use this prompt:

```text
Update this project zip with an agent delivery team package based on the included functional specification and development plan.
Return an updated zip.
```

## Expected returned zip structure

The returned zip should contain at least:

```text
package.json
README.md
src/index.js
docs/functional-specification.md
docs/development-plan.md
AGENTS.md
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
.gitignore
```

## What to check manually

After downloading the returned zip:

1. Unzip it to a temporary directory.
2. Confirm there is no extra top-level directory unless the GPT clearly preserved one from the input.
3. Confirm the original project files still exist.
4. Confirm `docs/functional-specification.md` and `docs/development-plan.md` were preserved.
5. Confirm the package files were added.
6. Confirm `.codex/agents/*.toml` files include `developer_instructions`.
7. Confirm no MCP servers or plugins were configured by default.
8. Confirm `.gitignore` includes `.chatgpt-zips/` and `*.zip`.
9. Confirm scripts are present.

## Step 7 success criteria

Step 7 is complete when:

- a minimal fake project fixture exists,
- a zipped version of the fixture exists,
- a GPT test prompt exists,
- an expected-output checklist exists,
- the workflow can be used to validate the GPT before real project use.
