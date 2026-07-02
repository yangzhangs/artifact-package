library(lmerTest)
library(car)

full <- read.csv("data/panel/rdd_panel_113.csv")
controls <- "log_stars + log_contributors + log_commits + log_repo_age_days"

DVs <- list(
  "Opened PRs"      = "log_new_prs",
  "Closed PRs"      = "log_prs_closed",
  "Review Comments" = "log_review_comments_mean",
  "Close Latency"   = "log_close_latency_h"
)

cat(sprintf("Panel: %d rows, %d repos\n", nrow(full), length(unique(full$repo_name))))
cat(sprintf("  Permissive: %d, Prohibited: %d\n",
    sum(full[!duplicated(full$repo_name), "prohibited"] == 0),
    sum(full[!duplicated(full$repo_name), "prohibited"] == 1)))

fmt_p <- function(p) {
  if (p < 0.001) return(sprintf("%.4f***", p))
  if (p < 0.01) return(sprintf("%.4f**", p))
  if (p < 0.05) return(sprintf("%.4f*", p))
  if (p < 0.1) return(sprintf("%.4f.", p))
  return(sprintf("%.4f", p))
}

for (dv_name in names(DVs)) {
  dv <- DVs[[dv_name]]
  cat(sprintf("\n========== %s (%s) ==========\n", dv_name, dv))
  for (grp in c("permissive", "prohibited")) {
    grp_val <- if (grp == "prohibited") 1 else 0
    sub <- full[full$prohibited == grp_val, ]
    sub_clean <- sub[!is.na(sub[[dv]]) & sub[[dv]] != "", ]
    sub_clean[[dv]] <- as.numeric(sub_clean[[dv]])
    n_repos <- length(unique(sub_clean$repo_name))

    formula_str <- sprintf("%s ~ time + intervention + time_after + %s + (1|repo_name)", dv, controls)
    model <- lmer(as.formula(formula_str), data = sub_clean, REML = TRUE)
    coefs <- summary(model)$coefficients

    cat(sprintf("  %s (n=%d, repos=%d): time=%.4f(%s) int=%.4f(%s) ta=%.4f(%s)\n",
                grp, nrow(sub_clean), n_repos,
                coefs["time", 1], fmt_p(coefs["time", 5]),
                coefs["intervention", 1], fmt_p(coefs["intervention", 5]),
                coefs["time_after", 1], fmt_p(coefs["time_after", 5])))
  }
}