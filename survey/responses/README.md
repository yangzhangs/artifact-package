# Survey Response Data

Anonymized per-respondent data for the two online surveys. Each row is one valid response:
`maintainer_responses.csv` contains the 68 maintainer responses, and
`contributor_responses.csv` contains the 59 contributor responses.

`respondent_id` is a sequential id in the original order of the survey
responses. Multi-select answers are separated by `;`. Option texts follow
the survey instruments (`maintainer_survey.md` / `contributor_survey.md`); the
administered form additionally included the grid rows on low-quality PRs,
merged-PR code quality, merge latency, new contributors, and community
engagement, which are kept with their original wording. Names and email
addresses are never released.

## maintainer_responses.csv

| Column | Survey question |
|---|---|
| `respondent_id` | Sequential id in the original response order |
| `country` | D1. In which country do you currently work? |
| `years_experience` | D2. How many years of open-source experience do you have? |
| `projects_maintained` | D3. How many open-source projects do you currently maintain or own? |
| `stance` | MQ1. What is your overall stance on AI contributions? |
| `rationale_prohibit` | MQ2. Why did you choose to prohibit AI-generated contribution? |
| `rationale_allow` | MQ3. Why did you choose to allow AI-generated contribution? |
| `conditions` | MQ4. What conditions do you consider important when allowing AI-generated contributions to your project? |
| `has_policy` | MQ5. Does your project have an AI contribution policy statement? |
| `expected_outcomes` | What do you expect or believe the AI policy can achieve? |
| `Total number of PRs submitted` | MQ6. Change in total number of PRs submitted |
| `Total number of AI-generated PRs submitted` | MQ6. Change in total number of AI-generated PRs submitted |
| `Total number of low-quality PRs submitted` | MQ6. Change in total number of low-quality PRs submitted |
| `Overall code quality of merged PRs` | MQ6. Change in overall code quality of merged PRs |
| `Review workload (time spent reviewing)` | MQ7. Change in review workload (time spent reviewing) |
| `Time to merge a PR (merge latency)` | MQ7. Change in time to merge a PR |
| `Review comment on a new PR` | MQ7. Change in time to first comment on a new PR |
| `Time to close a PR (close latency)` | MQ7. Change in time to close a non-merged PR |
| `Number of new contributors (first-time PR authors)` | Change in number of new contributors |
| `Community engagement (discussion, issues)` | Change in community engagement |
| `compliance` | MQ8. To what extent do you feel contributors have followed your AI contribution policy? |
| `enforcement_methods` | MQ9. What methods does your project currently have in place to enforce your AI contribution policy? |
| `difficulties` | MQ10. What are the main difficulties you have encountered in enforcing your AI contribution policy? |
| `comments` | MQ11. Open-ended comments |

## contributor_responses.csv

| Column | Survey question |
|---|---|
| `respondent_id` | Sequential id in the original response order |
| `country` | D1. In which country do you currently work? |
| `years_experience` | D2. How many years of open-source experience do you have? |
| `projects_contributed` | D3. How many open-source projects have you contributed to? |
| `ai_frequency` | How often do you use AI-assisted coding tools when contributing? |
| `ai_purposes` | For what purposes do you use AI tools when contributing? |
| `disclosure` | CQ1. When you use AI tools for open-source contributions, do you typically disclose this in the PR? |
| `aware` | CQ2. Are you aware that the projects you contribute to have AI contribution policies? |
| `perceived_stance` | CQ3. What is the overall stance of the AI contribution policy of the project you contribute to? |
| `reaction` | CQ4. What was your initial reaction to the policy? |
| `support_reasons` | Reasons for supporting the AI policy |
| `oppose_reasons` | Reasons for opposing the AI policy |
| `behavior_change` | CQ5. After learning about the AI policy, did your contribution behavior change? |
| `comments` | CQ6. Open-ended comments |
