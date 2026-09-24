## AI Code Assistant Usage

If you use AI code assistants, please follow these guidelines:

| Guideline | Details |
|-----------|---------|
| **Human verification** | Always review, test, and understand AI-generated code before submitting |
| **When to attribute** | Note substantial AI assistance in commit messages AND PR description using `Assisted-by:` |
| **Security** | Never input sensitive data (API keys, credentials, customer data) into AI tools |
| **Code quality** | AI-generated code must meet the same standards (tests, coverage, linting) |
| **License compliance** | Ensure AI suggestions don't introduce incompatible licenses |

**Create attribution statements:** Use <https://aiattribution.github.io/> to generate detailed AI attribution.

**Example commit message:**

```text
Add retry logic for API calls

Implements exponential backoff for transient failures.

Assisted-by: GitHub Copilot
```

**Example PR description:**

```text
Implemented retry logic for API calls

Assisted-by: GitHub Copilot
```
