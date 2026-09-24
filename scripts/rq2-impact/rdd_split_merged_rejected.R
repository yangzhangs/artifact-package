#!/usr/bin/env Rscript
# RQ2 split analysis: merged vs closed-without-merge PRs.
# Reads data/panel/split_merged_rejected_panel.csv and re-runs the
# grouped mixed-effects models (same specification as Tables IV and V)
# on log(merged PR count), log(rejected PR count), and their close latencies.

suppressMessages({library(lmerTest); library(lme4); library(performance)})

d <- read.csv("data/panel/split_merged_rejected_panel.csv")
d$time <- as.numeric(d$time)
d$intervention <- as.numeric(d$intervention)
d$time_after <- as.numeric(d$time_after)
d$log_merged <- log(d$merged + 1)
d$log_rejected <- log(d$rejected + 1)
d$log_merged_lat <- log(as.numeric(d$merged_latency_h) + 1)
d$log_rejected_lat <- log(as.numeric(d$rejected_latency_h) + 1)
d$log_stars <- log(as.numeric(d$stars))
d$log_contributors <- log(as.numeric(d$contributors))
d$log_commits <- log(as.numeric(d$commits))
d$log_repo_age_days <- log(as.numeric(d$repo_age_days))

fmt <- function(p) {
  if (p < 0.001) return("***")
  if (p < 0.01) return("**")
  if (p < 0.05) return("*")
  if (p < 0.1) return(".")
  return("")
}

for (dv in c("log_merged", "log_rejected", "log_merged_lat", "log_rejected_lat")) {
  cat(sprintf("== %s ==\n", dv))
  for (g in c("permissive", "prohibited")) {
    sub <- d[d$prohibited == ifelse(g == "prohibited", 1, 0), ]
    sub <- sub[!is.na(sub[[dv]]), ]
    m <- lmer(as.formula(paste(dv,
      "~ time + intervention + time_after + log_stars + log_contributors + log_commits + log_repo_age_days + (1|repo_name)")),
      data = sub, REML = TRUE)
    co <- summary(m)$coefficients
    r2 <- r2_nakagawa(m)
    cat(sprintf("  %-11s n=%d repos=%d | time=%.3f%s int=%.3f%s ta=%.3f%s | R2m=%.3f R2c=%.3f\n",
      g, nrow(sub), length(unique(sub$repo_name)),
      co["time", 1], fmt(co["time", 5]),
      co["intervention", 1], fmt(co["intervention", 5]),
      co["time_after", 1], fmt(co["time_after", 5]),
      r2$R2_marginal, r2$R2_conditional))
  }
}
