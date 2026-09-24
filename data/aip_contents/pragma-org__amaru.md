### Living CHANGELOG

Any PRs that add, remove, modify or fix any *user-facing behaviour* must include a [CHANGELOG](./CHANGELOG.md) entry — short and factual. Automated/LLM-generated suggestions are welcome, but humans must verify wording.

A user-facing behaviour is anything that a user of Amaru (as an executable or as a collection of libraries) may seemingly notice. This includes (but isn't limited to):

- command-line commands, options and arguments
- default behaviours and default configurations
- any exposed protocol API
- supported compilation targets
- exposed logs, traces and metrics
- `pub` modules or functions
- databases formats
- performances

> [!TIP]
> We follow specific guidelines to [keep a changelog](https://keepachangelog.com/en/1.0.0/):
>
> #### Guiding principles
>
> - Changelogs are for humans, not machines.
> - There should be an entry for every single version.
> - The same types of changes should be grouped.
> - Versions and sections should be linkable.
> - The latest version comes first.
> - The release date of each version is displayed.
>
> #### Types of changes
>
> - `Added` for new features.
> - `Changed` for changes in existing functionality.
> - `Deprecated` for soon-to-be removed features.
> - `Removed` for now removed features.
> - `Fixed` for any bug fixes.
> - `Security` in case of vulnerabilities.

---

#### Use of AI

We recognize the existence and importance of (generative) AI as part of our workflow for it has proven to be a useful **tool**.

We use it for reviews, for domain exploration, as search engine or for generating code when we see fit.

Our rule of thumb is: do not generate or publish anything you wouldn't feel confident writing yourself.

Importantly, AI cannot substitute itself for human validation and any use of _unsupervised AI_ is prohibited.
