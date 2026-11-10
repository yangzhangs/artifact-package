## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- <mark>[AI-Assisted Development](#ai-assisted-development)</mark>
- [Architecture Guidelines](#architecture-guidelines)

---

### Before Submitting

- [ ] Code follows Black formatting standards
- [ ] All tests pass locally
- [ ] New tests added for new functionality
- <mark>[ ] Documentation updated (README.md, CLAUDE.md if architecture changed)</mark>
- [ ] Pre-commit hooks pass
- [ ] No unnecessary dependencies added
- <mark>[ ] AI assistance disclosed (see below)</mark>

---

## <mark>AI Assistance</mark>
- <mark>Tools used: [e.g., Claude Code, GitHub Copilot]</mark>
- <mark>Model: [e.g., Claude Sonnet 4.5, GPT-4]</mark>
- Scope: [e.g., "Generated test cases", "Refactored function X"]

---

## <mark>AI-Assisted Development</mark>

<mark>**TerraVision welcomes the use of AI tools for development!** AI assistance can accelerate development, improve code quality, and help with documentation.</mark>

---

### Disclosure Requirement

<mark>**All AI use for coding must be disclosed in pull requests.** Please include:</mark>

1. <mark>**Tools used**: Name of AI tool(s) (e.g., Claude Code, GitHub Copilot, ChatGPT, Cursor)</mark>
2. <mark>**Model and version**: Specific model used (e.g., Claude Sonnet 4.5, GPT-4 Turbo, Llama 3.1 70B)</mark>
3. **Scope of assistance**: What the AI helped with (e.g., "Generated test fixtures", "Refactored VPC handler", "Wrote docstrings")

---

## <mark>AI Assistance</mark>

- <mark>**Tools**: Claude Code CLI</mark>
- <mark>**Model**: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)</mark>
- **Scope**:
  - Generated initial implementation of Azure resource handlers
  - Created unit tests for provider detection
  - Assisted with debugging Terraform graph parsing logic
```

---

### Why Disclose?

- **Transparency**: Helps maintainers understand the development process
- **Quality**: Allows reviewers to pay extra attention to AI-generated code
- **Learning**: Helps the community learn what AI tools work well for this project
- **Best practices**: Establishes a culture of responsible AI use

---

### AI Best Practices

- Always review and test AI-generated code thoroughly
- Ensure AI-generated code follows TerraVision's architecture patterns
- Verify that AI suggestions align with provider-specific conventions
- Use AI to augment your skills, not replace understanding
