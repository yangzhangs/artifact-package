## AI Tooling and Agentic Contribution Policy

<mark>We recognize that AI-assisted development tools are part of many developers' workflows. We have no problem with contributors using agentic tools thoughtfully. However, this project is built by and for humans, and we hold all contributions to that standard.</mark>

<mark>If your contribution was substantially produced by an AI tool, you are still fully responsible for every line of code, every test, and every word in the PR. "The AI generated it" is not a defense for low-quality or broken contributions.</mark>

---

### <mark>Requirements for AI-Assisted Contributions</mark>

1. Human-in-the-loop is mandatory. A human must review, understand, and validate every change before submission. Autonomous end-to-end generation of PRs is not acceptable.

2. <mark>Disclose AI tooling usage. If agentic coding tools (Copilot, Claude Code, Cursor, Aider, etc.) were used to produce a substantial portion of the change, state so in the PR description. This is about transparency, not gatekeeping.</mark>

3. You must be able to explain your changes. Maintainers reserve the right to ask you to explain any part of your contribution — the reasoning, the tradeoffs, the implementation details. If you cannot explain what your code does and why, the PR will be closed.

4. Features must be finite in scope and size. Large, sweeping, or unfocused PRs will be closed. Keep changes small, targeted, and reviewable. If a feature is large, break it into incremental PRs discussed in the linked issue.

5. Test coverage is mandatory. All new functionality and bug fixes must include tests. "It works on my machine" is not a test strategy.

6. Human testing of functionality is mandatory. You must have personally tested your changes in a running instance of the application. For minor changes, full UI automation test coverage may substitute, but the expectation is that a human verified the behavior. Describe what you tested in the PR description.

7. Documentation updates are mandatory. If your change affects user-facing behavior, CLI flags, configuration, APIs, or setup steps, update the relevant documentation in the same PR.

8. <mark>Security is your responsibility. You are responsible for auditing any AI-suggested code for security vulnerabilities, leaked secrets, hardcoded credentials, and license-incompatible code snippets. PRs that introduce security issues due to unreviewed AI output will be closed and may result in restricted access.</mark>

9. <mark>Commit messages and PR descriptions must be human-written and meaningful. Generic, obviously-templated, or LLM-boilerplate descriptions (e.g., "This PR improves the codebase by enhancing...") will result in the PR being closed. Describe what you changed, why, and what you tested — in your own words.</mark>

---

### What Is Not Welcome

- <mark>LLM-generated feedback, code reviews, or issue comments. Do not paste LLM output as review comments on other contributors' PRs or in issue threads. If we see comments that are clearly LLM-generated boilerplate (e.g., unsolicited refactoring suggestions, generic praise, hallucinated bug reports), they will be deleted and repeat offenders will be blocked.</mark>

- <mark>Speculative or AI-generated bug reports. Issues must describe behavior you personally observed while using the software. "I asked an LLM to analyze this codebase and it found..." is not a valid bug report. Include concrete reproduction steps from your actual usage.</mark>

- Bulk or spray contributions. Submitting multiple low-effort PRs in a short timeframe — especially auto-generated refactors, style changes, or typo fixes across many files — will result in all of them being closed and contributor access being restricted.

- Auto-generated refactoring PRs. Do not point an agentic tool at this repo and submit the output as a PR. Refactoring must be discussed and approved in an issue first, and must demonstrate a clear understanding of the codebase.
