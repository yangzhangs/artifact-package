# Contributing to Arcane

Thanks for helping make Arcane better! We've built a modern, streamlined development experience that gets you up and running in minutes.

> **Using AI tools?** Please read our [AI Usage Policy](AI_POLICY.md) before contributing.

## 🌟 Ways to Contribute

- 🐛 **Report bugs** using our issue templates
- 💡 **Suggest features** or improvements
- 🔧 **Code contributions** (frontend, backend, DevOps)
- 📚 **Documentation** improvements
- 🌍 **Translations** via [Crowdin](https://crowdin.com/project/arcane-docker-management)
- 🧪 **Testing** and quality assurance

## 🚀 Quick Start

### Prerequisites

- **Docker & Docker Compose** (that's it! 🎉)
- **VS Code** based IDE (recommended for the best developer experience)

> **💡 Working Directory**: Unless otherwise specified, all commands in this guide should be run from the project root directory (`arcane/`).

### 1. Fork and Clone

```bash
git clone https://github.com/<your-username>/arcane.git
cd arcane
```

### 2. Start Development Environment

From the project root directory:

```bash
./scripts/development/dev.sh start
```

That's it! The development environment will automatically:

- 🔥 Start both frontend and backend with hot reload
- 🐳 Handle all dependencies via Docker
- 📊 Set up health checks and monitoring
- 💾 Create persistent storage for your development data

Access your development environment:

- **Frontend**: http://localhost:3000 (SvelteKit with HMR)
- **Backend**: http://localhost:3552 (Go with Air hot reload)

## 🎯 VS Code Integration

For the best development experience, we've included VS Code tasks and workspace configuration.

### Recommended Extensions

When you open the project in VS Code, you'll be prompted to install our recommended extensions. These provide:

- Docker integration and management
- Go language support with debugging
- Svelte/TypeScript support
- Integrated terminal management

### One-Click Development Commands

Use `Ctrl/Cmd+Shift+P` → "Tasks: Run Task" to access:

| Task              | Description                                   |
| ----------------- | --------------------------------------------- |
| **Start**         | Start the development environment             |
| **Stop**          | Stop all services                             |
| **Restart**       | Restart all services                          |
| **Rebuild**       | Rebuild containers (after dependency changes) |
| **Clean**         | Remove all containers and volumes             |
| **Logs**          | Interactive log viewer with service selection |
| **Open Frontend** | Launch frontend in browser                    |

### Quick Build Shortcut

Press `Ctrl/Cmd+Shift+B` to run the default build task (Start Environment).

## 🔍 Development Workflow

### Making Changes

1. **Create a feature branch**:

   ```bash
   git switch -c feat/my-awesome-feature
   # or
   git switch -c fix/issue-123
   ```

2. **Start development** (from project root):

   ```bash
   ./scripts/development/dev.sh start
   # or use VS Code Task: "Start"
   ```

3. **Monitor logs** (choose your preferred method):

   ```bash
   # Interactive selector
   ./scripts/development/dev.sh logs

   # Specific service
   ./scripts/development/dev.sh logs frontend
   ./scripts/development/dev.sh logs backend

   # Or use VS Code Task: "Logs"
   ```

4. **Make your changes** - hot reload will automatically update:
   - **Frontend**: Instant HMR via Vite
   - **Backend**: Auto-rebuild and restart via Air

## 🛠️ Development Commands

**Note**: All commands should be run from the project root directory (`arcane/`).

### Justfile Shortcuts

We provide a `Justfile` for common workflows. Run `just --list` to see everything.

```bash
# Dev environment
just dev docker

# Tests
just test all

# Linting
just lint frontend

# Formatting
just format frontend
```

### Environment Management

```bash
# Start development environment
./scripts/development/dev.sh start

# View service status
./scripts/development/dev.sh status

# Stop all services
./scripts/development/dev.sh stop

# Restart services (for config changes)
./scripts/development/dev.sh restart

# Rebuild containers (for dependency changes)
./scripts/development/dev.sh rebuild

# Clean up everything (nuclear option)
./scripts/development/dev.sh clean
```

### Debugging & Logs

```bash
# Interactive log selection
./scripts/development/dev.sh logs

# All services
./scripts/development/dev.sh logs

# Frontend only (Vite/SvelteKit)
./scripts/development/dev.sh logs frontend

# Backend only (Go/Air)
./scripts/development/dev.sh logs backend

# Shell access
./scripts/development/dev.sh shell frontend
./scripts/development/dev.sh shell backend
```

## 🎨 Code Quality

### Automatic Formatting & Linting

Both services include development-time linting and formatting:

- **Frontend**: ESLint + Prettier (configured in VS Code)
- **Backend**: Go fmt + Go vet (built into Air hot reload)

### Manual Commands

If you need to run checks manually:

```bash
# Frontend checks
docker compose -f docker/compose.dev.yaml exec frontend pnpm check
docker compose -f docker/compose.dev.yaml exec frontend pnpm format

# Backend checks
docker compose -f docker/compose.dev.yaml exec backend go fmt ./...
docker compose -f docker/compose.dev.yaml exec backend go vet ./...
```

## 📝 Commit Guidelines

We use **Conventional Commits** for clear, semantic commit messages:

```bash
git commit -m "feat: add user authentication"
git commit -m "fix: resolve Docker volume mounting issue"
git commit -m "docs: update development setup guide"
git commit -m "refactor: simplify API response handling"
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 🔄 Pull Request Process

1. **Keep changes focused** - One feature/fix per PR
2. **Test your changes** - Ensure both frontend and backend work
3. **Update documentation** - If you change APIs or add features
4. **Link issues** - Reference issues with "Closes #123" or "Fixes #456"
5. **Be responsive** - Address review feedback promptly

### PR Checklist

- [ ] Code builds successfully in development environment
- [ ] Frontend hot reload works correctly
- [ ] Backend hot reload works correctly
- [ ] No linting errors
- [ ] Commit messages follow conventional format
- [ ] PR description explains the change and why it's needed

## 🐛 Troubleshooting

### Common Issues

**Port conflicts:**

```bash
# Stop and clean everything (from project root)
./scripts/development/dev.sh clean

# Check for conflicting processes
lsof -i :3000  # Frontend port
lsof -i :3552  # Backend port
```

**Docker issues:**

```bash
# Reset Docker environment (from project root)
./scripts/development/dev.sh clean
docker system prune -f

# Restart development
./scripts/development/dev.sh start
```

**VS Code tasks not working:**

- Ensure you've opened the project root folder (`arcane/`) in VS Code, not a subfolder or parent directory
- Install recommended extensions when prompted
- Restart VS Code if tasks don't appear
- Verify you're in the correct working directory when running terminal commands

### Need Help?

- **Bug Report**: [Create an issue](https://github.com/ofkm/arcane/issues/new?template=bug.yml)
- **Feature Request**: [Suggest a feature](https://github.com/ofkm/arcane/issues/new?template=feature.yml)
- **Development Question**: Open a discussion in the repository

Thank you for contributing to Arcane! Your help makes this project better for everyone. 🚀

---

# Standalone AI policy file

# AI Usage Policy

Arcane has clear rules for AI-assisted contributions:

- **All AI usage in any form must be disclosed.** You must state the tool you used (e.g., Claude Code, Cursor, GitHub Copilot, ChatGPT) along with the extent that the work was AI-assisted.

- **Pull requests created by AI must have been fully verified with human testing.** AI must not create hypothetically correct code that hasn't been tested. You must run the development environment, verify both frontend and backend work correctly, and manually test your changes. You must not allow AI to write code for platforms or environments you don't have access to manually test on.

- **Code must follow Arcane's existing patterns.** Before writing code, read [AGENTS.md](AGENTS.md) for technical guidance. AI-generated code that ignores project conventions (Svelte 5 syntax, service patterns, error handling) will be rejected.

- **Issues and discussions can use AI assistance but must have a full human-in-the-loop.** This means that any content generated with AI must have been reviewed *and edited* by a human before submission. AI is very good at being overly verbose and including noise that distracts from the main point. Humans must do their research and trim this down.

- **No AI-generated media is allowed** (art, images, videos, audio, etc.). Text and code are the only acceptable AI-generated content, per the other rules in this policy.

- **Contributors who ignore this policy will face consequences.** Undisclosed AI usage or suspected AI usage without disclosure will result in PR closure. Repeated violations may result in being blocked from contributing. You've been warned.

These rules apply to all outside contributions. Maintainers are exempt from these rules and may use AI tools at their discretion; they've proven themselves trustworthy to apply good judgment.

## Testing Requirements

Before submitting any AI-assisted contribution, you must:

1. Start the development environment: `./scripts/development/dev.sh start`
2. Access the frontend at http://localhost:3000 and verify it works
3. Verify the backend at http://localhost:3552 responds correctly
4. Test your specific changes manually
5. Ensure no linting errors exist
6. Verify hot reload works for both frontend and backend

If you prefer `just`, the `Justfile` includes equivalent shortcuts such as `just dev docker`, `just lint frontend`, and `just test backend`.

## There are Humans Here

Please remember that Arcane is maintained by humans.

Every discussion, issue, and pull request is read and reviewed by humans. It is a point of interaction between people and their work. Approaching this with low-effort, unverified submissions is disrespectful and puts the burden of validation on maintainers who volunteer their time.

In a perfect world, AI would produce high-quality, correct code every time. But that reality depends on the person using the AI. Today, we see too many contributions where AI-generated code hasn't been tested, doesn't follow project patterns, or solves problems that don't exist. Until this improves, we need clear rules to protect maintainer time.

## AI is Welcome Here

Arcane is developed with AI assistance, and maintainers use AI tools productively in their workflow. As a project, we welcome AI as a tool for those who use it responsibly!

**Our reason for this policy is not an anti-AI stance**, but rather a response to the increase in low-quality AI-generated pull requests that don't address real user needs or follow project standards. It's about the quality of contributions, not the tools used to create them.

This section exists to be transparent about the project's use of AI and to clarify that this policy targets contribution quality, not the use of AI tools themselves.

## Technical Guidance for AI Tools

If you're using AI tools to contribute to Arcane, ensure your AI is configured with our coding standards. See [AGENTS.md](AGENTS.md) for architecture patterns, anti-patterns to avoid, and project-specific conventions that will help AI tools generate code that matches our standards.

