## Quick Start Guide

We use `uv` as the package and project manager for all the Python packages in this repository. Before contributing, make sure you have `uv` installed (see [installation guide](https://docs.astral.sh/uv/getting-started/installation/)).

If you're ready to dive in, here’s a quick setup guide to get you going:

1. **Fork** the GitHub repo, clone your fork and open a terminal at the root of the git repository `llama_index`.
2. At the root of the repo, run the following command to setup the global virtual environment we use for the pre-commit hooks and the linters:

```bash
uv sync
```

Install `pre-commit` to run pre-commit hooks on each commit:

```bash
uv run pre-commit install
```

Whenever you make changes, make sure they comply with linting rules:

```bash
uv run make lint
```

3. <mark>Navigate to the project folder you want to work on. For example, if you want to work on the OpenAI LLM integration:</mark>

```bash
cd llama-index-integrations/llms/llama-index-llms-openai
```

4. `uv` will take care of creating and setting up the virtual environment for the specific project you're working on. For example, to run the tests you can do:

```bash
uv run -- pytest
```

**That’s it!** The package you're working on is already installed in editable mode, so you can go on, change the code and run the tests!

Once you get familiar with the project, scroll down to the [Development Guidelines](#development-guidelines) for more details.

---

---

## <mark>How to Use AI when Contributing</mark>

<mark>We welcome AI-assisted contributions, but we ask you to follow some core principles and guidelines that can help make the contribution and review process smoother for both you and us maintainers.</mark>

---

### Core Principles

- <mark>**Transparency**: highlight when and where you used AI to generate code, and explain how you verified and validated it</mark>
- <mark>**Accountability**: we require human oversight for every contribution, and we hold human developers accountable for their changes: in this sense, it is best if you don't propose changes you don't understand or cannot maintain</mark>
- <mark>**Quality**: AI code should meet the same quality standards as human code: this means being documented, tested, and following existing patterns</mark>
