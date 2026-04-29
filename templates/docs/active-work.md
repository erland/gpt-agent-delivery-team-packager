# Active Work

Type: none
Team profile: general-feature-delivery
Active plan: none
Status: No active work
Created from: n/a
Created at: n/a

## Current execution rule

No active work has been selected yet.

When a user provides or requests a work plan in chat, store the active plan under `docs/` before implementation,
update this file to point to the active plan, and then implement exactly one step if implementation was requested.

## Supported work types

- feature
- refactoring
- bugfix
- migration
- architecture-review

## Active work rules

- Only one active work item is assumed at a time.
- If a new active plan replaces an existing one, archive the previous plan under `docs/work-history/<type>/`.
- Do not implement from a chat-only plan until the plan has been stored in `docs/`.
- If the user asks only to create/store a plan, do not implement anything.
- If the user asks to create/store a plan and implement it, implement exactly the first incomplete step.
