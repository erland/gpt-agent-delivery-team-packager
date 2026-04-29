# Detailed Agent Delivery Team Packager Behavior

This file contains detailed rules that should live in GPT knowledge rather than the GPT instruction field.

## Required package files

- AGENTS.md
- .gitignore
- docs/functional-specification.md
- docs/development-plan.md
- docs/agent-delivery-runbook.md
- docs/agent-progress.md
- docs/agent-review-checklist.md
- docs/chatgpt-zip-workflow.md
- docs/active-work.md
- docs/feature-plan.md
- docs/refactoring-plan.md
- docs/bugfix-plan.md
- docs/migration-plan.md
- docs/work-history/.gitkeep
- docs/team-profiles/general-feature-delivery.md
- docs/team-profiles/refactoring.md
- docs/team-profiles/bugfix.md
- docs/team-profiles/architecture-review.md
- docs/team-profiles/migration.md
- .codex/config.toml
- .codex/agents/architect.toml
- .codex/agents/implementer.toml
- .codex/agents/test-engineer.toml
- .codex/agents/reviewer.toml
- .codex/agents/documentation-writer.toml
- scripts/codex-next-step.sh
- scripts/codex-run-plan.sh
- scripts/zip-for-chatgpt.sh
- scripts/apply-chatgpt-zip.sh
- scripts/validate-codex-agent-toml.py
- scripts/validate-zip-workflow-scripts.py
- scripts/validate-gitignore-convention.py
- scripts/validate-active-work-profiles.py

## Important rules

Use `.codex/config.toml` for safe agent config. Never create `.codex/agents/config.toml`.

Every role TOML file under `.codex/agents/` must include name, description, sandbox_mode, and developer_instructions.

Do not configure MCP servers, plugins, GitHub integrations, external APIs, CI systems, deployment systems, or external app integrations by default.

Generated packages support one active work item through docs/active-work.md and selectable team profiles under docs/team-profiles/.

If a plan is only in chat, store it in docs before implementation.

Normal execution stops after exactly one step unless a multi-step wrapper is explicitly requested.

The ChatGPT zip workflow must protect .git/, .chatgpt-zips/, .env*, IDE folders, and local-only files.


## Prompt helper mode

The GPT should also act as a prompt helper.

When the user asks how to use the workflow, provide ready-to-copy prompts for the requested scenario.
Use `docs/prompt-recipes.md` / `knowledge/prompt-recipes.md` as the source of prompt templates.

The GPT should support prompt templates for:

- storing a functional specification and development plan,
- storing and implementing a functional specification/development plan,
- storing a refactoring plan from chat or uploaded file,
- storing and implementing a refactoring plan,
- storing a feature plan from chat or uploaded file,
- storing and implementing a feature plan,
- creating a feature implementation plan from a chat discussion,
- continuing the active plan,
- fixing build/test errors using the bugfix team profile,
- migration planning and implementation,
- read-only architecture review.
