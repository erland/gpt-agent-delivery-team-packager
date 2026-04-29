# ChatGPT Zip Workflow

## Purpose

This document describes how to exchange project zips with ChatGPT while keeping the repository clean and reviewable.

## Directory convention

Use:

```text
.chatgpt-zips/
  outgoing/
  incoming/
  applied/
```

These directories are local exchange artifacts and should be ignored by Git.

## Upload workflow

1. Start from a clean Git working tree.
2. Run:

```bash
scripts/zip-for-chatgpt.sh
```

3. Upload the generated zip from `.chatgpt-zips/outgoing/`.
4. Ask ChatGPT:

```text
Use the agent delivery team package instructions.
Implement exactly the next incomplete step.
Return an updated zip.
```

## Apply returned zip

1. Save the returned zip under `.chatgpt-zips/incoming/`.
2. Apply it:

```bash
scripts/apply-chatgpt-zip.sh .chatgpt-zips/incoming/<returned-file>.zip
```

3. Inspect:

```bash
git status
git diff
```

4. Run verification commands.
5. Commit if the change is good.

## Delete behavior

The apply script should be conservative by default. It should not delete missing files unless explicitly invoked with:

```bash
scripts/apply-chatgpt-zip.sh .chatgpt-zips/incoming/<returned-file>.zip --delete-missing
```

Protected paths must never be deleted by the script:

```text
.git/
.chatgpt-zips/
.env
.env.*
.idea/
.vscode/
```


## Optional validation

Generated packages may include:

```bash
python3 scripts/validate-zip-workflow-scripts.py
```

Use it to check that zip workflow scripts and documentation include the expected safety behavior.


## `.gitignore` validation

Generated packages may include:

```bash
python3 scripts/validate-gitignore-convention.py
```

Use it to confirm `.chatgpt-zips/`, `*.zip`, and common build/cache outputs are ignored.
