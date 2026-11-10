## Pull Request Guidelines

1. **No Third-Party Frameworks** — Do not introduce third-party dependencies without discussion first
2. **Build Must Pass** — Run `swift build`
3. **Tests Must Pass** — Run `swift test`
4. **Linting** — Run `swiftlint --strict && swiftformat .` before submitting
5. **Small PRs** — Keep changes focused and reviewable
6. <mark>**Share AI Prompts** — If you used AI assistance, include the prompt in your PR (see below)</mark>

---

## <mark>AI-Assisted Contributions & Prompt Requests</mark>

<mark>We embrace AI-assisted development! Whether you use GitHub Copilot, Claude, Cursor, or other AI tools, we welcome contributions that leverage these capabilities.</mark>

---

### What is a Prompt Request?

A **prompt request** is a contribution where you share the AI prompt that generates code, rather than (or in addition to) the code itself. This approach:

- **Captures intent** — The prompt often explains *why* better than a code diff
- **Enables review before implementation** — Maintainers can validate the approach
- **Supports iteration** — Prompts can be refined before code is generated
- **Improves reproducibility** — Anyone can run the prompt to verify results

---

### <mark>Contributing with AI Assistance</mark>

---

#### Option 1: Traditional PR with AI Prompt Disclosure

Submit code as usual, but include the AI prompt in the PR template's "AI Prompt" section. This helps reviewers understand your approach and intent.

---

#### Option 2: Prompt Request (Prompt-Only)

Create an issue using the **Prompt Request** template if you:
- Have a well-crafted prompt but haven't run it yet
- Want feedback on your approach before implementation
- Prefer maintainers to run and merge the prompt themselves
