# Contributing to NH

<!--toc:start-->

- [Contributing to NH](#contributing-to-nh)
  - [Code of Conduct](#code-of-conduct)
  - [Making Changes](#making-changes)
    - [Writing Code](#writing-code)
      - [Pre-flight Checklist](#pre-flight-checklist)
  - [Testing](#testing)
    - [Running Tests](#running-tests)
    - [Platform-Specific Testing](#platform-specific-testing)
  - [Submitting Changes](#submitting-changes)
    - [Commit Messages](#commit-messages)
      - [Common Scopes](#common-scopes)
    - [Pull Request Process](#pull-request-process)
  - [Code Style](#code-style)
    - [Rust](#rust)
    - [Error Handling](#error-handling)
    - [Shell Command Quoting](#shell-command-quoting)
    - [Logging](#logging)
    - [Derive Macros](#derive-macros)
  - [AI Policy](#ai-policy)
    - [What This Means](#what-this-means)
  - [Getting Help](#getting-help)
  - [License](#license)

<!--toc:end-->

Thank you for your interest in contributing to NH! It is maintained by
volunteers at no cost to the users, and user contributions are the greatest form
of support we can receive. This document will streamline the contributing
process, provide information to help you contribute effectively, and establish
the guidelines you must be aware of.

---

## Code of Conduct

This project, and everyone participating within this project or the surrounding
spaces, are governed by our commitment to maintaining a welcoming and respectful
environment. We expect all contributors to:

- Be respectful and constructive in all interactions
- Accept constructive criticism gracefully
- Focus on what is best for the community and the project
- Show empathy towards others

---

## Making Changes

Before you start, it is _highly advisable_ that you check existing issues and
pull requests to avoid duplicate work. Sometimes certain issues take a little
too long to address while we discuss the specifics, and pull requests are not
immediately visible.

Likewise, for significant changes you should create either an issue or a
discussion to propose your idea. This is not critical, but it would help polish
a feature before it is implemented so that it fits the codebase.

Lastly, for bug fixes, consider referring to the issue number in the PR
discussion to make the issue author aware and help close it automatically once
the fix has been merged.

---

### Writing Code

[code style guidelines]: #code-style
[changelog]: ./CHANGELOG.md

1. Follow the [code style guidelines]
2. Prefer appropriate error handling patterns (e.g, `color_eyre::Result`) over
   `unwrap()` and `expect()`.
3. Write appropriate Rustdoc for new functions, but keep nested comments
   minimal. Code should be self-documenting where possible.
4. Update the [changelog] with your changes when your work is complete

---

#### Pre-flight Checklist

We use `just` to orchestrate some common maintenance tasks. The `just` tool is
provided by the default dev shell and may be invoked to either check for or
automatically fix common issues you might forget about. Before committing your
changes, consider running the "fix" task provided by the Justfile located in the
repository root. It will apply the necessary formatting and linting changes
enforced by `rustfmt` and `clippy`:

```bash

---

## AI Policy

> [!IMPORTANT]
> Pull requests created or submitted by autonomous or supervised AI agents are
> explicitly prohibited, and will be immediately closed without a review. NH, as
> a codebase, does not welcome AI-generated contributions.

This policy exists for the following reasons:

1. **Quality Assurance**: AI-generated code often lacks the contextual
   understanding required for systems-level software that interfaces with
   critical system components.

2. **Legal and Licensing**: The project is licensed under EUPL-1.2, which
   requires clear authorship and accountability. AI-generated contributions
   create ambiguity around copyright and licensing obligations. Not to mention
   the ethical concerns.

3. **Security**: NH operates with elevated privileges and manages system
   configurations. Changes to such software require human judgment, security
   awareness, and accountability.

4. **Maintenance Burden**: AI-generated contributions often require
   disproportionate maintainer effort to review, correct, and integrate
   properly.

---

### What This Means

- **Prohibited**: Submitting PRs where an AI agent (autonomous or supervised)
  generated the code, commit messages, or PR description, regardless of whether
  a human clicked the "submit" button.

- **Prohibited**: Using AI agents to automatically fix issues, respond to review
  comments, or generate follow-up commits.

- **Allowed**: Using AI tools as aids while writing code, provided a human
  author thoroughly reviews, tests, and takes full responsibility for the
  submission. AI-assisted PRs require **FULL DISCLOSURE** and appropriate proof
  that the user thoroughly understands the code generated.

By submitting a pull request, you attest that:

1. You are a human contributor
2. You have personally authored or thoroughly reviewed and tested all changes
3. You take full legal and ethical responsibility for the contribution
4. No autonomous or supervised AI agent was used to create or submit the PR
5. You understand the consequences of violating above guidelines.

Violations of this policy may result in a permanent ban from contributing to the
project.
