# Press F1 → "Dev Containers: Reopen in Container"
air realtime
```

**Key Rules:**

- ❌ No API v1 expansion → use `internal/api/v2/`
- ❌ No telemetry without explicit user opt-in
- ❌ No `any` types in TypeScript
- ✅ Frontend embedded in Go binary (use `air`, not Vite dev server)
- ✅ Pre-commit hooks auto-format & lint
- ✅ AI-assisted coding encouraged - use responsibly

**Need details?** Read the sections below. **Questions?** [Discord](https://discord.gg/gcSCFGUtsd)

---

---

## Table of Contents

- [License and Legal](#license-and-legal)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Code Quality](#code-quality)
- [Testing](#testing)
- [AI-Assisted Development](#ai-assisted-development)
- [Submitting Changes](#submitting-changes)
- [Additional Resources](#additional-resources)

---

## Getting Started

Before contributing:

1. **Read the [License](#license-and-legal)** and [Privacy Policy](PRIVACY.md)
2. **Review [ARCHITECTURE.md](ARCHITECTURE.md)** - Understand the tech stack
3. **Check [existing issues](https://github.com/tphakala/birdnet-go/issues)** - Avoid duplicates
4. **Join [Discord](https://discord.gg/gcSCFGUtsd)** - For discussions and support
5. **Read relevant CLAUDE.md files** - Development guidelines:
   - [CLAUDE.md](CLAUDE.md) - Project overview and universal rules
   - [internal/CLAUDE.md](internal/CLAUDE.md) - Go backend guidelines
   - [frontend/CLAUDE.md](frontend/CLAUDE.md) - Svelte 5 frontend guidelines
   - [internal/api/v2/CLAUDE.md](internal/api/v2/CLAUDE.md) - API v2 guidelines

   **Note:** CLAUDE.md files serve all contributors (AI-assisted or manual).

---

## AI-Assisted Development

BirdNET-Go **welcomes AI-assisted coding tools**. The main developer uses [Claude Code](https://claude.ai/claude-code), and all PRs receive [CodeRabbit AI](https://coderabbit.ai/) reviews.

---

### CLAUDE.md Guidelines

Project guidelines are in CLAUDE.md files (see [Getting Started](#getting-started)). These files work for both AI assistants and manual development.

---

### Responsible AI Usage

**✅ Good Use:**

- Understand codebase patterns
- Generate boilerplate and tests
- Refactor while maintaining behavior
- Write documentation
- Identify bugs and edge cases

**⚠️ Requirements:**

- Review all AI-generated code
- Understand what code does
- Test thoroughly
- Follow project guidelines
- Respect privacy (no sensitive data sharing)

**❌ Prohibited:**

- Submitting code without understanding
- Bypassing quality checks
- Sharing proprietary/sensitive data
- Unverified licensing/attribution
- Misleading/obfuscated code

---

### Getting Started with Claude Code

1. Install: [Claude Code guide](https://docs.claude.com/en/docs/claude-code)
2. Open BirdNET-Go repository
3. CLAUDE.md files provide automatic context
4. Ask Claude for help with specific tasks

**Questions?** Join [Discord](https://discord.gg/gcSCFGUtsd) to discuss AI-assisted development.

---

### Development Guidelines

- [Architecture](ARCHITECTURE.md)
- [Go Backend Guidelines](internal/CLAUDE.md)
- [Frontend Guidelines](frontend/CLAUDE.md)
- [API v2 Guidelines](internal/api/v2/CLAUDE.md)
