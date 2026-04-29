# Step 9 Test Prompt

Use this prompt with the Agent Delivery Team Packager GPT after it creates or updates a package:

```text
Validate the generated ChatGPT zip workflow support. Confirm that zip-for-chatgpt.sh, apply-chatgpt-zip.sh, docs/chatgpt-zip-workflow.md, and .gitignore support safe zip upload/download workflows. If anything is missing or unsafe, fix it and return an updated zip.
```

Expected result:
- The GPT checks the zip workflow files.
- The GPT adds or fixes missing scripts.
- The GPT ensures `.gitignore` excludes `.chatgpt-zips/` and `*.zip`.
- The GPT does not make apply behavior destructive by default.
- The GPT returns an updated zip if changes were needed.
