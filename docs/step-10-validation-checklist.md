# Step 10 Validation Checklist

Use this checklist on any generated agent delivery team package.

## Required

- [ ] `.gitignore` exists.
- [ ] `.gitignore` includes `.chatgpt-zips/`.
- [ ] `.gitignore` includes `*.zip`.
- [ ] The agent delivery / ChatGPT zip section is clearly marked.

## Recommended

- [ ] `.gitignore` includes `node_modules/`.
- [ ] `.gitignore` includes `target/`.
- [ ] `.gitignore` includes `build/`.
- [ ] `.gitignore` includes `dist/`.
- [ ] `.gitignore` includes `coverage/`.
- [ ] `.gitignore` includes `.next/`.
- [ ] `.gitignore` includes `.vite/`.
- [ ] `.gitignore` includes `.gradle/`.
- [ ] `.gitignore` includes `out/`.
- [ ] `.gitignore` includes `*.tsbuildinfo`.
- [ ] `.gitignore` includes `.DS_Store`.

## Existing project update behavior

When updating an existing project:

- [ ] Existing `.gitignore` content was preserved.
- [ ] Required entries were appended if missing.
- [ ] The GPT did not replace project-specific ignore rules.
- [ ] Duplicate entries were avoided where practical.

## Script validation

Run:

```bash
python3 scripts/validate-gitignore-convention.py
```

Expected output:

```text
.gitignore convention validation passed.
```

Warnings about recommended language/framework-specific entries may be acceptable if the project does not use those tools.
