# Step 10 Test Prompt

Use this prompt with the Agent Delivery Team Packager GPT after it creates or updates a package:

```text
Validate the generated .gitignore convention. Confirm that .chatgpt-zips/ and *.zip are ignored, common build/cache outputs are excluded, and existing .gitignore content is preserved. If anything is missing, fix it and return an updated zip.
```

Expected result:
- The GPT checks `.gitignore`.
- The GPT appends a clearly marked agent delivery / ChatGPT zip section if missing.
- The GPT preserves existing `.gitignore` entries.
- The GPT returns an updated zip if changes were needed.
