library(lmerTest)
library(car)

full <- read.csv("data/panel/rdd_panel_113.csv")
controls <- "log_stars + log_contributors + log_commits + log_repo_age_days + log_aip_latency_days"
DVs <- c("log_new_prs", "log_review_comments_mean", "log_total_closed", "log_close_latency_h")

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

cat("\n========== 113 repos: ALL repos (no per-DV screening) ==========\n")
for (dv in DVs) {
  cat(sprintf("\n--- %s ---\n", dv))
  for (grp in c("permissive", "prohibited")) {
    grp_val <- if(grp=="prohibited") 1 else 0
    sub <- full[full$prohibited == grp_val, ]
    sub_clean <- sub[!is.na(sub[[dv]]), ]
    n_repos <- length(unique(sub_clean$repo_name))
    
    formula_str <- sprintf("%s ~ time + intervention + time_after + %s + (1|repo_name)", dv, controls)
    model <- lmer(as.formula(formula_str), data=sub_clean, REML=TRUE)
    coefs <- summary(model)$coefficients
    
    cat(sprintf("  %s (n=%d, repos=%d): time=%.4f(%s) int=%.4f(%s) ta=%.4f(%s)\n",
                grp, nrow(sub_clean), n_repos,
                coefs["time",1], fmt_p(coefs["time",5]),
                coefs["intervention",1], fmt_p(coefs["intervention",5]),
                coefs["time_after",1], fmt_p(coefs["time_after",5])))
  }
}

cat("\n\n========== 113 repos: Per-DV screening ==========\n")
for (dv in DVs) {
  cat(sprintf("\n--- %s ---\n", dv))
  for (grp in c("permissive", "prohibited")) {
    grp_val <- if(grp=="prohibited") 1 else 0
    sub <- full[full$prohibited == grp_val, ]
    sub_clean <- sub[!is.na(sub[[dv]]), ]
    repo_bins <- tapply(sub_clean$bin, sub_clean$repo_name, function(x) length(unique(x)))
    complete_repos <- names(repo_bins[repo_bins == 12])
    sub_final <- sub_clean[sub_clean$repo_name %in% complete_repos, ]
    n_repos <- length(unique(sub_final$repo_name))
    
    formula_str <- sprintf("%s ~ time + intervention + time_after + %s + (1|repo_name)", dv, controls)
    model <- lmer(as.formula(formula_str), data=sub_final, REML=TRUE)
    coefs <- summary(model)$coefficients
    
    cat(sprintf("  %s (n=%d, repos=%d): time=%.4f(%s) int=%.4f(%s) ta=%.4f(%s)\n",
                grp, nrow(sub_final), n_repos,
                coefs["time",1], fmt_p(coefs["time",5]),
                coefs["intervention",1], fmt_p(coefs["intervention",5]),
                coefs["time_after",1], fmt_p(coefs["time_after",5])))
  }
}