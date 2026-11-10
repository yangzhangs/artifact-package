# Generate MODEL_RESULTS.md: full coefficient tables for every model.
# Run from the package root: Rscript scripts/rq2/model_results.R
#
# Layout follows Tables IV and V: one row per term, one column per outcome and
# stance, with R2m and R2c at the bottom of each block.

suppressMessages({library(lme4); library(lmerTest)})

root <- '.'
out_file <- file.path(root, 'MODEL_RESULTS.md')

base <- function(p) file.path(root, 'data/rq2/panels', p)

configs <- list(
  Baseline        = list(panel = base('main.csv'),
                         ctrl = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
                         vars = c('log_new_prs', 'log_prs_closed', 'log_review_comments_mean', 'log_close_latency_h')),
  `Exclusion band 15` = list(panel = base('exclusion_band15.csv'),
                         ctrl = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
                         vars = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  `Exclusion band 45` = list(panel = base('exclusion_band45.csv'),
                         ctrl = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
                         vars = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  `Exclusion band 60` = list(panel = base('exclusion_band60.csv'),
                         ctrl = 'log_stars_at_adoption + log_pre_authors + log_pre_commits + log_pre_repo_age_days',
                         vars = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  `Window 5 bins`  = list(panel = base('window5.csv'),
                         ctrl = 'log_stars + log_contributors + log_commits + log_age',
                         vars = c('log_opened', 'log_closed', 'log_comments', 'log_res')),
  `Window 4 bins`  = list(panel = base('window4.csv'),
                         ctrl = 'log_stars + log_contributors + log_commits + log_repo_age_days',
                         vars = c('log_new_prs', 'log_total_closed', 'log_review_comments_mean', 'log_close_latency_h'))
)

labels <- c('Opened PRs', 'Closed PRs', 'Review Comments', 'Time to Resolution')
ctrl_labels <- c('(Intercept)' = 'Intercept', 'time' = 'time (beta)', 'intervention' = 'intervention (gamma)',
                 'time_after' = 'time_after (delta)')

r2 <- function(m) {
  X <- model.matrix(m); b <- fixef(m); vf <- var(as.vector(X %*% b))
  vc <- as.data.frame(VarCorr(m)); vr <- sum(vc$vcov[vc$grp != 'Residual'])
  ve <- attr(VarCorr(m), 'sc')^2
  c(vf / (vf + vr + ve), (vf + vr) / (vf + vr + ve))
}

stars <- function(p) ifelse(p < .001, '***', ifelse(p < .01, '**', ifelse(p < .05, '*', ifelse(p < .1, '.', ''))))

fmt <- function(est, p) sprintf('%+.3f%s', est, stars(p))

fit_block <- function(panel, ctrl, vars, label) {
  d <- read.csv(panel)
  d$repo_name <- factor(d$repo_name)
  row_labels <- c('(Intercept)', 'time', 'intervention', 'time_after')
  disp <- c('Intercept', 'time (beta)', 'intervention (gamma)', 'time_after (delta)')
  # collect coefficients per column (outcome-major, then stance)
  coefs <- list(); r2m <- numeric(0); r2c <- numeric(0)
  for (i in seq_along(vars)) {
    for (g in c(0, 1)) {
      s <- subset(d, prohibited == g); s <- s[!is.na(s[[vars[i]]]), ]
      m <- lmer(as.formula(paste0(vars[i], ' ~ time + intervention + time_after + ', ctrl,
                                  ' + (1|repo_name)')), data = s, REML = FALSE)
      co <- summary(m)$coefficients
      ctrl_terms <- setdiff(rownames(co), c('(Intercept)', 'time', 'intervention', 'time_after'))
      coefs[[length(coefs) + 1]] <- list(co = co, ctrl = ctrl_terms)
      fit <- r2(m); r2m <- c(r2m, fit[1]); r2c <- c(r2c, fit[2])
    }
  }
  cn <- c()
  for (i in seq_along(vars)) cn <- c(cn, paste0(labels[i], ' (Permissive)'), paste0(labels[i], ' (Prohibited)'))
  # control labels by position
  ctrl_names <- c('log(stars)', 'log(contributors)', 'log(commits)', 'log(repo age)')
  hdr <- paste0('| Term | ', paste(cn, collapse = ' | '), ' |')
  sep <- paste0('|', paste(rep('---', length(cn) + 1), collapse = '|'), '|')
  rows <- c()
  # first block: intercept + controls (control sets are identical across models)
  ctrl_order <- coefs[[1]]$ctrl
  term_labels <- c('Intercept', ctrl_names[seq_along(ctrl_order)], 'time (beta)', 'intervention (gamma)', 'time_after (delta)')
  term_keys <- c('(Intercept)', ctrl_order, 'time', 'intervention', 'time_after')
  for (k in seq_along(term_keys)) {
    vals <- c()
    for (j in seq_along(coefs)) {
      co <- coefs[[j]]$co
      key <- term_keys[k]
      if (k > 1 && k <= 1 + length(ctrl_order)) key <- coefs[[j]]$ctrl[k - 1]
      vals <- c(vals, fmt(co[key, 1], co[key, 5]))
    }
    rows <- c(rows, paste0('| ', term_labels[k], ' | ', paste(vals, collapse = ' | '), ' |'))
  }
  # R2 in column order
  r2m_ord <- as.vector(rbind(r2m[seq(1, 8, by = 2)], r2m[seq(2, 8, by = 2)]))
  r2c_ord <- as.vector(rbind(r2c[seq(1, 8, by = 2)], r2c[seq(2, 8, by = 2)]))
  rows <- c(rows,
            paste0('| R2m | ', paste(sprintf('%.3f', r2m_ord), collapse = ' | '), ' |'),
            paste0('| R2c | ', paste(sprintf('%.3f', r2c_ord), collapse = ' | '), ' |'))
  c(paste0('### ', label), '', hdr, sep, rows, '')
}

md <- c('# Model results', '',
        'All terms of every estimated model. Coefficients are shown with significance markers:',
        '*** p < .001, ** p < .01, * p < .05, . p < .1. R2m and R2c are the marginal and',
        'conditional R2. Each column is a separate model estimated on one stance group.', '')

md <- c(md, fit_block(configs$Baseline$panel, configs$Baseline$ctrl, configs$Baseline$vars,
                      'Tables IV and V: baseline specification'))
for (nm in names(configs)[-1]) {
  md <- c(md, fit_block(configs[[nm]]$panel, configs[[nm]]$ctrl, configs[[nm]]$vars,
                        paste0('Table VIII: ', nm)))
}

# split models
d <- read.csv(base('split_merged_rejected.csv')); d$repo_name <- factor(d$repo_name)
d$log_merged <- log1p(d$merged); d$log_rejected <- log1p(d$rejected)
d$log_stars <- log(as.numeric(d$stars)); d$log_contributors <- log(as.numeric(d$contributors))
d$log_commits <- log(as.numeric(d$commits)); d$log_repo_age_days <- log(as.numeric(d$repo_age_days))
res <- list(); r2m <- numeric(0); r2c <- numeric(0)
for (g in c(0, 1)) for (dv in c('log_merged', 'log_rejected')) {
  s <- subset(d, prohibited == g)
  m <- lmer(as.formula(paste0(dv, ' ~ time + intervention + time_after + log_stars + log_contributors + log_commits + log_repo_age_days + (1|repo_name)')), data = s, REML = FALSE)
  res[[length(res) + 1]] <- summary(m)$coefficients
  fit <- r2(m); r2m <- c(r2m, fit[1]); r2c <- c(r2c, fit[2])
}
cn <- c('Merged PRs (Permissive)', 'Merged PRs (Prohibited)', 'Rejected PRs (Permissive)', 'Rejected PRs (Prohibited)')
hdr <- paste0('| Term | ', paste(cn, collapse = ' | '), ' |')
sep <- paste0('|', paste(rep('---', 5), collapse = '|'), '|')
term_keys <- c('(Intercept)', 'log_stars', 'log_contributors', 'log_commits', 'log_repo_age_days', 'time', 'intervention', 'time_after')
term_lab  <- c('Intercept', 'log(stars)', 'log(contributors)', 'log(commits)', 'log(repo age)', 'time (beta)', 'intervention (gamma)', 'time_after (delta)')
rows <- c()
for (k in seq_along(term_keys)) {
  vals <- c()
  for (j in seq_along(res)) vals <- c(vals, fmt(res[[j]][term_keys[k], 1], res[[j]][term_keys[k], 5]))
  rows <- c(rows, paste0('| ', term_lab[k], ' | ', paste(vals, collapse = ' | '), ' |'))
}
r2m_ord <- c(r2m[1], r2m[3], r2m[2], r2m[4]); r2c_ord <- c(r2c[1], r2c[3], r2c[2], r2c[4])
rows <- c(rows, paste0('| R2m | ', paste(sprintf('%.3f', r2m_ord), collapse = ' | '), ' |'),
                paste0('| R2c | ', paste(sprintf('%.3f', r2c_ord), collapse = ' | '), ' |'))
md <- c(md, '## Merged versus rejected split (Section IV.A)', '', hdr, sep, rows, '')

writeLines(md, out_file)
cat('wrote', out_file, '\n')
