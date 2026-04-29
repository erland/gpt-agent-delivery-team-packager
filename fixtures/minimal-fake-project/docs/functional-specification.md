# Functional Specification

## Purpose

Provide a minimal command-line JavaScript greeting utility.

## Required behavior

- The project exposes a `formatGreeting(name)` function.
- The function trims the provided name.
- If the trimmed name is non-empty, it returns `Hello, <name>!`.
- If the name is empty, missing, or blank, it returns `Hello!`.

## Out of scope

- No browser UI.
- No external dependencies.
- No persistence.
