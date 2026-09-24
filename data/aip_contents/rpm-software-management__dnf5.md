## <mark>AI-assisted contributions policy</mark>

<mark>The following policy is adapted from [the Fedora Council AI-Assisted Contributions Policy](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/), which was originally authored by Jason Brooks, the Fedora Council, and the Fedora community.</mark>

<mark>You **MAY** use AI assistance for contributing to this project, as long as you follow the principles described below.</mark>

1. **Accountability**:

   You **MUST** take the responsibility for your contribution.

   Contributing to this project means vouching for the quality, license compliance, and utility of your submission.

<mark>All contributions, whether from a human author or assisted by large language models (LLMs) or other generative AI tools, must meet our standards as described in this CONTRIBUTING document.</mark>

   The contributor is always the author and is fully accountable for the entirety of these contributions.

2. **Transparency**:

<mark>You **MUST** disclose the use of AI tools when the significant part of the contribution is taken from a tool without changes. You **MUST** use an `Assisted-by: <name of AI tool>` line at the end of your git commit messages to do so, for example:</mark>

     * <mark>`Assisted-by: generic LLM chatbot`</mark>

     * `Assisted-by: ChatGPTv5`

<mark>You **SHOULD** disclose the other uses of AI tools, where it might be useful.</mark>

   Routine use of assistive tools for correcting grammar and spelling, or for clarifying language, does not require disclosure.

3. **Contribution & Community Evaluation**:

<mark>AI tools may be used to assist human reviewers by providing analysis and suggestions.</mark>

<mark>You **MUST NOT** use AI as the sole or final arbiter in making a substantive or subjective judgment on a contribution.</mark>

   The final accountability for accepting a contribution always rests with the human contributor who authorizes the action.

---

## Pull request checklist

When you submit your pull request or push new commits to it, our automated
systems will run some checks on your new code. We require that your pull request
passes these checks. However, note that there are more criteria that your pull request must pass before we can
accept and merge it. We recommend that you ensure the following locally
before you submit your code:

* Code must build.

  Ensure that your code builds [locally](#setting-up-a-development-environment) unless you need some help from us or you need us
  to review work in progress changes.

* Code must be tested.

  If your pull request includes new or modified functionality within the library, we kindly request that you provide
  matching unit tests in the project's test directory to cover these changes. However, if the changes only affect
  the command-line interface, you can provide related CI tests in the
  [ci-dnf-stack](https://github.com/rpm-software-management/ci-dnf-stack) component.
  If you need our assistance, ask the maintainers for help.

* Code must pass sanity checks.

  Test the sanity of the codebase by performing [pre-commit](https://pre-commit.com/) checks.
  In the `dnf5` directory, run the following commands:

  ```bash
  pre-commit install
  git add _<your_changes>_
  git commit -m "_<your_commit>_"
  ...
  Check the results.

  ```

  All checks will run as part of a PR action on GitHub. Therefore, make sure not to skip the checks if you do not
  want to amend your contribution.

  As part of pre-commit checks, we perform checks such as trailing whitespaces, end of file fixes, clang-format,
  and rpmlint checks. For more information,
  see [.pre-commit-config.yml](https://github.com/rpm-software-management/dnf5/blob/main/.pre-commit-config.yaml).

* <mark>AI-assisted commits must be labeled according to the above AI-assisted contributions policy.</mark>
