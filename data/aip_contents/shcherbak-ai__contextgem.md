## 🤖 Using AI Coding Assistants

This repository is **AI agent-friendly** and includes configuration files to help AI coding assistants understand the codebase:

- **[AGENTS.md](AGENTS.md)** - Project overview, architecture patterns, coding conventions, and workflow guidelines for AI assistants ([agents.md standard](https://agents.md))
- **[CLAUDE.md](CLAUDE.md)** - Configuration for [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)

When using AI assistants (Claude Code, Cursor, etc.) to contribute:

1. **Review AI-generated code** - Always verify changes follow project patterns and pass tests
2. **Handle VCR cassettes yourself** - AI assistants should not run tests that call LLM APIs without existing cassettes
3. **Manage git operations yourself** - Review and commit changes manually rather than letting AI handle git

> **💡 Tip:** AI assistants work best when given specific, focused tasks. Break large contributions into smaller pieces for better results.

---

### 📁 Project Structure

Below is a high-level overview of the codebase layout and where to make different types of contributions:

```
contextgem/
│
├── contextgem/
│   │
│   ├── internal/                 # 🔧 Core implementation (start here for new features)
│   │   ├── base/                 #   - Core abstractions & business logic
│   │   │   ├── concepts.py       #     - Internal concept implementations
│   │   │   ├── aspects.py        #     - Internal aspect implementations  
│   │   │   ├── documents.py      #     - Internal document processing
│   │   │   ├── llms.py           #     - Internal LLM functionality
│   │   │   └── ...               #     - More internal implementations
│   │   ├── prompts/              #   - LLM prompt templates
│   │   ├── typings/              #   - Type definitions
│   │   └── ...                   #   - More internal modules
│   │
│   └── public/                   # 🎯 User-facing API (thin facades exposing internals)
│       ├── concepts.py           #   - Public concept facades
│       ├── aspects.py            #   - Public aspect facades 
│       ├── documents.py          #   - Public document facades
│       ├── pipelines.py          #   - Public pipeline facades
│       ├── llms.py               #   - Public LLM facades
│       └── ...                   #   - More public modules
│
├── tests/
│   ├── cassettes/                # 📼 VCR recordings (auto-generated)
│   ├── test_all.py               # ✅ Add your tests here
│   ├── utils.py                  # 🛠️ Test utilities & dummy env vars
│   └── ...                       # 📁 Test data files
│
├── docs/
│   ├── source/                   # 📚 Documentation source files
│   └── ...                       # 📋 Build configs & outputs
│
├── dev/
│   ├── usage_examples/           # 📝 Code examples for docs
│   ├── notebooks/                # 📓 Notebooks (auto-generated)
│   ├── readme.template.md        # ✏️ Edit this, not README.md
│   └── ...                       # 🛠️ Development scripts
│
├── pyproject.toml                # ⚙️ Dependencies & project config
└── README.md                     # 🤖 Auto-generated (don't edit)
```

**🎯 Quick Start for Your Contribution:**
- **Adding new functionality?** → Implement in `contextgem/internal/` (core logic). Then expose via a thin public facade in `contextgem/public/` using the registry.
- **Writing tests?** → Add to `tests/test_all.py::TestAll`  
- **Updating docs?** → Edit files in `docs/source/` or `dev/`
- **Fixing README?** → Edit `dev/readme.template.md`

> **💡 Note:** Implement functionality in `internal/` (base classes, validation, serialization, typing). Use `public/` to expose thin, documented facades that inherit from internal classes and are registered with `@_expose_in_registry` decorator to ensure deserialization and instance creation utils return public types. Do not import public classes in internal modules; use the registry for type resolution and publicization.


---

---

### ✏️ Making Changes

1. **🌿 Create a new branch**:

    For example:
    ```bash
    git checkout -b feature/your-feature-name
    ```

    When creating a branch, use one of the following prefixes that matches your change type:

    - `bugfix/` - For bug fixes (e.g., `bugfix/fix-llm-timeout`)
    - `feature/` - For new features (e.g., `feature/add-new-concept-type`)
    - `breaking/` - For breaking changes (e.g., `breaking/concepts-api-v2`)
    - `docs/` - For documentation updates (e.g., `docs/update-aspects-guide`)
    - `perf/` - For performance improvements (e.g., `perf/optimize-prompts`)
    - `refactor/` - For code cleanup or refactoring (e.g., `refactor/simplify-error-handling`)

    General guidelines:
    - Use hyphens (-) between words, not underscores or spaces
    - Be specific but concise about what the branch does
    - Include issue numbers when applicable (e.g., `bugfix/issue-42`)
    - Keep branch names lowercase

2. **📝 Make your changes** following our code style guidelines.

    We use several tools to maintain code quality:

    - **Ruff**: For code formatting and linting
    - **Pyright**: For static type checking
    - **Bandit**: For Python security vulnerability scanning
    - **Deptry**: For dependency health checks (unused, missing, transitive dependencies)
    - **Interrogate**: For docstring coverage checking
    - **Pre-commit hooks**: To automatically check and format code before commits

    The pre-commit hooks will automatically check and format your code when you commit. There are two scenarios to be aware of:

    **If the hooks modify any files during commit** (such as Ruff formatting):
    1. Review the changes made
    2. Add the modified files to the staging area
    3. Commit again

    **If security issues are detected** (Bandit):
    1. Review the security findings in the terminal output
    2. Fix the identified security issues in your code
    3. Add the fixed files to the staging area
    4. Commit again

3. **🧪 Run tests** to ensure your changes do not break existing functionality:
   ```bash
   uv run pytest
   ```

   > **Note:** We use [pytest-recording](https://github.com/kiwicom/pytest-recording) to record and replay LLM API interactions. Your changes may require re-recording VCR cassettes for the tests. See [VCR Cassette Management](#vcr-cassette-management) section below for details.

4. **💾 Commit your changes** using Conventional Commits format:
   
   We use [Conventional Commits](https://www.conventionalcommits.org/) format for our commit messages. Instead of using regular git commit, please use commitizen:

   ```bash
   uv run cz commit
   ```

   This will guide you through an interactive prompt to create a properly formatted commit message with:
   - Type of change (feat, fix, docs, style, refactor, etc.)
   - Optional scope (e.g., api, cli, docs)
   - Short description
   - Optional longer description and breaking change notes

   Example of resulting commit message:
   ```
   docs(readme): update installation instructions
   ```

   > **Note:** If pre-commit hooks fail or modify files during `cz commit`, you can retry with the same message:
   > ```bash
   > uv run cz commit --retry
   > ```

---

### 📼 VCR Cassette Management

We use [pytest-recording](https://github.com/kiwicom/pytest-recording) to record and replay HTTP interactions with LLM APIs (both cloud-based and local). This allows tests that call LLM APIs to run without making actual API calls after the initial recording.

> **Note:** Tests that do not call LLM APIs do not require or use VCR cassettes. The cassette system only applies to tests that interact with LLM APIs.

---

#### Why VCR Cassettes?

VCR cassettes provide the most reliable testing approach for ContextGem because:

- **Real API Testing**: Testing with actual LLM APIs ensures our functionality works as expected with real responses, edge cases, and API behaviors
- **Scalability**: With a significant number of LLM API tests, hardcoding requests/responses would be impractical and unmaintainable
- **Reproducibility**: Once recorded, tests run consistently without variability in LLM responses
- **No Setup Friction**: Contributors can run tests without API keys or local LLM installations

Local LLMs (Ollama, LM Studio, etc.) also use HTTP APIs (typically on localhost) and their interactions are recorded in cassettes too.

The test suite automatically uses dummy environment variables with pre-recorded cassettes when no `.env` file is present, so most contributors won't need to set up real API keys or local LLM servers.

---

#### ✅ Scenario 1: No Cassette Recording Required

**When this applies:**
- New tests that **do not** call LLM APIs
- Code changes that don't modify internal prompts or LLM parameters
- Changes are compatible with existing pre-recorded API calls (confirmed by passing tests)

**What to do:**
- Nothing! Tests that call LLM APIs should pass by replaying from existing cassettes with automatically-set dummy environment variables
- No need to create a `.env` file or set up API keys

---

---

#### 🆕 Scenario 2: New Cassettes Need Recording

**When this applies:**
- New test methods that call LLM APIs (cloud-based or local)
- Adding tests for new functionality that requires LLM interaction

**What to do:**

1. **Create a `.env` file** locally (ignored by git) with the API keys for the LLM services your new tests will use:
   ```
   # Only include the variables for LLM APIs your tests actually call
   
   # For OpenAI API tests
   CONTEXTGEM_OPENAI_API_KEY=your_openai_api_key
   
   # For Azure OpenAI tests
   CONTEXTGEM_AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   CONTEXTGEM_AZURE_OPENAI_API_BASE=your_azure_openai_base
   CONTEXTGEM_AZURE_OPENAI_API_VERSION=your_azure_openai_api_version
   
   # For debugging output
   CONTEXTGEM_LOGGER_LEVEL=DEBUG
   ```

2. **For new LLM providers**, create environment variables prefixed with `CONTEXTGEM_`:
   ```
   CONTEXTGEM_GOOGLE_AI_STUDIO_API_KEY=your_google_api_key
   ```

3. **Update dummy variables** in `tests/utils.py` by adding your new environment variables to the `default_env_vars` dictionary in `set_dummy_env_variables_for_testing_from_cassettes()`, mapped to a dummy value (e.g. "DUMMY")

4. **Add the VCR decorator** to your new test methods that call LLM APIs (cloud or local):
   ```python
   @pytest.mark.vcr
   def test_your_new_llm_feature(self):
       # Your test code that calls LLM APIs (cloud or local)
   ```
   > ⚠️ **Important:** Without the `@pytest.mark.vcr` decorator, no cassette will be recorded!

5. **Run your new tests** - new cassettes will be created automatically

6. **Verify redaction** - check that sensitive data is properly redacted in the new cassette files

7. **Test with dummy variables** - delete your `.env` file and run tests again to confirm LLM API tests pass by replaying from cassettes with dummy variables

---

---

#### 🔄🔄 Scenario 4: All Cassettes Need Re-recording

**When this applies:**
- You modified internal prompts (direct changes or code that renders prompts differently)
- You changed default LLM API parameters
- Multiple LLM-related tests fail due to your changes

**What to do:**

1. **Delete all cassette files**:
   ```bash
   # On Unix/Linux/Mac
   rm tests/cassettes/*.yaml
   
   # On Windows
   del tests\cassettes\*.yaml
   ```

2. **Create a `.env` file** with your API keys (same as Scenario 2)

3. **Run all tests** to re-record everything:
   ```bash
   uv run pytest
   ```

> ⚠️ **Important:** This will use significant API quota and may incur substantial costs!

---

---

#### Local LLM Testing

For local LLM testing, install the following tools and download the relevant models identified under `ollama` and `lm_studio` prefixes in `tests/test_all.py`:
- [Ollama](https://ollama.ai/) 
- [LM Studio](https://lmstudio.ai/)
> ⚠️ **Important:** Your system needs to have an appropriate GPU capacity to run such local LLMs.

---

#### Important Notes

> **💰 Cost Warning:** Recording cassettes for test methods that use live LLM API (non-local LLMs) uses your API keys and **will incur charges**. Scenario 4 (re-recording all cassettes) can be particularly expensive.

> **🔒 Security:** Environment variables such as API keys are automatically stripped from cassettes, but always verify new cassette content.

> **🧪 Testing:** After recording, delete your `.env` file and run tests again to ensure LLM API tests pass by replaying from cassettes with dummy variables.

---

#### Network Egress Control

The test suite uses [tethered](https://github.com/shcherbak-ai/tethered) to enforce network egress control at the socket level during VCR-marked tests:

- **Replay mode** (cassette exists): blocks all outbound connections except HuggingFace (for SaT model downloads not captured by VCR)
- **Recording mode** (no cassette): allows only approved endpoints (LLM APIs, HuggingFace for model downloads, genai-prices for cost data) and localhost for local LLMs

If you add tests that connect to new endpoints, update the `_TETHERED_RECORDING_ALLOW` list in `tests/conftest.py`.


---

---

### ⚠️✅ Expected Test Warnings

Warnings generated during tests are often expected and by design. Many warnings are intentionally triggered to test error handling, edge cases, and warning systems. Common expected warnings include:

- LLM extraction errors and retries (testing error handling)
- Missing LLM roles (testing validation logic)
- Concurrency optimization warnings (testing performance comparisons)
- Deprecation warnings from dependencies

**Key Point**: If tests **PASS** with warnings, this should **not** prevent you from submitting your PR. The test suite is designed to handle and expect these warnings as part of normal operation.
