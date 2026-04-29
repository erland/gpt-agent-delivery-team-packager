# General Feature Delivery Team Profile

## Purpose

Use this profile for planned feature implementation and ordinary development-plan work.

## Source of truth

Use, in order:

1. `docs/active-work.md`
2. `docs/feature-plan.md` if active work type is `feature`
3. `docs/functional-specification.md`
4. `docs/development-plan.md`
5. `docs/agent-progress.md`
6. `docs/agent-review-checklist.md`

## Rules

- Implement exactly one incomplete feature/development step.
- Keep diffs scoped to the selected step.
- Add or update tests for changed behavior.
- Preserve existing behavior unless the plan explicitly changes it.
- If the user provides only a feature discussion in chat, create and store a step-by-step plan in `docs/feature-plan.md` before implementation.
- If the user asks only to create the plan, do not implement anything.
- If the user asks to create the plan and implement it, implement exactly the first incomplete step.
