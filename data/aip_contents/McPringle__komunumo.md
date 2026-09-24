# Contributing

**In this document you will find a lot of information on how you can contribute to *Komunumo*.**

- [How to contribute](#how-to-contribute)
    - [Project Board](#project-board)
    - [Good first issues](#good-first-issues)
    - [Commit Messages](#commit-messages)
    - [Sign-off your commits](#sign-off-your-commits)
    - [AI generated code](#ai-generated-code)
    - [Testing](#testing)
    - [Pull Request Scope](#pull-request-scope)
- [Quickstart for Local Development](#quickstart-for-local-development)
    - [Prerequisites](#prerequisites)
    - [Clone and Verify](#clone-and-verify)
    - [Start Required Services](#start-required-services)
    - [Configure Environment Variables](#configure-environment-variables)
    - [Run Komunumo](#run-komunumo)
    - [Open in Browser](#open-in-browser)
    - [Stop Komunumo](#stop-komunumo)
- [Communication](#communication)
    - [Matrix Chat](#matrix-chat)
    - [GitHub Discussions](#github-discussions)
- [Architecture](#architecture)
    - [Structure](#structure)
    - [Boundary Control Entity Architecture](#boundary-control-entity-architecture)
    - [Useful Vaadin Links](#useful-vaadin-links)
- [Internationalization](#internationalization)
    - [Translation Files](#translation-files)
    - [Message Format](#message-format)
- [Database](#database)
    - [General Principles](#general-principles)
    - [Index Names](#index-names)
    - [Starting a Local MariaDB Instance](#starting-a-local-mariadb-instance)
- [Build](#build)
    - [Maven](#maven)
- [Running and debugging](#running-and-debugging)
    - [Running the server from the command line.](#running-the-server-from-the-command-line)
    - [Running and debugging the server in Intellij IDEA](#running-and-debugging-the-server-in-intellij-idea)
    - [Running and debugging the server in Eclipse](#running-and-debugging-the-server-in-eclipse)
- [Running using Docker](#running-using-docker)

---

## How to contribute

---

### Project Board

To get an overview of ongoing and upcoming work, you can check our [project board](https://github.com/orgs/komunumo/projects/1), which organizes issues in a Kanban-style workflow:

| Status      | Description                                                   |
|-------------|---------------------------------------------------------------|
| Backlog     | Ideas and requests that are not yet analyzed.                 |
| In Analysis | Issues currently under discussion or refinement.              |
| Ready       | Issues that are fully specified and ready to be implemented.  |
| In Progress | Issues actively being worked on.                              |
| Done        | Recently completed issues; older ones are archived over time. |

> [!TIP]
> If you’re looking for something to work on, focus on issues in the **Ready** column. These contain all necessary information to start contributing right away.

---

### Good first issues

To find possible tasks for your first contribution to *Komunumo*, we tagged some of the hopefully easier to solve issues as [good first issue](https://github.com/komunumo/komunumo/labels/good%20first%20issue).

If you prefer to meet people in real life to contribute to *Komunumo* together, we recommend to visit a [Hackergarten](https://www.hackergarten.net/) event. *Komunumo* is often selected as a contribution target in [Lucerne](https://www.meetup.com/hackergarten-luzern/), [Zurich](https://www.meetup.com/hackergarten-zurich/), and at the [CyberLand Open Source Camp](https://cyberland.ijug.eu/).

Please join our developer community using our [Matrix chat](#matrix-chat) to get support and help for contributing to *Komunumo*.

---

### Commit Messages

Please follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for all commit messages and pull request titles. This structured format helps automate changelogs, release processes, and code reviews.

For *Komunumo*, we love to add the issue number to the end of the commit message. This helps to track the changes in the code and the issue tracker. When the commit closes an issue, the `closes`, `fixes`, or `resolves` keyword can be used. This will automatically close the issue when the commit is merged into the main branch.

A commit message consists of the following parts:

```
<type>[optional scope]: <short description> [optional keyword] #<issue number>

[optional body]

[optional footer]
```

---

#### Examples

- `feat: add support for passkey authentication closes #123`
- `fix(event): correct date formatting in export fixes #456`
- `chore: add missing license headers to source files resolves #789`

---

#### Common `type` values:

| Type       | Purpose                                                               |
|------------|-----------------------------------------------------------------------|
| `feat`     | Introduce a new feature                                               |
| `fix`      | Fix a bug                                                             |
| `docs`     | Documentation-only changes                                            |
| `style`    | Code style changes (formatting, whitespace, missing semicolons, etc.) |
| `refactor` | Code refactoring without functional change                            |
| `perf`     | Improve performance without changing features or behavior             |
| `test`     | Add or update tests                                                   |
| `build`    | Changes to the build system, packaging or dependencies (e.g. Maven)   |
| `ci`       | Changes to CI/CD configuration (e.g. GitHub Actions, Woodpecker)      |
| `chore`    | Maintenance tasks (configs, license, release meta, etc.)              |
| `revert`   | Revert a previous commit                                              |
| `deps`     | Add, update, or remove dependencies                                   |
| `security` | Address security issues or vulnerabilities                            |

> [!TIP]
> For more information, see [conventionalcommits.org](https://www.conventionalcommits.org/)

---

### Sign-off your commits

It is important to sign-off *every* commit. That is a de facto standard way to ensure that *you* have the right to submit your content and that you agree to the [DCO](DCO.md) (Developer Certificate of Origin).

You can find more information about why this is important and how to do it easily in a very good [blog post](https://dev.to/janderssonse/git-signoff-and-signing-like-a-champ-41f3)  by Josef Andersson.

---

### AI generated code

AI generated source code is based on real existing source code, which is copied in whole or in part into the generated code. The license of the original source code with which the AI was trained is not taken into account. It is not clear which license conditions apply and how these can be complied with. For legal reasons, we therefore do not allow AI-generated source code at all.
