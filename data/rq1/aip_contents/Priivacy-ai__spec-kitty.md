## <mark>Supported AI Agents</mark>

<mark>Spec Kitty supports **12 AI coding agents**. When contributing features that affect slash commands, migrations, or templates, ensure changes apply to ALL agents:</mark>

- <mark>**Claude Code** (`.claude/commands/`)</mark>
- <mark>**GitHub Copilot** (`.github/prompts/`)</mark>
- **GitHub Codex** (`.codex/prompts/`)
- **OpenCode** (`.opencode/command/`)
- <mark>**Google Gemini** (`.gemini/commands/`)</mark>
- <mark>**Cursor** (`.cursor/commands/`)</mark>
- **Windsurf** (`.windsurf/workflows/`)
- **Qwen Code** (`.qwen/commands/`)
- **Kilocode** (`.kilocode/workflows/`)
- **Augment Code** (`.augment/commands/`)
- **Roo Cline** (`.roo/commands/`)
- **Amazon Q** (`.amazonq/prompts/`)

**For contributors**: Use the `AGENT_DIRS` constant from `src/specify_cli/upgrade/migrations/m_0_9_1_complete_lane_migration.py` when writing migrations or features that affect slash commands.

---

## Prerequisites for running and testing code

These are one time installations required to be able to test your changes locally as part of the pull request (PR) submission process.

1. Install [Python 3.11+](https://www.python.org/downloads/)
1. Install [uv](https://docs.astral.sh/uv/) for package management
1. Install [Git](https://git-scm.com/downloads)
1. <mark>Have an [AI coding agent available](README.md#-supported-ai-agents)</mark>

---

### Private Dependencies

Spec-kitty depends on two private libraries:
- **[spec-kitty-events](https://github.com/Priivacy-ai/spec-kitty-events)** v3.0.0 - Event system and mission-next integration
- **[spec-kitty-runtime](https://github.com/Priivacy-ai/spec-kitty-runtime)** v0.4.3 - Runtime execution engine

For CI/CD setup, see [SSH Deploy Keys documentation](docs/development/ssh-deploy-keys.md).

For local development, ensure you have SSH access to the repository.

---

## Release Process

Spec Kitty follows a structured release process using GitHub Actions for automated PyPI publishing.

> <mark>**For AI agents**: Use the `/release` skill (`.claude/skills/release/SKILL.md`) for a step-by-step guide.</mark>

---

### Branch Strategy

Spec Kitty maintains two long-lived branches:

- **`main`** — The release branch. All tags MUST be created from `main`.
- **`2.x`** — Development branch for the next major version.

If changes are made on `2.x`, cherry-pick them to `main` before releasing. The `2.x` branch may have test failures that do not affect `main`.

---

### Quick Release (Patch)

For simple bug fixes or improvements already committed to `main`:

```bash

---

### Full Release (Minor/Major)

For larger releases with multiple changes:

1. **Create a release branch**
   ```bash
   git checkout -b release/X.Y.Z main
   ```

2. **Update version number** in `pyproject.toml`
   - Use [Semantic Versioning](https://semver.org/):
     - **Patch** (X.Y.Z): Bug fixes, small improvements
     - **Minor** (X.Y.0): New features, backward compatible
     - **Major** (X.0.0): Breaking changes

3. **Update CHANGELOG.md**
   - Add a new version section immediately after `## [Unreleased]`:
     ```markdown
     ## [X.Y.Z] - YYYY-MM-DD

     ### <emoji> <Category>

     **Short bold summary**:
     - Bullet point details
     ```
   - Categories used in this project (with emoji headings):
     - `### ✨ Added` — New features
     - `### 🔧 Improved` — Enhancements to existing features
     - `### 🐛 Fixed` — Bug fixes
     - `### 💥 Breaking` — Breaking changes
     - `### 📝 Architecture` — ADRs, design decisions
     - `### 🧹 Maintenance` — Refactoring, dependency updates
   - Use ISO date format: `YYYY-MM-DD`

4. **Create a pull request**
   ```bash
   git push origin release/X.Y.Z
   gh pr create --title "Release X.Y.Z: Brief description" --base main
   ```

5. **Wait for PR checks and merge**
   - The Release Readiness Check workflow validates version, changelog, and tests
   - Get approval from a maintainer
   - Merge the PR (use "Merge commit" strategy, not squash)

6. **Create and push the release tag**
   ```bash
   git checkout main && git pull origin main
   git tag -a vX.Y.Z -m "Release vX.Y.Z - Brief description"
   git push origin vX.Y.Z
   ```

7. **Monitor the workflow**
   ```bash
   unset GITHUB_TOKEN && gh run list --workflow=release.yml --limit=1
   unset GITHUB_TOKEN && gh run watch <run-id>
   ```
   Note: `unset GITHUB_TOKEN` is needed because the env var token may have limited scopes (e.g., only `copilot`). The keyring token has full `repo` scope.

8. **Verify the release**
   ```bash
   unset GITHUB_TOKEN && gh release view vX.Y.Z
   pip install spec-kitty-cli==X.Y.Z
   ```

9. **Clean up**
   ```bash
   git branch -d release/X.Y.Z
   git push origin --delete release/X.Y.Z
   ```

---

## AI contributions in Spec Kitty

> [!IMPORTANT]
>
> If you are using **any kind of AI assistance** to contribute to Spec Kitty,
> it must be disclosed in the pull request or issue.

We welcome and encourage the use of AI tools to help improve Spec Kitty! Many valuable contributions have been enhanced with AI assistance for code generation, issue detection, and feature definition.

That being said, if you are using any kind of AI assistance (e.g., agents, ChatGPT) while contributing to Spec Kitty,
**this must be disclosed in the pull request or issue**, along with the extent to which AI assistance was used (e.g., documentation comments vs. code generation).

If your PR responses or comments are being generated by an AI, disclose that as well.

As an exception, trivial spacing or typo fixes don't need to be disclosed, so long as the changes are limited to small parts of the code or short phrases.

An example disclosure:

> This PR was written primarily by GitHub Copilot.

Or a more detailed disclosure:

> I consulted ChatGPT to understand the codebase but the solution
> was fully authored manually by myself.

Failure to disclose this is first and foremost rude to the human operators on the other end of the pull request, but it also makes it difficult to
determine how much scrutiny to apply to the contribution.

In a perfect world, AI assistance would produce equal or higher quality work than any human. That isn't the world we live in today, and in most cases
where human supervision or expertise is not in the loop, it's generating code that cannot be reasonably maintained or evolved.

---

### What we're looking for

When submitting AI-assisted contributions, please ensure they include:

- **Clear disclosure of AI use** - You are transparent about AI use and degree to which you're using it for the contribution
- **Human understanding and testing** - You've personally tested the changes and understand what they do
- **Clear rationale** - You can explain why the change is needed and how it fits within Spec Kitty's goals  
- **Concrete evidence** - Include test cases, scenarios, or examples that demonstrate the improvement
- **Your own analysis** - Share your thoughts on the end-to-end developer experience

---

### What we'll close

We reserve the right to close contributions that appear to be:

- Untested changes submitted without verification
- Generic suggestions that don't address specific Spec Kitty needs
- Bulk submissions that show no human review or understanding

---

### Guidelines for success

The key is demonstrating that you understand and have validated your proposed changes. If a maintainer can easily tell that a contribution was generated entirely by AI without human input or testing, it likely needs more work before submission.

Contributors who consistently submit low-effort AI-generated changes may be restricted from further contributions at the maintainers' discretion.

Please be respectful to maintainers and disclose AI assistance.
