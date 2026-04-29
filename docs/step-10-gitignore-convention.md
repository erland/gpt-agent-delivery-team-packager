# Step 10 — Add `.gitignore` Convention

This step formalizes the `.gitignore` convention for generated agent delivery team packages.

The goal is to keep ChatGPT zip exchange artifacts, returned zips, build outputs, dependency folders,
and local cache files out of Git.

## Recommended placement for zip exchange files

Use this local-only directory structure:

```text
.chatgpt-zips/
  outgoing/
  incoming/
  applied/
```

These folders should not be committed.

## Required `.gitignore` entries

Every generated package should include or append:

```gitignore
# Agent delivery / ChatGPT zip exchange artifacts
.chatgpt-zips/
*.zip
```

## Recommended build/cache entries

Generated packages should also include common build/cache exclusions where appropriate:

```gitignore
# Common build/cache outputs
node_modules/
target/
build/
dist/
coverage/
.next/
.vite/
.gradle/
out/
*.tsbuildinfo
.DS_Store
```

## Update behavior

When updating an existing project zip, the GPT should not blindly replace `.gitignore`.

Instead it should:

1. read the existing `.gitignore`,
2. append a clearly marked section if required entries are missing,
3. preserve existing project-specific ignore rules,
4. avoid duplicate entries where practical.

## Standalone package behavior

When creating a standalone agent delivery team package, the GPT should include a `.gitignore` with the required
zip exchange section and common build/cache entries.

## Template

This package includes:

```text
templates/git/gitignore-section.txt
```

The GPT should use this as the standard section to append or include.

## Validation script

This step adds:

```text
scripts/validate-gitignore-convention.py
templates/scripts/validate-gitignore-convention.py
```

Run it from an unpacked/generated package root:

```bash
python3 scripts/validate-gitignore-convention.py
```

Or point it at a package/project directory:

```bash
python3 scripts/validate-gitignore-convention.py path/to/project
```

## What the script checks

The script checks:

- `.gitignore` exists,
- `.chatgpt-zips/` is ignored,
- `*.zip` is ignored,
- common build/cache ignore patterns are present or warned about,
- the section is clearly marked.

## Step 10 success criteria

Step 10 is complete when:

- the `.gitignore` convention is documented,
- the reusable `.gitignore` template section exists,
- generated package behavior for existing and standalone projects is defined,
- a validation script exists,
- the minimal fake project fixture includes the convention.
