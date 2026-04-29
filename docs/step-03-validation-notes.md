# Step 3 Validation Notes

Use this checklist to validate the Step 3 templates.

## Required template files

- [ ] `templates/AGENTS.md`
- [ ] `templates/docs/functional-specification.md`
- [ ] `templates/docs/development-plan.md`
- [ ] `templates/docs/agent-delivery-runbook.md`
- [ ] `templates/docs/agent-progress.md`
- [ ] `templates/docs/agent-review-checklist.md`
- [ ] `templates/docs/chatgpt-zip-workflow.md`
- [ ] `templates/codex-agents/architect.toml`
- [ ] `templates/codex-agents/implementer.toml`
- [ ] `templates/codex-agents/test-engineer.toml`
- [ ] `templates/codex-agents/reviewer.toml`
- [ ] `templates/codex-agents/documentation-writer.toml`
- [ ] `templates/codex/config.toml`
- [ ] `templates/scripts/codex-next-step.sh`
- [ ] `templates/scripts/codex-run-plan.sh`
- [ ] `templates/scripts/zip-for-chatgpt.sh`
- [ ] `templates/scripts/apply-chatgpt-zip.sh`
- [ ] `templates/git/gitignore-section.txt`

## Codex custom agent template validation

Every role template must include:

- [ ] `name`
- [ ] `description`
- [ ] `developer_instructions`
- [ ] `sandbox_mode`

## Safety validation

- [ ] No template configures MCP servers by default.
- [ ] No template enables plugins by default.
- [ ] Zip scripts protect `.git/`.
- [ ] Zip scripts protect `.chatgpt-zips/`.
- [ ] Zip scripts protect `.env*`.
- [ ] Zip scripts avoid including common build/cache outputs.
