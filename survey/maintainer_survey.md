# Maintainer Survey: AI Contribution Policies in Open Source

## Part I: Background Information

**D1.** In which country do you currently work?
- ○ (Dropdown of countries)

**D2.** How many years of open-source experience do you have?
- ○ < 1 year
- ○ 1–3 years
- ○ 4–10 years
- ○ > 10 years

**D3.** How many open-source projects do you currently maintain or own?
- ○ Up to 5 projects
- ○ 6–10 projects
- ○ 11–15 projects
- ○ > 15 projects

---

## Part II: Overall Stance of AI Contributions

**MQ1.** What is your overall stance on AI contributions?
- ○ Prohibit — AI-generated content is not allowed
- ○ Permissive — AI-generated content is allowed (with or without conditions)

**MQ2.** (If MQ1 = Prohibit) Why did you choose to prohibit AI-generated contribution? (Select all that apply)
- □ AI-generated code is often low-quality or contains errors
- □ Security risks from AI-generated vulnerabilities
- □ Intellectual property and licensing concerns
- □ Concerns about security vulnerabilities introduced via AI-generated code
- □ Difficult to verify AI-generated code quality
- □ Maintainer bandwidth is too limited to review AI-generated PRs adequately
- □ Community consensus to prohibit
- □ Other: __________

**MQ3.** (If MQ1 = Permissive) Why did you choose to allow AI-generated contribution? (Select all that apply)
- □ AI tools can improve contributor productivity
- □ AI-generated code can be high quality when properly reviewed
- □ We trust contributors to use AI responsibly
- □ Allowing AI attracts more contributors
- □ Prohibiting AI use is impractical to enforce
- □ AI tools help lower the barrier for new contributors
- □ Community consensus to allow
- □ Other: __________

**MQ4.** (If MQ1 = Permissive) What conditions do you consider important when allowing AI-generated contributions to your project? (Select all that apply)
- □ AI-generated contributions must undergo manual review
- □ Contributors must explicitly disclose that AI tools were used
- □ AI-generated contributions must meet quality standards
- □ AI should only be used for specific types of work (e.g., documentation, tests, but not core logic)
- □ Only certain AI tools are permitted (e.g., coding assistants yes, autonomous agents no)
- □ AI-generated content must follow project rules/guides on how AI tools may be used (e.g., allowed use cases, prohibited outputs)
- □ AI-generated content must be supplemented with prompts/tests
- □ AI-generated content must adhere to the project's existing coding style
- □ No conditions needed
- □ Other: __________

---

## Part III: AI Contribution Policy Experience

**MQ5.** Does your project have an AI contribution policy statement (in the contributing guidelines or as a separate document)?
- ○ Yes
- ○ No

*(The following questions only apply if MQ5 = Yes)*

**MQ6.** What do you expect or believe the AI policy can achieve? (Select all that apply)
- □ Improve overall code quality
- □ Reduce review burden by filtering out low-quality PRs
- □ Ensure contributors understand and take responsibility for submitted code
- □ Protect the project from legal or IP risks
- □ Maintain community trust and transparency
- □ Block spam or low-effort AI-generated contributions
- □ Encourage more thoughtful and meaningful contributions
- □ Set expectations for new contributors
- □ Other: __________

**MQ7.** After the policy was established, what changes have you observed in terms of the quantity and quality of PRs?

| | Decreased a lot | Decreased somewhat | No change | Increased somewhat | Increased a lot |
|---|:---:|:---:|:---:|:---:|:---:|
| Total number of PRs submitted | ○ | ○ | ○ | ○ | ○ |
| Total number of AI-generated PRs submitted | ○ | ○ | ○ | ○ | ○ |
| Total number of low-quality PRs submitted | ○ | ○ | ○ | ○ | ○ |
| Overall code quality of merged PRs | ○ | ○ | ○ | ○ | ○ |

**MQ8.** After the policy was established, what changes have you observed in terms of the processing time costs?

| | Decreased a lot | Decreased somewhat | No change | Increased somewhat | Increased a lot |
|---|:---:|:---:|:---:|:---:|:---:|
| Review workload (time spent reviewing) | ○ | ○ | ○ | ○ | ○ |
| Time to merge a PR (merge latency) | ○ | ○ | ○ | ○ | ○ |
| Time to first comment on a new PR (response latency) | ○ | ○ | ○ | ○ | ○ |
| Time to close a non-merged PR (closure latency) | ○ | ○ | ○ | ○ | ○ |

**MQ9.** After the policy was established, what changes did you observe in terms of the community engagement?

| | Decreased a lot | Decreased somewhat | No change | Increased somewhat | Increased a lot |
|---|:---:|:---:|:---:|:---:|:---:|
| Number of new contributors (first-time PR authors) | ○ | ○ | ○ | ○ | ○ |
| Community engagement (discussion, issues) | ○ | ○ | ○ | ○ | ○ |

**MQ10.** To what extent do you feel contributors have followed your AI contribution policy?
- ○ Fully followed
- ○ Mostly followed
- ○ Somewhat followed
- ○ Rarely followed
- ○ Not followed at all

**MQ11.** What methods does your project currently have in place to enforce your AI contribution policy? (Select all that apply)
- □ Reviewers check for AI use during code review
- □ Compliance relies on contributors' self-reporting and good faith
- □ Contributors must sign/acknowledge the policy before submitting (e.g., CLA, PR checklist)
- □ Automated pipeline/tool checks that flag potential AI-generated code
- □ The policy specifies consequences for violations (e.g., PR rejection, temporary ban)
- □ Community members can flag suspected policy violations
- □ The policy exists but is not actively enforced
- □ Other: __________

**MQ12.** What are the main difficulties you have encountered in enforcing your AI contribution policy? (Select all that apply)
- □ Hard to detect whether a contribution is AI-generated
- □ Contributors unwilling to disclose AI use
- □ Policy too vague or difficult to interpret
- □ Lack of tools or processes to verify compliance
- □ Insufficient maintainer bandwidth to enforce
- □ Community pushback or disagreement with the policy
- □ Policy does not cover all AI use scenarios
- □ Other: __________

---

## Part IV: Open-Ended

**MQ13.** Please note any comments you have regarding the AI contribution policy.

_______________________________________________