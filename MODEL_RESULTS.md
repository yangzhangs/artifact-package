# Model results

All terms of every estimated model. Coefficients are shown with significance markers:
*** p < .001, ** p < .01, * p < .05, . p < .1. R2m and R2c are the marginal and
conditional R2. Each column is a separate model estimated on one stance group.

### Tables IV and V: baseline specification

| Term | Opened PRs (Permissive) | Opened PRs (Prohibited) | Closed PRs (Permissive) | Closed PRs (Prohibited) | Review Comments (Permissive) | Review Comments (Prohibited) | Time to Resolution (Permissive) | Time to Resolution (Prohibited) |
|---|---|---|---|---|---|---|---|---|
| Intercept | +1.864* | +3.012 | +2.004* | +3.029 | +0.987. | +0.787 | +3.348*** | +2.513 |
| log(stars) | -0.018 | +0.129 | -0.016 | +0.139 | -0.063* | -0.150 | -0.112* | -0.289* |
| log(contributors) | +0.434*** | +0.153 | +0.420*** | +0.191 | +0.206*** | +0.132 | +0.536*** | +1.209*** |
| log(commits) | +0.331*** | +0.362. | +0.317*** | +0.346. | -0.007 | -0.066 | -0.199* | -0.696** |
| log(repo age) | -0.387** | -0.637 | -0.395*** | -0.630 | -0.075 | +0.166 | +0.211 | +0.622 |
| time (beta) | +0.030* | +0.122* | +0.051** | +0.098. | +0.005 | -0.008 | +0.020 | +0.269*** |
| intervention (gamma) | -0.047 | +0.172 | +0.023 | +0.207 | +0.090* | +0.112 | -0.111 | -0.515 |
| time_after (delta) | -0.037* | -0.145. | -0.139*** | -0.156* | -0.025* | -0.042 | -0.044 | -0.400*** |
| R2m | 0.477 | 0.518 | 0.403 | 0.593 | 0.104 | 0.335 | 0.135 | 0.424 |
| R2c | 0.784 | 0.629 | 0.670 | 0.709 | 0.687 | 0.719 | 0.410 | 0.509 |

### Table VIII: Exclusion band 15

| Term | Opened PRs (Permissive) | Opened PRs (Prohibited) | Closed PRs (Permissive) | Closed PRs (Prohibited) | Review Comments (Permissive) | Review Comments (Prohibited) | Time to Resolution (Permissive) | Time to Resolution (Prohibited) |
|---|---|---|---|---|---|---|---|---|
| Intercept | +1.929* | +3.099 | +1.832* | +2.864 | +0.996. | +0.890 | +3.886*** | +2.666 |
| log(stars) | -0.014 | +0.134 | -0.017 | +0.127 | -0.062* | -0.152 | -0.083. | -0.269. |
| log(contributors) | +0.437*** | +0.123 | +0.441*** | +0.065 | +0.211*** | +0.134 | +0.472*** | +1.203*** |
| log(commits) | +0.321*** | +0.384. | +0.332*** | +0.433* | -0.014 | -0.075 | -0.181* | -0.698** |
| log(repo age) | -0.394*** | -0.674 | -0.397** | -0.659 | -0.075 | +0.164 | +0.121 | +0.611 |
| time (beta) | +0.040** | +0.143* | +0.042** | +0.131* | +0.012 | -0.001 | +0.021 | +0.231*** |
| intervention (gamma) | +0.238 | +1.250. | +0.302. | +1.261. | +0.182* | +0.403. | +0.269 | +1.857* |
| time_after (delta) | -0.046* | -0.164. | -0.054** | -0.155. | -0.022* | -0.048. | -0.053. | -0.336*** |
| R2m | 0.473 | 0.529 | 0.460 | 0.512 | 0.106 | 0.336 | 0.112 | 0.417 |
| R2c | 0.779 | 0.644 | 0.763 | 0.624 | 0.695 | 0.746 | 0.410 | 0.518 |

### Table VIII: Exclusion band 45

