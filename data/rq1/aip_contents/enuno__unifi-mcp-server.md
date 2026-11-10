## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Code Style Guidelines](#code-style-guidelines)
- [Commit Message Conventions](#commit-message-conventions)
- [Pull Request Process](#pull-request-process)
- <mark>[AI-Assisted Contributions](#ai-assisted-contributions)</mark>
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)

---

## <mark>AI-Assisted Contributions</mark>

---

### Transparency Requirements

When AI coding assistants contribute to this project:

1. <mark>**Tag Contributions:** Add a note in the PR description indicating AI assistance:</mark>

```markdown

---

## AI Assistance

This PR was created with assistance from [AI Tool Name].
```

2. <mark>**Human Review:** All AI-generated code must be reviewed by a human developer</mark>
3. <mark>**Testing:** AI-generated code must include comprehensive tests</mark>
4. <mark>**Documentation:** AI-generated code must be well-documented</mark>

---

### AI-Specific Guidelines

- AI assistants should follow the guidelines in `AGENTS.md`
- Never commit sensitive data (credentials, API keys, etc.)
- Always use environment variables for configuration
- Follow the principle of least privilege for permissions
- Include clear explanations for complex logic

See `AI_GIT_PRACTICES.md` and `CONTRIBUTION_BEST_PRACTICES.md` for additional AI-specific guidance.

---

### Bug Report Handler

The repository includes an automated bug report handler that activates when issues are created with `[Bug]` in the title:

**How It Works:**

1. **Automatic Trigger:** The workflow activates when a new issue is opened with `[Bug]` in the title
2. <mark>**Intelligent Analysis:** Claude AI analyzes the bug report to determine if it's:</mark>
   - A real bug that needs fixing
   - A usage misunderstanding that needs clarification
   - A duplicate of an existing issue

3. **Automated Actions:**
   - **For Usage Issues:** Posts helpful comments with correct usage examples, references documentation, and may close the issue with explanation
   - **For Real Bugs:** Attempts to reproduce and fix the bug, creates a PR with tests if successful
   - **For Complex Bugs:** Acknowledges the issue, adds appropriate labels, and tags maintainers

**What to Expect:**

- The workflow typically responds within a few minutes
- It will add appropriate labels (bug, documentation, needs-investigation, etc.)
- It may create a pull request if the bug can be automatically fixed
- It will always provide helpful feedback to the issue reporter

**Best Practices for Bug Reports:**

To get the most helpful automated response:

- Use the bug report template (`.github/ISSUE_TEMPLATE/bug_report.md`)
- Include complete error messages and stack traces
- Specify your environment (API mode, UniFi version, Python version)
- Describe steps to reproduce the issue
- Indicate what you expected vs. what actually happened

**Manual Override:**

If you believe the automated response is incorrect, simply comment on the issue and a human maintainer will review it.
