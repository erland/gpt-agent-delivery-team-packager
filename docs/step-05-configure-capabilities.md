# Step 5 — Configure GPT Capabilities

This step defines which GPT capabilities should be enabled for the Agent Delivery Team Packager.

The GPT's main job is to create and update downloadable zip packages. Therefore it needs file handling
and package generation capability, but it should not need external actions, GitHub integrations, MCP servers,
or API integrations by default.

## Recommended capability setup

Enable capabilities that allow the GPT to:

- read uploaded files and zips,
- inspect and transform text files,
- create downloadable files,
- generate zip archives,
- edit package contents in a controlled way.

Depending on the GPT editor wording, this may be shown as one or more of:

- file uploads,
- code interpreter,
- advanced data analysis,
- file generation,
- Python/code execution.

## Capabilities to enable

### File upload / file handling

Enable this if available.

Purpose:
- allow the user to upload an existing source project zip,
- allow the GPT to inspect functional specifications and development plans,
- allow the GPT to update an existing package.

### Code execution / advanced data analysis

Enable this if available.

Purpose:
- create zip files,
- unpack uploaded zips,
- preserve directory structure,
- generate multiple text files reliably,
- validate basic file presence and structure.

### Web browsing

Usually not required for normal package generation.

Enable only if you want the GPT to check current Codex/OpenAI documentation while creating packages.
If enabled, the GPT should still treat the package templates as the source of truth unless the user asks
for a current-format verification.

### Image generation

Do not enable. This GPT does not need image generation.

### Canvas

Optional. Not required for package generation.

## Custom actions

Do not add custom actions for the first version.

The GPT should not directly call GitHub, Codex, OpenCode, CI systems, package registries, or deployment systems.

Reasons:
- the package should remain portable,
- external actions add setup complexity,
- the GPT should not be the main execution engine,
- Codex CLI and local scripts handle execution.

## Apps and connectors

Do not require apps/connectors for the first version.

The user should be able to use the GPT by uploading files directly.

## Security and safety defaults

The GPT must not:

- configure MCP servers by default,
- enable plugins by default,
- add GitHub integrations by default,
- generate secrets,
- modify or include local `.env` files in generated zips,
- encourage applying returned zips without Git checkpoints,
- delete files without a conservative safety procedure.

## Expected GPT output behavior

When the GPT creates or updates a package, it should:

1. produce a zip file,
2. avoid an extra top-level directory when updating an existing project zip,
3. include or update `.gitignore` safely,
4. preserve existing project files,
5. avoid including build/cache files,
6. summarize changed files,
7. provide a download link,
8. note any assumptions or limitations.

## Capability configuration summary

Recommended first-version setup:

```text
File uploads: enabled
Code execution / advanced data analysis: enabled
Web browsing: optional
Image generation: disabled
Custom actions: none
External app integrations: none required
```

## Step 5 success criteria

Step 5 is complete when the GPT capability choices are documented and the first-version GPT is configured to:

- accept uploaded files,
- generate downloadable zip files,
- avoid custom actions,
- avoid default external integrations,
- preserve the package-as-source-of-truth model.
