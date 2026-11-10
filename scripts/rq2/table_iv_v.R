# Tables IV and V: mixed-effects interrupted time-series models of the four outcomes.
# Run from the package root: Rscript scripts/rq2/table_iv_v.R
#
# Specification (Section II.B of the paper):
#   y ~ time + intervention + time_after + stars + contributors + commits + age
#       + (1 | repo_name)
# estimated separately for permissive and prohibited repositories, REML = FALSE.
# Controls are measured at the AIP adoption date; age is measured to 2026-01-01.
# time is the bin index (-6..-1, 1..6), intervention marks post-adoption bins,
# and time_after is the post-adoption slope (delta).

suppressMessages({library(lme4); library(lmerTest)})

panel <- 'data/rq2/panels/main.csv'
out   <- 'data/rq2/results/table_iv_v.csv'

d <- read.csv(panel)
d$language  <- factor(d$language)
d$repo_name <- factor(d$repo_name)
d$prohibited <- as.integer(d$prohibited)

controls <- 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days'

outcomes <- data.frame(
  label = c('Opened PRs', 'Closed PRs', 'Review Comments', 'Time to Resolution'),
  var   = c('log_new_prs', 'log_prs_closed', 'log_review_comments_mean', 'log_close_latency_h'),
  table = c('IV', 'IV', 'V', 'V'),
  stringsAsFactors = FALSE
)

r2 <- function(m) {
  X  <- model.matrix(m); b <- fixef(m); vf <- var(as.vector(X %*% b))
  vc <- as.data.frame(VarCorr(m))
  vr <- sum(vc$vcov[vc$grp != 'Residual']); ve <- attr(VarCorr(m), 'sc')^2
  c(vf / (vf + vr + ve), (vf + vr) / (vf + vr + ve))
}

res <- list()
for (i in seq_len(nrow(outcomes))) {
  for (g in c(0, 1)) {
    s <- subset(d, prohibited == g)
    s <- s[!is.na(s[[outcomes$var[i]]]), ]
    f <- as.formula(paste0(outcomes$var[i], ' ~ time + intervention + time_after + ',
                           controls, ' + (1|repo_name)'))
    m  <- lmer(f, data = s, REML = FALSE)
    co <- summary(m)$coefficients
    fit <- r2(m)
    for (term in c('time', 'intervention', 'time_after')) {
      res[[length(res) + 1]] <- data.frame(
        table = outcomes$table[i], outcome = outcomes$label[i],
        group = ifelse(g == 0, 'Permissive', 'Prohibited'), term = term,
        estimate = co[term, 1], se = co[term, 2], t = co[term, 4], p = co[term, 5],
        n_obs = nrow(s), n_repos = length(unique(s$repo_name)),
        r2m = fit[1], r2c = fit[2], row.names = NULL)
    }
  }
}

res <- do.call(rbind, res)
res$sig <- ifelse(res$p < .001, '***', ifelse(res$p < .01, '**',
               ifelse(res$p < .05, '*', ifelse(res$p < .1, '.', ''))))
dir.create('data/rq2/results', showWarnings = FALSE, recursive = TRUE)
write.csv(res, out, row.names = FALSE)
cat('wrote', out, ':', nrow(res), 'rows\n')
