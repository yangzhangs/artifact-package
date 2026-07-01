#!/usr/bin/env python3
"""
Generate two separate PDFs for Fig 4 and Fig 5:
- Fig 4 (left): Opened PRs + Closed PRs (closed-in-bin) (1x2)
- Fig 5 (right): Review Comments + Close Latency (1x2)
- No (a)(b) labels
- Each PDF has its own legend
- Y-axis: 1 decimal place
- Uses 113 repos panel data
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import t as tdist
from matplotlib.lines import Line2D

plt.rcParams.update({
    'font.size': 10, 'font.family': 'sans-serif',
    'axes.labelsize': 10, 'xtick.labelsize': 9, 'ytick.labelsize': 9, 'legend.fontsize': 9,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
})

# Load data
# All DVs are in the main panel file
df_main = pd.read_csv('data/panel/rdd_panel_113.csv')
df_main = df_main[df_main['bin'] != 0]

perm_color = '#2166AC'
prob_color = '#B2182B'

DVs_left = [
    (df_main, 'log_new_prs', 'log(Opened PRs + 1)'),
    (df_main, 'log_prs_closed_in_bin', 'log(Closed PRs + 1)'),
]
DVs_right = [
    (df_main, 'log_review_comments_mean', 'log(Review Comments + 1)'),
    (df_main, 'log_close_latency_h', 'log(Close Latency + 1)'),
]

def plot_rdd_trend(ax, data, dv, ylabel, group_val, color):
    sub = data[data['prohibited'] == group_val].dropna(subset=[dv])
    
    summary = sub.groupby('bin').agg(
        mean=(dv, 'mean'), std=(dv, 'std'), n=(dv, 'count')
    ).reset_index()
    summary['se'] = summary['std'] / np.sqrt(summary['n'])
    summary['ci'] = 1.96 * summary['se']
    
    pre = summary[summary['bin'] < 0].sort_values('bin')
    post = summary[summary['bin'] > 0].sort_values('bin')
    
    marker = 'o' if group_val == 0 else 's'
    ms = 4.5
    
    ax.errorbar(pre['bin'], pre['mean'], yerr=pre['ci'], fmt=marker, color=color,
                capsize=2.5, alpha=0.8, zorder=3, markersize=ms)
    ax.errorbar(post['bin'], post['mean'], yerr=post['ci'], fmt=marker, color=color,
                capsize=2.5, alpha=0.8, zorder=3, markersize=ms)
    
    linestyle = '-' if group_val == 0 else '--'
    lw = 2 if group_val == 0 else 1.8
    
    for seg, x_range in [(pre, (-6, -1)), (post, (1, 6))]:
        if len(seg) >= 2:
            z = np.polyfit(seg['bin'], seg['mean'], 1)
            x = np.linspace(x_range[0], x_range[1], 50)
            y = np.poly1d(z)(x)
            
            resid_se = np.sqrt(np.sum((seg['mean'] - np.poly1d(z)(seg['bin']))**2) / max(len(seg) - 2, 1))
            t_val = tdist.ppf(0.975, max(len(seg) - 2, 1))
            mx = seg['bin'].mean()
            ss = np.sum((seg['bin'] - mx)**2)
            if ss > 0:
                ci = t_val * resid_se * np.sqrt(1/len(seg) + (x - mx)**2 / ss)
            else:
                ci = np.zeros_like(x)
            
            ax.plot(x, y, linestyle, color=color, linewidth=lw, zorder=2)
            ax.fill_between(x, y - ci, y + ci, color=color, alpha=0.15)
    
    ax.axvline(x=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Month index')
    ax.set_xticks(range(-6, 7, 2))
    # Y-axis: 1 decimal
    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))
    ax.tick_params(axis='both', labelsize=9)
    ax.grid(alpha=0.3, linewidth=0.5)

def make_figure(dvs, filename, figsize=(7, 3.0)):
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    for idx, (data, dv, ylabel) in enumerate(dvs):
        ax = axes[idx]
        plot_rdd_trend(ax, data, dv, ylabel, 0, perm_color)
        plot_rdd_trend(ax, data, dv, ylabel, 1, prob_color)
    
    # Legend - placed on top, tight spacing
    legend_elements = [
        Line2D([0], [0], color=perm_color, linewidth=2, marker='o', markersize=4.5, label='Permissive'),
        Line2D([0], [0], color=prob_color, linewidth=1.8, linestyle='--', marker='s', markersize=4.5, label='Prohibited'),
    ]
    fig.legend(handles=legend_elements, loc='upper center', ncol=2, frameon=False, fontsize=9,
               bbox_to_anchor=(0.55, 1.0), handletextpad=0.5, columnspacing=1.0)
    
    plt.tight_layout(w_pad=2.0, rect=[0, 0, 1, 0.94])
    plt.subplots_adjust(bottom=0.20, top=0.88)
    fig.savefig(filename, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved: {filename}')

# Fig 4: Opened PRs + Closed PRs (closed-in-bin)
make_figure(DVs_left, 'figures/fig4_rdd_trend_left.pdf')

# Fig 5: Review Comments + Close Latency
make_figure(DVs_right, 'figures/fig4_rdd_trend_right.pdf')