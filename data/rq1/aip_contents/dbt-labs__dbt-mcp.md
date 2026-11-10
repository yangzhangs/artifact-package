## <mark>LLM-Assisted Contributions</mark>

<mark>We welcome contributions made with the help of AI coding assistants and LLMs. If you use LLMs, use them responsibly.</mark>

In practice, this means:

- <mark>**Review what was generated.** Don't submit code you haven't read and understood. LLMs can produce plausible-looking but incorrect logic, especially around edge cases.</mark>
- **Verify accuracy.** Check that generated code, logic, tool descriptions, and prompts are correct — inaccurate descriptions directly affect how AI assistants use these tools, and subtle logic errors may not be caught by tests alone.
- <mark>**Run the checks.** LLM-generated code must still pass `task check` and `task test:unit` before submitting a PR.</mark>
- **Show your work.** For non-trivial changes, include evidence of testing in your PR description (e.g., screenshots, logs, or a description of what you ran and observed). The burden of validation is on the author, not the reviewer.

The bar for contribution quality is the same regardless of how the code was written.

---

### Manual Testing

<mark>To test in a client like Cursor or Claude, use a configuration file like this:</mark>

```
{
  "mcpServers": {
    "dbt": {
      "command": "<path-to-uv>",
      "args": [
        "--directory",
        "<path-to-this-directory>/dbt-mcp",
        "run",
        "dbt-mcp",
        "--env-file",
        "<path-to-this-directory>/dbt-mcp/.env"
      ]
    }
  }
}
```

Or, if you would like to test with Oauth, use a configuration like this:

```
{
  "mcpServers": {
    "dbt": {
      "command": "<path-to-uv>",
      "args": [
        "--directory",
        "<path-to-this-directory>/dbt-mcp",
        "run",
        "dbt-mcp",
      ],
      "env": {
        "DBT_HOST": "<dbt-host-with-custom-subdomain>",
      }
    }
  }
}
```

For improved debugging, you can set the `DBT_MCP_SERVER_FILE_LOGGING=true` environment variable to log to a `./dbt-mcp.log` file.

---

### Adding a tool with interactive UI (MCP Apps)

<mark>MCP Apps are tools that have an associated interactive UI rendered by the host (e.g., Claude, VS Code). They build on top of regular tools with two additions:</mark>

1. **Use `structured_output` and `meta`** to link the tool to a UI resource:
   ```python
   @dbt_mcp_tool(
       description=get_prompt("category/tool_name"),
       title="My Visualization",
       read_only_hint=True,
       structured_output=True,
       meta={"ui": {"resourceUri": "ui://dbt-mcp/my-app"}},
   )
   async def my_viz_tool(context: MyToolContext, param: str) -> MyResult:
       ...
   ```
   `structured_output=True` is required so the host can pass structured JSON to the UI. The return type should be a Pydantic model.

2. **Register an MCP resource** at the matching `ui://` URI to serve the HTML app:
   ```python
   @dbt_mcp.resource(
       uri="ui://dbt-mcp/my-app",
       name="My App",
       mime_type="text/html;profile=mcp-app",
   )
   def get_my_app_ui() -> str:
       return Path("packages/my-app/dist/index.html").read_text()
   ```

3. **Build a frontend** in `packages/` using `@modelcontextprotocol/ext-apps`. The app receives tool results via the `ontoolresult` callback and must be bundled as a single HTML file (e.g., using `vite-plugin-singlefile`) or reference external resources via CSP `resourceDomains`.

The `ui://` URI convention is `ui://<server-name>/<resource-name>`. The `meta` field is passed through the full tool registration pipeline (`@dbt_mcp_tool` → `GenericToolDefinition` → `adapt_context` → `register_tools` → `FastMCP.add_tool`).
