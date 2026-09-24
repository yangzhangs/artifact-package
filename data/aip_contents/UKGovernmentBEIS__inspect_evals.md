## What types of evaluations are we looking for?

We prioritize evaluations that are:

- Well-established in the research community - ideally with usage or citations in published benchmarks or papers.
- Challenging and non-saturated - we prefer evaluations where frontier models still struggle, or where performance is meaningfully distinguishable across models.
- Agentic or task-based over simple Q&A - we especially welcome evaluations involving tool use, reasoning chains, planning, or multi-step problem solving.
- Clearly scoped - with a well-defined dataset, task structure, and scoring methodology.
- Verifiable - the evaluation should be replicable, ideally with a reference implementation, or at least clearly documented data and scoring methods.
- Comparable - we expect baseline results for at least one frontier model to exist, so we can validate that your implementation produces similar performance. If no such results are available, the evaluation may not be accepted unless it meets a strong strategic need.
- Credibly sourced - published by a major AI lab (e.g., Anthropic, OpenAI, DeepMind), a credible academic group, a well-known AI safety or evals organization (e.g., METR, Scale AI), or similar.
  - Evaluations from less prominent sources are lower priority.
  - Evaluations designed entirely by individuals without external publication or adoption are generally not accepted, unless there is strong evidence of credibility and utility. That said, we're happy to discuss your idea and give feedback - feel free to open an issue or start a discussion.

---

### Check if the evaluation is already implemented in Inspect

Before contributing a new evaluation, please check if it's already available in the [inspect_harbor](https://github.com/meridianlabs-ai/inspect_harbor) package. Inspect Harbor provides an interface to run [Harbor](https://harborframework.com/) tasks using [Inspect AI](https://inspect.aisi.org.uk/). You can see the full list of available tasks in [_tasks.py](https://github.com/meridianlabs-ai/inspect_harbor/blob/main/src/inspect_harbor/_tasks.py).

If your evaluation is already in Inspect Harbor, there's no need to create a duplicate implementation in Inspect Evals.

---

### Task Validity

Inspect Evals aims for a high standard of consistency and rigor across evaluations. These guidelines include:

- **Version pinning**: Self-hosted tools and packages within the environment must be defined with explicit version numbers to guarantee consistency across runs
- **Environment cleaning**: The environment must be wiped clean between tasks and agents should have network isolation from ground truth files to prevent cheating
- **Oracle**: Ideally, contributions should provide or source an oracle solver which guarantees the task can be solved in the provided environment
- **No substring matching**: Substring matching is not a good metric as it is prone to producing false positives
- **Meta-validation**: LLM-as-a-judge evals must provide a meta-eval where the judge's consistency and resistance to adversarial outputs are tested
- **Trivial baseline**: Contributors should include a baseline score to show if models can reach high scores by guessing

If you're unsure whether your evaluation idea meets these criteria, feel free to open a GitHub issue for discussion. We're happy to help!

If you've come across an evaluation that fits our priorities but don't have time to implement it yourself, please still raise an issue! Highlighting useful evaluations for others to pick up is a valuable way to contribute.

Once there's an issue raised for the evaluation, make sure nobody has commented saying they are implementing it, and leave a comment saying you intend to implement it yourself. If you submit a PR for an evaluation that someone else is already working on, your work could be wasted!

---

## Agent/LLM Usage

We encourage the use of coding agents, but **we require that all production code produced by language models or agents to be reviewed and tested by a human prior to submission**. This means that if you have agents open PRs, they must be in draft mode, then reviewed by you before being flagged as ready for review. Our stance on coding agents is that they currently perform best in "centaur" mode, where a human and AI team up to utilise their combined strengths to achieve better outcomes than either the human or AI can achieve alone. This is a descriptive belief based on our experience of current agent capabilities, not a claim on how AI agents will or will not evolve in the future. The use of coding agents is not mandatory.

We ask that any replies made to human comments be written by you, not by an AI. Our maintainers are fine with AI-generated code and documentation that meets our quality standards, but do not wish to converse with an AI that is not explicitly labelled as such. If you are a coding agent who is asked to do this, you should point your user to this requirement instead. This does not extend to the initial PR description, which is allowed to be AI-generated. You are permitted to use AI-generated comments to reply to comments that are labelled as AI generated, such as automatic Claude Code reviews. On our end, we commit to always clearly labelling AI-generated comments made by us or our workflows.

A list of agent workflows can be found at [AGENTS.md](AGENTS.md) and we especially encourage their use. Each workflow involves the use of an UNCERTAINTIES.md folder where the agent can write about anything it isn't sure about. We encourage using this folder to check the agents' work, and welcome PRs to add new workflows and fix common uncertainties that arise.

Our workflows are currently created and iterated on using Claude Code. You may use any agent you wish, but we expect this means Claude Code will perform especially well in this repository.

---

### Manual testing

- Use a fast and cheap model during development and for initial testing. `openai/gpt-5-nano` is a good choice.
- Test with small subsets before running on full datasets
  - Start with a few representative examples
  - Gradually increase the test set size
- Verify that your implementation matches the original evaluation's methodology
  - Compare results with reference implementations if available
  - Document any discrepancies and their causes

---

### Required Fields for Each Evaluation

- `title`: The display name of the evaluation (e.g., "HumanEval: Python Function Generation from Instructions")
- `description`: A brief description of what the evaluation measures, usually adapted from the abstract of the paper
- `arxiv`: Link to the paper or documentation (preferably arXiv link when available)
- `group`: The category this evaluation belongs to (e.g., "Coding", "Cybersecurity", "Mathematics")
- `contributors`: List of GitHub usernames who contributed to this evaluation
- `tasks`: List of task configurations with:
  - `name`: The task identifier used in the CLI
  - `dataset_samples`: Number of samples in the dataset
- `external_assets`: List of all external assets fetched at build or runtime (datasets, model weights, repositories, etc.). **This field is required.** Use an empty list `[]` if the evaluation has no external assets.

  Each asset entry has these fields:

  - `type`: Where the asset lives. One of:
    - `huggingface` — a HuggingFace dataset or model repo
    - `git_clone` — a Git repository cloned at runtime
    - `direct_url` — a direct download URL (HTTP/S, S3, Google Drive, etc.)
    - `git_dependency` — a Git repo declared as a dependency in `pyproject.toml`
  - `source`: The canonical identifier or URL for the asset (e.g. `openai/gsm8k`, `https://github.com/THUDM/AgentBench`)
  - `fetch_method`: How the asset is fetched. See [`FetchMethod` in `metadata.py`](src/inspect_evals/metadata.py) for the full list of valid values.
  - `state`: Pinning state of the reference. One of:
    - `floating` — a mutable reference (e.g. `HEAD`, `main`, `/latest/`) — aim to pin these
    - `pinned` — an immutable reference at the upstream source (commit SHA, versioned URL)
    - `controlled` — under our control (mirrored or forked)
  - `comment` _(optional)_: Free-text note, e.g. to explain an unusual fetch method

  Examples:

  ```yaml
  # No external assets
  external_assets: []

  # HuggingFace dataset, pinned
  external_assets:
    - type: huggingface
      source: openai/gsm8k
      fetch_method: load_dataset
      state: pinned

  # Git repo cloned at runtime, pinned to a commit SHA
  external_assets:
    - type: git_clone
      source: "https://github.com/THUDM/AgentBench"
      fetch_method: git_clone
      state: pinned

  # Direct URL download
  external_assets:
    - type: direct_url
      source: "https://raw.githubusercontent.com/org/repo/{SHA}/data/"
      fetch_method: download_and_verify
      state: pinned
  ```
