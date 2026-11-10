## <mark>On AI-Assisted Code</mark>

<mark>We're fine with AI tools. Copilot, Claude, Cursor, whatever helps you work. But there are expectations.</mark>

<mark>**You own what you submit.** If you can't explain the code or debug it when something breaks, that's a problem. We've had PRs where contributors couldn't answer basic questions about their own submissions because they didn't actually understand what the AI generated. That's not a contribution, it's a maintenance burden.</mark>

<mark>**Disclose significant AI usage in your PR.** Not every autocomplete suggestion, but if AI wrote substantial portions of your code, say so. This helps reviewers know where to look carefully. The PR template has a checkbox for this.</mark>

**Tests matter more than ever.** If you understood the code well enough to write it, you can write tests for it. PRs that add features without tests often indicate the contributor doesn't fully grasp what they've built.

<mark>To be clear: we're not trying to gatekeep or ban AI. These tools are useful. But a 5,000-line PR with no tests and a contributor who can't explain the implementation creates real problems for maintainers.</mark>
