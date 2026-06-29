#!/usr/bin/env python3
"""Horizontal bar chart for AIP compliance perception - compact, font 13."""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 13,
    'figure.dpi': 300,
})

categories = ['Not followed at all', 'Rarely followed', 'Somewhat followed', 'Mostly followed', 'Fully followed']
percentages = [9.5, 4.8, 33.3, 42.9, 9.5]

colors = ['#D94F5C', '#F4A582', '#CCCCCC', '#8FBEEA', '#5B9BD5']

fig, ax = plt.subplots(figsize=(3.4, 2.0))

y_pos = np.arange(len(categories))
bars = ax.barh(y_pos, percentages, color=colors, height=0.55, edgecolor='white', linewidth=0.5)

for i, (bar, pct) in enumerate(zip(bars, percentages)):
    width = bar.get_width()
    ax.text(width + 0.8, bar.get_y() + bar.get_height()/2,
            f'{pct:.1f}%', ha='left', va='center', fontsize=13, color='#333333')

ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=13)
ax.set_xlabel('Respondents (%)', fontsize=13)
ax.set_xlim(0, 50)
ax.set_xticks([0, 10, 20, 30, 40, 50])
ax.set_xticklabels(['0', '10', '20', '30', '40', '50'], fontsize=13)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.invert_yaxis()

plt.subplots_adjust(left=0.20, right=0.85, top=0.97, bottom=0.17)

plt.savefig('figures/fig_compliance_likert.pdf',
            bbox_inches='tight', dpi=300, pad_inches=0.02)
plt.savefig('figures/fig_compliance_likert.png',
            bbox_inches='tight', dpi=300, pad_inches=0.02)
print('Saved')
