# Contributing
1. See [pull_request_template.md](/.github/pull_request_template.md) for pull request (PR) requirements.
2. See [BUILD.md](/src/docs/BUILD.md) for instructions on how to build `OpenVINO™ GenAI`.
3. Code style is determined by the file the change is made in. If ambiguous, look into the neighboring files of the same type. In case of contradiction, pick any of the options but stay consistent in your choice.
4. Don't push branches directly to the upstream repository. Once a branch is pushed to upstream, non-admins lose push access to it, preventing you from updating your changes. Instead, push to your fork and open PRs from there.
5. Your PR will be tested after one of the developers approves the tests run.
6. Branching policy is aligned with [OpenVINO's policy](https://github.com/openvinotoolkit/openvino/blob/71ee9cc42ec63b3affb2801dbbc4a77e6d8003f6/CONTRIBUTING_PR.md#branching-policy).
7. <mark>Contributions with use of AI must comply with [OpenVINO's AI Usage Policy](https://github.com/openvinotoolkit/openvino/blob/c4f4325c57977c684184e758449d1f8825ebbfd7/AI_USAGE_POLICY.md).</mark>

---

# New feature contribution
In order to get accepted PR with new features, the following list of items MUST be completed. Otherwise, PR will be rejected.
1. Proof of Concept (PoC) pipeline including model preparation step using `optimum-intel` and `GenAI` inference implementation.
2. Pass architectural review with
    1. API proposal for `optimum-intel` and `GenAI`
    2. Working PoC
    3. Command line arguments for model conversion with `optimum-cli export openvino`
    4. `GenAI` sample

---

# Standalone AI policy file

# <mark>AI Usage Policy</mark>

## Purpose

<mark>OpenVINO welcomes responsible use of AI tools in open-source collaboration.</mark>
This policy exists to protect maintainer time, keep review quality high, and
ensure long-term maintainability of the project.

The key principle is simple: **contributions are evaluated by quality,
accountability, and maintainability, not by tool choice alone**.

## Scope

This policy applies to:

- Pull requests and code changes
- Issues and discussions
- Review communication on GitHub

## <mark>Allowed AI Assistance</mark>

<mark>You may use AI tools to assist your work, including but not limited to:</mark>

- Brainstorming and research
- Explaining APIs, language features, and error messages
- Drafting small self-contained snippets
- Refactoring suggestions
- Test ideas and documentation editing

<mark>All AI-assisted output must still meet OpenVINO contribution standards.</mark>

## Contributor Responsibilities

<mark>If you use AI in any meaningful way, you must:</mark>

1. **Understand your submission end-to-end** and be ready to explain design and
   implementation decisions.
2. **Verify correctness yourself** (build, tests, behavior, and edge cases).
3. **Take full responsibility for every line submitted**, regardless of how it
   was drafted.
4. <mark>**Disclose significant AI assistance** in the PR description.</mark>

Suggested disclosure format:

```text
AI assistance used: <no | yes>
If yes: <how AI was used>
Human validation performed: <build/tests/manual checks>
```

## Not Acceptable

The following are not acceptable and may lead to immediate closure of the
contribution:

- Submitting code you cannot explain or maintain
- <mark>Large, low-context, or low-quality AI-generated changes without thorough</mark>
  human validation
- <mark>Using AI-generated responses in place of direct, human-to-human communication</mark>
  during review
- Auto-generated issues/discussions that do not describe reproducible,
  first-hand observations
- Fabricated citations, benchmarks, bug reports, or security claims

## Review and Enforcement

Maintainers may:

- Ask for a clear explanation of any part of a contribution
- Request changes, reduction of scope, or additional tests
- Deprioritize or decline review when quality or ownership is unclear
- Close contributions that do not follow this policy or project guidelines

<mark>This policy is not based on AI detection. Enforcement is based on observed</mark>
contribution quality, reviewer confidence, and adherence to project rules.

## Practical Guidance for New Contributors

- Start with small, focused PRs
- Link each PR to a concrete issue when possible
- Avoid broad multi-component changes in a first contribution
- Prefer clear commit history and explicit rationale in PR descriptions

## Relationship to Other Project Policies

This document supplements, and does not replace:

- [Contributing Guidelines](./CONTRIBUTING.md)
- [PR Guidelines](./CONTRIBUTING_PR.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)

In case of conflict, maintainers' review decisions and repository governance
policies take precedence.
