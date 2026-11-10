## <mark>Use of AI Tools</mark>

<mark>We welcome contributions regardless of how they are written — including with the help of AI coding assistants. That said, AI-generated code requires the same level of scrutiny as any other code, and in practice it often requires *more*.</mark>

Even capable AI models frequently produce subtle mistakes: incorrect assumptions about library conventions, unnecessary abstractions, hallucinated APIs, or code that compiles but doesn't align with the project's design. These issues are not always obvious at first glance, but they add up quickly during review.

<mark>**What we expect from AI-assisted contributions:**</mark>

- <mark>**You are responsible for the code you submit.** Treat AI output as a first draft, not a finished product. Review it thoroughly, understand every line, and verify that it follows the conventions of this library.</mark>
- **Run the full CI pipeline locally before opening a PR.** At a minimum, ensure that `cargo test`, `cargo clippy`, and `cargo fmt` all pass. The [workflow section above](#a-typical-workflow) has the exact commands.
- <mark>**Match the library's patterns and style.** Spend time reading existing modules to understand how things are structured here. AI tools lack this context and will often produce code that works in isolation but feels foreign to the codebase.</mark>

**What happens with low-effort, unreviewed submissions:**

Our team has limited time and a tight development schedule. When a PR is clearly unreviewed AI output — full of basic mistakes, inconsistent style, or misaligned design — we cannot justify the time it takes to review it. In such cases:

- The PR will be closed without a detailed review.
- Repeated low-effort submissions from the same contributor may result in future PRs not being considered.

<mark>This is not about discouraging AI usage — it's about respecting everyone's time. A good contribution, whether written by hand or with AI assistance, should feel like it has already been reviewed by someone who understands the library.</mark>

We genuinely want to encourage external contributions, and we are always happy to help you get your PR across the finish line. If something is unclear or you are unsure about a design choice, open an issue or ask in the PR — we'd much rather help early than close a PR late.