| Term | Opened PRs (Permissive) | Opened PRs (Prohibited) | Closed PRs (Permissive) | Closed PRs (Prohibited) | Review Comments (Permissive) | Review Comments (Prohibited) | Time to Resolution (Permissive) | Time to Resolution (Prohibited) |
|---|---|---|---|---|---|---|---|---|
| Intercept | +1.841* | +2.479 | +1.682* | +2.202 | +1.056* | +0.646 | +3.822*** | +3.346 |
| log(stars) | -0.017 | +0.125 | -0.021 | +0.123 | -0.061* | -0.147 | -0.108* | -0.255 |
| log(contributors) | +0.433*** | +0.192 | +0.439*** | +0.144 | +0.204*** | +0.136 | +0.525*** | +1.249*** |
| log(commits) | +0.332*** | +0.326 | +0.348*** | +0.365. | -0.009 | -0.067 | -0.210** | -0.705** |
| log(repo age) | -0.382** | -0.543 | -0.381** | -0.521 | -0.084 | +0.182 | +0.142 | +0.533 |
| time (beta) | +0.022. | +0.145* | +0.022 | +0.137* | +0.002 | -0.000 | +0.041. | +0.142* |
| intervention (gamma) | +0.372* | +1.572* | +0.343* | +1.427. | +0.230** | +0.321 | +0.483. | +1.117 |
| time_after (delta) | -0.047* | -0.199* | -0.045* | -0.179. | -0.018. | -0.043 | -0.087** | -0.222* |
| R2m | 0.470 | 0.477 | 0.460 | 0.461 | 0.099 | 0.341 | 0.126 | 0.457 |
| R2c | 0.773 | 0.568 | 0.762 | 0.550 | 0.668 | 0.713 | 0.413 | 0.597 |

### Table VIII: Exclusion band 60

| Term | Opened PRs (Permissive) | Opened PRs (Prohibited) | Closed PRs (Permissive) | Closed PRs (Prohibited) | Review Comments (Permissive) | Review Comments (Prohibited) | Time to Resolution (Permissive) | Time to Resolution (Prohibited) |
|---|---|---|---|---|---|---|---|---|
| Intercept | +1.648* | +2.166 | +1.415. | +1.890 | +1.099* | +0.531 | +4.029*** | +3.543 |
| log(stars) | -0.016 | +0.117 | -0.016 | +0.118 | -0.064* | -0.135 | -0.092. | -0.281. |
| log(contributors) | +0.438*** | +0.194 | +0.439*** | +0.156 | +0.208*** | +0.124 | +0.506*** | +1.233*** |
| log(commits) | +0.332*** | +0.329. | +0.344*** | +0.358. | -0.012 | -0.067 | -0.212** | -0.703** |
| log(repo age) | -0.363** | -0.508 | -0.349** | -0.487 | -0.088 | +0.198 | +0.118 | +0.554 |
| time (beta) | +0.027. | +0.163* | +0.030* | +0.163* | +0.008 | -0.002 | +0.020 | +0.105. |
| intervention (gamma) | +0.703*** | +1.949* | +0.606*** | +1.657* | +0.444*** | +0.273 | +0.497. | +1.017 |
| time_after (delta) | -0.085*** | -0.247* | -0.077*** | -0.218* | -0.046*** | -0.041 | -0.077* | -0.186* |
| R2m | 0.445 | 0.468 | 0.445 | 0.457 | 0.107 | 0.347 | 0.116 | 0.465 |
| R2c | 0.729 | 0.552 | 0.739 | 0.539 | 0.673 | 0.715 | 0.384 | 0.606 |

### Table VIII: Window 5 bins

