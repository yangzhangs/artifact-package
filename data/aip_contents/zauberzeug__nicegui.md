### AI Assistant Integration

This project is designed to work well with AI assistants like Cursor, GitHub Copilot, and others.
See [AGENTS.md](AGENTS.md) for guidelines specifically for AI assistants that complement this contributing guide.

We provide review instructions for PR reviews in [.github/copilot-instructions.md](.github/copilot-instructions.md).
You should review your changes with an AI assistant before committing/pushing:

In Cursor or VS Code with GitHub Copilot Chat:

Select Agent Mode with claude-4.5-sonnet and write: `Review my current branch according to @.github/copilot-instructions.md`

> [!TIP]
> In Cursor, you can use these custom commands for easy access:
>
> - `/review-uncommitted` - Review your local uncommitted changes
> - `/review-changes` - Review your current branch vs main

Ensure to address any valid feedback.
That will make your life and that of the maintainers much easier.

---

### AI Co-Authorship

If you used an AI coding agent to help write your PR, please check for co-authorship attribution in your commit messages.
This helps maintainers understand the origin of changes and smooths the review process.

Some agents add a `Co-authored-by` trailer automatically, but others do not.
Some even silently **remove** existing co-authorship lines when amending or rebasing commits.
If you find it missing, please include the appropriate line for your agent in your commit message (pick one):

```
Co-authored-by: copilot-swe-agent[bot] <198982749+Copilot@users.noreply.github.com>
Co-authored-by: Claude Opus 4.6 <noreply@anthropic.com>
Co-authored-by: opencode <noreply@opencode.ai>
```

> [!TIP]
> PRs are welcome to add co-authorship lines for other coding agents not yet listed here.
