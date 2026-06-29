#!/usr/bin/env python3
"""
Extract AIP content from CONTRIBUTING.md files of confirmed repositories.
Reads each confirmed repo's CONTRIBUTING.md, locates the AIP section,
and extracts the policy text for manual classification.
"""

import os
import re
import csv
import argparse

def extract_aip_section(content, keywords=None):
    """Extract the section of CONTRIBUTING.md that contains AIP content."""
    if keywords is None:
        keywords = [
            r'#{1,4}\s.*(AI|artificial intelligence|generated|copilot|chatgpt|llm).*',
            r'#{1,4}\s.*(contribution|contributing).*\n.*\n.*(?:AI|generated|copilot)',
        ]
    
    lines = content.split('\n')
    section_start = None
    section_lines = []
    
    for i, line in enumerate(lines):
        for kw in keywords:
            if re.search(kw, line, re.IGNORECASE):
                section_start = i
                break
        if section_start is not None:
            break
    
    if section_start is None:
        return ""
    
    # Determine heading level
    heading_match = re.match(r'^(#{1,4})\s', lines[section_start])
    if heading_match:
        heading_level = len(heading_match.group(1))
        section_lines.append(lines[section_start])
        for j in range(section_start + 1, len(lines)):
            next_heading = re.match(r'^(#{1,4})\s', lines[j])
            if next_heading and len(next_heading.group(1)) <= heading_level:
                break
            section_lines.append(lines[j])
    else:
        # Not a heading; extract surrounding paragraph
        start = max(0, section_start - 5)
        end = min(len(lines), section_start + 30)
        section_lines = lines[start:end]
    
    return '\n'.join(section_lines).strip()


def extract_aip_from_file(filepath):
    """Read a CONTRIBUTING.md file and extract AIP content."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return extract_aip_section(content)


def batch_extract(repo_list_path, contributing_dir, output_path):
    """Extract AIP content for all confirmed repos."""
    repos = []
    with open(repo_list_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            repos.append(row['repo_name'])
    
    results = []
    for repo in repos:
        # Try common path patterns
        found = False
        for path_pattern in [
            f'{contributing_dir}/{repo.replace("/", "_")}_root_contributing.md',
            f'{contributing_dir}/{repo.replace("/", "_")}.github_contributing.md',
            f'{contributing_dir}/{repo.replace("/", "_")}_docs_contributing.md',
        ]:
            if os.path.exists(path_pattern):
                aip_text = extract_aip_from_file(path_pattern)
                results.append({
                    'repo_name': repo,
                    'aip_content': aip_text,
                    'source_file': os.path.basename(path_pattern),
                })
                found = True
                break
        if not found:
            results.append({
                'repo_name': repo,
                'aip_content': '',
                'source_file': 'NOT_FOUND',
            })
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['repo_name', 'aip_content', 'source_file'])
        writer.writeheader()
        writer.writerows(results)
    
    found_count = sum(1 for r in results if r['aip_content'])
    print(f"Extracted AIP content for {found_count}/{len(repos)} repos")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract AIP content from CONTRIBUTING.md files')
    parser.add_argument('--repo-list', required=True, help='CSV file with confirmed repo list')
    parser.add_argument('--contributing-dir', required=True, help='Directory containing downloaded CONTRIBUTING.md files')
    parser.add_argument('--output', default='aip_content_extracted.csv', help='Output CSV path')
    args = parser.parse_args()
    
    batch_extract(args.repo_list, args.contributing_dir, args.output)