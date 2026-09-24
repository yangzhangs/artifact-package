## Table of Contents

- [Where to Find Code](#where-to-find-code)
- [How to Run Tests and Other Checks](#how-to-run-tests-and-other-checks)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Branch Naming Guidelines](#branch-naming-guidelines)
- [Editor Configuration](#editor-configuration)
- [Automation](#bots-and-automation)
- <mark>[AI Policy](#ai-policy)</mark>
- [Community](#community)

---

### <mark>AI-Assisted Editors</mark>

<mark>For AI-assisted editors like Claude Code, Codex, Cursor or GitHub Copilot, refer to the [`AGENTS.md`](./AGENTS.md) file for comprehensive guidance on working with this codebase.</mark>

---

## <mark>AI Policy</mark>

<mark>As a contributor you're encouraged to use AI tools in your workflow just as you would use classic tools such as search engines, language servers, linters, debuggers, documentation, or books. These tools are an invaluable resource and can help you write better code and explore ideas more efficiently.</mark>

<mark>That said, AI tools are different than classic tools because they can blur the line between helping you to do the work and doing the work for you. And when that line becomes blurry, it can limit opportunities to build the deep understanding that comes from writing and reasoning through code yourself.</mark>

As an open source project, Kubetail is not only commited to building the most user-friendly logging platform for Kubernetes but also to helping our contributors grow as engineers. We invest a lot of time and effort into code quality, thoughtful reviews, and well-defined engineering specs. We do so happily because we enjoy it but also because it's our responsibility to the community.

<mark>In return, we ask that contributions be authored by you. While AI tools can support your workflow, submitted code should reflect your own understanding and intent. To keep our focus on meaningful collaboration within the community, we do not accept contributions authored entirely by llms.</mark>

<mark>When you use an AI tool, include an Assisted-by tag in the following format:</mark>

```
Assisted-by: AGENT_NAME:MODEL_VERSION
```

Where:

<mark>`AGENT_NAME` is the name of the AI tool or framework</mark>
    `MODEL_VERSION` is the specific model version used

Example:

```
git commit -a -s --trailer "Assisted-by: Claude:claude-opus-4.6" -m "<message>"
```
