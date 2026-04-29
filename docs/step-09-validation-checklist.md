# Step 9 Validation Checklist

Use this checklist on any generated agent delivery team package.

## Required files

- [ ] `scripts/zip-for-chatgpt.sh`
- [ ] `scripts/apply-chatgpt-zip.sh`
- [ ] `docs/chatgpt-zip-workflow.md`
- [ ] `.gitignore`

## Zip creation script

`zip-for-chatgpt.sh`:

- [ ] creates `.chatgpt-zips/outgoing/`,
- [ ] creates a timestamped zip,
- [ ] warns if the Git working tree is dirty,
- [ ] excludes `.git/`,
- [ ] excludes `.chatgpt-zips/`,
- [ ] excludes `node_modules/`,
- [ ] excludes `target/`,
- [ ] excludes `build/`,
- [ ] excludes `dist/`,
- [ ] excludes `coverage/`,
- [ ] excludes `*.zip`,
- [ ] excludes `*.tsbuildinfo`.

## Apply script

`apply-chatgpt-zip.sh`:

- [ ] requires a zip argument,
- [ ] refuses to run with dirty Git working tree,
- [ ] unpacks to a temp directory,
- [ ] protects `.git/`,
- [ ] protects `.chatgpt-zips/`,
- [ ] protects `.env` and `.env.*`,
- [ ] protects `.idea/` and `.vscode/`,
- [ ] does not delete missing files by default,
- [ ] supports explicit `--delete-missing`,
- [ ] shows `git status` after applying.

## Documentation

`docs/chatgpt-zip-workflow.md`:

- [ ] explains `.chatgpt-zips/outgoing/`,
- [ ] explains `.chatgpt-zips/incoming/`,
- [ ] explains `.chatgpt-zips/applied/`,
- [ ] explains upload flow,
- [ ] explains returned zip apply flow,
- [ ] tells the user to inspect `git diff`,
- [ ] tells the user to run verification,
- [ ] tells the user to commit after successful verification.

## Script validation

Run:

```bash
python3 scripts/validate-zip-workflow-scripts.py
```

Expected output:

```text
ChatGPT zip workflow script validation passed.
```
