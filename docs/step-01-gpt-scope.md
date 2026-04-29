# Step 1 — GPT Scope

## GPT name

Agent Delivery Team Packager

## Primary responsibility

Create and update downloadable agent delivery team packages for software projects.

The GPT should take a functional specification and a development plan, then produce a zip package
that can be unpacked into a project root.

The generated package should be:

- Codex-first
- partly OpenCode-compatible
- compatible with ChatGPT zip upload/download workflows
- self-contained, so executor behavior lives inside the generated repository package

## What the GPT should create

The GPT should create or update packages containing, at minimum:

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

## What the GPT should not be

The GPT should not be the main execution engine for coding work.

Execution rules should live inside the generated package, mainly in:

```text
AGENTS.md
docs/agent-delivery-runbook.md
docs/agent-progress.md
docs/agent-review-checklist.md
```

The GPT may assist with ChatGPT zip workflows, but the package itself should contain enough
plain-language instructions for ordinary ChatGPT, Codex CLI, or a custom GPT to follow.

## Execution modes supported by generated packages

### Codex CLI mode

The generated package should support local Codex CLI workflows, including:

- one-step-at-a-time execution
- role-based custom agents
- scoped diffs
- local verification commands
- progress tracking

### ChatGPT zip workflow mode

The generated package should also support this workflow:

1. Create clean upload zip from local repo.
2. Upload zip to ChatGPT.
3. Ask ChatGPT to implement exactly the next incomplete step.
4. Receive updated zip.
5. Apply zip locally.
6. Inspect diff.
7. Run verification.
8. Commit.
9. Continue with next step.

## Core design principles

1. The repository package is the source of truth.
2. The GPT is a packager/template enforcer, not the sole executor.
3. Every implementation loop should stop after exactly one step unless explicitly running a multi-step wrapper.
4. No MCP servers, plugins, external APIs, or GitHub integrations should be configured by default.
5. Every generated Codex custom agent TOML file must include:
   - `name`
   - `description`
   - `developer_instructions`
6. `developer_instructions` must be a TOML multiline string.
7. Generated packages should include safe zip workflow scripts.
8. Generated packages should include `.gitignore` conventions for zip artifacts and build outputs.

## Out of scope for the first GPT version

The first version should not attempt to:

- run Codex itself
- directly access GitHub
- manage PRs
- install dependencies
- execute long-running implementation work
- configure MCP servers by default
- replace local build/test verification

## Success criteria for Step 1

This step is complete when the GPT scope is documented clearly enough that later steps can add:

- full GPT instruction text
- template files
- validation checklist
- test workflow
