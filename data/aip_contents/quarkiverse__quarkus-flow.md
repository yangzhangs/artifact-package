### Important Testing Notes

<mark>**Mocked LLM Calls**: Integration tests mock Ollama/LLM model calls to avoid resource-intensive operations in CI. Do not make real LLM API calls in tests.</mark>

**Parallel Execution**: Tests run in parallel. **Never use fixed ports** in your tests. If you need a port, use an unusual/random port or let the framework assign one (e.g., `@QuarkusTest` auto-assigns ports).

---

## <mark>LLM Usage Policy</mark>

<mark>We welcome AI tools (ChatGPT, GitHub Copilot, Claude Code, etc.) that help developers be more productive.</mark>

However, to maintain a healthy community and high-quality contributions, the following expectations apply:

---

### Acceptable Use

- <mark>✅ Use LLMs to **assist your development** (drafting code, writing docs, proposing fixes)</mark>
- <mark>✅ **Understand, validate, and take responsibility** for all LLM-generated content</mark>
- ✅ Submit contributions that reflect **your own understanding and intent**
- <mark>✅ Use LLMs to help you **write better**, not to **post more**</mark>

---

### Unacceptable Use

- <mark>❌ Submitting code/tests/comments **copied directly from an LLM** with little or no human oversight</mark>
- ❌ Posting **large volumes of low-effort suggestions** or vague issues
- <mark>❌ Submitting **AI-generated tests that don't validate actual behavior**</mark>
- ❌ Using bots/agents to **automatically open PRs or file issues** without human authorship

---

### If in Doubt

<mark>**Ask!** We're happy to help contributors use AI tools effectively without creating noise.</mark>

> <mark>This isn't about banning AI — it's about keeping Quarkus Flow collaborative, human-driven, and focused on quality.</mark>
