## <mark>AI usage policy</mark>

---

### <mark>General AI tool policy</mark>

<mark>AI tools (e.g., LLMs, code assistants, and proofreaders) are permitted as</mark>
assistive supplements, not replacements for human judgment.

- **Code review:**
<mark>AI tools may act as a preliminary "peer reviewer" to catch syntax or style</mark>
<mark>issues, similar to a non-AI code analysis tool.</mark>
  However, a human must perform the final review, validate logic,
  and take full responsibility for all decisions.
- **Automation:**
  AI is acceptable for offloading repetitive, well-understood, and
  time-consuming boilerplate tasks.
- **Verification:**
<mark>All AI-generated suggestions must be manually verified for security,</mark>
  performance, and project alignment.

---

### Special policy for Google Summer of Code (GSoC)

GSoC is a mentorship and learning program.
Over-reliance on AI undermines the educational goals and the evaluation of the
contributor's growth.

- **Writing & proposals:**
  - Prohibited: Generating full proposals, final reports, PR descriptions,
    or substantial parts of those.
  - Permitted: Spell-checking, grammar correction, and feedback on structural
    coherence.
  - Requirement: PR descriptions must be written by the contributor to
    demonstrate a deep understanding of what was changed and why.
  - Note: Your English skills will not be graded; mentors care about your code
    and understanding.
- **Code generation:**
  - <mark>Prohibited: Using AI to write entire modules or significant logic blocks.</mark>
  - Rationale: The goal of GSoC is your development as a contributor within
    a community. Writing your own code and code comments is essential for
<mark>learning. Furthermore, LLMs often provide inaccurate results for SPDX 3.x,</mark>
    as the lack of public datasets for these new standards leads to frequent
    technical hallucinations.
- **Transparency:**
  - <mark>Contributors must disclose if AI was used significantly in any part of</mark>
    their workflow.
  - <mark>Unattributed AI-generated code may be considered a violation of integrity,</mark>
    which may result in a failing project evaluation.

All GSoC contributors must adhere to the official
<mark>[Guidance for GSoC Contributors using AI tooling in GSoC 2026][gsoc-ai-guidance].</mark>

[gsoc-ai-guidance]: https://developers.google.com/open-source/gsoc/resources/ai_guidance#1_always_validate_and_fully_understand_the_code
