# How To Contribute

> [!IMPORTANT]
> - This document is mainly to help you to get started by codifying tribal knowledge and expectations and make it more accessible to everyone.
>   But don't be afraid to open half-finished PRs and ask questions if something is unclear!
>
> <mark>- If you use LLM / "AI" tools for your contributions, please read and follow our [_Generative AI / LLM Policy_][llm].</mark>

---

## Workflow

> [!WARNING]
> Before starting to work on **feature** pull requests, **please** discuss your idea with us on the [Ideas board](https://github.com/hynek/stamina/discussions/categories/ideas) to save you time and effort!

First off, thank you for considering to contribute!
It's people like *you* who make this project such a great tool for everyone.

- No contribution is too small!
  Please submit as many fixes for typos and grammar bloopers as you can!

- **Only contribute code that you fully understand.**
<mark>See also our [AI policy][llm].</mark>

- Very relatedly, our pull request check list is our mandatory [Van Halen test](https://en.wikipedia.org/wiki/Van_Halen_test).
  Sadly, the current state of the world has forced us into being stricter about policies -- sorry fellow humans!

- Try to limit each pull request to *one* change only (except for typos -- please group those).

- Since we squash on merge, it's up to you how you handle updates to the `main` branch.
  Whether you prefer to rebase on `main` or merge `main` into your branch, do whatever is more comfortable for you.

  Just remember to [not use your own `main` branch for the pull request](https://hynek.me/articles/pull-requests-branch/).

- *Always* add tests and docs for your code.
  This is a hard rule; patches with missing tests or documentation won't be merged.

- Consider updating [`CHANGELOG.md`](../CHANGELOG.md) to reflect the changes as observed by people *using* this library.

- Make sure your changes pass our [CI](https://github.com/hynek/stamina/actions).
  You won't get any feedback until it's green unless you ask for it.

  For the CI to pass, the coverage must be 100%.
  If you have problems to test something, open anyway and ask for advice.
  In some situations, we may agree to add an `# pragma: no cover`.

- Once you've addressed review feedback, make sure to bump the pull request with a short note, so we know you're done.

- Don't break [backwards-compatibility](SECURITY.md).

---

## See you on GitHub!

Again, this whole file is mainly to help you to get started by codifying tribal knowledge and expectations to save you time and turnarounds.
It is **not** meant to be a barrier to entry, so don't be afraid to open half-finished PRs and ask questions if something is unclear!

Please note that this project is released with a Contributor [Code of Conduct](CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.
Please report any harm to [Hynek Schlawack](https://hynek.me/about/) in any way you find appropriate.


[semantic newlines]: https://rhodesmill.org/brandon/2012/one-sentence-per-line/
<mark>[llm]: AI_POLICY.md</mark>

---

# Standalone AI policy file

# <mark>Generative AI / LLM Policy</mark>

<mark>We appreciate that we can't realistically police how you author your pull requests, which includes whether you employ large-language model (LLM)-based development tools.</mark>
So, we don't.

However, due to both legal and human reasons, we have to establish boundaries.

> [!CAUTION]
> **TL;DR:**
> - We take the responsibility for this project very seriously and we expect you to take your responsibility for your contributions seriously, too.
>   This used to be a given, but it changed now that a pull request is just one prompt away.
>
> - Every contribution has to be backed by a human who unequivocally owns the copyright for all changes.
> <mark>  No LLM bots in `Co-authored-by:`s.</mark>
>
> <mark>- DoS-by-slop leads to a permanent ban.</mark>
>
> - Absolutely **no** unsupervised agentic tools like OpenClaw.
>
> ---
>
> By submitting a pull request, you certify that:
>
> - You are the author of the contribution or have the legal right to submit it.
> - You either hold the copyright to the changes or have explicit legal authorization to contribute them under this project's license.
> - You understand the code.
> - You accept full responsibility for it.


## Legal

<mark>There is ongoing legal uncertainty regarding the copyright status of LLM-generated works and their provenance.</mark>
Since we do not have a formal [Contributor License Agreement](https://en.wikipedia.org/wiki/Contributor_license_agreement) (CLA), you retain your copyright to your changes to this project.

<mark>Therefore, allowing contributions by LLMs has unpredictable consequences for the copyright status of this project – even when leaving aside possible copyright violations due to plagiarism.</mark>


## Human

As the makers of software that is used by millions of people worldwide and with a reputation for high-quality maintenance, we take our responsibility to our users very seriously.
<mark>No matter what LLM vendors or boosters on LinkedIn tell you, we have to manually review every change before merging, because it's **our responsibility** to keep the project stable.</mark>

Please understand that by opening low-quality pull requests you're not helping anyone.
<mark>Worse, you're [poisoning the open source ecosystem](https://lwn.net/Articles/1058266/) that was precarious even before the arrival of LLM tools.</mark>
Having to wade through plausible-looking-but-low-quality pull requests and trying to determine which ones are legit is extremely demoralizing and has already burned out many good maintainers.

<mark>Put bluntly, we have no time or interest to become part of your vibe coding loop where you drop LLM slop at our door, we spend time and energy to review it, and you just feed it back into the LLM for another iteration.</mark>

This dynamic is especially pernicious because it poisons the well for mentoring new contributors which we are committed to.


## Summary

In practice, this means:

- <mark>Pull requests that have an LLM product listed as co-author can't be merged and will be closed without further discussion.</mark>
  We cannot risk the copyright status of this project.

<mark>If you used LLM tools during development, you may still submit – but you must remove any LLM co-author tags and take full ownership of every line.</mark>

- By submitting a pull request, **you** take full **technical and legal** responsibility for the contents of the pull request and promise that **you** hold the copyright for the changes submitted.

<mark>"An LLM wrote it" is **not** an acceptable response to questions or critique.</mark>
  **If you cannot explain and defend the changes you submit, do not submit them** and open a high-quality bug report/feature request instead.

- Accounts that exercise bot-like behavior – like automated mass pull requests – will be permanently banned, whether they belong to a human or not.

- <mark>Do **not** post LLM-generated review comments – we can prompt LLMs ourselves should we desire their wisdom.</mark>
  Do **not** post summaries unless you've fact-checked them and take responsibility for 100% of their content.
<mark>Remember that *all* LLM output *looks* **plausible**.</mark>
  When using these tools, it's **your** responsibility to ensure that it's also **correct** and has a reasonable signal-to-noise ratio.
