## The best contribution is a great issue

<mark>FastMCP is an opinionated framework, and its maintainers use AI-assisted tooling that is deeply tuned to those opinions — the design philosophy, the API patterns, the way the framework is meant to evolve. A well-written issue with a clear problem description is often more valuable than a pull request, because it lets maintainers produce a solution that isn't just correct, but consistent with how the framework wants to work. That matters more than speed, though it's faster too.</mark>

**A great issue looks like this:**

1. A short, motivating description of the problem or gap
2. A minimal reproducible example (for bugs) or a concrete use case (for enhancements)
3. A brief note on expected vs. actual behavior

That's it. No need to diagnose root causes, propose API designs, or suggest implementations. If you've done genuine investigation and have a non-obvious insight, include it.

---

## <mark>Using AI to contribute</mark>

<mark>We encourage you to use LLMs to help identify bugs, write MREs, and prepare contributions. But if you do, your LLM must take into account the conventions and contributing guidelines of this repo — including how we want issues formatted and when it's appropriate to open a PR. Generic LLM output that ignores these guidelines tells us the contribution wasn't made thoughtfully, and we will close it. A good AI-assisted contribution is indistinguishable from a good human one. A bad one is obvious.</mark>

---

## PR guidelines

If you do open a PR:

- **Reference an issue.** Every PR should address a tracked issue. If there isn't one, open an issue first. This isn't a permission step — you don't need to wait for a response. But the issue gives us context on the problem, and if a maintainer is already working on it, we can let you know before you invest time in code.
- **Keep it focused.** One logical change per PR. Don't bundle unrelated fixes or refactors.
- **Match existing patterns.** Follow the code style, type annotation conventions, and test patterns you see in the codebase. Run `uv run prek run --all-files` before submitting.
- **Write tests.** Bug fixes should include a test that fails without the fix. Enhancements should include tests for the new behavior.
- **Fix the cause, not the symptom.** If the bug is that a code path skips a step, the fix should make it stop skipping that step — not add compensation elsewhere. Workaround-style fixes will be sent back for revision.
- <mark>**Don't submit generated boilerplate.** We review every line. PRs that read like unedited LLM output — verbose descriptions, speculative changes, shotgun-style fixes — will be closed.</mark>
