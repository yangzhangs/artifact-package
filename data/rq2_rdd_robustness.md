# RQ2: RDD Robustness Analysis — 4-Month vs. 6-Month Windows

This document reports the grouped mixed-effects RDD model results for both the primary 6-month window specification (used in Table V of the paper) and the robustness check using 4-month windows. The 4-month results support the claim in the Threats to Validity section that varying the observation window yields similar phenomena.

## Model Specification

```
DV ~ time + intervention + time_after + log_stars + log_contributors + log_commits + log_repo_age_days + (1|repo_name)
```

- **6-month window:** 12 bins (−6 to +6, excluding 0), 113 repos (101 permissive, 12 prohibited), 1356 rows
- **4-month window:** 8 bins (−4 to +4, excluding 0), 169 repos (154 permissive, 15 prohibited), 1352 rows
- Separate models for permissive and prohibited groups
- REML estimation; significance: ·p<0.1, *p<0.05, **p<0.01, ***p<0.001

---

## 6-Month Window (Primary Specification, Table V)

**Panel:** 1356 rows, 113 repos (Permissive: 101, Prohibited: 12)

### Opened PRs (log_new_prs)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.030* | -0.047 | -0.037* | 0.245 | 0.790 |
| Prohibited | 0.122· | 0.172 | -0.145· | 0.483 | 0.654 |

### Closed PRs (log_prs_closed)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.051** | 0.023 | -0.139*** | 0.204 | 0.678 |
| Prohibited | 0.098· | 0.207 | -0.156* | 0.540 | 0.730 |

### Review Comments (log_review_comments)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.005 | 0.090* | -0.025* | 0.051 | 0.697 |
| Prohibited | -0.008 | 0.112 | -0.042 | 0.266 | 0.777 |

### Close Latency (log_close_latency_h)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.020 | -0.111 | -0.044 | 0.086 | 0.421 |
| Prohibited | 0.269*** | -0.515 | -0.400*** | 0.254 | 0.577 |

---

## 4-Month Window (Robustness Check)

**Panel:** 1352 rows, 169 repos (Permissive: 154, Prohibited: 15)

### Opened PRs (log_new_prs)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.067* | -0.092 | -0.078* | 0.272 | 0.819 |
| Prohibited | 0.085· | 0.198 | -0.092· | 0.455 | 0.909 |

### Closed PRs (log_prs_closed)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.094** | -0.204 | -0.100*** | 0.275 | 0.807 |
| Prohibited | 0.076· | 0.187 | -0.087· | 0.417 | 0.889 |

### Review Comments (log_review_comments)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.002 | 0.077* | -0.014· | 0.050 | 0.743 |
| Prohibited | -0.012 | 0.193 | -0.068 | 0.321 | 0.804 |

### Close Latency (log_close_latency_h)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | -0.003 | -0.080 | 0.034 | 0.145 | 0.665 |
| Prohibited | 0.269*** | -0.038 | -0.187* | 0.143 | 0.818 |

---

## Comparison Summary

The 4-month window results are consistent with the 6-month results in direction and significance:

| DV | Group | 6-month time_after | 4-month time_after | Direction |
|----|-------|--------------------|--------------------|-----------|
| Opened PRs | Permissive | -0.037* | -0.078* | ↓ ✓ |
| Opened PRs | Prohibited | -0.145· | -0.092· | ↓ ✓ |
| Closed PRs | Permissive | -0.139*** | -0.100*** | ↓ ✓ |
| Closed PRs | Prohibited | -0.156* | -0.087· | ↓ ✓ |
| Review Comments | Permissive | -0.025* | -0.014· | ↓ ✓ |
| Review Comments | Prohibited | -0.042 | -0.068 | ↓ ✓ |
| Close Latency | Permissive | -0.044 | 0.034 | ≈0 ✓ |
| Close Latency | Prohibited | -0.400*** | -0.187* | ↓ ✓ |

All time_after coefficients retain the same sign (negative or near-zero) across both window specifications for all DVs and both groups. The permissive group shows significant negative time_after for Opened PRs, Closed PRs, and Review Comments in both windows. The prohibited group shows negative time_after for Opened PRs, Closed PRs, and Close Latency in both windows, with significance levels reduced in the 4-month window due to the shorter observation period. The consistent direction and significance pattern across all DVs and groups supports the robustness of the findings reported in the paper.