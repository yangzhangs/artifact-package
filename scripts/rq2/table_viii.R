# Table VIII: post-adoption slope (delta) across alternative specifications.
# Run from the package root: Rscript scripts/rq2/table_viii.R
#
# Each configuration is a bin-level panel built with the same outcome definitions
# and controls as the main analysis but a different exclusion band (B) or a
# different number of bins per side. This script fits every configuration that is
# present in data/rq2/panels/ and writes the post-adoption slopes to
# data/rq2/results/table_viii.csv.
#
# Shipped panels (all six configurations):
#   main.csv              B = 30 days, 6 bins per side (Baseline)
#   exclusion_band15.csv  B = 15 days
#   exclusion_band45.csv  B = 45 days
#   exclusion_band60.csv  B = 60 days
#   window5.csv          5 bins per side
#   window4.csv          4 bins per side

suppressMessages({library(lme4); library(lmerTest)})

configs <- list(
  Baseline = list(panel = 'data/rq2/panels/main.csv',
                  ctrl  = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
                  vars  = c('log_new_prs', 'log_prs_closed', 'log_review_comments_mean', 'log_close_latency_h')),
  B15 = list(panel = 'data/rq2/panels/exclusion_band15.csv',
             ctrl  = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
             vars  = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  B45 = list(panel = 'data/rq2/panels/exclusion_band45.csv',
             ctrl  = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
             vars  = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  B60 = list(panel = 'data/rq2/panels/exclusion_band60.csv',
             ctrl  = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
             vars  = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  W5  = list(panel = 'data/rq2/panels/window5.csv',
             ctrl  = 'log_stars + log_contributors + log_commits + log_age',
             vars  = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  W4  = list(panel = 'data/rq2/panels/window4.csv',
             ctrl  = 'log_stars + log_contributors + log_commits + log_repo_age_days',
             vars  = c('log_new_prs', 'log_total_closed', 'log_review_comments_mean', 'log_close_latency_h'))
)
labels <- c('Opened PRs', 'Closed PRs', 'Review Comments', 'Time to Resolution')


fit_delta <- function(path, dv, g, controls) {
  d <- read.csv(path)
  d$language <- factor(d$language); d$repo_name <- factor(d$repo_name)
  s <- subset(d, prohibited == g); s <- s[!is.na(s[[dv]]), ]
  m <- lmer(as.formula(paste0(dv, ' ~ time + intervention + time_after + ', controls,
                              ' + (1|repo_name)')), data = s, REML = FALSE)
  co <- summary(m)$coefficients
  X <- model.matrix(m); b <- fixef(m); vf <- var(as.vector(X %*% b))
  vc <- as.data.frame(VarCorr(m)); vr <- sum(vc$vcov[vc$grp != 'Residual'])
  ve <- attr(VarCorr(m), 'sc')^2
  data.frame(term = rownames(co),
             estimate = co[, 1], se = co[, 2], p = co[, 5],
             r2m = vf / (vf + vr + ve), r2c = (vf + vr) / (vf + vr + ve))
}

res <- list()
for (nm in names(configs)) {
  path <- configs[[nm]]$panel
  if (!file.exists(path)) next
  for (j in seq_along(labels)) {
    for (g in c(0, 1)) {
      v <- fit_delta(path, configs[[nm]]$vars[j], g, configs[[nm]]$ctrl)
      res[[length(res) + 1]] <- data.frame(
        spec = nm, outcome = labels[j],
        group = ifelse(g == 0, 'Permissive', 'Prohibited'),
        v, row.names = NULL)
    }
  }
}
res <- do.call(rbind, res)
res$sig <- ifelse(res$p < .001, '***', ifelse(res$p < .01, '**',
               ifelse(res$p < .05, '*', ifelse(res$p < .1, '.', ''))))
dir.create('data/rq2/results', showWarnings = FALSE, recursive = TRUE)
write.csv(res, 'data/rq2/results/table_viii.csv', row.names = FALSE)
print(res[res$term == 'time_after', c('spec', 'outcome', 'group', 'estimate', 'p')], row.names = FALSE)
cat('wrote data/rq2/results/table_viii.csv\n')
