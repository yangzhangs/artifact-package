## Before You Start

> **Issue first, PR second.** Every pull request must be linked to an approved issue. If you want to work on something, [open an issue](https://github.com/the-booklore/booklore/issues/new) (or find an existing one) and wait for a maintainer to approve it before writing code. PRs submitted without a linked, approved issue will be closed.

This protects both your time and ours. It ensures that the work is actually wanted and that you're heading in the right direction before you invest effort.

**What will get your PR closed immediately:**
- No linked issue
- No screenshots or screen recording proving the change works
- No test output pasted in the PR
- Bulk AI-generated changes that clearly haven't been reviewed or tested
- Unsolicited refactors, cleanups, or "improvements" nobody asked for
- PRs with 1000+ changed lines (split them up)

---

### AI-Assisted Contributions

Contributions using AI tools (Copilot, Claude, ChatGPT, etc.) are welcome, but the quality bar is the same as human-written code. **If you ship it, you own it.**

We've seen a sharp increase in AI-generated PRs where the contributor clearly never ran the code, didn't test it, and can't explain what it does. These waste maintainer time and will be closed on sight.

**If you use AI to help write code, you must still:**

- **Run the code yourself.** Build the project, start the full stack, and manually verify the change works. Trusting the AI's output without running it is not acceptable.
- **Review every line.** You must be able to explain any part of your change during review. If asked "why did you do X?" and your answer is "the AI suggested it," the PR will be closed.
- **Keep PRs focused.** One feature, one fix, or one refactor per PR. Do not submit a dump of everything the AI suggested.
- **Scrutinize AI-generated tests.** They often pass trivially without asserting anything meaningful. Tests that don't validate real behavior will be rejected.
- **Clean up.** Remove dead code, placeholder comments, empty catch blocks, and unnecessary boilerplate.
- **Stay in scope.** Do not submit refactors, style changes, or "improvements" the AI suggested that are outside the scope of the linked issue.

---
