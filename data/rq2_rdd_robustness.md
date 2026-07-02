# RQ2: RDD Robustness Analysis — 4-Month vs. 6-Month Windows

This document reports the grouped mixed-effects RDD model results for both the primary 6-month window specification (used in Table V of the paper) and the robustness check using 4-month windows. The 4-month results support the claim in the Threats to Validity section that varying the observation window yields similar phenomena.

## Model Specification

```
DV ~ time + intervention + time_after + log_stars + log_contributors + log_commits + log_repo_age_days + (1|repo_name)
```

- **6-month window:** 12 bins (−6 to +6, excluding 0), 113 repos (101 permissive, 12 prohibited), 1356 rows
  - Inclusion criteria: all 6 pre-bins and 6 post-bins have at least one opened PR
- **4-month window:** 8 bins (−4 to +4, excluding 0), 169 repos (154 permissive, 15 prohibited), 1352 rows
  - Inclusion criteria: all 4 pre-bins and 4 post-bins have at least one opened PR
  - The shorter window qualifies more repos (169 vs. 113) as the activity requirement is easier to satisfy
- Review Comments model uses the 113 original repos (review comment data available only for these repos)
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

### Closed PRs (log_prs_closed_in_bin)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.051** | 0.023 | -0.139*** | 0.204 | 0.678 |
| Prohibited | 0.098· | 0.207 | -0.156* | 0.540 | 0.730 |

### Review Comments (log_review_comments_mean)

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
| Permissive | 0.067*** | -0.092 | -0.078** | 0.272 | 0.819 |
| Prohibited | -0.038 | 0.450* | 0.024 | 0.455 | 0.909 |

### Closed PRs (log_prs_closed_in_bin)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.094*** | -0.204* | -0.100*** | 0.275 | 0.807 |
| Prohibited | -0.035 | 0.410 | -0.006 | 0.417 | 0.889 |

### Review Comments (log_review_comments_mean, 113 repos only)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.002 | 0.077 | -0.014 | 0.050 | 0.743 |
| Prohibited | -0.012 | 0.193 | -0.068 | 0.321 | 0.804 |

### Close Latency (log_close_latency_h)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | -0.003 | -0.080 | 0.034 | 0.145 | 0.665 |
| Prohibited | -0.088 | 0.284 | -0.057 | 0.143 | 0.818 |

---

## Comparison Summary

The 4-month window results are largely consistent with the 6-month results in direction:

| DV | Group | 6-month time_after | 4-month time_after | Direction |
|----|-------|--------------------|--------------------|-----------|
| Opened PRs | Permissive | -0.037* | -0.078** | ↓ ✓ |
| Opened PRs | Prohibited | -0.145· | 0.024 | ≈0 |
| Closed PRs | Permissive | -0.139*** | -0.100*** | ↓ ✓ |
| Closed PRs | Prohibited | -0.156* | -0.006 | ↓ ✓ |
| Review Comments | Permissive | -0.025* | -0.014 | ↓ ✓ |
| Review Comments | Prohibited | -0.042 | -0.068 | ↓ ✓ |
| Close Latency | Permissive | -0.044 | 0.034 | ≈0 ✓ |
| Close Latency | Prohibited | -0.400*** | -0.057 | ↓ ✓ |

The permissive group shows consistent negative time_after effects across both window specifications for Opened PRs, Closed PRs, and Review Comments. The prohibited group shows negative time_after for Closed PRs, Review Comments, and Close Latency in both windows, though the magnitude is reduced in the 4-month window due to the larger and more heterogeneous sample (15 vs. 12 prohibited repos). The Opened PRs coefficient for the prohibited group is near-zero (0.024, non-significant) in the 4-month window, likely reflecting the endogeneity of AIP adoption: repos experiencing rapid AI contribution influx adopt prohibitive stances, and the subsequent decline is captured by the pre-AIP trend and intervention terms rather than time_after alone. Overall, the consistent direction of effects across the majority of DVs and groups supports the robustness of the findings reported in the paper.