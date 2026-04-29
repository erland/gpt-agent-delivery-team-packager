# Step 9 — Validate Zip Workflow Scripts

This step adds validation guidance and a helper script for the ChatGPT zip upload/download workflow.

The purpose is to make sure generated packages include safe, repeatable scripts for:

- creating clean upload zips,
- applying returned zips,
- protecting Git metadata and local-only files,
- excluding build/cache artifacts,
- keeping the zip exchange artifacts out of Git.

## Required files in generated packages

A generated agent delivery team package should include:

```text
scripts/zip-for-chatgpt.sh
scripts/apply-chatgpt-zip.sh
docs/chatgpt-zip-workflow.md
```

The generated package should also include or update:

```text
.gitignore
```

with a section for ChatGPT zip exchange artifacts and common build outputs.

## Expected zip creation behavior

`scripts/zip-for-chatgpt.sh` should:

- create `.chatgpt-zips/outgoing/` if missing,
- create a timestamped zip file,
- warn if the Git working tree is dirty,
- exclude `.git/`,
- exclude `.chatgpt-zips/`,
- exclude `node_modules/`,
- exclude `target/`,
- exclude `build/`,
- exclude `dist/`,
- exclude `coverage/`,
- exclude `.next/`,
- exclude `.vite/`,
- exclude `.gradle/`,
- exclude `out/`,
- exclude `*.zip`,
- exclude `*.tsbuildinfo`,
- exclude `.DS_Store`.

## Expected apply behavior

`scripts/apply-chatgpt-zip.sh` should:

- require a zip path argument,
- refuse to run if the Git working tree is dirty,
- unpack the returned zip into a temporary directory,
- detect whether the zip has one top-level directory,
- copy files into the repo using a safe sync operation,
- protect `.git/`,
- protect `.chatgpt-zips/`,
- protect `.env` and `.env.*`,
- protect IDE directories such as `.idea/` and `.vscode/`,
- not delete missing files by default,
- support an explicit `--delete-missing` option,
- show `git status` after applying.

## Recommended exchange directories

Use:

```text
.chatgpt-zips/
  outgoing/
  incoming/
  applied/
```

The directories are local workflow artifacts and should be ignored by Git.

## Validation script

This step adds:

```text
scripts/validate-zip-workflow-scripts.py
templates/scripts/validate-zip-workflow-scripts.py
```

Run it from an unpacked/generated package root:

```bash
python3 scripts/validate-zip-workflow-scripts.py
```

Or point it at a package/project directory:

```bash
python3 scripts/validate-zip-workflow-scripts.py path/to/project
```

## What the script checks

The script checks:

- `scripts/zip-for-chatgpt.sh` exists,
- `scripts/apply-chatgpt-zip.sh` exists,
- `docs/chatgpt-zip-workflow.md` exists,
- zip script contains expected exclude patterns,
- apply script contains expected safety/protection snippets,
- documentation mentions the expected workflow,
- `.gitignore` contains `.chatgpt-zips/` and `*.zip` if `.gitignore` exists.

## Step 9 success criteria

Step 9 is complete when:

- zip workflow validation rules are documented,
- a zip workflow validation script exists,
- the validation script is available as a generated-package template,
- the GPT has concrete rules for safe zip upload/download workflow generation.


## Relation to Step 10

Step 9 checks that zip workflow scripts and docs exist and contain important safety behavior.
Step 10 adds stricter `.gitignore` convention validation.
