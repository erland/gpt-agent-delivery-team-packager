# Step 5 Validation Checklist

Use this checklist when configuring the GPT capabilities.

## Required / recommended

- [ ] File uploads or file handling enabled.
- [ ] Code execution / advanced data analysis enabled if available.
- [ ] GPT can create downloadable files.
- [ ] GPT can generate zip archives.

## Optional

- [ ] Web browsing enabled only if you want current documentation checks.
- [ ] Canvas enabled only if useful for drafting docs.

## Disabled / omitted by default

- [ ] Image generation disabled.
- [ ] Custom actions omitted.
- [ ] GitHub actions/integration omitted.
- [ ] MCP server configuration omitted.
- [ ] External deployment/CI integrations omitted.

## Smoke test

Ask the GPT:

```text
Create a tiny test zip containing README.md with the text "Agent Delivery Team Packager smoke test".
```

Expected result:

- [ ] GPT creates a downloadable zip.
- [ ] Zip contains `README.md`.
- [ ] GPT summarizes the generated file.
- [ ] GPT does not ask to connect GitHub or external services.

## Failure indicators

The GPT capability setup needs adjustment if it:

- cannot create downloadable zip files,
- cannot read uploaded project zips,
- suggests using a custom action for normal package creation,
- requires GitHub or external services for package generation,
- tries to configure MCP servers/plugins by default.
