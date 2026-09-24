## Contribution Guidelines

Contributors must review, test, and understand all changes before submitting a PR. This applies equally to manually written and tool-generated code. Use of AI or other tools does not transfer responsibility — the contributor is fully accountable for the final patch.

Changes must be small and focused. Avoid unrelated edits, cleanup, or formatting changes. Maintainers may ask for large or mixed changes to be split before review.

Refactors are allowed but must be directly relevant to the change. Do not include opportunistic or drive-by refactoring.

All relevant build, lint, and test steps must pass locally before opening a PR.

PRs must be ready for review when submitted, not ready for validation. The contributor is responsible for verifying correctness before asking for a reviewer's time.

For detailed code and eBPF/C guidelines, see [AGENTS.md](AGENTS.md).

---

### Code Ownership

AI tools are permitted, but they do not change what is expected of contributors. Every line in a PR is your responsibility, regardless of how it was produced. If you cannot explain a change, do not submit it.

Reviewers will ask you to walk through your changes. Inability to explain the rationale, the approach, or the details of any part of a PR is grounds for rejection. This includes changes generated or suggested by AI tools.

**Avoid reimplementing existing code.** AI tools frequently generate new implementations of functionality that already exists in the codebase. Before introducing any new utility, helper, abstraction, or pattern, search the codebase first. Reviewers will reject code that duplicates existing functionality.

**Vet AI-generated plans and issue reports before filing.** If you use an AI tool to draft an issue, design proposal, or implementation plan, read it critically before submitting. Check that it accurately reflects the codebase, does not contradict existing architecture, and does not propose work that is already done. Unvetted AI output creates noise and wastes reviewer time.
