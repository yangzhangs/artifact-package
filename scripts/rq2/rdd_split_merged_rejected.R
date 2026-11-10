#!/usr/bin/env Rscript
# RQ2 split analysis: merged vs closed-without-merge PR counts.
# Reads data/rq2/panels/split_merged_rejected.csv and re-runs the
# grouped mixed-effects models (same specification as Tables IV and V)
# on log(merged PR count) and log(rejected PR count).

suppressMessages({library(lmerTest); library(lme4)})

d <- read.csv("data/rq2/panels/split_merged_rejected.csv")
d$time <- as.numeric(d$time)
d$intervention <- as.numeric(d$intervention)
d$time_after <- as.numeric(d$time_after)
d$log_merged <- log(d$merged + 1)
d$log_rejected <- log(d$rejected + 1)
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

res <- list()
for (dv in c("log_merged", "log_rejected")) {
  cat(sprintf("== %s ==\n", dv))
  for (g in c("permissive", "prohibited")) {
    sub <- d[d$prohibited == ifelse(g == "prohibited", 1, 0), ]
    sub <- sub[!is.na(sub[[dv]]), ]
    m <- lmer(as.formula(paste(dv,
      "~ time + intervention + time_after + log_stars + log_contributors + log_commits + log_repo_age_days + (1|repo_name)")),
      data = sub, REML = FALSE)
    co <- summary(m)$coefficients
    X <- model.matrix(m); b <- fixef(m); vf <- var(as.vector(X %*% b))
    vc <- as.data.frame(VarCorr(m)); vr <- sum(vc$vcov[vc$grp != 'Residual'])
    ve <- attr(VarCorr(m), 'sc')^2
    r2 <- list(R2_marginal = vf / (vf + vr + ve), R2_conditional = (vf + vr) / (vf + vr + ve))
    cat(sprintf("  %-11s n=%d repos=%d | time=%.3f%s int=%.3f%s ta=%.3f%s | R2m=%.3f R2c=%.3f\n",
      g, nrow(sub), length(unique(sub$repo_name)),
      co["time", 1], fmt(co["time", 5]),
      co["intervention", 1], fmt(co["intervention", 5]),
      co["time_after", 1], fmt(co["time_after", 5]),
      r2$R2_marginal, r2$R2_conditional))
    for (tm in rownames(co)) {
      res[[length(res) + 1]] <- data.frame(
        outcome = sub("^log_", "", dv), group = g, term = tm,
        estimate = co[tm, 1], se = co[tm, 2], p = co[tm, 5],
        r2m = r2$R2_marginal, r2c = r2$R2_conditional, row.names = NULL)
    }
  }
}
res <- do.call(rbind, res)
dir.create("data/rq2/results", showWarnings = FALSE, recursive = TRUE)
write.csv(res, "data/rq2/results/split_merged_rejected_coefficients.csv", row.names = FALSE)
cat("wrote data/rq2/results/split_merged_rejected_coefficients.csv\n")
