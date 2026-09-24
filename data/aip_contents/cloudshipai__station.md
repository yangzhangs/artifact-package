## 🤖 Agentic Coding PRs Welcome!

<mark>We **encourage and welcome** Pull Requests created with AI assistance (Claude, GPT, Copilot, etc.)! However, to maintain code quality and project coherence, agentic PRs must follow these guidelines:</mark>

---

### ✅ Requirements for Agentic PRs

1. **Small, Focused Changes**: Break large features into multiple small PRs (ideally <300 lines changed)
2. **Passing Tests**: All existing tests must pass, and new functionality must include tests
3. **Clear Explanation**: Include a detailed explanation of:
   - What the change does and why it's needed
   - How you tested the functionality
   - <mark>Any AI tools used in development</mark>
   - Any design decisions made during implementation

4. **Documentation**: Update relevant documentation (README, code comments, etc.)

### Commit Messages

Use conventional commits format:
- `feat:` - New features
- `fix:` - Bug fixes  
- `refactor:` - Code refactoring
- `docs:` - Documentation changes
- `test:` - Test additions/modifications

Example:
```
feat: add support for PostgreSQL MCP server

- Add PostgreSQL query templates with {{variables}}
- Implement connection pooling configuration
- Add integration tests for database operations

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```
