## Table of Contents

- [Quick Start](#quick-start)
- <mark>[Tips for Using AI-Assisted Coding](#tips-for-using-ai-assisted-coding)</mark>
- [CI/CD](#cicd)

---

## Quick Start

1. **Fork and Clone:**

   ```bash
   # Fork the repository on GitHub, then:
   git clone https://github.com/YOUR-USERNAME/AReaL
   cd AReaL
   ```

1. **Install Development Dependencies:**

   Check our
   [installation guide](https://inclusionai.github.io/AReaL/en/tutorial/installation.html)
   for detailed setup instructions.

1. **Set Up Pre-commit Hooks:**

   ```bash
   # Install hooks (includes formatting, linting, and commit message checks)
   pre-commit install --install-hooks
   # Subsequent commits will automatically check your files and commit messages:
   git commit -a -m 'feat(engine): my change'
   ```

1. **Find an Issue:**

   - Browse
     [good first issues](https://github.com/inclusionAI/AReaL/labels/good%20first%20issue)
   - Check [help wanted](https://github.com/inclusionAI/AReaL/labels/help%20wanted)
     issues
   - Or create a new issue using our
     [issue templates](https://github.com/inclusionAI/AReaL/issues/new/choose)

1. **Make Your Changes:**

   - Create a branch: `git checkout -b your-feature-name`
   - Make your changes with proper formatting
   - Test your changes following the next step

1. **Test Your Changes:**

   ```bash
   # --sw: step-wise debugging
   # --lf: run the last failed test first
   pytest -sv --sw --lf tests/
   ```

   Our test suite includes:

   - Running all examples to ensure they can execute one RL step
   - Checking individual engine functionalities, including rollout, forward-backward,
     and weight updates
   - Verifying numerical consistency of our packed data format with HuggingFace padded
     input, with and without Ulysses
   - Testing staleness management functionality
   - Ensuring GSM8K SFT loss decreases and RL rewards increase
   - Running other unit tests for individual components

   Some unit tests require multiple GPUs. The entry point scripts are located under
   `tests/torchrun`. In the corresponding test files (e.g.,
   `test_data_redistribution.py`), we use subprocesses to launch distributed experiments
   with `torchrun` and wait for results.

   If you have modified documentation, prepare doc in English and Chinese (use
   [/translate-doc-zh](../en/reference/ai_assisted_dev.md#commands) if needed), then
   build the docs and preview locally:

   ```bash
   ./docs/build_all.sh
   ```

1. **Submit a Pull Request**

We suggest applying our provided agent harness command `/create-pr` whenever possible.
<mark>Use that in `claude`, `opencode`, or any other coding agent CLI.</mark>

**IMPORTANT**: For new features and code refactoring, please submit a corresponding
issue or open a draft PR to discuss with the core developers before making any code
changes. Directly opening a PR that conflicts with our future [roadmap](ROADMAP.md) may
waste your effort.

---

## <mark>Tips for Using AI-Assisted Coding</mark>

See the full
<mark>[AI-Assisted Development Guide](https://inclusionai.github.io/AReaL/en/reference/ai_assisted_dev.html)</mark>
for detailed documentation.
