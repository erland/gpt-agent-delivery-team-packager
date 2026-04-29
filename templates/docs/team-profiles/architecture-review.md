# Architecture Review Team Profile

## Purpose

Use this profile for source-code analysis, architecture review, dependency mapping, risk review, and plan creation.

## Source of truth

Use, in order:

1. The user's review question or analysis request
2. Existing architecture rules or documentation
3. Source code and configuration files
4. `docs/agent-review-checklist.md`

## Rules

- Read-only by default.
- Do not edit source code unless the user explicitly asks for implementation.
- Produce findings, reports, diagrams, or implementation/refactoring plans.
- Prefer concrete file/module references and prioritized recommendations.
- If implementation is requested after the review, first store a plan under `docs/feature-plan.md`, `docs/refactoring-plan.md`, or another active plan file.
