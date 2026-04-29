# Step 8 Test Prompt

Use this prompt with the Agent Delivery Team Packager GPT after it creates a package:

```text
Validate the generated Codex custom agent files. Confirm that every .codex/agents/*.toml role file includes name, description, developer_instructions, and suitable sandbox_mode. If anything is invalid, fix it and return an updated zip.
```

Expected result:
- The GPT checks all role files.
- The GPT fixes any missing `developer_instructions`.
- The GPT does not add MCP server or plugin configuration by default.
- The GPT returns an updated zip if changes were needed.
