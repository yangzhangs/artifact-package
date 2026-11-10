# <mark>Contributing to Auto Claude</mark>

<mark>Thank you for your interest in contributing to Auto Claude! This document provides guidelines and instructions for contributing to the project.</mark>

---

## How to Contribute

| What you want to do | Where to start |
|----------------------|----------------|
| Bug fixes & small improvements | Open a PR directly |
| New features / architecture changes | Start a [GitHub Discussion](https://github.com/AndyMik90/Auto-Claude/discussions) or ask in [Discord](https://discord.com/channels/1448614759996854284/1451298184612548779) first |
| Questions & setup help | [Discord #setup-help](https://discord.com/channels/1448614759996854284/1451298184612548779) |

---

## <mark>AI-Assisted Contributions</mark>

<mark>PRs built with AI tools (Claude, Codex, Copilot, etc.) are welcome here -- given what this project does, it would be odd if they weren't.</mark>

<mark>That said, we've seen AI-generated PRs that introduce regressions because the contributor didn't verify what the code actually does. To keep quality high, we ask that AI-assisted PRs include the following:</mark>

- <mark>**Flag it** -- mention AI assistance in the PR description (the PR template has a section for this)</mark>
- **State your testing level** -- untested, lightly tested, or fully tested
- **Share context if you can** -- prompts or session logs help reviewers understand intent
- **Confirm you understand the code** -- you should be able to describe what the PR does and how the underlying code works

<mark>AI-assisted PRs go through the same review process as any other contribution. Transparency just helps reviewers know where to look more carefully.</mark>

---

## Table of Contents

- [How to Contribute](#how-to-contribute)
- <mark>[AI-Assisted Contributions](#ai-assisted-contributions)</mark>
- [Contributor License Agreement (CLA)](#contributor-license-agreement-cla)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Development Setup](#development-setup)
- [Pre-commit Hooks](#pre-commit-hooks)
- [Code Style](#code-style)
- [Testing](#testing)
- [Continuous Integration](#continuous-integration)
- [Git Workflow](#git-workflow)
  - [Working with Forks](#working-with-forks)
  - [Branch Overview](#branch-overview)
  - [Main Branches](#main-branches)
  - [Supporting Branches](#supporting-branches)
  - [Branch Naming](#branch-naming)
  - [Where to Branch From](#where-to-branch-from)
  - [Pull Request Targets](#pull-request-targets)
  - [Release Process](#release-process-maintainers)
  - [Commit Messages](#commit-messages)
  - [PR Hygiene](#pr-hygiene)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Architecture Overview](#architecture-overview)

---

### Why We Require a CLA

<mark>Auto Claude is currently licensed under AGPL-3.0. The CLA ensures the project has proper licensing flexibility should we introduce additional licensing options (such as commercial/enterprise licenses) in the future.</mark>

You retain full copyright ownership of your contributions.

---

# Clone the repository
<mark>git clone https://github.com/AndyMik90/Auto-Claude.git</mark>
<mark>cd Auto-Claude</mark>

---

### Other Useful Commands

```bash
npm start              # Build and run production
npm run build          # Build for production
npm run package        # Package for distribution
npm test               # Run frontend tests
```

<details>
<summary><b>Windows users:</b> If installation fails with node-gyp errors, click here</summary>

<mark>Auto Claude automatically downloads prebuilt binaries for Windows. If prebuilts aren't available for your Electron version yet, you'll need Visual Studio Build Tools:</mark>

1. Download [Visual Studio Build Tools 2022](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Select "Desktop development with C++" workload
3. In "Individual Components", add "MSVC v143 - VS 2022 C++ x64/x86 Spectre-mitigated libs"
4. Restart terminal and run `npm install` again

</details>

> <mark>**Note:** For regular usage, we recommend downloading the pre-built releases from [GitHub Releases](https://github.com/AndyMik90/Auto-Claude/releases). Running from source is primarily for contributors and those testing unreleased features.</mark>

---

### Working with Forks

<mark>When contributing to Auto Claude, you'll typically fork the repository first. Proper fork configuration is essential to avoid sync issues.</mark>

---

#### Initial Fork Setup

```bash

---

# 2. Clone YOUR fork (not the original repo)
git clone https://github.com/YOUR-USERNAME/Auto-Claude.git
cd Auto-Claude

---

# origin  https://github.com/YOUR-USERNAME/Auto-Claude.git (fetch)

---

# origin  https://github.com/YOUR-USERNAME/Auto-Claude.git (push)

---

# 4. Add upstream remote to sync with the original repo
git remote add upstream https://github.com/AndyMik90/Auto-Claude.git
```

---

#### Keeping Your Fork Updated

```bash

---

### Bug Reports

When reporting a bug, include:

1. **Clear title** describing the issue
2. **Environment details**:
   - OS and version
   - Node.js version
   - Auto Claude version
3. **Steps to reproduce** the issue
4. **Expected behavior** vs **actual behavior**
5. **Error messages** or logs (if applicable)
6. **Screenshots** (for UI issues)

---

## Architecture Overview

Auto Claude is a single Electron desktop application in `apps/desktop/`.

---

### Electron Desktop (`apps/desktop/`)

- **AI Agent Layer** (`src/main/ai/`) - Vercel AI SDK v6 agent runtime, providers, tools, security, orchestration
- **Main Process** (`src/main/`) - IPC handlers, agent queue, terminal management, claude-profile
- **Renderer** (`src/renderer/`) - React UI components and Zustand stores
- **Shared** (`src/shared/`) - Types, i18n locales, constants, utilities

For detailed architecture information, see [CLAUDE.md](CLAUDE.md).

---

---

## Questions?

If you have questions about contributing, feel free to:

1. Open a GitHub issue with the `question` label
2. Review existing issues and discussions

Thank you for contributing to Auto Claude!
