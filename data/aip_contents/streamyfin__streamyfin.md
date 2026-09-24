## Table of Contents


- [AI Assistance Disclosure](#ai-assistance-disclosure)
- [Reporting Issues](#reporting-issues)
- [Reporting Security Vulnerabilities](#reporting-security-vulnerabilities)
- [Requesting Features & Enhancements](#requesting-features--enhancements)
- [Developing the Mobile App](#developing-the-mobile-app)
  - [Codebase Overview](#codebase-overview)
  - [Setting Up Your Development Environment](#setting-up-your-development-environment)
  - [Making Changes](#making-changes)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Release Process](#release-process)
- [Getting Help and Community](#getting-help-and-community)

---

---

## AI Assistance Disclosure

> [!IMPORTANT]  
> If any AI tool was used while contributing to Streamyfin, it must be disclosed in the pull request.

State in your PR whether AI assistance was used and to what extent (for example, *docs only* or *code generation*).  
If AI-generated text was used in PR discussions or responses, disclose that as well.  
Minor autocomplete or keyword suggestions do not require disclosure.

---

### Examples

> This PR was written primarily by Claude Code.  
> I used Cursor to explore parts of the codebase, but the implementation is fully manual.

Failing to disclose AI usage wastes maintainers’ time and complicates review efforts.  
AI-assisted contributions are welcome, but contributors remain fully responsible for the code they submit.  

Always disclose AI involvement to maintain transparency and respect for maintainers’ time.

---

## Pull Request Guidelines

When opening a PR:

- Title should clearly summarize the change.
- Reference any related issue(s) using keywords like `closes #123`.
- Follow our [Conventional Commits](https://www.conventionalcommits.org/) style, e.g., `feat: add new playback controls`.
- Provide a detailed description in the PR body, explaining what, why, and any impacts.
- Include screenshots or recordings if UI changes are involved.
- Ensure CI checks are green (lint, type-check, build).
- Confirm that the branch is **up to date with `main`** before submission. 
- Mention if AI-generated code or content was used (see [AI Assistance Disclosure](#ai-assistance-disclosure)).  
- Do not include secrets, tokens, or production credentials. Redact sensitive data in logs and screenshots.
- Keep PRs focused; avoid bundling unrelated changes together.

PRs require review and approval by maintainers before merging.---
