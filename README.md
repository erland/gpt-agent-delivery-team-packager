# Agent Delivery Team Packager GPT

This repository is the current source for the Agent Delivery Team Packager custom GPT and its portable ChatGPT package.

## Current GPT configuration

Use these files when configuring the Custom GPT:

- `gpt-configuration/instructions.txt`
- `gpt-configuration/conversation-starters.md`
- the six files in `knowledge/`

The current upload set is documented in `docs/package-manifest.md`.

## Source assets

`templates/` contains the maintained package templates and helper scripts used when evolving the GPT's generated delivery-team packages.

`fixtures/minimal-fake-project/` is retained as a compact validation fixture. It is not GPT Knowledge.

## Distribution packages

Build and validate locally with:

```bash
python scripts/build_distributions.py
python scripts/validate_distributions.py
```

This produces:

- `agent-delivery-team-packager-custom-gpt-vX.Y.Z.zip`
- `agent-delivery-team-packager-chat-vX.Y.Z.zip`

Normal push, pull request, and manual workflow builds use the fallback version in `VERSION`.

When a GitHub Release is published with a semantic-version tag such as `v1.1.0`, the release tag is the version source. The workflow builds and validates both packages and attaches them to the GitHub Release.

## Repository hygiene

Generated distributions, Python bytecode, `__pycache__` directories, and common local OS files are ignored and should not be committed.
