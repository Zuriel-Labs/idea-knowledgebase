#!/usr/bin/env python3
"""Check local Markdown links; this does not validate external sources."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path(__file__).resolve().parent.parent
errors = []
checked = 0
for file in sorted(root.rglob('*.md')):
    if '.git' in file.parts:
        continue
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
        target = target.split(' "', 1)[0].strip('<>')
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(('#', '//', 'mailto:')):
            continue
        path = unquote(parsed.path)
        if not path:
            continue
        checked += 1
        resolved = (file.parent / path).resolve()
        if not resolved.is_relative_to(root) or not resolved.exists():
            errors.append(f'{file.relative_to(root)}: {target}')
for error in errors:
    print(f'MISSING: {error}')
print(f'Checked {checked} local links; {len(errors)} error(s). External links and anchor fragments not checked.')
sys.exit(bool(errors))
