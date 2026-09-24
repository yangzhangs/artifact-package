## Pull requests

- <mark>Include an AI disclosure</mark>
- Self-review (comment) on your code
- Break up big 1k+ line PRs into smaller PRs (100 loc)
- Include video of before/after with light/dark mode and mobile/desktop experiences represented.
- Include updates to any tests, especially end-to-end tests!
- Deploy the app to a preview URL and include QA steps

---

### PR description structure

Non-trivial PRs should follow this structure:

- **What** — What this PR does. Concrete changes, not a list of files.
- **Why** — Why this change exists and why this approach was chosen over alternatives.
- **Before/After** — Screenshots or video for UI/CSS changes only. Include desktop and mobile, light and dark mode.
- **Test Results** — Screenshot of tests passing locally.

<mark>End with an AI disclosure after a `---` separator. Name the specific model (e.g., "Claude Opus 4.6") and list the prompts given to the agent.</mark>

---

## AI models

<mark>Use the latest and greatest state-of-the-art models from American AI companies like [Anthropic](https://www.anthropic.com/) and [OpenAI](https://openai.com/). As of this writing, that means Claude Opus 4.6 and GPT-5.4, but always check for the newest releases. Don't settle for last-gen models when better ones are available.</mark>
