## How to start a contribution

The team always encourages early communication for all types of contributions. Found a bug or see something that could be improved? Open an issue. Want to address something bigger like adding new package manager support or overhauling the entire project? Open an issue or start a Discussion on Github. This way, we can give you guidance and avoid your work being wasted on an implementation which does not fit the project's scope and goal.

Alternatively, submit a pull request with one of the following

* A high-level design of the feature, highlighting goals and key decision points.
* A proof-of-concept implementation.
* In case the change is trivial, you can start with a draft or even provide a PR with the final implementation.

When working on a pull request please make sure that you have followed [pull
request guidelines](#pull-request-guidelines). For AI-assisted contributions,
make sure to comply with the [AI Contribution Policy](AI_CONTRIBUTION_POLICY.md).
Please consult [Development](#development) section, it contains a lot of helpful
information which will make contributing fast and pleasant process.

---

### How we deal with larger features

Implementing a larger feature (such as adding a new package manager) is usually a very long and
detailed effort. This type of work does not fit well into a single pull request; after several
comment threads it becomes almost unmanageable (for you) and very hard to review (for us). For that
reason, we request the following:

- Submit a design document that supplements the code. For new package managers, we have a
  [design template](docs/design/package-manager-template.md) that can help guide the implementation.
- New package managers should mark themselves as "experimental" by adding the `x-` prefix to its name.
- Submit small pull requests, with each one implementing a single piece of the overall feature.
  Experimental features do not need to work end to end, though these should provide warnings/errors
  for missing functionality when possible.

Note the following:

* Experimental features are not fully endorsed by the maintainers, and maintainers will not provide support.
* Experimental features are not production-ready and should never be used in production.
* Always expect that an experimental feature can be fully dropped from this project without any prior notice.
* A feature toggle is needed to allow users to opt-in. This is currently handled by prefixing the package manager name with `x-`
  (e.g.`"type": "x-foo"` instead of `"type": "foo"`).
* All SBOMs produced when an experimental feature is used will be marked as such.

If, for some reason, you feel this proposed workflow does not fit the feature you're contributing, please reach out to the maintainers so we can provide an alternative.

---

#### Making experimental features production-ready

When a feature's development has reached a stable point, you can propose making it an official part of the project. This signals to users that the feature is production-ready. To communicate this intent to the maintainers, open a pull request containing an Architecture Decision Record (ADR) with an outline of the implementation, and a clear statement of all decisions which were made (as well as their rationale).

Once maintainers are confident that they have enough information to maintain the new feature as officially supported they will accept it and help with moving it out from under experimental flag.

---

### Hermeto's Ethos

Whenever adding a new feature to Hermeto, it is important to keep these fundamental aspects in mind

1. Report prefetched dependencies as accurately as possible

    Hermeto's primary goal is to prefetch content and enable hermetic builds. But hermetic builds are only useful if they end up providing a more accurate SBOM than a non-hermetic build would. Hermeto strives to download only what's explicitly declared in a project's source code, and accurately report it in the resulting SBOM.

2. Avoid arbitrary code execution

    Some package manager implementations rely on third-party tools to gather data or even for fetching dependencies. This brings the risk of arbitrary code execution, which opens the door for random things to be part of the prefetched content. This undermines the accuracy of the SBOM, and must be avoided at all costs.

3. Always perform checksum validation

    The content provided to the build will only be safe if all of the downloaded packages have their checksums verified. In case a mismatch is found, the entire request must be failed, since the prefetched content is tainted and is potentially malicious. There are two types of checksums: server-provided and user-provided. Hermeto prefers but does not require the latter. Every dependency which does not have a user-provided checksum verified, must be clearly marked as such in the resulting SBOM (e.g. see 'pip' support). All dependencies must have at least one checksum in order to be considered validated.

4. Favor reproducibility

    Always use fully resolved lockfiles or similar input files to determine what content needs to be download for a specific project (e.g. npm's `package-lock.json`, a `pip-compile` generated `requirements.txt`, etc). Resolving the dependencies during the prefetch will prevent its behavior from being deterministic—in other words, the same repository and the same commit hash should always result in identical prefetch results.

[=== 独立AI政策文件: AI_CONTRIBUTION_POLICY.md ===]

# AI Contribution Policy

## Purpose

This policy establishes guidelines for contributions to Hermeto that involve the
use of AI tools, including but not limited to Large Language Models (LLMs), code
generation assistants, and similar technologies. It aims to balance openness to
modern development workflows with the project's need for high-quality,
well-understood contributions.

## Position

Hermeto takes a **permissive approach** toward AI-assisted contributions. We
recognize AI tools as legitimate development aids that can improve productivity
and code quality when used responsibly.

This position is consistent with the [Linux Foundation's Generative AI
Policy](https://www.linuxfoundation.org/legal/generative-ai), which states that
code generated in whole or in part using AI tools can be contributed to open
source projects, **provided that licensing and intellectual property
considerations are properly addressed**.

## Contributor accountability

Regardless of AI involvement, **the contributor is fully responsible for every
aspect of their submission**. This includes correctness, security, adherence to
project standards, and licensing compliance.

Hermeto is a security-sensitive and security-oriented project: it prefetches
dependencies, validates checksums, and produces SBOMs that downstream consumers
rely on. AI-generated code that is submitted without thorough human review and
understanding poses a direct risk to its mission.

### What we expect

- **Understand your code.** You must be able to explain every line of your
    submission, defend design decisions during review, and respond to reviewer
    feedback with substance.

- **Review AI output critically.** AI tools can produce code that is
    syntactically correct, but semantically or logically flawed. Treat all AI
    output as untrusted input that requires careful validation.

- **Follow project standards.** AI-assisted contributions must meet the same
    coding standards, test coverage, and review quality as any other
    contribution. See [CONTRIBUTING.md](CONTRIBUTING.md).

### What we will reject

- **"Vibecoded" contributions.** Submissions that are purely AI-generated with
    minimal or no human review, understanding, or refinement will be rejected.
    If a contribution appears to be an unreviewed dump of AI output,
    maintainers may reject it without detailed feedback.

- **Contributions the author cannot explain.** If during code review a
    contributor is unable to demonstrate understanding of how their submission
    works, or cannot meaningfully address reviewer feedback, the contribution
    may be rejected regardless of code quality.

- **Autonomous AI agent submissions.** Pull requests should NOT be opened by
    AI agents independently. A human must be the author and submitter of every
    contribution. Contributors are also expected to engage directly with
    maintainers during code review, i.e. relaying chatbot responses to
    reviewer's comments is not acceptable.

## Disclosure requirements

Contributors **MUST** disclose AI tool usage when submitting code,
documentation, or other content to the project. Undisclosed AI usage discovered
during review may result in the contribution being rejected and a request to
re-submit with proper disclosure. Disclosure is done via [git commit
trailer](https://git-scm.com/docs/git-interpret-trailers) lines. Accepted
formats include:

```text
Assisted-by: Claude
Assisted-by: Claude Code (Claude Opus 4.6)
Co-authored-by: Claude
...
```

Note these trailers must appear in addition to the required
[`Signed-off-by`](https://developercertificate.org) trailer (DCO sign-off).

### What requires disclosure

- AI wrote significant code blocks included in the submission
- AI suggested algorithms, data structures, or architectural approaches that
  were adopted
- AI generated tests, documentation, or commit messages that were used as-is or
  with minor edits
- AI-suggested solutions that materially shaped the final implementation

### What does not require disclosure

- General Q&A or learning about a technology
- IDE autocomplete or line-level completions (e.g. basic Copilot suggestions)
- Using AI to explain existing code
- Asking AI to review human-written code
- Spell checking or minor syntax corrections
- Content that was substantially rewritten to the point where the original AI
  output is unrecognizable

## Licensing considerations

Hermeto is licensed under the [GNU General Public License v3.0](LICENSE).
**Contributors must ensure that:**

- **The terms of their AI tool do not impose restrictions on the generated
    output that conflict with the GPL-3.0 license**

- **AI-generated output does not contain copyrighted material from third parties
    that would violate the GPL-3.0 or the rights of the original authors**

- **They can legitimately provide a DCO sign-off for the contribution,
    certifying that they have the right to submit it under the project's
    license**

When in doubt about whether an AI tool's terms are compatible with GPL-3.0, err
on the side of caution and consult the tool's terms of service or reach out to
the maintainers.

## Review standards

Maintainers will evaluate all contributions — whether AI-assisted or not — on
the same criteria:

- Adherence to [coding standards](CONTRIBUTING.md#coding-standards) and
  [project guidelines](CONTRIBUTING.md#pull-request-guidelines)
- Test coverage and quality (see [test guidelines](CONTRIBUTING.md#test-guidelines))
- Security implications (especially for dependency handling and checksum
  validation)
- Long-term maintainability
- Clarity and correctness of the implementation

---

# Standalone AI policy file

# AI Contribution Policy

## Purpose

This policy establishes guidelines for contributions to Hermeto that involve the
use of AI tools, including but not limited to Large Language Models (LLMs), code
generation assistants, and similar technologies. It aims to balance openness to
modern development workflows with the project's need for high-quality,
well-understood contributions.

## Position

Hermeto takes a **permissive approach** toward AI-assisted contributions. We
recognize AI tools as legitimate development aids that can improve productivity
and code quality when used responsibly.

This position is consistent with the [Linux Foundation's Generative AI
Policy](https://www.linuxfoundation.org/legal/generative-ai), which states that
code generated in whole or in part using AI tools can be contributed to open
source projects, **provided that licensing and intellectual property
considerations are properly addressed**.

## Contributor accountability

Regardless of AI involvement, **the contributor is fully responsible for every
aspect of their submission**. This includes correctness, security, adherence to
project standards, and licensing compliance.

Hermeto is a security-sensitive and security-oriented project: it prefetches
dependencies, validates checksums, and produces SBOMs that downstream consumers
rely on. AI-generated code that is submitted without thorough human review and
understanding poses a direct risk to its mission.

### What we expect

- **Understand your code.** You must be able to explain every line of your
    submission, defend design decisions during review, and respond to reviewer
    feedback with substance.

- **Review AI output critically.** AI tools can produce code that is
    syntactically correct, but semantically or logically flawed. Treat all AI
    output as untrusted input that requires careful validation.

- **Follow project standards.** AI-assisted contributions must meet the same
    coding standards, test coverage, and review quality as any other
    contribution. See [CONTRIBUTING.md](CONTRIBUTING.md).

### What we will reject

- **"Vibecoded" contributions.** Submissions that are purely AI-generated with
    minimal or no human review, understanding, or refinement will be rejected.
    If a contribution appears to be an unreviewed dump of AI output,
    maintainers may reject it without detailed feedback.

- **Contributions the author cannot explain.** If during code review a
    contributor is unable to demonstrate understanding of how their submission
    works, or cannot meaningfully address reviewer feedback, the contribution
    may be rejected regardless of code quality.

- **Autonomous AI agent submissions.** Pull requests should NOT be opened by
    AI agents independently. A human must be the author and submitter of every
    contribution. Contributors are also expected to engage directly with
    maintainers during code review, i.e. relaying chatbot responses to
    reviewer's comments is not acceptable.

## Disclosure requirements

Contributors **MUST** disclose AI tool usage when submitting code,
documentation, or other content to the project. Undisclosed AI usage discovered
during review may result in the contribution being rejected and a request to
re-submit with proper disclosure. Disclosure is done via [git commit
trailer](https://git-scm.com/docs/git-interpret-trailers) lines. Accepted
formats include:

```text
Assisted-by: Claude
Assisted-by: Claude Code (Claude Opus 4.6)
Co-authored-by: Claude
...
```

Note these trailers must appear in addition to the required
[`Signed-off-by`](https://developercertificate.org) trailer (DCO sign-off).

### What requires disclosure

- AI wrote significant code blocks included in the submission
- AI suggested algorithms, data structures, or architectural approaches that
  were adopted
- AI generated tests, documentation, or commit messages that were used as-is or
  with minor edits
- AI-suggested solutions that materially shaped the final implementation

### What does not require disclosure

- General Q&A or learning about a technology
- IDE autocomplete or line-level completions (e.g. basic Copilot suggestions)
- Using AI to explain existing code
- Asking AI to review human-written code
- Spell checking or minor syntax corrections
- Content that was substantially rewritten to the point where the original AI
  output is unrecognizable

## Licensing considerations

Hermeto is licensed under the [GNU General Public License v3.0](LICENSE).
**Contributors must ensure that:**

- **The terms of their AI tool do not impose restrictions on the generated
    output that conflict with the GPL-3.0 license**

- **AI-generated output does not contain copyrighted material from third parties
    that would violate the GPL-3.0 or the rights of the original authors**

- **They can legitimately provide a DCO sign-off for the contribution,
    certifying that they have the right to submit it under the project's
    license**

When in doubt about whether an AI tool's terms are compatible with GPL-3.0, err
on the side of caution and consult the tool's terms of service or reach out to
the maintainers.

## Review standards

Maintainers will evaluate all contributions — whether AI-assisted or not — on
the same criteria:

- Adherence to [coding standards](CONTRIBUTING.md#coding-standards) and
  [project guidelines](CONTRIBUTING.md#pull-request-guidelines)
- Test coverage and quality (see [test guidelines](CONTRIBUTING.md#test-guidelines))
- Security implications (especially for dependency handling and checksum
  validation)
- Long-term maintainability
- Clarity and correctness of the implementation