| Term | Opened PRs (Permissive) | Opened PRs (Prohibited) | Closed PRs (Permissive) | Closed PRs (Prohibited) | Review Comments (Permissive) | Review Comments (Prohibited) | Time to Resolution (Permissive) | Time to Resolution (Prohibited) |
|---|---|---|---|---|---|---|---|---|
| Intercept | +4.117** | +9.118 | +4.040** | +9.564 | +0.088 | +2.221 | +2.992** | -2.084 |
| log(stars) | +0.078 | -0.021 | +0.074 | -0.061 | -0.001 | -0.193. | -0.037 | +0.115 |
| log(contributors) | +0.096 | -0.479 | +0.096 | -0.570 | +0.107 | +0.144 | +0.412*** | +1.311** |
| log(commits) | +0.263** | +0.861. | +0.271** | +0.934. | -0.021 | -0.081 | -0.240** | -0.897* |
| log(repo age) | -0.481** | -1.557. | -0.479** | -1.622. | +0.059 | -0.023 | +0.321* | +1.261. |
| time (beta) | +0.043** | +0.047 | +0.043** | +0.052 | +0.006 | -0.042. | +0.009 | +0.113. |
| intervention (gamma) | -0.067 | +0.358 | -0.114 | +0.463. | +0.062. | +0.206. | +0.043 | -0.470 |
| time_after (delta) | -0.054* | -0.077 | -0.045. | -0.131 | -0.022* | -0.015 | -0.082* | -0.145 |
| R2m | 0.200 | 0.421 | 0.189 | 0.375 | 0.037 | 0.368 | 0.081 | 0.384 |
| R2c | 0.793 | 0.833 | 0.782 | 0.808 | 0.784 | 0.777 | 0.384 | 0.678 |

### Table VIII: Window 4 bins

| Term | Opened PRs (Permissive) | Opened PRs (Prohibited) | Closed PRs (Permissive) | Closed PRs (Prohibited) | Review Comments (Permissive) | Review Comments (Prohibited) | Time to Resolution (Permissive) | Time to Resolution (Prohibited) |
|---|---|---|---|---|---|---|---|---|
| Intercept | +1.943* | +9.780. | +1.919* | +10.124. | -0.418 | +4.344. | +2.974*** | +7.119 |
| log(stars) | +0.110* | -0.036 | +0.105* | -0.048 | -0.026 | -0.272** | -0.071 | -0.175 |
| log(contributors) | +0.111 | -0.559 | +0.102 | -0.578 | +0.150* | +0.114 | +0.540*** | +0.917 |
| log(commits) | +0.349*** | +0.960* | +0.361*** | +0.964* | -0.038 | +0.035 | -0.329*** | -0.234 |
| log(repo age) | -0.293* | -1.736* | -0.296* | -1.767* | +0.133. | -0.390 | +0.390** | -0.497 |
| time (beta) | +0.065** | -0.031 | +0.062** | -0.028 | +0.001 | -0.009 | +0.023 | -0.028 |
| intervention (gamma) | -0.101 | +0.439. | -0.086 | +0.472* | +0.055 | +0.154 | -0.042 | -0.116 |
| time_after (delta) | -0.074* | +0.016 | -0.091** | -0.019 | -0.011 | -0.054 | -0.094. | -0.021 |
| R2m | 0.276 | 0.535 | 0.268 | 0.506 | 0.065 | 0.372 | 0.136 | 0.244 |
| R2c | 0.810 | 0.896 | 0.802 | 0.893 | 0.852 | 0.835 | 0.463 | 0.728 |

## Merged versus rejected split (Section IV.A)

| Term | Merged PRs (Permissive) | Merged PRs (Prohibited) | Rejected PRs (Permissive) | Rejected PRs (Prohibited) |
|---|---|---|---|---|
| Intercept | +2.375. | +2.546* | +3.751 | -3.842 |
| log(stars) | +0.048 | +0.031 | +0.077 | +0.218 |
| log(contributors) | +0.122 | +0.380*** | -0.222 | +0.794 |
| log(commits) | +0.331** | +0.027 | +0.692** | -0.018 |
| log(repo age) | -0.356. | -0.429* | -0.875* | +0.065 |
| time (beta) | +0.042** | +0.071*** | +0.091* | +0.099. |
| intervention (gamma) | -0.079 | -0.228** | +0.211 | -0.020 |
| time_after (delta) | -0.069*** | -0.033 | -0.158* | -0.020 |
| R2m | 0.238 | 0.632 | 0.238 | 0.549 |
| R2c | 0.757 | 0.730 | 0.685 | 0.770 |

