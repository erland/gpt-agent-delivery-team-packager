# Conversation Starters Reference

Copy these into the GPT editor.

## Primary starters

1.

```text
Create an agent delivery team package from this functional specification and development plan.
```

2.

```text
Update this project zip with an agent delivery team package based on the included or provided functional specification and development plan.
```

3.

```text
Review this uploaded agent delivery team package and fix any invalid Codex agent TOML files.
```

4.

```text
Add ChatGPT zip workflow support scripts and documentation to this agent delivery team package.
```

## Optional fifth starter

```text
Create a specialized agent delivery team package for this task type: refactoring, bugfix, feature delivery, architecture review, or ops/environment mapping.
```

## First preview prompt

After adding the starters, test the GPT with:

```text
Summarize your role and explain when I should use each conversation starter.
```

Expected result:
- The GPT explains that it creates or updates agent delivery team packages.
- It distinguishes standalone package creation from updating an existing project zip.
- It mentions Codex CLI compatibility and ChatGPT zip workflow compatibility.
- It says execution behavior belongs in the generated package.


## Active work / team profile starters

```text
Use the general feature delivery team profile. Based on the functionality we discussed in this chat, create a step-by-step implementation plan, store it as docs/feature-plan.md, update docs/active-work.md, and return an updated zip. Do not implement anything yet.
```

```text
Use the refactoring team profile. Store the refactoring plan from this chat as docs/refactoring-plan.md, update docs/active-work.md, and return an updated zip. Do not implement anything yet.
```

```text
Use the bugfix team profile. Create or update docs/bugfix-plan.md from the failing command output in this chat, implement exactly the first incomplete bugfix step, update progress, and return an updated zip.
```

```text
Use the active team profile from docs/active-work.md. Continue the active plan and implement exactly the next incomplete step. Return an updated zip.
```


## Prompt helper conversation starters

```text
Give me the prompt for storing a functional specification and development plan without implementing anything.
```

```text
Give me the prompt for storing a refactoring plan from this chat without implementing it.
```

```text
Give me the prompt for creating a feature implementation plan from what we discussed.
```

```text
Give me the prompt for continuing the active plan.
```

```text
Give me the prompt for fixing build/test errors from the latest returned zip.
```
