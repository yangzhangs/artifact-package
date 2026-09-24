## Contributing changes

Before you start your first pull request, please complete this checklist:

- Read this entire contributor guide.
- Read the [Code of Conduct](./CODE_OF_CONDUCT.md).
- If you are using AI to assist with coding, read our
  [AI Tool Use Policy](./AI_TOOL_POLICY.md).

---

### Step 1: Evaluate and get buy-in on the change

First, consider that several parts of this repository currently do not accept
contributions. You should refer to the README or CONTRIBUTING file nearest the
code you're interested in.

We also want to be sure that you spend your time efficiently and prepare
changes that aren’t controversial and get stuck in long rounds of reviews. So
if the change is non-trivial, please submit an issue or write a proposal, as
described in the corresponding sections.

For example, we accept contributions to the following sections where you can
find specific contribution guidelines:

- [Mojo standard library](mojo/CONTRIBUTING.md)
- [MAX API and models](/max/CONTRIBUTING.md)
- [MAX AI kernels](/max/kernels/CONTRIBUTING.md)
- [Code examples](examples#contributing)
- [Mojo documentation](mojo/docs#contributing)

---

### Step 2: Create a pull request

If you're experienced with GitHub, here's the basic process:

1. Fork this repo.

2. Create a branch from `main`.

   If you're contributing to the Mojo standard library, see the
   [Mojo standard library developer guide](mojo/stdlib/docs/development.md).

3. Create a PR into the `main` branch of this repo.

4. Skip to [Step 3: PR triage and review](#step-3-pr-triage-and-review).

---

#### Format your changes

Please make sure your changes are formatted before submitting a pull request.
Otherwise, CI will fail in its lint and formatting checks. `bazel` setup
provides a `format` command. So, you can format your changes like so:

```bash
./bazelw run format
```

It is advised, to avoid forgetting, to set-up `pre-commit`, which will format
your changes automatically at each commit, and will also ensure that you
always have the latest linting tools applied.

To do so, install pre-commit:

```bash
pixi x pre-commit install
```

If you need to manually apply the `pre-commit`, for example, if you made a
commit with the github UI, you can do `pixi x pre-commit run --all-files`, and
it will apply the formatting to all Mojo and Python files.

You can also consider setting up your editor to automatically format
Mojo and Python files upon saving.

---

#### Validate your changes

Before submitting, make sure your changes are correct and complete:

- **Run the relevant tests.** If you changed code, run the tests for the
  affected area. For the Mojo standard library, see the
  [development guide](mojo/stdlib/docs/development.md) for instructions.
- **Check for regressions.** Run a broader test pass if your change touches
  shared infrastructure or has wide impact.
- **Assess quality.** Review your diff as a maintainer would. Is the logic
  clear? Are edge cases handled? Is the change well-scoped?

Contributors are responsible for the correctness and quality of their
submissions regardless of whether AI tools were used to produce them.
