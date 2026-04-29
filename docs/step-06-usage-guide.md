# Step 6 Usage Guide

This guide explains which conversation starter to use for common situations.

## I have only a functional spec and development plan

Use:

```text
Create an agent delivery team package from this functional specification and development plan.
```

Result:
- standalone package zip,
- no source project files,
- ready to unpack into a project root.

## I have a source project zip

Use:

```text
Update this project zip with an agent delivery team package based on the included or provided functional specification and development plan.
```

Result:
- source project preserved,
- package files added,
- updated project zip returned.

## Codex shows malformed agent warnings

Use:

```text
Review this uploaded agent delivery team package and fix any invalid Codex agent TOML files.
```

Result:
- `.codex/agents/*.toml` files corrected,
- `developer_instructions` added where missing,
- invalid role/prompt/objective-only TOML files repaired.

## I want to use ChatGPT zip round-tripping

Use:

```text
Add ChatGPT zip workflow support scripts and documentation to this agent delivery team package.
```

Result:
- zip creation/apply scripts added,
- `.chatgpt-zips/` convention documented,
- runbook fallback section updated.

## I need a task-specific team

Use:

```text
Create a specialized agent delivery team package for this task type: refactoring, bugfix, feature delivery, architecture review, or ops/environment mapping.
```

Result:
- same package structure,
- adjusted role emphasis,
- adjusted review checklist,
- same one-step stop rule.
