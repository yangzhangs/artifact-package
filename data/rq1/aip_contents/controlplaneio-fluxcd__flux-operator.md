## <mark>AI Contribution Policy</mark>

<mark>Using AI Agents to help write your PR is acceptable, but as the author, you are responsible</mark>
<mark>for understanding the code and the documentation you submit. Please review all the AI-generated</mark>
content and make sure it follows the guidelines in this document before submitting your PR.

The Flux Operator repository contain an `AGENTS.md` file. You must point your AI Agent to
`AGENTS.md` and ask it to follow the guidelines and conventions described there.

The `Signed-off-by` and `Co-authored-by` tags must identify the human who can
legally certify the [DCO](https://developercertificate.org/), please don’t fill these will AI product names.

<mark>You should disclose the use of AI Agents in the description of your PR and</mark>
in the commit message using the `Assisted-by: AGENT_NAME/LLM_VERSION` tag.

Adding the `Assisted-by` tag to the commit message can be done with:

```sh
git commit -s -m "Your commit message" --trailer "Assisted-by: <agent>/<model>"
```

**Note** that the `Signed-off-by` tag is set via the `-s` flag using your real name and email
(`user.name` and `user.email` must be set in Git config).
