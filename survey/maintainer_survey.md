# Maintainer Survey: AI Contribution Policies in Open Source

## Part I: Demographics

**D1.** How long have you been contributing to open-source projects on GitHub?
- ○ Less than 1 year
- ○ 1–3 years
- ○ 3–5 years
- ○ 5–10 years
- ○ More than 10 years

**D2.** What role(s) do you typically play in open-source projects? (Select all that apply)
- □ External contributor (occasional PRs)
- □ Regular contributor (frequent commits)
- □ Maintainer / code reviewer
- □ Project owner / administrator
- □ Other: __________

**D3.** How many open-source projects have you contributed to (with at least one merged PR)?
- ○ 1–3
- ○ 4–10
- ○ 11–25
- ○ 26–50
- ○ More than 50

**D4.** What is your primary programming language?
- ○ Python  ○ JavaScript/TypeScript  ○ Java  ○ Go  ○ Rust  ○ C/C++  ○ Other: __________

**D5.** What is your age group?
- ○ 18–24  ○ 25–34  ○ 35–44  ○ 45–54  ○ 55+

**D6.** What is your professional status?
- ○ Student  ○ Software engineer (industry)  ○ Researcher/academic  ○ Independent/freelance  ○ Other: __________

---

## Part II: AI Tool Usage

**B1.** How often do you use AI-assisted coding tools (e.g., GitHub Copilot, ChatGPT, Claude, Cursor) when contributing to open-source projects?
- ○ Never
- ○ Rarely (less than 10% of my PRs)
- ○ Sometimes (10–30%)
- ○ Often (30–70%)
- ○ Most of the time (more than 70%)

**B2.** For what purposes do you use AI tools in your open-source contributions? (Select all that apply)
- □ Generating code from scratch
- □ Completing boilerplate / repetitive code
- □ Writing tests
- □ Debugging / understanding code
- □ Writing documentation
- □ Translating code between languages
- □ I do not use AI tools
- □ Other: __________

**B3.** In your experience, how does AI-assisted code typically compare to human-written code in terms of overall quality?
- ○ Much higher quality
- ○ Somewhat higher quality
- ○ About the same
- ○ Somewhat lower quality
- ○ Much lower quality
- ○ It varies too much to generalize

**B4.** Have you noticed an increase in AI-generated pull requests in projects you contribute to?
- ○ Yes, a noticeable increase
- ○ Yes, a slight increase
- ○ No change
- ○ A decrease in AI-generated PRs
- ○ I cannot tell

**B5.** (If B4 = noticeable or slight increase) How would you characterize the quality of these AI-generated PRs compared to human-written ones?
- ○ Generally higher quality
- ○ About the same
- ○ Generally lower quality but still useful
- ○ Generally low quality (e.g., superficial fixes, incorrect code, spam)
- ○ Highly variable — some are good, many are poor

---

## Part III: AIP Awareness and Status

**MQ1.** What is your overall stance on AI contributions?
- ○ Permitted (with or without conditions)
- ○ Prohibited

**MQ2.** (If MQ1 = Prohibited) Why did you choose to prohibit AI contribution? (Select all that apply)
- □ AI-generated code is often low-quality
- □ Difficult to verify AI-generated code correctness
- □ Intellectual property and licensing concerns
- □ Maintainer bandwidth is limited to review adequately
- □ Lack of clear accountability for AI-generated code
- □ Security risks from AI-generated vulnerabilities
- □ Other: __________

**MQ3.** (If MQ1 = Permitted) Why did you choose to allow AI contribution? (Select all that apply)
- □ AI tools can improve contributor productivity
- □ Prohibiting AI use is impractical to enforce
- □ Properly reviewed AI code can be high quality
- □ We trust contributors to use AI responsibly
- □ AI tools help lower the barrier for new contributors
- □ Allowing AI attracts more contributors
- □ Other: __________

**MQ4.** (If MQ1 = Permitted) What conditions do you consider important when allowing AI-generated contributions? (Select all that apply)
- □ Human review of AI-generated code
- □ Explicit disclosure of AI use
- □ Follow AI-specific rules (e.g., scope limits, quantitative caps)
- □ Meet quality standards (same as human-written code)
- □ Supplement evidence (e.g., include prompts, add tests)
- □ Other: __________

**MQ5.** Does your project have an AI contribution policy statement (in the contributing guidelines or as a separate document)?
- ○ Yes
- ○ No

*(The following questions only apply if MQ5 = Yes)*

**MQ6.** After the policy was established, what changes have you observed in terms of the PR quantity & quality?

| | Decreased a lot | Decreased somewhat | No change | Increased somewhat | Increased a lot | Not sure |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Total number of PRs submitted | ○ | ○ | ○ | ○ | ○ | ○ |
| Number of new contributors | ○ | ○ | ○ | ○ | ○ | ○ |
| Proportion of low-quality PRs | ○ | ○ | ○ | ○ | ○ | ○ |
| Review workload | ○ | ○ | ○ | ○ | ○ | ○ |
| Time to merge a PR | ○ | ○ | ○ | ○ | ○ | ○ |
| Overall code quality of merged PRs | ○ | ○ | ○ | ○ | ○ | ○ |

**MQ7.** After the policy was established, what changes have you observed in terms of the processing time costs?

| | Decreased | No change | Increased | Not sure |
|---|:---:|:---:|:---:|:---:|
| Review comments per PR | ○ | ○ | ○ | ○ |
| Close latency (time to close a PR) | ○ | ○ | ○ | ○ |

**MQ8.** To what extent do you feel contributors have followed your AI contribution policy?
- ○ Not followed at all
- ○ Rarely followed
- ○ Somewhat followed
- ○ Mostly followed
- ○ Fully followed

**MQ9.** What methods does your project currently have in place to enforce your AI contribution policy? (Select all that apply)
- □ Reviewers check for AI use during code review
- □ Compliance relies on self-reporting and good faith
- □ Policy specifies consequences for violations (e.g., PR rejection, temporary ban)
- □ Contributors must sign policy before submitting (e.g., CLA, PR checklist)
- □ Community members can flag suspected violations
- □ Other: __________

**MQ10.** What are the main difficulties you have encountered in enforcing your AI contribution policy? (Select all that apply)
- □ Hard to detect whether a contribution is AI-generated
- □ Contributors unwilling to disclose AI use
- □ Lack of tools or processes to verify compliance
- □ Insufficient maintainer bandwidth to enforce
- □ Policy too vague or difficult to interpret
- □ Other: __________

**MQ11.** (Optional) Any additional comments on AI contribution policies?

_______________________________________________