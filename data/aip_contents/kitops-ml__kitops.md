# Contributing Guide

* [Ways to Contribute](#ways-to-contribute)
* [Development Environment Setup](#development-environment-setup)
* [Pull Request Lifecycle](#pull-request-lifecycle)
* <mark>[AI-Assisted Contributions](#ai-assisted-contributions)</mark>
* [Sign Your Commits](#sign-your-commits)
* [Ask for Help](#ask-for-help)

Welcome! We are so excited that you want to contribute to our project! 💖

As you get started, you are in the best position to give us feedback on areas of our project that we need help with including:

* Problems found during setting up a new developer environment
* Gaps in our guides or documentation
* Bugs in our tools and automation scripts

If anything doesn't make sense, or doesn't work when you try it, please open a bug report and let us know!

---

## Ways to Contribute

We welcome many different types of contributions including:

* [New features](https://github.com/kitops-ml/kitops/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
* [Bug fixes](https://github.com/kitops-ml/kitops/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
* [Documentation](https://github.com/kitops-ml/kitops/issues?q=is%3Aopen+is%3Aissue+label%3Adocumentation)
* [Builds and CI/CD](https://github.com/kitops-ml/kitops/issues?q=is%3Aopen+is%3Aissue+label%3Abuild)
* Release management
* Issue triage
* Answering questions on Discord, or the mailing list
* Web design
* Communications, social media, blog posts, or other marketing

If you think there's something else you can help with please contact us in the [#general channel of our Discord server](https://discord.gg/Tapeh8agYy) or during our [office hours meeting](https://github.com/kitops-ml/kitops/blob/main/GOVERNANCE.md#-meetings) and let's discuss how we can work together.

---

## Development Environment Setup

---

### Prerequisites

* Go (Golang): The latest version of Go, as the project is written in this language. Go's installation guide can be found at https://golang.org/doc/install.
* Git: Version control system for cloning the repository and managing code changes. Installation instructions are available at https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

---

### Setting up the project

1. Clone the Repository: Clone the KitOps source code to your local machine:

    ```shell
    git clone https://github.com/kitops-ml/kitops.git
    cd kitops
    ```

1. Install Go Dependencies: Inside the project directory, fetch and install the project's dependencies using the Go command:

    ```shell
    go mod tidy
    ```

1. Generate the dev mode harness and ui

    ```shell
    go generate ./...
    ```

1. Build the Kit CLI: Compile the source code into an executable named kit:

    ```shell
    go build -o kit
    ```

1. Run Your Build: Execute the built CLI to see all available commands:

    ```shell
    go run .
    ```

1. Updating Dependencies: If you add or update dependencies, ensure to update the go.mod and go.sum files by running `go mod tidy` again and include these changes in your commits.

---

## Pull Request Lifecycle

Pull requests are often called a "PR". KitOps generally follows the standard [GitHub pull request process](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

---

## <mark>AI-Assisted Contributions</mark>

<mark>We welcome the use of AI coding assistants (GitHub Copilot, Claude, ChatGPT, etc.) to help write code, documentation, and tests. However, you are fully responsible for reviewing and understanding all AI-generated code before submitting it.</mark>

---

### <mark>Requirements for AI-Assisted PRs</mark>

* <mark>**Review everything**: Read every line of AI-generated code. Understand what it does and why.</mark>
* **Test thoroughly**: AI can generate plausible-looking code that doesn't work or has subtle bugs. Run tests and verify behavior.
* **Remove AI artifacts**: Delete verbose comments, unnecessary explanations, or boilerplate that AI tends to add.
* **Check for hallucinations**: AI models can invent APIs, packages, or patterns that don't exist. Verify all imports and function calls.
* <mark>**Attest in your PR**: Use the AI-Assisted Code checklist in the PR template to acknowledge your review.</mark>

---

### What Reviewers Look For

<mark>Maintainers will be alert to common AI-generated code patterns:</mark>

* Overly defensive error handling or excessive nil checks
* Verbose or redundant comments explaining obvious operations
* Cargo-culted patterns that don't fit our codebase conventions
* Inconsistent style mixing modern and legacy approaches
* Test cases that pass but don't actually validate behavior

<mark>If a PR shows signs of unreviewed AI output, we'll reject it with feedback. This isn't punitive. It's about maintaining code quality and helping you learn to use AI tools effectively.</mark>
