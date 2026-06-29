#!/usr/bin/env python3
"""
Build the RDD panel data for 113 active repositories.
Constructs 30-day time windows (6 before + 6 after AIP introduction),
excluding the transition window. Aggregates four dependent variables:
  - Opened PRs (count of newly opened PRs per bin)
  - Closed PRs (count of PRs closed per bin)
  - Review Comments (mean review comments per PR)
  - Close Latency (mean hours from PR creation to closure)
Also computes control variables: stars, contributors, commits, repo age.
"""

import argparse
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from collections import defaultdict

def build_panel(pr_data_path, repo_list_path, aip_dates_path, output_path):
    """
    Build the RDD panel from PR-level data.
    
    Parameters
    ----------
    pr_data_path : str
        Path to CSV containing PR-level data (repo_name, pr_created_at, pr_closed_at, etc.)
    repo_list_path : str
        Path to CSV of confirmed repos with metadata (stars, contributors, etc.)
    aip_dates_path : str
        Path to CSV with AIP first introduction dates per repo
    output_path : str
        Path for the output panel CSV
    """
    # Load data
    prs = pd.read_csv(pr_data_path)
    repos = pd.read_csv(repo_list_path)
    aip_dates = pd.read_csv(aip_dates_path)
    
    # Parse dates
    prs['pr_created_at'] = pd.to_datetime(prs['pr_created_at'])
    prs['pr_closed_at'] = pd.to_datetime(prs['pr_closed_at'])
    
    # Merge AIP dates
    repo_dates = dict(zip(aip_dates['repo_name'], 
                          pd.to_datetime(aip_dates['aip_first_date'])))
    
    # Filter to repos with AIP dates
    repos = repos[repos['repo_name'].isin(repo_dates.keys())]
    
    # Build 30-day bins
    panel_rows = []
    
    for repo_name in repos['repo_name'].unique():
        if repo_name not in repo_dates:
            continue
        
        aip_date = repo_dates[repo_name]
        repo_prs = prs[prs['repo_name'] == repo_name].copy()
        
        # Compute bin index relative to AIP date
        repo_prs['days_from_aip'] = (repo_prs['pr_created_at'] - aip_date).dt.days
        repo_prs['bin'] = repo_prs['days_from_aip'] // 30
        
        # Filter to ±6 bins (excluding bin 0, the transition window)
        repo_prs = repo_prs[(repo_prs['bin'] >= -6) & (repo_prs['bin'] <= 6)]
        repo_prs = repo_prs[repo_prs['bin'] != 0]
        
        if len(repo_prs) == 0:
            continue
        
        repo_meta = repos[repos['repo_name'] == repo_name].iloc[0]
        
        for bin_idx in range(-6, 7):
            if bin_idx == 0:
                continue
            
            bin_prs = repo_prs[repo_prs['bin'] == bin_idx]
            
            row = {
                'repo_name': repo_name,
                'bin': bin_idx,
                'new_prs': len(bin_prs),
                'merged_prs': bin_prs['pr_merged'].sum() if 'pr_merged' in bin_prs else 0,
                'total_closed': bin_prs['pr_state'].isin(['closed', 'merged']).sum() if 'pr_state' in bin_prs else 0,
                'review_comments_mean': bin_prs['review_comments'].mean() if 'review_comments' in bin_prs else 0,
                'close_latency_h': np.nan,
                'prohibited': int(repo_meta.get('cat1', 'permissive') == 'prohibited'),
                'language': repo_meta.get('language', ''),
                'stars': repo_meta.get('stars', 0),
                'contributors': repo_meta.get('contributors', 0),
                'commits': repo_meta.get('commits', 0),
                'repo_age_days': (datetime(2026, 1, 1) - pd.to_datetime(repo_meta.get('created_at', datetime(2026, 1, 1)))).days,
                'time': abs(bin_idx),
                'intervention': int(bin_idx > 0),
                'time_after': max(0, bin_idx) if bin_idx > 0 else 0,
            }
            
            # Close latency for closed PRs
            closed_prs = bin_prs[bin_prs['pr_closed_at'].notna()]
            if len(closed_prs) > 0:
                latencies = (closed_prs['pr_closed_at'] - closed_prs['pr_created_at']).dt.total_seconds() / 3600
                row['close_latency_h'] = latencies.mean()
            
            # Log transforms
            for col in ['new_prs', 'merged_prs', 'total_closed', 'review_comments_mean', 
                        'close_latency_h', 'stars', 'contributors', 'commits', 'repo_age_days']:
                log_col = f'log_{col}'
                val = row[col]
                row[log_col] = np.log(val + 1) if val and not np.isnan(val) else 0
            
            panel_rows.append(row)
    
    panel = pd.DataFrame(panel_rows)
    
    # Fill missing bins with zeros for count DVs
    count_cols = ['new_prs', 'merged_prs', 'total_closed']
    for repo_name in panel['repo_name'].unique():
        for bin_idx in range(-6, 7):
            if bin_idx == 0:
                continue
            if not ((panel['repo_name'] == repo_name) & (panel['bin'] == bin_idx)).any():
                # Add zero row
                pass  # Already handled in loop above
    
    panel.to_csv(output_path, index=False)
    print(f"Panel built: {len(panel)} rows, {panel['repo_name'].nunique()} repos")
    print(f"  Permissive: {sum(panel.groupby('repo_name')['prohibited'].first() == 0)}")
    print(f"  Prohibited: {sum(panel.groupby('repo_name')['prohibited'].first() == 1)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build RDD panel data')
    parser.add_argument('--pr-data', required=True, help='CSV with PR-level data')
    parser.add_argument('--repo-list', required=True, help='CSV with repo metadata')
    parser.add_argument('--aip-dates', required=True, help='CSV with AIP first dates')
    parser.add_argument('--output', default='rdd_panel_113.csv', help='Output panel CSV path')
    args = parser.parse_args()
    
    build_panel(args.pr_data, args.repo_list, args.aip_dates, args.output)