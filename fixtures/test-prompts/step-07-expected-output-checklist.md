# Step 7 Expected Output Checklist

Use this checklist to evaluate the zip returned by the GPT.

## Original project files preserved

- [ ] `package.json`
- [ ] `README.md`
- [ ] `src/index.js`
- [ ] `docs/functional-specification.md`
- [ ] `docs/development-plan.md`

## Agent delivery package files added

- [ ] `AGENTS.md`
- [ ] `docs/agent-delivery-runbook.md`
- [ ] `docs/agent-progress.md`
- [ ] `docs/agent-review-checklist.md`
- [ ] `docs/chatgpt-zip-workflow.md`

## Codex custom agent files added

- [ ] `.codex/agents/architect.toml`
- [ ] `.codex/agents/implementer.toml`
- [ ] `.codex/agents/test-engineer.toml`
- [ ] `.codex/agents/reviewer.toml`
- [ ] `.codex/agents/documentation-writer.toml`
- [ ] `.codex/config.toml`

## Script files added

- [ ] `scripts/codex-next-step.sh`
- [ ] `scripts/codex-run-plan.sh`
- [ ] `scripts/zip-for-chatgpt.sh`
- [ ] `scripts/apply-chatgpt-zip.sh`

## Codex TOML validity

Each role TOML file includes:

- [ ] `name`
- [ ] `description`
- [ ] `developer_instructions`
- [ ] suitable `sandbox_mode`

## Safety and workflow

- [ ] No MCP server configuration is present by default.
- [ ] No plugin configuration is present by default.
- [ ] `.gitignore` includes `.chatgpt-zips/`.
- [ ] `.gitignore` includes `*.zip`.
- [ ] Zip workflow docs mention clean tree, upload, apply, inspect diff, verify, commit.
- [ ] The runbook says to stop after exactly one step.
- [ ] The runbook includes ChatGPT zip workflow fallback instructions.

## Structure

- [ ] No unwanted extra top-level directory was added.
- [ ] Build/cache folders were not included.


## Active work and team profile files added

- [ ] `docs/active-work.md`
- [ ] `docs/feature-plan.md`
- [ ] `docs/refactoring-plan.md`
- [ ] `docs/bugfix-plan.md`
- [ ] `docs/migration-plan.md`
- [ ] `docs/work-history/.gitkeep`
- [ ] `docs/team-profiles/general-feature-delivery.md`
- [ ] `docs/team-profiles/refactoring.md`
- [ ] `docs/team-profiles/bugfix.md`
- [ ] `docs/team-profiles/architecture-review.md`
- [ ] `docs/team-profiles/migration.md`
- [ ] `scripts/validate-active-work-profiles.py`
