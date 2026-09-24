## AI-Assisted Development with OpenCode

We use [OpenCode](https://opencode.ai) for AI-assisted development. OpenCode provides custom commands and skills to help maintain consistency and streamline common workflows.

OpenCode works with most major AI providers (Anthropic, OpenAI, Google, etc.) or you can use [Zen](https://opencode.ai/zen) for optimized coding models. Configure your preferred provider in the OpenCode settings.

> **Important**: All AI-generated code must be thoroughly reviewed by the contributor before submitting a PR. You are responsible for understanding and validating every line of code you submit. If we detect that contributors are simply throwing AI-generated code over the wall without proper review, they will be blocked from the repository.

---

### Getting Started

1. Install OpenCode (see [opencode.ai](https://opencode.ai) for other install methods):
   ```bash
   curl -fsSL https://opencode.ai/install | bash
   ```
2. Configure your AI provider (or use Zen for optimized models)
3. Run `opencode` in the project root

---

### Available Commands

Use these commands in OpenCode by typing the command name:

| Command                        | Description                                              |
| ------------------------------ | -------------------------------------------------------- |
| `/implement <spec-path>`       | Implement a spec from `.agents/plans/` autonomously      |
| `/continue <spec-path>`        | Continue implementing a spec from a previous session     |
| `/interview <file-path>`       | Deep-dive interview to flesh out a spec or design        |
| `/document <module-path>`      | Generate MDX documentation for a module or feature       |
| `/commit`                      | Create a conventional commit for staged changes          |
| `/create-plan <slug>`          | Create a new plan file in `.agents/plans/`               |
| `/create-scratch <slug>`       | Create a scratch file for notes in `.agents/scratches/`  |
| `/create-justification <slug>` | Create a justification file in `.agents/justifications/` |

---

### Typical Workflow

1. **Create a plan**: Use `/create-plan my-feature` to draft a spec for a new feature
2. **Flesh out the spec**: Use `/interview .agents/plans/<file>.md` to refine requirements
3. **Implement**: Use `/implement .agents/plans/<file>.md` to build the feature
4. **Continue if needed**: Use `/continue .agents/plans/<file>.md` to pick up where you left off
5. **Commit**: Use `/commit` to create a conventional commit

---

### Agent Files

The `.agents/` directory stores AI-generated artifacts:

- **`.agents/plans/`** - Feature specs and implementation plans
- **`.agents/scratches/`** - Temporary notes and explorations
- **`.agents/justifications/`** - Decision rationale and technical justifications

These files use a unique ID format (`{word}-{word}-{word}-{slug}.md`) to prevent conflicts.
