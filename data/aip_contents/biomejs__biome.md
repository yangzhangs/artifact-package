## Table of Contents

- [🚀 Contributing](#-contributing)
  * [AI assistance notice](#ai-assistance-notice)
  * [Asking questions, making proposals](#asking-questions-making-proposals)
  * [Reporting bugs](#reporting-bugs)
  * [Getting Started](#getting-started)
    + [Local development](#local-development)
      - [Install the required tools](#install-the-required-tools)
    + [GitHub Codespaces](#github-codespaces)
  * [Testing](#testing)
    + [Debugging](#debugging)
  * [Debug binaries](#debug-binaries)
  * [Production binaries](#production-binaries)
  * [Checks](#checks)
  * [Crates development](#crates-development)
    + [Create new crates](#create-new-crates)
    + [Analyzers and lint rules](#analyzers-and-lint-rules)
    + [Parser](#parser)
    + [Formatter](#formatter)
  * [Crate dependencies](#crate-dependencies)
  * [Node.js development](#nodejs-development)
    + [Translations](#translations)
  * [Commit messages](#commit-messages)
  * [Creating pull requests](#creating-pull-requests)
    + [Changelog](#changelog)
      - [Create a changeset](#create-a-changeset)
      - [Choose the correct packages](#choose-the-correct-packages)
      - [Choose the correct type of change](#choose-the-correct-type-of-change)
      - [Writing a changeset](#writing-a-changeset)
    + [Documentation](#documentation)
    + [Versioning](#versioning)
  * [Releasing](#releasing)
    + [Beta releases](#beta-releases)
    + [Regular releases](#regular-releases)
  * [Resources](#resources)
  * [Current Members](#current-members)
    + [Lead team](#lead-team)
    + [Core Contributors team](#core-contributors-team)
    + [Maintainers team](#maintainers-team)
    + [Past Maintainers](#past-maintainers)

---

## AI assistance notice

> [!IMPORTANT]
>
> If you are using **any kind of AI assistance** to contribute to Biome,
> it must be disclosed in the pull request.

If you relied on AI assistance to make a pull request, you must disclose it in the
pull request, together with the extent of the usage. For example, if you used
AI to generate docs or tests, you must say it.
An example disclosure:

- > This PR was written primarily by Claude Code.
- > I consulted ChatGPT to understand the codebase but the solution
  > was fully authored manually by myself.

Providing this information helps reviewers understand the context of the
pull request and apply the right level of scrutiny, ensuring a smoother
and more efficient review process.

AI assistance isn't always perfect, even when used with the utmost care.

Please be respectful to maintainers and disclose AI assistance.

Please do not use AI to write pull request descriptions or contributor communication for this project. Maintainers have limited review bandwidth, and unnecessarily long or low-signal explanations can slow down the review process.

If we believe AI-generated communication was used, we may close the pull request at our discretion. Repeated attempts to contest that decision in comments or re-open the PR may affect whether we accept future contributions from the same contributor.
