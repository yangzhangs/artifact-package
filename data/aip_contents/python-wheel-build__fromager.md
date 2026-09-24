# Contributing to Fromager

Fromager thrives on practical, well-tested contributions. This guide summarizes how to set up a workspace, follow our standards, and submit polished changes. Skim it once, keep it handy, and refer back whenever you are unsure.

> **Note**: If you're using AI coding assistants, also see [AGENTS.md](AGENTS.md) for AI-optimized quick reference.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Commit Guidelines](#commit-guidelines)
- [Before Submitting](#before-submitting)
- [Design Patterns Used in Fromager](#design-patterns-used-in-fromager)
- [Quick Reference](#quick-reference)
- [Getting Help](#getting-help)
- [Resources](#resources)

---

---

## Quick Start

---

### Prerequisites

- Python 3.12 or newer

- `hatch` for environment and task management

  ```bash
  pip install hatch
  # or
  pipx install hatch  # recommended
  ```

---

### Initial Setup

```bash

---

### AI-Generated Code Attribution

When AI tools create or significantly modify code, add attribution:

```text
feat(resolver): add exponential backoff for HTTP retries

Improves resilience when PyPI is under load by adding jittered backoff.

Co-Authored-By: Claude <claude@anthropic.com>
Closes: #456
```

Avoid vague messages like `fix bug`, `update files`, or `WIP`.

---
