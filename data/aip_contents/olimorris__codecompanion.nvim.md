### <mark>AI-Assisted Contributions</mark>

<mark>While CodeCompanion itself is a tool for AI-assisted development, that does not mean I am willing to accept "vibe-coded" contributions - PRs where the contributor used an LLM to generate code but doesn't deeply understand what they're submitting.</mark>

**Red flags:**
- User cannot explain implementation decisions when asked
- Code doesn't match existing architectural patterns
- Tests appear comprehensive but don't actually validate edge cases
- <mark>Generic LLM patterns (overly defensive coding, verbose comments)</mark>

**What I Expect**:
- **Understand** the codebase before contributing (use the rules, read the tests, explore the architecture)
- **Own** your contribution - you should be able to explain every line you submit
- **Test** thoroughly - write tests that demonstrate you understand the feature
- **Iterate** based on feedback - PRs are conversations, not fire-and-forget submissions

> <mark>As a rule of thumb, use an LLM to create a feature _OR_ a test. But never both.</mark>

---

### Use Rules

<mark>When working inside the CodeCompanion repository, you have access to the built-in [rule](https://codecompanion.olimorris.dev/usage/chat-buffer/rules) files. These give an LLM knowledge of how a certain aspect of the plugin has been implemented. If you're looking to add a new feature to CodeCompanion, rules are a great way of ensuring you follow existing practices and that your LLM fully understands the architecture and design decisions that have been made.</mark>

You can load rules into the chat via the Action Palette:

<img src="https://github.com/user-attachments/assets/7ea80fd0-136e-4d7e-9d70-f4d08dec005c">

Or, via the `/rules` slash command.

---

## Project Structure

CodeCompanion.nvim is organized into several key directories:

- `lua/codecompanion/`:
  - <mark>`adapters/`: Adapters for different LLM providers (OpenAI, Anthropic, etc.)</mark>
  - `interactions/`:
    - `chat/`: Chat buffer implementation
    - `inline/`: Inline code editing functionality
    - `cmd/`: Command-line editing
  - `providers/`: Integration of providers (e.g. Snacks.nvim, Telescope.nvim)
  - `utils/`: Utility functions
- `doc/`: The documentation for the CodeCompanion site and vim docs
- `queries/`: Tree-sitter queries for various languages
- `tests/`: Various tests for the plugin

---

### Debug Chat

<mark>When developing, you can debug the message history in the chat buffer by pressing `gd` to open a debug window. This shows the current messages (from yourself and the LLM) alongside any adapter settings.</mark>

---

### Debug Requests with Proxy

<mark>If you need to debug requests and responses sent to LLM providers, you can use the `proxy` option to forward requests to a proxy server.</mark>

A simple proxy server can be set up using [mitmproxy](https://mitmproxy.org/).

1. Follow the [mitmproxy installation guide](https://docs.mitmproxy.org/stable/overview-installation/) to install mitmproxy.
2. Start mitmproxy with the web interface and listen on port 4141: `mitmweb --set listen_port=4141`
3. Configure CodeCompanion to use the proxy server:

```lua
{
  dir = "/full/path/to/local/codecompanion.nvim",
  -- The rest of your configuration ...
  opts = {
    adapters = {
      opts = {
        allow_insecure = true,
        proxy = "http://127.0.0.1:4141",
      },
    }
    -- The rest of your configuration ...
  }
}
```

From now on, all requests will be forwarded to the proxy server.

<details>
<summary>screenshot</summary>
<img width="1506" alt="debug request with proxy screenshot" src="https://github.com/user-attachments/assets/60f31736-da83-4b80-bc61-341bb7fc82f7" />
</details>

With mitmproxy you can much more using custom scripts/hooks like simulating slower connections, patch requests, etc. Check out the [documentation](https://docs.mitmproxy.org/stable/addons-overview/) for more information.

---

### Testing Tips

<mark>Trying to understand the CodeCompanion codebase and then having to learn how to create tests can feel onerous. So to make this process easier, it's recommended to load the `test` rules into your chat buffer to give your LLM knowledge of how Mini.Test works.</mark>

<mark>It can also be useful to share an example [test file](https://github.com/olimorris/codecompanion.nvim/blob/main/tests/adapters/test_openai.lua) with an LLM too.</mark>
