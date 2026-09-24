# RQ2: Merged vs. Closed-Without-Merge PRs — Split Analysis

This document reports an additional analysis that separates closed PRs into
**merged** and **closed-without-merge (rejected)** PRs, and re-runs the RQ2 mixed-effects models on each subset. The results
support the interpretation in the paper: the post-adoption decline in closed
PRs is driven by fewer merged PRs, while rejected PRs show no significant
change.

The reproduction script is `scripts/rq2-impact/rdd_split_merged_rejected.R`.

## Results

| DV | Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c | 
|---|---|---|---|---|---|---|---|---|
| Merged PR count | Permissive | 0.042** | -0.079 | **-0.069\*\*\*** | 0.231 | 0.763 | 
| Merged PR count | Prohibited | 0.091* | 0.211 | **-0.158\*** | 0.579 | 0.747 |
| Rejected PR count | Permissive | 0.071*** | -0.228** | -0.033 | 0.232 | 0.692 | 
| Rejected PR count | Prohibited | 0.099 | -0.020 | -0.020 | 0.467 | 0.800 | 

Significance: ·p<0.1, *p<0.05, **p<0.01, ***p<0.001.


The overall decline in closed PRs (Tables IV and V) is carried by **merged
PRs**, with significant negative post-adoption slopes in both groups
(permissive -0.069***, prohibited -0.158*). Rejected PR counts show no
significant change, so the decline accompanies the decline in opened PRs
rather than an independent change in closure behavior.
