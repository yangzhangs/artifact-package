<!--
SPDX-FileCopyrightText: 2025 The BAR Lobby Authors

SPDX-License-Identifier: CC0-1.0
-->

# How to Contribute

Thank you for your interest in contributing to BAR Lobby! As a project driven entirely by volunteers, we depend on community contributions to move forward and thrive. We appreciate you being here to help.

## Communication

If you haven't already, join our Discord at https://discord.gg/beyond-all-reason and select the "Development Role" in the "Channels & Roles" section. The [#new-client](https://discord.com/channels/549281623154229250/927564746104905728) channel is dedicated to everything related to BAR Lobby.

Please feel free to ask questions and seek help from the community in the channel. Often, a fellow contributor can provide a quick answer!

While Discord is our primary communication tool, it is an ephemeral medium. To keep the project organized, all binding discussions, decisions, and code contributions must be recorded on GitHub. This allows us to track changes and decisions in a structured way that can be referenced later. If you see a discussion on Discord that should be preserved, please help us by creating an issue or pull request to document it. If there is already an open discussion on GitHub, prefer it to Discord.

## A Note on Reviews & Merging

While you can often get _an_ answer to a question on Discord quickly, we are _very_ short on maintainers able to review pull requests and respond to questions _authoritatively_ in a timely manner: it's effectively less than one person. Please be patient.

## New Contributor Guide

If you are new to contributing to open source projects on GitHub, we recommend familiarizing yourself with the documentation at https://docs.github.com/en/get-started, especially:

- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Collaborating with Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)

## Getting Started

1.  **Help Review Pull Requests:** A great way to start is by helping to review open PRs. This helps you learn the codebase, helps the contributor get faster feedback, and helps the maintainers save time.
2.  Get an overview of the project by reading the [README](README.md) file.
3.  Set up your local development environment by following the steps in the [README](README.md) file.
4.  Take a look at [issues tagged with the "good first issue" tag](https://github.com/beyond-all-reason/bar-lobby/contribute).
5.  If you have any questions, need help, find something ambiguous, or want to work on something not well scoped yet or without an issue, **please, please discuss it with us**! We want to ensure that we are aligned, you aren't wasting your time, and you have a good experience!
6.  Develop the change we all agreed on, and send it for review following the [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) process.

## Testing

We have automated tests, but we do not currently have a strict project-wide policy around test coverage thresholds or exactly what kinds of tests must exist for every change.

That said:

- **Do not break existing tests.** If CI is failing due to your change, please fix it before requesting review.
- **Adding tests is strongly encouraged.** PRs that include test coverage for the behavior they change (unit tests and/or E2E where appropriate) are typically easier to review and merge.
- For details on how to run and write tests in this repo (Vitest + Playwright/Electron E2E, CI notes, etc.), see **[TESTING.md](TESTING.md)**.

## AI-Assisted Contributions

If you use AI tools to assist with code or text contributions, you must follow our [AI Usage Policy](AI_POLICY.md). This includes clear disclosure of AI involvement in pull requests, human verification of all AI-generated code, and other important requirements. Please review the policy before submitting AI-assisted work.

## Other Ways to Contribute

Code is just one part of the project. We are always in need of other skills! If you're interested in helping with design, documentation, testing, UI design, art or community management, please talk to us on Discord. We will try to find something for you to do. ☺️

---

# Standalone AI policy file

<!--
SPDX-FileCopyrightText: 2026 The BAR Lobby Authors
SPDX-FileCopyrightText: 2024 Mitchell Hashimoto, Ghostty contributors
SPDX-License-Identifier: CC0-1.0 AND MIT
-->

# AI Usage Policy

## Disclosure requirements

**AI usage in generating code must be explicitly disclosed in the associated Pull Request.**

Contributors must clearly state:

- which AI tool(s) were used (for example: Claude Code, Cursor, Copilot)
- the extent to which the contribution was AI-assisted

**Undisclosed AI usage will result in closure.**

If maintainers reasonably suspect undisclosed AI use, the pull request will be closed.

**Non-direct AI usage does not require disclosure.**

The above requirements apply to cases where AI is used to write production code.
If AI is used solely as an advisory or educational tool, disclosure is not required.

## Verification and testing

**All AI-assisted code must be fully verified by a human contributor.**

Contributors are responsible for ensuring that:

- the code has been run and tested
- the code behaves correctly in practice, not just in theory

It is recommended to attach test artifacts, such as screenshots or recordings, that demonstrate your code working for each test step.

## Issues and discussions

**AI assistance is permitted in issues and discussions, with a strict human-in-the-loop requirement:**

- AI-generated content must be reviewed and edited by a human before submission.
- Verbosity, noise, and speculative content must be removed.
- Contributors remain responsible for research, accuracy, and clarity.

AI may assist with explanations, summaries, or drafting, but must not replace understanding or judgment.

## Prohibited content

**AI-generated media is not permitted.**

This includes, but is not limited to: art, images, videos, and audio.
Only text and code are eligible for AI assistance, subject to the rules above.

## Enforcement

**Repeated or intentional misuse of AI tools may result in contributor bans.**

Maintainers may enforce this policy at their discretion.

## Why is this important?

This repository is maintained by humans.

Every issue, discussion, and pull request is read and reviewed by maintainers who volunteer their time and expertise. Submitting low-effort, unverified, or poorly understood work shifts the burden of validation onto maintainers and is considered disrespectful of that effort.

The primary behavior this policy seeks to prevent is **Vibe Coding**, defined as the uncritical generation and submission of AI-produced code without sufficient understanding, verification, or accountability by the contributor. This policy exists to prevent wasted maintainer time and to ensure high standards of code quality and maintainability.

This policy exists to protect maintainers, preserve code quality, and ensure that collaboration remains productive and sustainable.

## Responsible AI usage is welcome

Maintainers actively use AI tools as part of their workflow.
This policy does not represent an anti-AI position.

The restrictions outlined above exist due to repeated misuse of AI by contributors who submit unverified, low-quality, or poorly understood work. The issue is not the tools themselves, but how they are applied.

When used responsibly, transparently, and with proper human oversight, AI can be a valuable productivity aid.

## Attribution

This policy is adapted from the original AI usage policy published by the [Ghostty](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md) organization.
The maintainers acknowledge and appreciate the clarity and intent of the original text.

