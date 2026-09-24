## AI-Assisted Contributions

We use AI tools extensively in our own development and welcome AI-assisted contributions, but we hold them to the same quality bar as our internal work. We publish the [agent skills](https://github.com/freenet/freenet-agent-skills) our team uses — specifically:

- **[pr-creation](https://github.com/freenet/freenet-agent-skills/tree/main/skills/pr-creation)** — covers the full PR lifecycle: testing, code simplification, and self-review before submission.
- **[pr-review](https://github.com/freenet/freenet-agent-skills/tree/main/skills/pr-review)** — four-perspective code review (code-first, testing, skeptical, big-picture).

If you're using AI to generate PRs, please use these skills or equivalent tooling that understands the Freenet codebase. PRs that appear AI-generated without adequate quality control (missing tests, unrelated changes bundled together, hardcoded paths, stacked commits across PRs, etc.) will be closed.

**AI tooling requirements:** Freenet's codebase involves async networking, cryptographic protocols, and subtle concurrency — areas where AI models vary dramatically in capability. Our team uses frontier models with project-specific context and still catches significant issues in self-review.

We require the use of a frontier-class model (as of early 2026: Claude Opus 4, GPT-5, Gemini 3, etc.) with an agentic coding tool. Smaller and local models consistently produce plausible-looking code that introduces subtle bugs in this codebase. PRs that show signs of inadequate AI tooling will be closed.
