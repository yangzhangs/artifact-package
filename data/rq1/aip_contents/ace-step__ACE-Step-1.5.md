## <mark>Recommended AI-Assisted Workflow (Copilot / CodePilot / Codex)</mark>

---

### Step 1: Commit-Scoped Review (First Pass)
Once you feel work is complete, and whatever manual or automated testing passes, commit your work to your local project. Note the commit number, or ask your agent to provide the number for your latest commit.

**Use a different agent to review your work than was used to produce the work**

<mark>If you use Claud or OpenAI codex, use your free Copilot tokens in VScode to get a Copilot review. If in doubt, ask your main agent to formulate a prompt for the review agent. It will 'know' what it has worked on and can suggest appropriate focus areas for the review agent.</mark>

Ask the agent to review **only your commit diff**, not the whole repo.

Prompt example:

Review commit <sha> only.
Focus on regressions, behaviour changes, and missing tests.
Ignore pre-existing issues outside changed hunks.
Output findings by severity with file/line references.

Fix the issues raised by the review, rerun the review process until only non-breaking trivial issues exist. This may need to be repeated a number of times until the commit is clean, but watch that this does not incorrectly blow scope out beyond what is required for the primary fix.
---

---

### Reviewer Notes
- Known pre-existing issues not addressed
- Follow-up items (if any)

<mark>Your PR description should look something like [this](https://github.com/ace-step/ACE-Step-1.5/pull/309), demonstrating care and rigor applied by the author before hitting the PR button. If you have multiple Coderabbit/copilot responses to your PR, its probably a good idea to revoke the PR, fix the issues raised by the review bot, and resubmit.</mark>

---

Maintainers are balancing **correctness, stability, and review bandwidth**.

PRs that are:
- tightly scoped
- clearly explained
- minimally risky
- easy to reason about

are **much more likely to be reviewed and merged quickly**.

Thanks for helping keep the project stable and enjoyable to work on.
