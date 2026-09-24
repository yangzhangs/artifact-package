## AI usage policy

---

### General AI tool policy

AI tools (e.g., LLMs, code assistants, and proofreaders) are permitted as
assistive supplements, not replacements for human judgment.

- **Code review:**
  AI tools may act as a preliminary "peer reviewer" to catch syntax or style
  issues, similar to a non-AI code analysis tool.
  However, a human must perform the final review, validate logic,
  and take full responsibility for all decisions.
- **Automation:**
  AI is acceptable for offloading repetitive, well-understood, and
  time-consuming boilerplate tasks.
- **Verification:**
  All AI-generated suggestions must be manually verified for security,
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
  - Prohibited: Using AI to write entire modules or significant logic blocks.
  - Rationale: The goal of GSoC is your development as a contributor within
    a community. Writing your own code and code comments is essential for
    learning. Furthermore, LLMs often provide inaccurate results for SPDX 3.x,
    as the lack of public datasets for these new standards leads to frequent
    technical hallucinations.
- **Transparency:**
  - Contributors must disclose if AI was used significantly in any part of
    their workflow.
  - Unattributed AI-generated code may be considered a violation of integrity,
    which may result in a failing project evaluation.

All GSoC contributors must adhere to the official
[Guidance for GSoC Contributors using AI tooling in GSoC 2026][gsoc-ai-guidance].

[gsoc-ai-guidance]: https://developers.google.com/open-source/gsoc/resources/ai_guidance#1_always_validate_and_fully_understand_the_code
