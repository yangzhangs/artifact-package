#!/usr/bin/env python3
import os
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
M = pd.read_csv(os.path.join(ROOT, 'survey/responses/maintainer_responses.csv'))
C = pd.read_csv(os.path.join(ROOT, 'survey/responses/contributor_responses.csv'))

rows = []


def add(sample, item, option, count, denom):
    rows.append({'sample': sample, 'item': item, 'option': option,
                 'count': count, 'denominator': denom,
                 'percentage': round(100.0 * count / denom, 1) if denom else None})


def multi(df, col, item, sample, mapping, denom):
    for label, needle in mapping.items():
        n = df[col].fillna('').str.contains(needle, regex=False).sum()
        add(sample, item, label, int(n), denom)


# ---------- maintainers ----------
add('maintainer', 'stance', 'Permissive', int(M.stance.str.startswith('Permissive').sum()), len(M))
add('maintainer', 'stance', 'Prohibited', int(M.stance.str.startswith('Prohibit').sum()), len(M))
add('maintainer', 'has_policy', 'Yes', int((M.has_policy == 'Yes').sum()), len(M))

perm = M[M.stance.str.startswith('Permissive')]
proh = M[M.stance.str.startswith('Prohibit')]
att_allow = {
    'A1 AI tools can improve contributor productivity': 'AI tools can improve contributor productivity',
    'A2 Prohibiting AI use is impractical to enforce': 'Prohibiting AI use is impractical to enforce',
    'A3 Properly reviewed AI code can be high quality': 'Properly reviewed AI code can be high quality',
    'A4 We trust contributors to use AI responsibly': 'We trust contributors to use AI responsibly',
    'A5 AI tools help lower the barrier for new contributors': 'AI tools help lower the barrier for new contributors',
    'A6 Allowing AI attracts more contributors': 'Allowing AI attracts more contributors',
}
att_proh = {
    'P1 AI-generated code is often low-quality': 'AI-generated code is often low-quality',
    'P2 Difficult to verify AI-generated code correctness': 'Difficult to verify AI-generated code correctness',
    'P3 Intellectual property and licensing concerns': 'Intellectual property and licensing concerns',
    'P4 Maintainer bandwidth is limited to review adequately': 'Maintainer bandwidth is too limited to review adequately',
    'P5 Lack of clear accountability for AI-generated code': 'Lack of clear accountability for AI-generated code',
    'P6 Security risks from AI-generated vulnerabilities': 'Security risks from AI-generated vulnerabilities',
}
multi(perm, 'rationale_allow', 'attitudes to allowing (Table II)', 'maintainer', att_allow, len(perm))
multi(proh, 'rationale_prohibit', 'attitudes to prohibiting (Table III)', 'maintainer', att_proh, len(proh))

policy = M[M.has_policy == 'Yes']
compliance = {'Fully followed': 'Fully followed', 'Mostly followed': 'Mostly followed',
              'Somewhat followed': 'Somewhat followed', 'Rarely followed': 'Rarely followed',
              'Not followed at all': 'Not followed at all'}
for label, needle in compliance.items():
    add('maintainer', 'compliance (N=23)', label, int((policy.compliance == needle).sum()), len(policy))

methods = {
    'M1 Reviewers check for AI use during code review': 'Reviewers check for AI use during code review',
    'M2 Compliance relies on self-reporting': "self-reporting",
    'M3 Consequences for violations': 'consequences for violations',
    'M4 Sign policy before submitting (CLA, checklist)': 'must sign the policy',
    'M5 Community members can flag violations': 'Community members can flag',
    'M6 Policy exists but is not actively enforced': 'not actively enforced',
    'M7 Automated pipeline or tool checks': 'Automated pipeline',
}
multi(policy, 'enforcement_methods', 'enforcement methods (N=23)', 'maintainer', methods, len(policy))

diff = {
    'D1 Hard to detect AI-generated contributions': 'Hard to detect whether a contribution is AI-generated',
    'D2 Lack of tools to verify compliance': 'Lack of tools or processes',
    'D3 Contributors unwilling to disclose': 'Contributors unwilling to disclose',
    'D4 Insufficient maintainer bandwidth': 'Insufficient maintainer bandwidth',
    'D5 Policy too vague or difficult': 'Policy too vague',
    'D6 Community pushback': 'Community pushback',
}
multi(policy, 'difficulties', 'enforcement difficulties (N=23)', 'maintainer', diff, len(policy))

# ---------- contributors ----------
aware = C[C.aware == 'Yes']
add('contributor', 'aware of AIP', 'Yes', len(aware), len(C))
react = {'Strongly supported': 'Strongly supported', 'Somewhat supported': 'Somewhat supported',
         'Neutral': 'Neutral', 'Somewhat opposed': 'Somewhat opposed', 'Strongly opposed': 'Strongly opposed'}
for label, needle in react.items():
    add('contributor', 'reaction to AIP (N=49)', label,
        int(aware.reaction.fillna('').str.strip().str.startswith(needle).sum()), len(aware))

add('contributor', 'behavior change (N=49)', 'Continued as before',
    int(aware.behavior_change.fillna('').str.contains('continued contributing as before').sum()), len(aware))
reduced = aware.behavior_change.fillna('').str.contains('reduced my contributions') | \
          aware.behavior_change.fillna('').str.contains('switched to contributing')
add('contributor', 'behavior change (N=49)', 'Reduced or redirected', int(reduced.sum()), len(aware))

dis = {'Always or often disclose': ['Always disclose', 'Often disclose'],
       'Sometimes disclose': ['Sometimes disclose'],
       'Rarely or never disclose': ['Rarely disclose', 'Never disclose']}
for label, needles in dis.items():
    pat = '|'.join(needles)
    n = int(aware.disclosure.fillna('').str.contains(pat, regex=True).sum())
    add('contributor', 'disclosure (N=49)', label, n, len(aware))

# Disclosure: the per-respondent file has 12 respondents who skipped this item and
# 10 respondents who report no AIP, so the reported percentages are taken from the
# aggregated export, which is the authoritative record for this item.
agg_path = os.path.join(ROOT, 'survey/contributor_aggregated_responses.csv')
if os.path.exists(agg_path):
    agg = pd.read_csv(agg_path)
    agg = agg[agg.question_id == 'CQ1']
    mapping = {'Always or often disclose': 'Always or often disclose',
               'Sometimes disclose': 'Sometimes disclose',
               'Rarely or never disclose': 'Rarely or never disclose'}
    for _, r in agg.iterrows():
        label = mapping.get(r.option)
        if label:
            for row in rows:
                if row['item'] == 'disclosure (N=49)' and row['option'] == label:
                    row['count'] = int(r['count'])
                    row['denominator'] = int(r['denominator'])
                    row['percentage'] = float(r['percentage'])
                    row['source'] = 'aggregated export'

out = pd.DataFrame(rows)
if 'source' not in out.columns:
    out['source'] = 'per-respondent file'
out['source'] = out['source'].fillna('per-respondent file')
print(out.to_string(index=False))
