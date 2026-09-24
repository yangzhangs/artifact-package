## AI-Assisted Development

Rackula is built using AI-assisted development workflows, primarily using [Claude Code](https://claude.com/claude-code) via [Happy](https://happy.engineering). This approach enables rapid iteration, comprehensive testing, and high code quality through AI-human collaboration.

---

### Working with the AI Workflow

- **Planning documents**: See `.claude/context/` for technical specifications, prompts, and roadmaps
- **AI-specific guidance**: Read `CLAUDE.md` for detailed instructions on using Claude Code with this project
- **Commit co-authoring**: Many commits include AI co-authorship attribution
- **Both approaches welcome**: You can contribute using traditional development or AI-assisted workflows

This is NOT an AI-exclusive project - human contributors are equally welcome! The AI tooling simply provides additional development capabilities and maintains consistency with the existing codebase architecture.

---

### When to Include AI Attribution

Follow these guidelines when using AI assistance in your contributions:

- ✅ **Include attribution** when AI generates substantial code:
  - Complete functions or classes
  - Entire features or components
  - The bulk of a commit's changes
  - Complex algorithms or logic

- ❌ **Skip attribution** for trivial AI assists:
  - Autocomplete suggestions
  - Code formatting
  - Variable name suggestions
  - Docstring generation
  - Minor syntax fixes

When attribution is appropriate, use the `Co-authored-by:` trailer in your commit message (see `CLAUDE.md` for the exact format).

---

### Documentation

Key documentation for contributors:

- **Architecture overview:** `docs/ARCHITECTURE.md` - Start here for codebase orientation
- **Technical overview:** `docs/reference/SPEC.md` - Technical overview and design principles
- **Testing guide:** `docs/guides/TESTING.md` - Testing patterns and best practices
- **AI instructions:** `CLAUDE.md` - Claude Code development workflow

---

## Pull Request Process

1. **Create a Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write tests first (TDD)
   - Implement the feature
   - Ensure all tests pass
   - Run linting and formatting

3. **Commit**
   - Use clear, descriptive commit messages
   - Follow conventional commits format when applicable
   - If using AI assistance, include co-author attribution (see `CLAUDE.md` for format)

4. **Push and Create PR**
   - Push your branch
   - Create a pull request with a clear description
   - Reference any related issues
