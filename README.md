# Artifact for AIP Study

## Overview

This artifact package supports the replication of a mixed-methods empirical study investigating **AI Policies (AIPs)** in open source software (OSS) contribution guidelines. The study combines content analysis of 615 AIPs from GitHub repositories, Regression Discontinuity Design (RDD) analysis of 113 active repositories, and surveys of 68 maintainers and 59 contributors.

---

## Directory Structure

```
artifact-package/
├── README.md                          # This file
├── data/
│   ├── repos/
│   │   ├── repos_sampled_57331.csv        # Initial SEART-GHS sample (57,331 repos)
│   │   ├── repos_with_contributing_18902.csv # Repos with CONTRIBUTING.md (18,902 repos)
│   │   ├── confirmed_repos_615.csv        # Confirmed AIP repos (615 repos)
│   │   ├── aip_first_date_final.csv       # AIP introduction dates per repo
│   │   └── repo_created_dates.csv         # Repo creation dates
│   ├── panel/
│   │   └── rdd_panel_113.csv              # Main RDD panel (113 repos × 12 bins)
│   └── aip/
│       ├── aip_keyword_patterns.txt       # Two-layer keyword patterns (40 + 48)
│       ├── ai_pr_detection_per_repo.csv   # AI-PR detection results per repo
│       └── ai_pr_detection_refined_matches.csv # Refined AI-PR matches
├── scripts/
│   ├── rq1-design/                        # RQ1: Design of AIPs
│   │   ├── keyword_screening.py          # Two-layer keyword screening
│   │   ├── extract_aip_content.py         # Extract AIP text from CONTRIBUTING.md
│   │   └── plot_stance_distribution.py    # Stance distribution donut chart
│   ├── rq2-impact/                       # RQ2: Associations with Contribution Dynamics
│   │   ├── rdd_grouped_lmer.R            # Grouped mixed-effects RDD models (Table V)
│   │   └── plot_rdd_trends.py            # Fig 4/5: RDD trend plots
│   ├── rq3-enforcement/                  # RQ3: Enforcement of AIP
│   │   ├── plot_compliance.py            # Compliance perception chart
│   │   └── plot_contributor_attitude.py   # Contributor attitude bar chart
│   └── shared/                           # Shared utilities
│       └── detect_aip_first_date.py       # Detect AIP first appearance date
├── survey/
│   ├── maintainer_survey.md               # Complete maintainer survey
│   └── contributor_survey.md             # Complete contributor survey
└── figures/
    ├── overview.pdf                        # Methodology overview
    ├── ai-policy-example-1.pdf             # Example AIP from CONTRIBUTING.md
    ├── fig_stance_distribution.pdf         # Stance distribution (permissive vs. prohibited)
    ├── fig4_rdd_trend_left.pdf             # RQ2: Opened PRs + Closed PRs trends
    ├── fig4_rdd_trend_right.pdf            # RQ2: Review Comments + Close Latency trends
    ├── fig_compliance_likert.pdf           # RQ3: Compliance perception
    └── fig_contributor_attitude.pdf        # RQ3: Contributor attitudes
```

---

## Data Description

### `data/repos/repos_sampled_57331.csv`
Initial repository sample from SEART-GHS with inclusion criteria: ≥10 stars/forks, ≥100 commits, ≥10 issues/PRs, not a fork, created between 2021-01-01 and 2025-12-31. Contains 57,331 repositories with metadata (stars, forks, contributors, commits, language, etc.).

### `data/repos/repos_with_contributing_18902.csv`
Subset of the initial sample that contain a CONTRIBUTING.md file (searched at root, `.github/`, and `docs/` paths). Contains 18,902 repositories with contributing guideline file paths and SHA hashes.

### `data/repos/confirmed_repos_615.csv`
Repositories confirmed through two-layer keyword screening and manual verification to contain genuine AIPs. Contains 615 repositories with stance labels (permissive/prohibited), policy first dates, language, and other metadata.

**Key columns:** `repo_name`, `cat1` (permissive/prohibited), `stance`, `policy_first_date`, `language`, `total_prs_db`, `group`

### `data/repos/aip_first_date_final.csv`
Verified AIP introduction dates for each confirmed repository, determined by scanning the git history of CONTRIBUTING.md files with keyword matching and manual verification.

### `data/panel/rdd_panel_113.csv`
Main RDD panel data for 113 active repositories (101 permissive, 12 prohibited). Each row represents a 30-day time window (bin) relative to the AIP introduction date, spanning 6 bins before and 6 bins after (excluding the transition window, bin 0).

