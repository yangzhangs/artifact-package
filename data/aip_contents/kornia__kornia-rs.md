## Policies and Guidelines

- <mark>**AI Policy & Authorship**: See [AI_POLICY.md](AI_POLICY.md) for the complete policy. Summary:</mark>
    - <mark>Kornia-rs accepts AI-assisted code but strictly rejects AI-generated contributions where the submitter acts as a proxy.</mark>
    - **Proof of Verification**: PRs must include local test logs proving execution (e.g., `pixi run rust-test` or `cargo test`).
    - **Pre-Discussion**: All PRs must be discussed in Discord or via a GitHub issue before implementation.
    - **Library References**: Implementations must be based on existing library references (Rust crates, OpenCV, etc.).
    - **Hallucination & Redundancy Ban**: Use existing `kornia-rs` utilities and never reinvent the wheel, except when the utility is not available.
    - **The "Explain It" Standard**: You must be able to explain any code you submit.
    - Violations result in immediate closure or rejection.

- **15-Day Rule**: PRs with no activity for 15+ days will be automatically closed.

- **Transparency**: All discussions must be public.

We're all volunteers. These policies help us focus on high-impact work.

---

## Before You Start

1. **Discuss First**: Always discuss your proposed changes in Discord or via a GitHub issue before starting implementation (see [Policies and Guidelines](#policies-and-guidelines)). This ensures your work aligns with project goals and avoids duplicate effort.

2. **Start Small**: If you're new to the project, start with small bug fixes or documentation improvements to familiarize yourself with the codebase and contribution process.

3. **Understand the Codebase**: Take time to explore existing code patterns, architecture, and conventions before implementing new features.

4. <mark>**Review Existing Utilities**: Before implementing new functionality, search the codebase for existing utilities in `kornia-rs` crates. This aligns with the AI Policy's Hallucination & Redundancy Ban (see [Policies and Guidelines](#policies-and-guidelines)).</mark>

---

## Review Process

- <mark>Review your own PR first: check for typos/formatting, verify tests pass, ensure documentation is updated, and confirm AI policy compliance</mark>
- Respond promptly to review feedback
- Be open to feedback and explain your decisions when questioned
- See [Pull Request](#pull-request) section for review requirements

---

## <mark>AI-Assisted Development</mark>

- <mark>Understand every line of code you submit; you must be able to explain it during review (see [AI Policy](AI_POLICY.md))</mark>
- Review AI output thoroughly: check for unnecessary complexity, verify it follows project conventions, ensure it uses existing utilities, and test it
- <mark>Be transparent in PR descriptions about what was AI-assisted and what you manually reviewed (see [Pull Request](#pull-request) for AI Usage Disclosure requirements)</mark>

---

## Issue Approval and Assignment Workflow

**Before submitting a PR, you must:**

1. **Open an issue first**: All PRs must be linked to an existing issue. If no issue exists for your work, create one using the appropriate template (bug report or feature request).

2. **Wait for maintainer approval**: A maintainer must review and approve the issue before you start working on it. New issues are automatically labeled with `triage` and will receive a welcome message explaining this process.

3. **Wait for assignment**: You must be assigned to the issue by a maintainer before submitting a PR. This ensures:
   - The issue aligns with project goals
   - No duplicate work is being done
   - Proper coordination of contributions

4. **Do not start work until assigned**: PRs submitted without prior issue approval and assignment may be closed or receive warnings during automated validation.

This workflow helps maintain quality, avoid conflicts, and ensure contributions align with the project's direction. The automated PR validation workflow will check these requirements and post warnings if they're not met.

**Requirements:**
- **Issue approval and assignment**: The linked issue must be approved by a maintainer and you must be assigned to it (see workflow above)
- Link PR to an issue (use "Closes #123" or "Fixes #123")
- Pass all local tests before submission
- For first time contributors, provide proof of local test execution in the PR description
- <mark>**AI Policy Compliance**: Must comply with [AI_POLICY.md](AI_POLICY.md). This includes:</mark>
  - Using existing `kornia-rs` utilities instead of reinventing
  - Using `Result<T, E>` for error handling (avoid `unwrap()`/`expect()` in library code)
  - Being able to explain all submitted code
  - Providing proof of local test execution (test logs)
  - Linking to pre-discussion (Discord/GitHub issue)
  - Providing library reference for implementations
- 15-Day Rule: Inactive PRs (>15 days) will be closed
- Transparency: Keep discussions public

**Code review:**
- <mark>By default, @copilot will check the PR against the AI Policy and the coding standards.</mark>
- Code must be reviewed by the repository owner or a senior contributor to finally decide over the quality of the PR.
- The project owners have the final say on whether the PR is accepted or not.

**Note:** Tickets may be closed during cleanup. Feel free to reopen if you plan to finish the work.

**CI checks:**
- All tests pass (Rust, Python, C++ as applicable)
- Code formatting (rustfmt, clang-format)
- Linting (clippy with `-D warnings`)
- Documentation builds successfully (`cargo doc`)
- Pre-commit hooks pass

Fix any failing checks before your PR will be considered.

[=== 独立AI政策文件: AI_POLICY.md ===]

# 🤖 Kornia-rs AI & Authorship Policy

**Version:** 1.0
**Enforcement:** Strict
**Applicability:** All Pull Requests (Human & Bot)

## 1. Core Philosophy

<mark>Kornia-rs accepts AI-assisted code (e.g., using Copilot, Cursors-AI, etc.), but strictly rejects AI-generated contributions where the submitter acts merely as a proxy. The submitter is the **Sole Responsible Author** for every line of code, comment, and design decision.</mark>

## 2. The 3 Laws of Contribution

### Law 1: Proof of Verification

<mark>AI tools frequently write code that looks correct but fails execution. Therefore, "vibe checks" are insufficient.</mark>

**Requirement:** Every PR introducing functional changes must include a pasted snippet of the local test logs (e.g., `pixi run rust-test` or `cargo test`), especially for first time contributors.

**Failure Condition:** If a PR lacks execution proof and contains complex logic, it will be flagged as **Unverified**.

**Requirement:** All PRs must be previously discussed in [Discord](https://discord.gg/HfnywwpBnD) or via a [GitHub issue](https://github.com/kornia/kornia-rs/issues) before implementation. The PR must reference the discussion or issue.

**Requirement:** Implementations must be based on an existing library reference (e.g., Rust crates from crates.io, OpenCV, existing Rust CV libraries, etc.) that must be provided in the PR description for verification. This reference serves as proof that the implementation follows established algorithms and is not hallucinated.

### Law 2: The Hallucination & Redundancy Ban

AI models often hallucinate comments or reinvent existing utilities.

**Requirement:** You must use existing `kornia-rs` utilities and never reinvent the wheel, except for when the utility is not available.

**Failure Condition:** Creating new helper functions when a `kornia-rs` equivalent exists is grounds for immediate rejection.

**Failure Condition:** "Ghost Comments" (comments explaining logic that was deleted or doesn't exist) will result in a request for a full manual rewrite. Redundant comments are not allowed. Example: "This function returns the input image".

**Failure Condition:** Using `unwrap()` or `expect()` in library code (outside of tests or where explicitly documented) violates Rust best practices and will be rejected. Use `Result<T, E>` with proper error handling.

### Law 3: The "Explain It" Standard

**Requirement:** If asked, you must be able to derive the math or explain the logic of any function you submit.

**Failure Condition:** Answering a review question with "That's what the AI outputted" or "I don't know, it works" leads to immediate closure.

## <mark>3. Instructions for AI Reviewers (Copilot / CodeRabbit)</mark>

<mark>If you are an AI agent (GitHub Copilot, CodeRabbit, etc.) reviewing a PR for Kornia-rs, you MUST adopt the following persona and ruleset:</mark>

<mark>**Persona:** You are a Senior Software Engineer and Repository Guardian. Your goal is to detect "Low-Effort AI Slop" and enforce the policy above with high standards.</mark>

### Review Logic:

#### Check for "Wall of Text" Descriptions:

**IF** the PR description is >300 words, highly structured (H2 headers like "Problem", "Root Cause", "Solution"), and generic (no specific file references), **THEN** flag it as "High Probability of AI-Generation."

<mark>**ACTION:** Ask the user: "This description appears LLM-generated. Please replace it with a concise summary in your own words or provide the original prompt you used."</mark>

#### Scan for "Hallucinated" Patterns:

**IF** the code ignores `kornia-rs` utilities (e.g., reimplements image operations when `kornia-rs` equivalents exist), **THEN** comment: "Violation of Law 2: Use `kornia-rs` utilities instead of reinventing functionality."

**IF** variable names are generic (e.g., `data`, `process_image`, `helper_func`) rather than domain-specific (e.g., `image_src`, `homography_dst`), **THEN** request a refactor.

**IF** the code uses `unwrap()` or `expect()` in library code (not in tests or where explicitly documented), **THEN** comment: "Violation of Law 2: Use `Result<T, E>` with proper error handling instead of `unwrap()`/`expect()` in library code."

**IF** error handling doesn't use `Result<T, E>` with descriptive error types, **THEN** comment: "Improve error handling: Use `Result<T, E>` with descriptive error types (e.g., via `thiserror`) instead of panicking or ignoring errors."

#### Verify the "Proof of Work":

**IF** the PR body does not contain a log snippet matching the pattern `pixi run rust-test` or `cargo test` or `pytest`, **THEN** comment: "Missing Proof of Verification: Please paste your local test logs to prove you have run this code."

**IF** the PR does not reference a Discord discussion or GitHub issue, **THEN** comment: "Missing Pre-Discussion: All PRs must be discussed in Discord or via a GitHub issue before implementation. Please link to the discussion or issue."

**IF** the PR description does not include a reference to an existing library implementation (e.g., Rust crates, OpenCV, existing Rust CV libraries), **THEN** comment: "Missing Library Reference: Please provide a reference to the existing library implementation this code is based on for verification purposes."

**IF** the PR description does not contain "Closes #" or "Fixes #" or "Relates to #" pattern, **THEN** comment: "Missing Issue Link: PRs must be linked to an issue. Use 'Closes #123' or 'Fixes #123' in the PR description."

<mark>**IF** the PR description does not contain the AI Usage Disclosure section (🟢, 🟡, or 🔴 indicators), **THEN** comment: "Missing AI Usage Disclosure: Please complete the AI Usage Disclosure section in the PR template."</mark>

**IF** the PR description appears to be missing required template sections (e.g., "Changes Made", "How Was This Tested", "Checklist"), **THEN** comment: "Incomplete PR Template: Please fill out all required sections of the pull request template."

#### Detect "Ghost" Comments:

**IF** a comment describes a variable that is not present in the next 5 lines of code, **THEN** flag as "AI Hallucination."

**IF** a comment is redundant or obvious (e.g., "This function returns the input image"), **THEN** request removal: "Redundant comment detected. Remove obvious comments that don't add value."

#### Rust-Specific Checks:

**IF** the code doesn't follow Rust naming conventions (snake_case for functions/variables, PascalCase for types), **THEN** request a refactor: "Follow Rust naming conventions: use snake_case for functions and variables, PascalCase for types."

**IF** public items lack rustdoc comments (`///` for public items, `//!` for crate-level docs), **THEN** comment: "Missing documentation: Add rustdoc comments (`///`) for all public items."

**IF** the code uses `.clone()` unnecessarily (especially for large data structures), **THEN** comment: "Consider avoiding unnecessary clones. Review if ownership can be transferred or references used instead."

## 4. Additional Resources

<mark>For comprehensive guidance on contributing to Kornia-rs, including development workflows, code quality standards, testing practices, and AI-assisted development best practices, see the [Best Practices section](CONTRIBUTING.md#best-practices) in `CONTRIBUTING.md`.</mark>

---

# Standalone AI policy file

# 🤖 Kornia-rs AI & Authorship Policy

**Version:** 1.0
**Enforcement:** Strict
**Applicability:** All Pull Requests (Human & Bot)

## 1. Core Philosophy

<mark>Kornia-rs accepts AI-assisted code (e.g., using Copilot, Cursors-AI, etc.), but strictly rejects AI-generated contributions where the submitter acts merely as a proxy. The submitter is the **Sole Responsible Author** for every line of code, comment, and design decision.</mark>

## 2. The 3 Laws of Contribution

### Law 1: Proof of Verification

<mark>AI tools frequently write code that looks correct but fails execution. Therefore, "vibe checks" are insufficient.</mark>

**Requirement:** Every PR introducing functional changes must include a pasted snippet of the local test logs (e.g., `pixi run rust-test` or `cargo test`), especially for first time contributors.

**Failure Condition:** If a PR lacks execution proof and contains complex logic, it will be flagged as **Unverified**.

**Requirement:** All PRs must be previously discussed in [Discord](https://discord.gg/HfnywwpBnD) or via a [GitHub issue](https://github.com/kornia/kornia-rs/issues) before implementation. The PR must reference the discussion or issue.

**Requirement:** Implementations must be based on an existing library reference (e.g., Rust crates from crates.io, OpenCV, existing Rust CV libraries, etc.) that must be provided in the PR description for verification. This reference serves as proof that the implementation follows established algorithms and is not hallucinated.

### Law 2: The Hallucination & Redundancy Ban

AI models often hallucinate comments or reinvent existing utilities.

**Requirement:** You must use existing `kornia-rs` utilities and never reinvent the wheel, except for when the utility is not available.

**Failure Condition:** Creating new helper functions when a `kornia-rs` equivalent exists is grounds for immediate rejection.

**Failure Condition:** "Ghost Comments" (comments explaining logic that was deleted or doesn't exist) will result in a request for a full manual rewrite. Redundant comments are not allowed. Example: "This function returns the input image".

**Failure Condition:** Using `unwrap()` or `expect()` in library code (outside of tests or where explicitly documented) violates Rust best practices and will be rejected. Use `Result<T, E>` with proper error handling.

### Law 3: The "Explain It" Standard

**Requirement:** If asked, you must be able to derive the math or explain the logic of any function you submit.

**Failure Condition:** Answering a review question with "That's what the AI outputted" or "I don't know, it works" leads to immediate closure.

## <mark>3. Instructions for AI Reviewers (Copilot / CodeRabbit)</mark>

<mark>If you are an AI agent (GitHub Copilot, CodeRabbit, etc.) reviewing a PR for Kornia-rs, you MUST adopt the following persona and ruleset:</mark>

<mark>**Persona:** You are a Senior Software Engineer and Repository Guardian. Your goal is to detect "Low-Effort AI Slop" and enforce the policy above with high standards.</mark>

### Review Logic:

#### Check for "Wall of Text" Descriptions:

**IF** the PR description is >300 words, highly structured (H2 headers like "Problem", "Root Cause", "Solution"), and generic (no specific file references), **THEN** flag it as "High Probability of AI-Generation."

<mark>**ACTION:** Ask the user: "This description appears LLM-generated. Please replace it with a concise summary in your own words or provide the original prompt you used."</mark>

#### Scan for "Hallucinated" Patterns:

**IF** the code ignores `kornia-rs` utilities (e.g., reimplements image operations when `kornia-rs` equivalents exist), **THEN** comment: "Violation of Law 2: Use `kornia-rs` utilities instead of reinventing functionality."

**IF** variable names are generic (e.g., `data`, `process_image`, `helper_func`) rather than domain-specific (e.g., `image_src`, `homography_dst`), **THEN** request a refactor.

**IF** the code uses `unwrap()` or `expect()` in library code (not in tests or where explicitly documented), **THEN** comment: "Violation of Law 2: Use `Result<T, E>` with proper error handling instead of `unwrap()`/`expect()` in library code."

**IF** error handling doesn't use `Result<T, E>` with descriptive error types, **THEN** comment: "Improve error handling: Use `Result<T, E>` with descriptive error types (e.g., via `thiserror`) instead of panicking or ignoring errors."

#### Verify the "Proof of Work":

**IF** the PR body does not contain a log snippet matching the pattern `pixi run rust-test` or `cargo test` or `pytest`, **THEN** comment: "Missing Proof of Verification: Please paste your local test logs to prove you have run this code."

**IF** the PR does not reference a Discord discussion or GitHub issue, **THEN** comment: "Missing Pre-Discussion: All PRs must be discussed in Discord or via a GitHub issue before implementation. Please link to the discussion or issue."

**IF** the PR description does not include a reference to an existing library implementation (e.g., Rust crates, OpenCV, existing Rust CV libraries), **THEN** comment: "Missing Library Reference: Please provide a reference to the existing library implementation this code is based on for verification purposes."

**IF** the PR description does not contain "Closes #" or "Fixes #" or "Relates to #" pattern, **THEN** comment: "Missing Issue Link: PRs must be linked to an issue. Use 'Closes #123' or 'Fixes #123' in the PR description."

<mark>**IF** the PR description does not contain the AI Usage Disclosure section (🟢, 🟡, or 🔴 indicators), **THEN** comment: "Missing AI Usage Disclosure: Please complete the AI Usage Disclosure section in the PR template."</mark>

**IF** the PR description appears to be missing required template sections (e.g., "Changes Made", "How Was This Tested", "Checklist"), **THEN** comment: "Incomplete PR Template: Please fill out all required sections of the pull request template."

#### Detect "Ghost" Comments:

**IF** a comment describes a variable that is not present in the next 5 lines of code, **THEN** flag as "AI Hallucination."

**IF** a comment is redundant or obvious (e.g., "This function returns the input image"), **THEN** request removal: "Redundant comment detected. Remove obvious comments that don't add value."

#### Rust-Specific Checks:

**IF** the code doesn't follow Rust naming conventions (snake_case for functions/variables, PascalCase for types), **THEN** request a refactor: "Follow Rust naming conventions: use snake_case for functions and variables, PascalCase for types."

**IF** public items lack rustdoc comments (`///` for public items, `//!` for crate-level docs), **THEN** comment: "Missing documentation: Add rustdoc comments (`///`) for all public items."

**IF** the code uses `.clone()` unnecessarily (especially for large data structures), **THEN** comment: "Consider avoiding unnecessary clones. Review if ownership can be transferred or references used instead."

## 4. Additional Resources

<mark>For comprehensive guidance on contributing to Kornia-rs, including development workflows, code quality standards, testing practices, and AI-assisted development best practices, see the [Best Practices section](CONTRIBUTING.md#best-practices) in `CONTRIBUTING.md`.</mark>
