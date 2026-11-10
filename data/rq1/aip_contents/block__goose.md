# Contribution Guide

goose is open source!

<mark>We welcome pull requests for general contributions! In these days of AI it is easier than ever to contribute, but</mark>
there are some pitfalls to avoid. This document describes the best practices for new and experienced contributors
to get work landed as smoothly as possible.

> [!TIP]
> Beyond code, check out [other ways to contribute](#other-ways-to-contribute)

---

---

## Getting Started

Your first contribution to goose should probably be a small bug fix. The goose maintainers have a lot of incoming
PRs to review, and the reputation of the author is an important signal. While contributions to goose are generally
<mark>of remarkably high quality, we do get our fair share of AI slop. When a first-time contributor opens a</mark>
3k line PR touching 20 files, we have no easy way to tell whether it’s thoughtful work or
<mark>blindly AI-generated without doing a deep dive.</mark>

So please start small to establish trust and work your way up from there. A small bug fix or performance improvement
is a good start. Linking your fix to an existing issue shows that you are responding to a community need.

If your first PR gets closed with a link to this section, please don’t take it personally. 
It just means the change was too large for a first contribution. Start with something smaller and try again.

---

### Issues

If you spot a bug or have a concrete proposal for a feature, please open an issue. This shows the community and
the maintainers the direction of your thinking.

For bugs, describe how to reproduce the problem as clearly as possible. If the issue involves an interaction
<mark>with an LLM, include a diagnostics report if possible.</mark>

---

## <mark>AI Code Reviews</mark>

<mark>We use codex as an AI code reviewer. AI code reviewing has come a long way and more often than not points</mark>
out real issues. So we expect you to address all of them by either fixing the code or adding a one-line
answer as to why this is not an issue or not worth fixing.

If not, we might close the PR and/or reply with a link to this section. Once you address the comments, you
can always reopen.

---

## <mark>Quick Responsible AI Tips</mark>

There's no need to tell us you used AI in your work. You are contributing to an agent, it would be odd if 
<mark>you had not. Our general thinking is, use AI any way you want, but until the robot revolution comes, you</mark>
are responsible for the final code. Before submitting a PR for review, make sure you have reviewed it yourself.
<mark>We'll close any vibe coded submissions that obviously skip this step.</mark>

You can use whatever agent and whatever methodology you like as long as you stick to that principle. We hope
<mark>you like goose of course and use that. One thing to watch out for is LLM eagerness. They like to please and</mark>
are in a hurry. 

   * **Think first**. Agents tend to jump straight to code writing. Explain the architecture you want first to 
      avoid this behavior, based on your own understanding of the code, or have the agent explore the code first and
      suggest approaches. If the first implementation doesn't look quite right, just start over and use
      what you learned to do better next time.
   * <mark>**Spot the laziness**. LLMs will make their job easy. They'll write trivial tests, make types wide and</mark>
      optional so the compiler doesn't complain, catch exceptions and just log instead of handling errors
      and copy local patterns whether appropriate or not. Push back!
   * **Spot the uncertainty**. As much as the bots declare I see the issue now clearly, they often do not. Call
      them on it, if you see the agent flailing. Another telltale sign is if the agent starts listing the
      number of ways it fixed an issue or starts writing overly defensive code.
   * **Spot the bloat**. Agents like to insert redundant comments or worse, commenting on the change at hand,
     not the resulting code. They create loads of tests that don't really test anything and if they do,
     test the implementation, not the intention. They also like to log anything, just in case.

---

### Rust

First let's compile goose and try it out
Since goose requires Hermit for managing dependencies, let's activate hermit.

```
cd goose
source ./bin/activate-hermit
cargo build
```

When that completes, debug builds of the binaries are available, including the goose CLI:

```
./target/debug/goose --help
```

For first-time setup, run the configure command:

```
./target/debug/goose configure
```

<mark>Once a connection to an LLM provider is working, start a session:</mark>

```
./target/debug/goose session
```

These same commands can be recompiled and immediately run using `cargo run -p goose-cli` for iteration.
When making changes to the Rust code, test them on the CLI or run checks, tests, and the linter:

```
cargo check  # verify changes compile
cargo test  # run tests with changes
cargo fmt   # format code
cargo clippy --all-targets -- -D warnings # run the linter
```
