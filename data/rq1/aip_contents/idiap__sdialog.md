## Guidelines

- Keep functions/classes small & composable
- Add/extend tests for new features or bug fixes
- Document public APIs (docstrings + docs reference where appropriate)
- Prefer pure functions where state is not needed
- Avoid introducing heavy deps without discussion (open issue first)
- <mark>Use meaningful names; avoid abbreviations except standard ones (LLM, NLP, etc.)</mark>

---

## <mark>AI-assisted development</mark>
<mark>This project provides an [llm.txt file](https://sdialog.readthedocs.io/en/latest/llm.txt) following the [llms.txt specification](https://llmstxt.org/) for AI coding assistants. GitHub Copilot and other AI tools can fetch structured project information with: `#fetch https://sdialog.readthedocs.io/en/latest/llm.txt`</mark>
