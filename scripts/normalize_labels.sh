#!/bin/bash
# Normalize features, components and tags in all repos/*/*/overview.json
# by replacing values that match a label in analyze_labels_output.json
# with the corresponding category name.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 << 'EOF'
import json
import glob
import os
import sys

MAPPING_FILE = 'analyze_labels_output.json'
SECTIONS = ['features', 'components', 'tags']

os.chdir(os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else '.')

with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
    mapping = json.load(f)

# Build lookup: { section: { label_lowercase: category } }
lookups = {}
for section in SECTIONS:
    lookups[section] = {}
    for cat_obj in mapping.get(section, []):
        category = cat_obj['category']
        for label_obj in cat_obj.get('labels', []):
            label_lower = label_obj['label'].strip().lower()
            # First occurrence wins (highest count is listed first)
            lookups[section].setdefault(label_lower, category)

overview_files = sorted(glob.glob('repos/*/*/overview.json'))
print(f"Found {len(overview_files)} overview.json files", flush=True)

modified_count = 0

for filepath in overview_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  ERROR parsing {filepath}: {e}", file=sys.stderr)
            continue

    changed = False

    for section in SECTIONS:
        if section not in data or not isinstance(data[section], list):
            continue

        new_values = []
        seen = set()

        for value in data[section]:
            if not isinstance(value, str):
                new_values.append(value)
                continue

            mapped = lookups[section].get(value.strip().lower())
            replacement = mapped if mapped else value

            # Deduplicate (preserve first occurrence)
            if replacement not in seen:
                seen.add(replacement)
                new_values.append(replacement)

            if mapped and mapped != value:
                changed = True

        data[section] = new_values

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        modified_count += 1
        print(f"  modified: {filepath}")

print(f"\nDone. Modified {modified_count}/{len(overview_files)} files.")
EOF
