# Contributing to Delta Kernel (Rust)

> [!NOTE]
> **Found a bug?** Please first search [existing issues] to avoid duplicates. If you find a related
> issue, add your details there. Otherwise, open a new issue with a reproducible example including
> Rust version, delta-kernel-rs version, code executed, and error message.

[existing issues]: (https://github.com/delta-io/delta-kernel-rs/issues)

## How to Contribute

For trivial fixes, etc. please feel free to open a PR directly (Please see [Getting you PR
reviewed](#getting-your-pr-reviewed) below). For larger changes, we follow a structured contribution
process to ensure high-quality code:

1. **Start with an issue and/or design sketch**: Open an issue describing what you want to
   contribute and why. Continue to step 2 after reaching some consensus. This helps us avoid wasted
   effort (perhaps you were building something that someone else was already pursuing or already
   explored and rejected). Including a design sketch will help drive consensus (often a simple
   diagram or bullet points outlining high-level changes is sufficient).
2. **Prototype/POC**: Create a PR marked as prototype/draft (not intended to merge) and gather
   feedback to further de-risk the design. This PR is not intended to be merged but will guide the
   implementation and serve as a proving ground for the design. Then, pieces are torn out into
   smaller PRs that can be merged.
3. **Implementation**: Finally, create PR(s) to implement the feature (production code, tests,
   thorough docs, etc.). Often the initial POC will be split into multiple smaller PRs (e.g.,
   refactors, then feature additions, then public APIs specifically). Care should be taken to ensure
   each PR is easily review-able and thoroughly tested.

## Getting your PR reviewed

We invite everyone who would like their PRs reviewed to review _other_ open PRs as
well. Like most open source projects, our review bandwidth is limited, and help from users is
greatly appreciated. This helps increase the overall review rate, and allows contributors to build
credibility within the project.

PRs from contributors who do not review others' work will be lower priority, though we do try to
review all PRs as promptly as possible.

We also encourage contributors to optimize their PRs for review:
- A crisp and complete PR description that explains clearly what the change is for cross-checking
  against the code.
- Tightly-scoped. That is, don't mix multiple changes in a single PR.
- Code structure and doc comments optimized for understandability (e.g. avoid bloat, redundancy, and
convoluted control flow).

PRs that do not follow these principles are much more time consuming to review, and less likely to
get prompt reviews.

## AI-Assisted Contributions

We welcome contributors who use AI coding tools, but all contributions must reflect genuine
understanding of the changes being made. Please read our [AI Policy](AI_POLICY.md) before
submitting a PR.

## Forking and Setup

1. Fork the repository into your account
2. Clone your fork locally:
   ```bash
   git clone git@github.com:YOUR_USERNAME/delta-kernel-rs.git
   cd delta-kernel-rs
   ```
3. Add the upstream remote:
   ```bash
   git remote add upstream git@github.com:delta-io/delta-kernel-rs.git
   ```

Now you have:
- `origin` pointing to your fork
- `upstream` pointing to the original repository

## Development Workflow

Our trunk branch is named `main`. Here's the typical workflow:

1. Pull the latest main to get a fresh checkout:
   ```bash
   git checkout main
   git pull upstream main
   ```
2. Create a new feature branch:
   ```bash
   git checkout -b my-feature
   ```
   (NB: Consider using `git worktrees` for managing multiple branches!)
3. Make your changes and test them locally. See our CI runs for a full set of tests.
   ```bash
   # run most of our tests, typically sufficient for quick iteration
   cargo test
   # run clippy
   cargo clippy --all-features --tests --benches -- -D warnings
   # build docs
   cargo doc --workspace --all-features
   # highly recommend editor that automatically formats, but in case you need to:
   cargo +nightly fmt

   # run more tests
   cargo test --workspace --all-features -- --skip read_table_version_hdfs

   # see ffi/ dir for more about testing FFI specifically
   ```
4. Push to your fork:
   ```bash
   git push origin my-feature
   ```
5. Open a PR from `origin/my-feature` to `upstream/main`
6. Celebrate! 🎉

**Note**: Our CI runs all tests and clippy checks. Warnings will cause CI to fail.

**Note**: We require two approvals from code owners for any PR to be merged.

## Pull Request Best Practices

#### General Tips

1. When making your first PR, please read our contributor guidelines: https://github.com/delta-incubator/delta-kernel-rs/blob/main/CONTRIBUTING.md
2. Run `cargo t --all-features --all-targets` to get started testing, and run `cargo +nightly fmt`.
3. Ensure you have added or run the appropriate tests for your PR.
4. If the PR is unfinished, add '[WIP]' in your PR title, e.g., '[WIP] Your PR title ...'.
5. Be sure to keep the PR description updated to reflect all changes.

#### PR Title Formatting

This project uses conventional commits: https://www.conventionalcommits.org/

Each PR corresponds to a commit on the `main` branch, with the title of the PR (typically) being
used for the commit message on main. In order to ensure proper formatting in the CHANGELOG please
ensure your PR title adheres to the conventional commit specification.

Examples:
- new feature PR: "feat: new API for snapshot.update()"
- bugfix PR: "fix: correctly apply DV in read-table example"

#### PR Testing

Please make sure to add test cases that check the changes thoroughly including negative and positive cases if possible.
If it was tested in a way different from regular unit tests, please clarify how you tested, ideally via a reproducible test documented in the PR description.

## Resources

- [Delta Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md)
- [Delta Lake Slack](https://go.delta.io/slack) - Join us in the `#delta-kernel` channel

---

# Standalone AI policy file

# Delta Kernel (Rust) AI Policy

### Overview

We recognize that AI coding assistants are part of many developers' workflows. Thoughtful use of these tools can improve productivity and help contributors explore unfamiliar parts of the codebase. However, delta-kernel-rs implements the Delta Lake protocol with strict correctness requirements, and contributions must reflect genuine understanding of the changes being made.

### Guidelines for Contributors

**Be respectful of reviewers and other contributors**. Reviewing takes time and effort, and changes that are needlessly complex, poorly structured, or bloated make that work harder. Plus, future contributors will have to work with (or around) whatever code you merge. If you're unsure whether your contribution is well-structured or appropriately scoped, seek guidance before investing significant effort. You can open a GitHub issue to discuss your approach, use a draft PR to get early feedback on direction, or ask in the Delta-Users Slack.

**Understand and own your changes.** Every change you push and every review you leave reflects on your professional character and reputation – regardless of whether you used tools like AI. If you use AI tools to assist with code generation, you must fully understand every line of the resulting contribution. You should be able to explain the design, justify implementation choices, and debug issues during review. If you cannot, the contribution is not ready to submit. 

Additionally, please **write your own PR description** and ensure it is crisp, complete, and correct.

**Call out unknowns.** If there are any parts of the change you are less confident about – AI generated or otherwise – leave comments on your own PR explaining the concern and what steps you took to verify correctness. Reviewers can then focus their attention where it matters most.

**Match project conventions.** AI tools often generate code that is stylistically inconsistent with a project. Ensure your contributions follow the conventions used in the rest of the codebase, including PR titles (conventional commit format), doc comments, data model, use of helper/utility functions, and error handling patterns.

**Watch for common AI pitfalls:**

* Protocol-incompatible behavior that looks plausible but violates the Delta spec  
* Incorrect or superficial fixes that mask the real problem  
* Changing correct kernel code to match incorrect test expectations (or vice-versa)  
* Bloated and/or duplicative code (AI agents often struggle with encapsulation and abstraction)  
* Overly verbose, duplicated and/or unnecessary documentation  
* Doc and code comments that are stale or refer to the development process (such as dead-end prototyping attempts or initial implementation bugs that were already fixed) rather than describing the current state of the code and the design behind it. These are often called "temporal references."  
* Unnecessary test cases or test scaffolding, or bloated/duplicated test structure (use helpers\!)

**Disclose copyrighted materials**. Contributors are responsible for ensuring that any copyrighted third-party material appearing in AI-generated output has appropriate attribution and licensing. See the [Linux Foundation's Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai) for further information on licensing considerations.

### What We Will Not Accept

**Unreviewed AI PRs**. PRs that appear to be raw AI output submitted without meaningful engagement from the author may be closed without review. Maintainers with access to AI tools could generate such code more efficiently themselves, and the contributor gains nothing from the review process.

**Unreviewed AI-assisted comments on issues or PRs.** The same ownership principle applies to review comments as to code: if you use AI tools to help draft a comment or review, you are responsible for its quality, completeness, and accuracy. Review and edit AI-assisted output before posting — do not paste raw AI output as-is, as such comments tend to be formulaic and consume attention without adding value.

Automated bots or agents that post AI-generated content without human review are strictly prohibited, unless explicitly configured by project maintainers (e.g., CI-integrated review tools).

### Why This Matters

**delta-kernel-rs is a protocol implementation where correctness is critical**. A subtle bug can cause data loss or corruption for downstream connectors. Code review is a collaborative process that depends on the author understanding their changes well enough to engage meaningfully with reviewer feedback.

**Our reviewing capacity is limited**. Large PRs that lack the requisite understanding may not get reviewed and may eventually be closed. If you want to contribute but are unfamiliar with the codebase, a high-quality issue with a clear problem statement and reproducible example is often a more valuable starting point than an AI-generated PR out of thin air.

### Disclosures

AI tools were used to refine early drafts of this policy, and the final content was edited, reviewed, and approved by human maintainers.

### Sources

This policy was written with input from:

* [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai)  
* [Matplotlib Contributing Guide — Restrictions on Generative AI Usage](https://matplotlib.org/devdocs/devel/contribute.html?utm_source=chatgpt.com#restrictions-on-generative-ai-usage)  
* [Delta-RS Contributing Guide — AI Generated Code](https://github.com/delta-io/delta-rs/blob/main/CONTRIBUTING.md?utm_source=chatgpt.com#ai-generated-code)  
* [DataFusion Contributor Guide — AI-Assisted Contributions](https://datafusion.apache.org/contributor-guide/index.html?#ai-assisted-contributions)

