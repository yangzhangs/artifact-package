### AI Assistant Integration

<mark>This project is designed to work well with AI assistants like Cursor, GitHub Copilot, and others.</mark>
<mark>See [AGENTS.md](AGENTS.md) for guidelines specifically for AI assistants that complement this contributing guide.</mark>

<mark>We provide review instructions for PR reviews in [.github/copilot-instructions.md](.github/copilot-instructions.md).</mark>
You should review your changes with an AI assistant before committing/pushing:

<mark>In Cursor or VS Code with GitHub Copilot Chat:</mark>

<mark>Select Agent Mode with claude-4.5-sonnet and write: `Review my current branch according to @.github/copilot-instructions.md`</mark>

> [!TIP]
> <mark>In Cursor, you can use these custom commands for easy access:</mark>
>
> - `/review-uncommitted` - Review your local uncommitted changes
> - `/review-changes` - Review your current branch vs main

Ensure to address any valid feedback.
That will make your life and that of the maintainers much easier.

---

### <mark>AI Co-Authorship</mark>

<mark>If you used an AI coding agent to help write your PR, please check for co-authorship attribution in your commit messages.</mark>
This helps maintainers understand the origin of changes and smooths the review process.

Some agents add a `Co-authored-by` trailer automatically, but others do not.
<mark>Some even silently **remove** existing co-authorship lines when amending or rebasing commits.</mark>
If you find it missing, please include the appropriate line for your agent in your commit message (pick one):

```
Co-authored-by: copilot-swe-agent[bot] <198982749+Copilot@users.noreply.github.com>
Co-authored-by: Claude Opus 4.6 <noreply@anthropic.com>
Co-authored-by: opencode <noreply@opencode.ai>
```

> [!TIP]
> <mark>PRs are welcome to add co-authorship lines for other coding agents not yet listed here.</mark>
