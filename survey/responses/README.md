# Survey Response Data

Anonymized per-respondent data for the two online surveys. Each row is one valid response:
`maintainer_responses.csv` contains the 68 maintainer responses, and
`contributor_responses.csv` contains the 59 contributor responses.

`respondent_id` is a sequential id in the original order of the survey
responses. Columns correspond to the questions in the survey instruments
(`maintainer_survey.md` / `contributor_survey.md`); option texts follow the
instrument wording. Multi-select answers are separated by `;`. Names and email
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
| `Total number of PRs submitted` | MQ6. Change in total number of PRs submitted |
| `Total number of AI-generated PRs submitted` | MQ6. Change in total number of AI-generated PRs submitted |
| `Total number of PRs closed` | MQ6. Change in total number of PRs closed |
| `Review workload (time spent reviewing)` | MQ7. Change in review workload (time spent reviewing) |
| `Time to close a PR (close latency)` | MQ7. Change in time to close a PR (close latency) |
| `Review comment on a new PR` | MQ7. Change in review comment on a new PR |
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
| `disclosure` | CQ1. When you use AI tools for open-source contributions, do you typically disclose this in the PR? |
| `aware` | CQ2. Are you aware that the projects you contribute to have AI contribution policies? |
| `perceived_stance` | CQ3. What is the overall stance of the AI contribution policy of the project you contribute to? |
| `reaction` | CQ4. What was your initial reaction to the policy? |
| `behavior_change` | CQ5. After learning about the AI policy, did your contribution behavior change? |
| `comments` | CQ6. Open-ended comments |

Free-text answers to the reasons-for-opposing question asked in the
administered form are appended to the `comments` column. For the maintainer
survey, all columns correspond one-to-one to the instrument questions.
