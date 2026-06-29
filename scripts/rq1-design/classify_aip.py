#!/usr/bin/env python3
"""
Classify AIPs along two dimensions:
1. Stance: Permissive vs. Prohibited
2. Conditions: Human review, Disclosure, AI-specific rules, Quality standards, Evidence supplementation

This script provides a classification framework. The final labels in the paper
were produced through manual annotation by two independent raters, with
inter-rater reliability measured by Cohen's kappa.
"""

import os
import csv
import re
import argparse

# Stance classification patterns
PROHIBIT_PATTERNS = [
    r'\b(?:prohibit|forbid|ban|not allow|not accept|strictly forbidden|do not (?:use|submit|allow))\b.*\b(?:ai|artificial intelligence|generated|llm)\b',
    r'\b(?:ai|artificial intelligence|generated|llm)\b.*\b(?:prohibit|forbid|ban|not allow|not accept|strictly forbidden|do not (?:use|submit|allow))\b',
    r'\bno ai\b',
    r'\bai[- ]?free\b',
]

PERMISSIVE_PATTERNS = [
    r'\b(?:allow|permit|welcome|accept|support|encourage)\b.*\b(?:ai|artificial intelligence|generated|llm)\b',
    r'\b(?:ai|artificial intelligence|generated|llm)\b.*\b(?:allow|permit|welcome|accept|support|encourage)\b',
    r'\bai (?:tool|tools|assistant|assistance)\b',
    r'\b(?:may|can|are welcome to|feel free to)\b.*\b(?:use|using)\b.*\bai\b',
]

# Condition classification patterns
CONDITION_PATTERNS = {
    'human_review': [
        r'\bhuman (?:review|oversight|verification|approval)\b',
        r'\breview.*\b(?:ai|generated)\b.*\bhuman\b',
        r'\b(?:understand|verify|personally review)\b.*\bai[- ]?generated\b',
        r'\bresponsib(?:le|ility)\b.*\bai\b',
        r'\baccountab(?:le|ility)\b.*\bai\b',
    ],
    'disclosure': [
        r'\bdisclos(?:e|ure)\b.*\b(?:ai|generated)\b',
        r'\b(?:ai|generated).*disclos(?:e|ure)\b',
        r'\b(?:mark|label|tag|flag)\b.*\bai[- ]?generated\b',
        r'\battribution\b.*\bai\b',
    ],
    'ai_specific_rules': [
        r'\bai[- ]?specific\b',
        r'\brule(?:s)?\b.*\bai\b',
        r'\blimit(?:s)?\b.*\bai\b',
        r'\bscope\b.*\bai\b',
    ],
    'quality_standards': [
        r'\bquality (?:bar|standard|requirement)\b',
        r'\bsame (?:quality|standard)\b.*\b(?:ai|human)\b',
        r'\bmeet.*quality\b',
    ],
    'evidence': [
        r'\b(?:prompt|prompts)\b.*\b(?:include|provide|submit)\b',
        r'\btest(?:s)?\b.*\b(?:include|provide|alongside)\b.*\bai\b',
        r'\bevidence\b.*\bai\b',
    ],
}


def classify_stance(text):
    """Classify AIP stance as Prohibited or Permissive based on text patterns."""
    text_lower = text.lower()
    
    prohibit_hits = sum(1 for p in PROHIBIT_PATTERNS if re.search(p, text_lower))
    permissive_hits = sum(1 for p in PERMISSIVE_PATTERNS if re.search(p, text_lower))
    
    if prohibit_hits > permissive_hits:
        return 'prohibited'
    elif permissive_hits > 0:
        return 'permissive'
    else:
        return 'unknown'


def classify_conditions(text):
    """Classify conditions in permissive AIPs."""
    text_lower = text.lower()
    conditions = []
    
    for condition, patterns in CONDITION_PATTERNS.items():
        if any(re.search(p, text_lower) for p in patterns):
            conditions.append(condition)
    
    return conditions


def classify_batch(input_csv, output_csv):
    """Classify all AIPs in the input CSV."""
    results = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = row.get('aip_content', '')
            stance = classify_stance(text)
            conditions = classify_conditions(text) if stance == 'permissive' else []
            results.append({
                'repo_name': row['repo_name'],
                'stance': stance,
                'conditions': '; '.join(conditions),
            })
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['repo_name', 'stance', 'conditions'])
        writer.writeheader()
        writer.writerows(results)
    
    prohibited = sum(1 for r in results if r['stance'] == 'prohibited')
    permissive = sum(1 for r in results if r['stance'] == 'permissive')
    print(f"Classified {len(results)} AIPs: {permissive} permissive, {prohibited} prohibited")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classify AIP stance and conditions')
    parser.add_argument('--input', required=True, help='CSV with AIP content (from extract_aip_content.py)')
    parser.add_argument('--output', default='aip_classification.csv', help='Output CSV path')
    args = parser.parse_args()
    
    classify_batch(args.input, args.output)