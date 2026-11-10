### Setting up the Development Environment

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mudler/LocalAI.git
   cd LocalAI
   ```

2. **Build LocalAI:**

   ```bash
   make build
   ```

   This runs protobuf generation, installs Go tools, builds the React UI, and compiles the `local-ai` binary. Key build variables you can set:

   | Variable | Description | Example |
   |---|---|---|
   | `BUILD_TYPE` | GPU/accelerator type (`cublas`, `hipblas`, `intel`, ``) | `BUILD_TYPE=cublas make build` |
   | `GO_TAGS` | Additional Go build tags | `GO_TAGS=debug make build` |
   | `CUDA_MAJOR_VERSION` | CUDA major version (default: `13`) | `CUDA_MAJOR_VERSION=12` |

3. **Run LocalAI:**

   ```bash
   ./local-ai
   ```

4. **Development mode with live reload:**

   ```bash
   make build-dev
   ```

   This installs [`air`](https://github.com/air-verse/air) automatically and watches for file changes, rebuilding and restarting the server on each save.

5. **Containerized build** (no local toolchain needed):

   ```bash
   make docker
   ```

<mark>For GPU-specific Docker builds, see the `docker-build-*` targets in the Makefile and refer to [CLAUDE.md](CLAUDE.md) for detailed backend build instructions.</mark>

---

## Coding Guidelines

This project uses an [`.editorconfig`](.editorconfig) file to define formatting standards (indentation, line endings, charset, etc.). Please configure your editor to respect it.

<mark>For AI-assisted development, see [`AGENTS.md`](AGENTS.md) (or the equivalent [`CLAUDE.md`](CLAUDE.md) symlink) for agent-specific guidelines including build instructions and backend architecture details. Contributions produced with AI assistance must follow the rules in the [AI Coding Assistants](#ai-coding-assistants) section below.</mark>

---

### General Principles

- Write code that can be tested. All new features and bug fixes should include test coverage.
- Use comments sparingly to explain **why** code does something, not **what** it does. Comments should add context that would be difficult to deduce from reading the code alone.
- Keep changes focused. Avoid unrelated refactors, formatting changes, or feature additions in the same PR.

---

### Go Code

- Prefer modern Go idioms — for example, use `any` instead of `interface{}`.
- Use [`golangci-lint`](https://golangci-lint.run) to catch common issues before submitting a PR.
- Use [`github.com/mudler/xlog`](https://github.com/mudler/xlog) for logging (same API as `slog`). Do not use `fmt.Println` or the standard `log` package for operational logging.
- Use tab indentation for Go files (as defined in `.editorconfig`).

---

### Python Code

- Use 4-space indentation (as defined in `.editorconfig`).
- Include a `requirements.txt` for any new dependencies.

---

### Code Review

- All contributions go through code review via pull requests.
- Reviewers will check for correctness, test coverage, adherence to these guidelines, and clarity of intent.
- Be responsive to review feedback and keep discussions constructive.

---

## AI Coding Assistants

<mark>LocalAI follows the **same guidelines as the Linux kernel project** for AI-assisted contributions: <https://docs.kernel.org/process/coding-assistants.html>.</mark>

<mark>The full policy for this repository lives in [`.agents/ai-coding-assistants.md`](.agents/ai-coding-assistants.md). Summary:</mark>

- **AI agents MUST NOT add `Signed-off-by` tags.** Only humans can certify the Developer Certificate of Origin.
- **AI agents MUST NOT add `Co-Authored-By` trailers** attributing themselves as co-authors.
- **Attribute AI involvement with an `Assisted-by` trailer** in the commit message:

  ```
  Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]
  ```

<mark>Example: `Assisted-by: Claude:claude-opus-4-7 golangci-lint`</mark>

  Basic development tools (git, go, make, editors) should not be listed.
- <mark>**The human submitter is responsible** for reviewing, testing, and fully understanding every line of AI-generated code — including verifying that any referenced APIs, flags, or file paths actually exist in the tree.</mark>
- Contributions must remain compatible with LocalAI's **MIT License**.
