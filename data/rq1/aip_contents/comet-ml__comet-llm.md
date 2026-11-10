## <mark>AI-assisted contributions</mark>
<mark>AI assistance is allowed, but human authors remain accountable for correctness, licensing, and security.</mark>

Rules:
- Always run relevant tests/linters for touched code.
- Always be explicit about human/users interaction with produced output.
- Always review prior issues, pull requests, and existing code for related solutions.
- Always address system-generated reviews (Baz, Greptile).
- Never submit unreviewed AI output.
- Never include secrets, tokens, private prompts, internal system instructions, or customer-sensitive data in generated/public content.
- Never disclose vulnerabilities, exploit steps, or incident details in public issues/PRs (use private maintainer/security channels).
- <mark>Include the PR template AI watermark/disclosure block when AI is used.</mark>

---

## Agent/editor setup
- <mark>Cursor compatibility: `make cursor` (`.cursor -> .agents`)</mark>
- Codex compatibility: `make codex` (`.codex -> .agents`, generates `AGENTS.override.md` from `.agents/rules/*.mdc`)
- <mark>Claude sync: `make claude` (syncs `.agents` to `.claude`)</mark>
- Git hooks: `make hooks`
