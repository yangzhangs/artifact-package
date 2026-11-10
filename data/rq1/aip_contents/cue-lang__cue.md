### <mark>AI-assisted development with OpenSpec</mark>

Contributors can optionally use [OpenSpec](https://github.com/Fission-AI/OpenSpec/)
<mark>for AI-assisted development. OpenSpec provides a structured workflow for creating</mark>
proposals, designs, specs, and implementation tasks with AI coding assistants like
<mark>Claude Code, GitHub Copilot, Gemini, and others.</mark>

**Setup:**

1. Install OpenSpec CLI (requires Node.js 20.19.0+):
   ```console
   $ npm install -g @fission-ai/openspec@latest
   ```

2. Run the setup script from the repository root:
   ```console
   $ ./_scripts/setup-openspec.sh
   ```

This creates local-only tooling files (gitignored) while specs and context are
tracked in `doc/`:

- `doc/specs/` - Main specs (source of truth, tracked)
- `doc/context/` - Shared context like language change checklists (tracked)
- `openspec/` - Workflow state and config (local only, gitignored)

**Quick start commands** (in your AI assistant):
- `/opsx:new` - Start a new change with proposal → design → specs → tasks workflow
- `/opsx:continue` - Continue working on an existing change
- `/opsx:apply` - Implement tasks from a change

**Updating after OpenSpec upgrades:**
```console
$ ./_scripts/setup-openspec.sh update
```
