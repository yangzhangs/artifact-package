# Contributing to the FOCUS Working Group

> This repository represents the written spec, not working code.  As such, most people will not need any development environment; most of the work around the spec happens in regularly scheduled discussions and issues here in Github.

Thank you for your interest in contributing to the **FinOps Open Cost and Usage Specification (FOCUS)**.  
This repository contains the technical specification and supporting documentation for the FOCUS project under the **FinOps Foundation**.

Before contributing, please review the following guidelines carefully to ensure consistency and efficiency across all contributions.

---

## 1. Before You Start

1. **Join the FOCUS Project**
   * If you’re not already a participant, visit the [FOCUS Enrolment](https://enrollment.lfx.linuxfoundation.org/?project=finopsopenbillingspec) for instructions on how **your company** can join the FOCUS Open Standards Project. In addition, you must be approved by your company as a contributor to this project. You are required to complete the steps indicated in the [README of the EasyCLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA/blob/main/README.md) repository.
   * Only authorized contributors can submit or review Pull Requests.

2. **Get Familiar with the Project**
   * Review the [FOCUS Specification Overview](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/README.md#overview) and the latest release.
   * Join the **FOCUS Slack working-group** for discussions and meeting updates. _(you will be invited once you have completed the [README CLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA/blob/main/README.md) steps)_
   * Familiarize yourself with the [Roles & Tasks](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md#22-organization-roles) and [Review & Approval Process](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md#52-review--approval).

---

## 2. Types of Contributions

You can contribute to this repository in several ways:

* **Action Items** – Updates or follow-up tasks resulting from meetings.

* **Feature Requests** – Proposals for new functionality, attributes, or examples.

* **Feedback** – Comments or recommendations on existing content.

* **Maintenance** – Fixes or updates for typos, structure, or metadata.

* **Work Items** – Specific contributions tracked as GitHub issues.

If you are not sure where your contribution fits, open a **Blank Issue** first and request feedback before submitting a Pull Request (PR).

---

## 3. AI-Assisted Contributions

AI tools (such as GitHub Copilot, Claude Code, Cursor, and similar coding assistants) may be used to assist with FOCUS contributions. AI-generated content follows the same review standards as human-authored content.

**Key requirements:**

* A CLA-covered human MUST take responsibility for all contributions
* Approved AI agents MAY create PRs on behalf of a human who requested the work
* The responsible human reviews and approves AI-generated contributions
* AI-assisted contributions follow the same review process as other contributions, including peer review and consensus approval

For complete guidance, see [AI Usage Guidelines](guidelines/contributors/ai-usage-guidelines.md).

---

## 4. Contribution Process

1. **Fork this repository** and create a branch for your work:
```bash
git checkout -b feature/your-change-description
```

> For further details on how to work with Git and GitHub, refer to the [GitHub Guidelines](guidelines/contributors/github-guidelines.md).

2. **Reference existing issues** or create a new one to track your change. Include the issue number in your PR title or description (e.g., Fixes #845).

3. **Follow FOCUS content conventions:**

* Use BCP-14 keywords (**MUST**, **SHOULD**, **MAY**, etc.) correctly.  
* Do not remove normative content without prior discussion.

> See [Typographic Conventions](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/specification/overview.md#typographic-conventions), (e.g., “for how to use BCP-14 keywords”).

4. **Submit your PR**

* Include a clear summary of the change.  
* Use one PR per logical change.  
* Assign appropriate labels (e.g., `normative-change`, `editorial`, `discussion`).

> For details about labels and stages, see [Git Issues - Project - Content Creation](guidelines/contributors/development-processes.md#focus-development-process)

5. **Participate in the review**

* Your PR will go through the following review sequence:

    * **Maintainers / Task Force(s) → Members (for review and approval)**

    * Be responsive to reviewer comments and requested edits.

---

6. **Writing Style and Format**

* Use the provided Markdown Editorial Guidelines for all specification text.  
* Follow the structure of existing sections (Introduction → Requirements → Examples → Notes).  
* Use **RFC 2119** language for normative statements.

> Visit [Editorial Guidelines](guidelines/contributors/editorial-guidelines.md) for further information.


7. **Normative vs Supporting Content**

* **Normative content** defines required behavior using **MUST**, **SHALL**, or **SHOULD**.  
* **Supporting content** explains context or provides examples.  
* If your contribution changes a normative rule, it will require review by the **Task Force** and **Members** before approval.

---

8. **Review and Approval Flow**

| Stage | Responsible Group     | Description                                           |
|:------:|----------------------|-------------------------------------------------------|
| 1 | Maintainers | Broad alignment and quality assurance |
| 2 | Task Force | Technical review and discussion of proposed change |
| 3 | Members Working Group | Broad review and approval |

Status changes and approvals are tracked in GitHub **Issues** and **Pull Requests**.

---

9. **Resources and References**

* [FOCUS Specification Website](https://focus.finops.org/focus-specification/)  
* [FOCUS Governance Repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation)  
* [FOCUS Membership Enrollment](https://enrollment.lfx.linuxfoundation.org/?project=finopsopenbillingspec) _Company joining instructions_ 
* [FOCUS CLA Contribution](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA) _Contributors approved by own company_
* [FinOps Foundation](https://www.finops.org)  

10. **License and Intellectual Property**

All contributions are made under the terms of the **[FOCUS Member Agreement](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/FOCUS_-_Membership_Agreement_Package_for_use.pdf)**, as stated in the [LICENSE](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/license.md) file.  
By submitting a contribution, you agree that:

* Your work complies with the project’s **[IPR and CLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/FOCUS_-_Membership_Agreement_Package_for_use.pdf)** requirements.  
* You have the rights to submit the content.  
* Contributions become part of the open **FinOps FOCUS Specification**.

---

# Standalone AI policy file

# AI Usage Guidelines

## Overview

This document defines the FOCUS Working Group's policy for using AI tools in specification development. It aligns with the [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai) and applies to all contributions to this repository.

AI tools may be used to assist with FOCUS contributions. AI-generated content is permitted and follows the same intellectual property, licensing, and review standards as human-authored content.

The use of AI in specification development is still evolving, and this is therefore a living document that will shift as AI usage patterns mature.
## Usage Modes

AI tools (e.g., GitHub Copilot, Claude Code, Cursor, and similar coding assistants) are typically used in two modes:

* **Interactive**: A human contributor works with AI assistance in real-time. The human reviews, edits, and submits the contribution.
* **Autonomous**: A human requests AI to work independently. The AI creates a PR, comments, or suggestions and assigns them to the human for review. The PR serves as the human review checkpoint.

## Contribution Requirements

### Human Responsibility

* A human contributor covered by a [Contributor License Agreement](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA) (CLA) MUST take responsibility for all contributions.
* AI agents MAY create PRs on behalf of a human who requested the work.
* The CLA-covered human MUST be accountable for:
  * Reviewing AI-generated output for correctness and quality
  * Ensuring compliance with FOCUS normative requirements and editorial conventions
  * Verifying no third-party intellectual property conflicts exist
  * Confirming the AI tool's terms of service do not conflict with FOCUS licensing

### Review Process

AI-assisted contributions follow the same review process as human-authored contributions:

1. **Human Self-Review**: The CLA-covered contributor MUST thoroughly review and validate all AI-generated content before requesting peer review. When possible, the responsible human SHOULD provide an approving review as sign-off.
2. **Technical Validation**: The relevant Task Force MUST review the contribution for technical accuracy and schema compliance.
3. **Strategic Alignment**: WG Members MUST review the contribution to ensure it aligns with broader community goals and the FOCUS roadmap.
4. **Standard Approval**: All contributions MUST follow the established workflow per [Development Processes](development-processes.md).
5. **Acceptance of Suggestions**: If the author chooses to apply the suggestion via a separate commit through the use of an AI assistant, the author MUST manually record the commenter's co-authorship in the commit message using standard `Co-authored-by:` trailers.

AI-generated content does not bypass any approval workflow or receive different treatment during review.

### Generation of Specification Examples

AI tools frequently generate plausible but incorrect data, mathematical inconsistencies, and schema violations. Because examples serve as the ground truth for specification implementation, they require the highest level of scrutiny.

To minimize the burden on reviewers:
* **Manual Verification:** Contributors MUST independently calculate, parse, or manually verify all AI-generated examples before committing them to a pull request.
* **No Blind Commits:** Contributors MUST NOT directly commit AI-generated examples without human validation.
* **Mathematical and Schema Accuracy:** Contributors MUST ensure all data within an AI-generated example is logically consistent and mathematically accurate according to the FOCUS normative requirements.
* **Zero-Tolerance for Unreviewed Examples:** Maintainers MUST return a pull request to draft if they determine it contains obviously unreviewed, hallucinated, or broken AI-assisted examples.

### CLA Coverage

**Interactive Mode:** 
* Human contributions made using AI tools MUST be covered by the contributor’s existing CLA. No separate CLA is required for AI tools used interactively where the human controls orchestration and PR submission.
* Per the [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai), the contributor MUST ensure that the terms and conditions of the AI tool do not place any contractual restrictions on its output that are inconsistent with FOCUS' [open source software license](https://creativecommons.org/licenses/by/4.0/) and [intellectual property policies](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md#514-consistency--ipr-reviews).
* The contributor MUST assume full responsibility for ensuring the AI-generated content adheres to all project standards and legal requirements.

**Autonomous mode**: 
* AI agents that create PRs directly MUST be onboarded through the Linux Foundation CLA process. 
* To onboard an AI agent, a contributor MUST submit a [Maintenance Task](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/new?template=maintenance.yml) issue.

## Attribution

The contributor MAY attribute AI assistance and/or tool usage in pull request descriptions, but this is not required.

The FOCUS project does not mandate a specific attribution format. This aligns with the Linux Foundation policy, which focuses on human responsibility rather than disclosure requirements.

## AI Agent Configuration

This repository includes configuration files for AI coding assistants:

* `AGENTS.md` - Project context and conventions (at root for tool compatibility)
* `.ai/commands/` - Reusable workflow definitions
* `.ai/memory/` - Persistent learnings across sessions
* `.ai/<branch-name>/` - Working files for active issues (deleted after PR merge)

Tool-specific wrapper files reference the centralized configuration:

* `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md` - Symlinks to `AGENTS.md`
* `.claude/commands/`, `.cursor/commands/`, `.github/prompts/` - Tool-specific wrappers for interactive use

### Creating Shared Commands

To create a new shared command available across all supported AI tools:

1. **Create the main workflow** in `.ai/commands/<name>.md` with full process documentation
2. **Create tool-specific wrappers** that reference the main workflow:

| Tool | File | Format |
| --- | --- | --- |
| Claude Code | `.claude/commands/<name>.md` | YAML frontmatter with `allowed-tools`, then reference |
| Cursor | `.cursor/commands/<name>.md` | Simple reference to `.ai/commands/<name>.md` |
| GitHub Copilot | `.github/prompts/<name>.prompt.md` | Simple reference to `.ai/commands/<name>.md` |

See existing commands (e.g., `feature`, `pr-update`) for examples.

### Working File Lifecycle

Working folders (`.ai/work/<issue-number>-<kebab-case-name>/`) contain research, plans, and task tracking for active issues. Use the same naming convention as your branch.

After a PR is approved but before merging:

1. **Migrate valuable content**: Include broadly useful research in `supporting_content/`
2. **Capture execution details**: Add relevant implementation notes to the PR description or linked issue
3. **Delete the working folder**: Remove the `.ai/work/` folder in a final commit

**Important**: Do not delete working files until final approval is received. A PR readiness check will remind you when cleanup is needed.

These configuration files help AI tools work effectively within the repository, producing consistent content that aligns with project goals and conventions.

## References

* [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai)
* [Apache Software Foundation Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)
* [FOCUS Development Processes](development-processes.md)
* [FOCUS CLA and IPR Requirements](../ipr.md)

