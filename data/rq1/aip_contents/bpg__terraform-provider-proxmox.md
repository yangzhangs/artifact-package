## Table of contents

- [Quick start](#quick-start)
- [Build the provider](#build-the-provider)
- [IDE support](#ide-support)
- [Devcontainer support](#devcontainer-support)
- [Testing](#testing)
- [Provider implementation guidance](#provider-implementation-guidance)
- [Coding conventions](#coding-conventions)
- [Commit message conventions](#commit-message-conventions)
- [Developer Certificate of Origin (DCO)](#developer-certificate-of-origin-dco)
- [Submitting changes](#submitting-changes)
- <mark>[Using AI assistants and LLM agents](#using-ai-assistants-and-llm-agents)</mark>
- [Releasing](#releasing)

---

## <mark>Using AI assistants and LLM agents</mark>

<mark>We welcome contributions that use AI assistants, LLM agents, or AI-powered coding tools. These tools can help with code generation, testing, documentation, and other development tasks.</mark>

---

### Guidelines

**Allowed and encouraged:**

- <mark>Using AI assistants (GitHub Copilot, Cursor, Claude, ChatGPT, etc.) to help write code</mark>
- <mark>Using LLM agents to automate repetitive tasks</mark>
- Leveraging AI for test generation, documentation, or debugging
- Any tool that helps you complete the task effectively

**Contributor responsibility:**

<mark>While AI tools can assist with contributions, **the person submitting the change is fully responsible** for:</mark>

1. <mark>**Code quality and correctness** — Review all AI-generated code carefully. You are accountable for what you submit.</mark>
2. **DCO sign-off** — By signing off (`git commit -s`), you personally certify that you have the right to submit the code under the project's license, regardless of how it was generated.
3. **Reproducible proof of work** — See [Proof of work](#proof-of-work) requirements above.
4. **Understanding the change** — Be prepared to explain and defend your contribution during code review.

> [!IMPORTANT]
> <mark>The DCO sign-off is a legal certification. When you sign off on a commit, you are affirming that you wrote or have the right to submit the code, and that you agree to license it under the project's terms. This applies equally to human-written and AI-assisted code.</mark>

---

### Agent instructions

For AI agents working on this repository:

- <mark>**[CLAUDE.md](CLAUDE.md)** — Development guidelines and critical rules</mark>
- <mark>**[GEMINI.md](GEMINI.md)** — PR review instructions</mark>
- <mark>**[.dev/README.md](.dev/README.md#working-with-llm-agents)** — Detailed workflow with skills (`/bpg:start-issue`, `/bpg:ready`, `/bpg:debug-api`, `/bpg:prepare-pr`, `/bpg:resume`)</mark>

The skills automate common workflows like setting up branches, running checklists, and preparing PR submissions.
