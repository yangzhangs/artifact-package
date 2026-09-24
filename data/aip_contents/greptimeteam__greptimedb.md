## AI-Assisted contributions

We have the following policy for AI-assisted PRs:

- The PR author should **understand the core ideas** behind the implementation **end-to-end**, and be able to justify the design and code during review.
- **Calls out unknowns and assumptions**. It's okay to not fully understand some bits of AI generated code. You should comment on these cases and point them out to reviewers so that they can use their knowledge of the codebase to clear up any concerns. For example, you might comment "calling this function here seems to work but I'm not familiar with how it works internally, I wonder if there's a race condition if it is called concurrently".

---

### Why fully AI-generated PRs without understanding are not helpful

Today, AI tools cannot reliably make complex changes to GreptimeDB on their own, which is why we rely on pull requests and code review.

The purposes of code review are:

1. Finish the intended task.
2. Share knowledge between authors and reviewers, as a long-term investment in the project. For this reason, even if someone familiar with the codebase can finish a task quickly, we're still happy to help a new contributor work on it even if it takes longer.

An AI dump for an issue doesn’t meet these purposes. Maintainers could finish the task faster by using AI directly, and the submitters gain little knowledge if they act only as a pass through AI proxy without understanding.

Please understand the reviewing capacity is **very limited** for the project, so large PRs which appear to not have the requisite understanding might not get reviewed, and eventually closed or redirected.
