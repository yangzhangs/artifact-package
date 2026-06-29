#!/usr/bin/env python3
"""Plot stance-only donut chart (right panel of original Fig 3), no title."""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 15,
    'axes.linewidth': 0.8,
    'figure.dpi': 300,
})

stance_labels = ['Permissive', 'Prohibited']
stance_sizes   = [544, 71]
stance_colors   = ['#5B9BD5', '#E8636B']

fig, ax = plt.subplots(figsize=(4.5, 4))

total = sum(stance_sizes)
wedges, texts, autotexts = ax.pie(
    stance_sizes, labels=None, autopct='',
    startangle=90, colors=stance_colors,
    pctdistance=0.75,
    wedgeprops=dict(width=0.65, edgecolor='white', linewidth=1.5),
)

# External labels with leader lines
for i, (wedge, size) in enumerate(zip(wedges, stance_sizes)):
    pct = size / total * 100
    ang = (wedge.theta2 + wedge.theta1) / 2.0
    
    r_mid = 0.72
    r_outer = 1.05
    x1 = np.cos(np.deg2rad(ang)) * r_mid
    y1 = np.sin(np.deg2rad(ang)) * r_mid
    x2 = np.cos(np.deg2rad(ang)) * r_outer
    y2 = np.sin(np.deg2rad(ang)) * r_outer
    
    ext = 0.3
    if x2 >= 0:
        x3 = x2 + ext
        ha = 'left'
    else:
        x3 = x2 - ext
        ha = 'right'
    
    ax.plot([x1, x2, x3], [y1, y2, y2], '-', lw=0.7, color='#888888')
    ax.text(x3, y2, stance_labels[i] + '\n' + f'({pct:.1f}%)',
            ha=ha, va='center', fontsize=15, color='#333333')

ax.text(0, 0, f'$n$={total}', ha='center', va='center',
        fontsize=13, fontweight='bold', color='#333333')

ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.3, 1.3)
ax.axis('off')

plt.tight_layout(pad=0.5)
plt.savefig('figures/fig_stance_distribution.pdf',
            bbox_inches='tight', dpi=300)
plt.savefig('figures/fig_stance_distribution.png',
            bbox_inches='tight', dpi=300)
print('Saved')