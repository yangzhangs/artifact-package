## Pull Requests

Pull Requests (PRs) on GitHub are how you submit changes to the core codebase.

When writing a pull request, you are expected:
- To follow language-specific format guidelines (see below sections)
- To fit the style and design of the project
- To have discussed your PR in advance (GitHub issue, or Discord) before making it
- To explain your PR when submitting it in the OP (doesn't have to be long, just has to be reasonably clear enough to figure out what's going on)
- To be able and willing to answer questions regarding your code, or make changes if/when needed.
    - ie, you must actually understand your own work. If an LLM wrote it for you and you don't understand it, do not try to PR it.
- To have tested your own work prior to submitting.

Pull Requests from newer contributors that are not directly addressing an issue with the `Easy PR` label may be closed without warning or reason. Frequent contributors may take issues that do not have that label. Only trusted maintainers should make code changes not related to a listed issue.

Pull Requests should seek to solve exactly one problem at a time. Do not combine several different things into one PR, please submit those separately.

---

## LLM-Written Code

This is an AI project, so obviously we don't hate AI here. However, we also understand its limitations well, so we ask that you are reasonable about using of AI language models:
- "Intelligent autocomplete" tools (Copilot, Cursor, etc.) are completely fine.
- Asking a chatbot for tips or methods to use is fine. Double-check the accuracy of anything it claims before doing it.
- "Hey ChatGPT write this code for me" or similar, is NEVER okay.
- Agentic development tools are experimental, only very powerful ones well tuned to the codebase tend to get even close, and even then they require significant experienced human monitoring, and therefore are not permitted for external contribution.
    - If you are able to make numerous contributions on your own and demonstrate capable understanding of the repo, you may request permission to use agents for contributing.
- Broadly, make your own decisions about what to write and how to write it. The LLM can replace the keyboard clacking, and it can help you recall specific functions, but they tend to be quite bad at larger scale planning.
- You are expected to understand every line of your own code submission. You may even be asked during PR review.
- Especially double check that any LLM written code both (1) followed the usual formatting rules and (2) used relevant functions.
    - LLMs will often write to much older standards of the language, and will be unaware that there are 'proper' functions in the local context, eg an LLM writing JS might try to use `fetch` (JS API) instead of the proper `genericRequest` (Swarm site.js)
- You are expected to have tested your own contribution, obviously. If you submit non-functional LLM-written code you may be barred permanently from further contributions, as a spammer.
