## LLM-assisted coding ("vibe coding")

Mindwtr is not strictly against LLM-assisted coding. LLM tools are improving quickly and can be productive when used correctly.

If you use LLM/coding agents for contributions, follow these rules:

1. Do not use web chat interfaces as your main coding tool.
   Use coding agents in an IDE or CLI with repository indexing and full codebase context.
2. Use coding-focused agents, not general chat models.
   Example: use Codex or Claude Code agent for coding tasks, not generic chatbot mode.
3. Start with a clear implementation goal.
   Define the bug/feature, expected behavior, and intended implementation before prompting.
4. Avoid over-engineering.
   Prefer small, maintainable changes that match Mindwtr's "simple by default" philosophy.
5. Always review and validate generated code.
   Run relevant tests and verify behavior on real devices/platforms to catch regressions.
6. Keep security in scope.
   Do not introduce insecure defaults, unsafe parsing, token leaks, or new attack surfaces.
