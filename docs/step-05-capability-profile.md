# Capability Profile

Use this as a concise capability configuration reference when setting up the GPT.

## GPT name

Agent Delivery Team Packager

## Required capabilities

- File upload / file handling
- Code execution or advanced data analysis
- File generation / downloadable artifacts

## Optional capabilities

- Web browsing, only for checking current documentation or tool-format changes
- Canvas, only for drafting package documentation

## Disabled by default

- Image generation
- Custom actions
- Required apps/connectors
- Direct GitHub integration
- MCP server management
- Deployment or CI integration

## Rationale

This GPT is a packager/template enforcer. It creates portable repository packages.
Execution should happen through generated package instructions, local scripts, Codex CLI, or the ChatGPT zip fallback.
