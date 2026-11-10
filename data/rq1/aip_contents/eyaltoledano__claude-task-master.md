## 🤝 Our Collaborative Approach

We're a **PR-friendly team** that values collaboration:

- ✅ **We review PRs quickly** - Usually within hours, not days
- ✅ **We're super reactive** - Expect fast feedback and engagement
- ✅ **We sometimes take over PRs** - If your contribution is valuable but needs cleanup, we might jump in to help finish it
- ✅ **We're open to all contributions** - From bug fixes to major features

<mark>**We don't mind AI-generated code**, but we do expect you to:</mark>

- <mark>✅ **Review and understand** what the AI generated</mark>
- ✅ **Test the code thoroughly** before submitting
- ✅ **Ensure it's well-written** and follows our patterns
- <mark>❌ **Don't submit "AI slop"** - untested, unreviewed AI output</mark>

> **Why this matters**: We spend significant time reviewing PRs. Help us help you by submitting quality contributions that save everyone time!

---

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/claude-task-master.git
cd claude-task-master
npm install
```

---

### How to Create a Changeset

1. **After making your changes**:

   ```bash
   npm run changeset
   ```

2. **Choose the bump type**:

   - **Major**: Breaking changes
   - **Minor**: New features
   - **Patch**: Bug fixes, docs, performance improvements

3. **Write a clear summary**:

   ```
   Add support for custom AI models in MCP configuration
   ```

4. **Commit the changeset file** with your changes:
   ```bash
   git add .changeset/*.md
   git commit -m "feat: add custom AI model support"
   ```

---

### What We Look For

✅ **Good PRs**:

- Clear, focused changes
- Comprehensive testing
- Good commit messages
- Proper changeset (when needed)
- Self-reviewed code

❌ **Avoid**:

- Massive PRs that change everything
- Untested code
- Formatting issues
- Missing changesets for user-facing changes
- <mark>AI-generated code that wasn't reviewed</mark>

---

## 🏗️ Project Structure

```
claude-task-master/
├── bin/                    # CLI executables
├── mcp-server/            # MCP server implementation
├── scripts/               # Core task management logic
├── src/                   # Shared utilities and providers and well refactored code (we are slowly moving everything here)
├── tests/                 # Test files
├── docs/                  # Documentation
└── .cursor/               # Cursor IDE rules and configuration
└── assets/							   # Assets like rules and configuration for all IDEs
```

---

### Key Areas for Contribution

- **CLI Commands**: `scripts/modules/commands.js`
- **MCP Tools**: `mcp-server/src/tools/`
- **Core Logic**: `scripts/modules/task-manager/`
- **AI Providers**: `src/ai-providers/`
- **Tests**: `tests/`

---

## 💬 Getting Help

- **Discord**: [Join our community](https://discord.gg/taskmasterai)
- <mark>**Issues**: [GitHub Issues](https://github.com/eyaltoledano/claude-task-master/issues)</mark>
- <mark>**Discussions**: [GitHub Discussions](https://github.com/eyaltoledano/claude-task-master/discussions)</mark>
