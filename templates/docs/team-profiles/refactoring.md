# Refactoring Team Profile

## Purpose

Use this profile for step-by-step refactoring plans and behavior-preserving structural improvements.

## Source of truth

Use, in order:

1. `docs/active-work.md`
2. `docs/refactoring-plan.md`
3. `docs/agent-progress.md`
4. `docs/agent-review-checklist.md`
5. `docs/functional-specification.md`, if present, to understand externally visible behavior

## Rules

- Preserve externally visible behavior unless the plan explicitly requires a behavior change.
- Do not add features.
- Prefer small, reversible changes.
- Reduce complexity, improve boundaries, or improve maintainability according to the selected step.
- Add or preserve regression tests where practical.
- Stop if behavior change seems necessary but is not documented.
- If the user provides a refactoring plan in chat, store it in `docs/refactoring-plan.md` before implementation.
- If a different active refactoring already exists, archive it under `docs/work-history/refactoring/` before replacing it.
- Implement exactly one incomplete refactoring step.
