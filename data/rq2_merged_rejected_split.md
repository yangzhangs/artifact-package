# RQ2: Merged vs. Closed-Without-Merge PRs — Split Analysis

This document reports an additional analysis that separates closed PRs into
**merged** and **closed-without-merge (rejected)** PRs, and re-runs the RQ2 mixed-effects models on each subset. The results
support the interpretation in the paper: the post-adoption decline in closed
PRs is driven by fewer merged PRs, while rejected PRs show no significant
change.

## Data Construction

- Per-PR data for the 113 RQ2 repositories (source: `repo_pull_requests` table
  in the study database; `pr_merged` distinguishes merged from
  closed-without-merge PRs).
- Each PR is assigned to a 30-day bin by its close time, relative to the
  repository's AIP adoption date (`aip_first_date_final.csv`), spanning 6 bins
  before and 6 after adoption and excluding the 30-day window centered on the
  adoption date, exactly as in the main panel.
- Per repository and bin we compute the number of merged PRs and the number of
  rejected PRs.
- The resulting panel is in `data/panel/split_merged_rejected_panel.csv`
  (1,345 repository-bin rows; bins with no PR activity are absent).

## Model

Same specification as the paper's Tables IV and V, estimated per group
(permissive: 101 repositories, prohibited: 12 repositories):

```
log(count + 1) ~ time + intervention + time_after
               + log_stars + log_contributors + log_commits + log_repo_age_days
               + (1 | repo_name)
```

`time_after` (δ) captures the post-adoption change in slope. The
reproduction script is `scripts/rq2-impact/rdd_split_merged_rejected.R`.

## Results

| DV | Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c | n | repos |
|---|---|---|---|---|---|---|---|---|
| Merged PR count | Permissive | 0.042** | -0.079 | **-0.069\*\*\*** | 0.231 | 0.763 | 1,201 | 101 |
| Merged PR count | Prohibited | 0.091* | 0.211 | **-0.158\*** | 0.579 | 0.747 | 144 | 12 |
| Rejected PR count | Permissive | 0.071*** | -0.228** | -0.033 | 0.232 | 0.692 | 1,201 | 101 |
| Rejected PR count | Prohibited | 0.099 | -0.020 | -0.020 | 0.467 | 0.800 | 144 | 12 |

Significance: ·p<0.1, *p<0.05, **p<0.01, ***p<0.001.

## Interpretation

The overall decline in closed PRs (Tables IV and V) is carried by **merged
PRs**, with significant negative post-adoption slopes in both groups
(permissive -0.069***, prohibited -0.158*). Rejected PR counts show no
significant change, so the decline accompanies the decline in opened PRs
rather than an independent change in closure behavior.
