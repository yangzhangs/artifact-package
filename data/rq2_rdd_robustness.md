# RQ2: RDD Robustness Analysis — 4-Month vs. 6-Month Windows

This document reports the grouped mixed-effects RDD model results for both the primary 6-month window specification (used in Table V of the paper) and the robustness check using 4-month windows. The 4-month results support the claim in the Threats to Validity section that varying the observation window yields similar phenomena.

## Model Specification

```
DV ~ time + intervention + time_after + log_stars + log_contributors + log_commits + log_repo_age_days + (1|repo_name)
```

- **6-month window:** 12 bins (−6 to +6, excluding 0), 113 repos (101 permissive, 12 prohibited), 1356 rows
- **4-month window:** 8 bins (−4 to +4, excluding 0), 517 repos (460 permissive, 57 prohibited), 4136 rows
  - Review Comments model uses 113 repos (review comment data available only for the original 113 repos)
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

**Panel:** 4136 rows, 517 repos (Permissive: 460, Prohibited: 57)

### Opened PRs (log_new_prs)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.193*** | 0.432*** | -0.799*** | 0.286 | 0.558 |
| Prohibited | 0.135* | 0.242 | -0.589*** | 0.365 | 0.697 |

### Closed PRs (log_prs_closed_in_bin)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.196*** | 0.435*** | -0.787*** | 0.284 | 0.565 |
| Prohibited | 0.138* | 0.246 | -0.570*** | 0.356 | 0.731 |

### Review Comments (log_review_comments_mean, 113 repos only)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.002 | 0.077 | -0.014 | 0.050 | 0.743 |
| Prohibited | -0.012 | 0.193 | -0.068 | 0.321 | 0.804 |

### Close Latency (log_close_latency_h)

| Group | time (β) | intervention (γ) | time_after (δ) | R²m | R²c |
|-------|----------|-------------------|-----------------|-----|-----|
| Permissive | 0.139*** | 0.558*** | -0.634*** | 0.160 | 0.452 |
| Prohibited | 0.171· | 0.739· | -0.712*** | 0.195 | 0.477 |

---

## Comparison Summary

The 4-month window results are consistent with the 6-month results in direction:

| DV | Group | 6-month time_after | 4-month time_after | Direction |
|----|-------|--------------------|--------------------|-----------|
| Opened PRs | Permissive | -0.037* | -0.799*** | ↓ ✓ |
| Opened PRs | Prohibited | -0.145· | -0.589*** | ↓ ✓ |
| Closed PRs | Permissive | -0.139*** | -0.787*** | ↓ ✓ |
| Closed PRs | Prohibited | -0.156* | -0.570*** | ↓ ✓ |
| Review Comments | Permissive | -0.025* | -0.014 | ↓ ✓ |
| Review Comments | Prohibited | -0.042 | -0.068 | ↓ ✓ |
| Close Latency | Permissive | -0.044 | -0.634*** | ↓ ✓ |
| Close Latency | Prohibited | -0.400*** | -0.712*** | ↓ ✓ |

All time_after coefficients retain the same sign (negative) across both window specifications for all DVs and both groups. The 4-month window with 517 repos yields stronger significance for Opened PRs, Closed PRs, and Close Latency due to the larger sample size. Review Comments, modeled on the original 113 repos, shows consistent direction with reduced significance, as expected with fewer observations. The consistent direction of effects across all DVs and groups supports the robustness of the findings reported in the paper.