**Key columns:**
- `repo_name`, `bin` (−6 to +6, excluding 0)
- `new_prs` — opened PRs per bin (by creation time)
- `prs_closed_in_bin` — closed PRs per bin (by close time)
- `review_comments_mean`, `close_latency_h` — review engagement and processing efficiency
- `prohibited` (0=permissive, 1=prohibited), `language`, `stars`, `contributors`, `commits`, `repo_age_days` — controls
- `time`, `intervention`, `time_after` — RDD model variables
- `log_*` — log-transformed versions of each variable

### `data/aip/aip_keyword_patterns.txt`
The complete two-layer keyword pattern set used for AIP screening: 40 AI-content patterns (Layer 1) and 48 AI-policy patterns (Layer 2). A repository is flagged as a candidate only when at least one pattern from each layer matches.

### `data/aip/ai_pr_detection_per_repo.csv`
Results of AI-PR detection across 113 repositories using keyword matching on PR titles and labels, used for robustness analysis.

### `data/aip/ai_pr_detection_refined_matches.csv`
Refined AI-PR detection matches after manual filtering of false positives.

---

## Survey Instruments

### `survey/maintainer_survey.md`
Complete survey instrument for maintainers, including:
- **Demographics** (D1–D6): experience, role, project count, language, age, occupation
- **AI Tool Usage** (B1–B5): frequency, purposes, quality perception, AI-PR trends
- **AIP Status** (MQ1–MQ11): stance, rationale (allow/prohibit), conditions, observed changes, compliance, enforcement methods, enforcement difficulties, open-ended comments

### `survey/contributor_survey.md`
Complete survey instrument for contributors, including:
- **Demographics** (D1–D6): same as maintainer survey
- **AI Tool Usage** (CQ1): disclosure behavior
- **AIP Awareness & Reactions** (CQ2–CQ8): awareness, perceived stance, initial reaction, support/opposition reasons, behavioral change, open-ended comments

---

## Software Requirements

- **Python 3.9+** with packages: `pandas`, `numpy`, `matplotlib`, `scipy`, `pymysql` (for database access)
- **R 4.0+** with packages: `lmerTest`, `lme4`, `car`, `performance`

---

## Reproduction Steps

### RQ1: Design of AIPs

1. **Repository Sampling** — The initial 57,331 repositories were obtained from SEART-GHS using the criteria in the paper. See `data/repos/repos_sampled_57331.csv`.

2. **Contributing Guideline Detection** — Filter to repositories containing CONTRIBUTING.md files. See `data/repos/repos_with_contributing_18902.csv`.

3. **Keyword Screening** — Run two-layer keyword screening:
   ```bash
   python scripts/rq1-design/keyword_screening.py \
     --dl-dir <path_to_downloaded_contributing_files> \
     --export --output screening_results.csv
   ```
   This identifies 1,114 candidate repositories.

4. **Manual Verification** — Manually review each candidate's CONTRIBUTING.md to confirm genuine AIPs, yielding 615 confirmed repositories. Results in `data/repos/confirmed_repos_615.csv`.

5. **AIP Content Extraction**:
   ```bash
   python scripts/rq1-design/extract_aip_content.py \
     --repo-list data/repos/confirmed_repos_615.csv \
     --contributing-dir <path_to_downloaded_files> \
     --output aip_content_extracted.csv
   ```

6. **Stance Distribution Figure**:
   ```bash
   python scripts/rq1-design/plot_stance_distribution.py
   ```

### RQ2: Associations with Contribution Dynamics

1. **AIP Date Detection** — Detect AIP first appearance dates from git history:
   ```bash
   python scripts/shared/detect_aip_first_date.py
   ```
   Results in `data/repos/aip_first_date_final.csv` (after manual verification).

2. **Regression Analysis** — Run grouped mixed-effects models:
   ```R
   Rscript scripts/rq2-impact/rdd_grouped_lmer.R
   ```
   This produces the results in Table V: separate models for permissive and prohibited groups across 4 DVs (Opened PRs, Closed PRs, Review Comments, Close Latency). The panel data is in `data/panel/rdd_panel_113.csv`.

3. **Trend Plots**:
   ```bash
   python scripts/rq2-impact/plot_rdd_trends.py
   ```
   Generates Fig 4 (contribution volume) and Fig 5 (review cost) trend plots.

### RQ3: Enforcement Perceptions

1. **Survey Administration** — The survey instruments are in `survey/`. Maintainers were recruited from the 615 confirmed repositories; contributors were recruited from PR author data. Surveys were administered via Google Forms.

2. **Result Visualization**:
   ```bash
   python scripts/rq3-enforcement/plot_compliance.py
   python scripts/rq3-enforcement/plot_contributor_attitude.py
   ```

---

## Notes

- All repository names in the datasets are public GitHub repository identifiers (format: `owner/repo`). No personally identifiable information (PII) is included.
- Survey respondent data (emails, names, responses) are not included to protect participant privacy.
- Database credentials have been removed from all scripts; set them via environment variables when running scripts that require database access.