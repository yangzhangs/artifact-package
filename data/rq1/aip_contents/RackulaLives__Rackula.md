## <mark>AI-Assisted Development</mark>

<mark>Rackula is built using AI-assisted development workflows, primarily using [Claude Code](https://claude.com/claude-code) via [Happy](https://happy.engineering). This approach enables rapid iteration, comprehensive testing, and high code quality through AI-human collaboration.</mark>

---

### Working with the AI Workflow

- <mark>**Planning documents**: See `.claude/context/` for technical specifications, prompts, and roadmaps</mark>
- <mark>**AI-specific guidance**: Read `CLAUDE.md` for detailed instructions on using Claude Code with this project</mark>
- <mark>**Commit co-authoring**: Many commits include AI co-authorship attribution</mark>
- <mark>**Both approaches welcome**: You can contribute using traditional development or AI-assisted workflows</mark>

<mark>This is NOT an AI-exclusive project - human contributors are equally welcome! The AI tooling simply provides additional development capabilities and maintains consistency with the existing codebase architecture.</mark>

---

### <mark>When to Include AI Attribution</mark>

<mark>Follow these guidelines when using AI assistance in your contributions:</mark>

- <mark>✅ **Include attribution** when AI generates substantial code:</mark>
  - Complete functions or classes
  - Entire features or components
  - The bulk of a commit's changes
  - Complex algorithms or logic

- <mark>❌ **Skip attribution** for trivial AI assists:</mark>
  - Autocomplete suggestions
  - Code formatting
  - Variable name suggestions
  - Docstring generation
  - Minor syntax fixes

<mark>When attribution is appropriate, use the `Co-authored-by:` trailer in your commit message (see `CLAUDE.md` for the exact format).</mark>

---

### Documentation

Key documentation for contributors:

- **Architecture overview:** `docs/ARCHITECTURE.md` - Start here for codebase orientation
- **Technical overview:** `docs/reference/SPEC.md` - Technical overview and design principles
- **Testing guide:** `docs/guides/TESTING.md` - Testing patterns and best practices
- <mark>**AI instructions:** `CLAUDE.md` - Claude Code development workflow</mark>

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
   - <mark>If using AI assistance, include co-author attribution (see `CLAUDE.md` for format)</mark>

4. **Push and Create PR**
   - Push your branch
   - Create a pull request with a clear description
   - Reference any related issues
