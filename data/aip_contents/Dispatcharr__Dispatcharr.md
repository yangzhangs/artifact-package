## Table of Contents

- [Before You Start](#before-you-start)
- [Project Overview](#project-overview)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Code Standards](#code-standards)
- [Writing Tests](#writing-tests)
- [Submitting a Pull Request](#submitting-a-pull-request)
- <mark>[On AI-Assisted Code](#on-ai-assisted-code)</mark>
- [What We Will Decline](#what-we-will-decline)
- [Contributor License Agreement](#contributor-license-agreement)

---

---

## <mark>On AI-Assisted Code</mark>

We are aware that AI coding tools are capable of generating plausible-looking code quickly. We do not prohibit their use, but we require the following:

**You must understand every line of code you submit.**

<mark>AI tools frequently produce code that:</mark>

- Duplicates logic that already exists elsewhere in the codebase
- Ignores the established patterns for how the project is structured
- Introduces subtle bugs that are invisible without domain knowledge
- Passes superficial review but breaks edge cases in production

If you cannot explain, during code review, why a particular line of code is written the way it is — including the tradeoffs involved — the PR will not be merged. There are no exceptions.

<mark>Using an AI tool to help you understand the codebase, generate a first draft, or write boilerplate is fine. Submitting code you have not read and do not understand is not.</mark>

---

---

## What We Will Decline

To save your time and ours, the following types of PRs will be closed without extended review:

- **Undiscussed feature additions.** If there is no linked issue where the feature was agreed upon, we will close the PR and ask you to open one.
- **Large, unfocused diffs.** A PR that touches 20 files across 5 apps to "improve code quality" is almost never reviewable. Scope your changes.
- **Dependency bumps without justification.** Don't open a PR just to bump a library version unless you have identified a specific bug or security issue it resolves.
- **Cosmetic/style-only changes.** Reformatting files, renaming variables for preference, or reorganizing imports with no functional change.
- **Duplicate work.** Check open PRs and issues before starting. If someone is already working on it, coordinate with them.
- <mark>**Code the author cannot explain.** See [On AI-Assisted Code](#on-ai-assisted-code).</mark>

---
