"""Verify which techniques are on the main page."""

import re
from pathlib import Path

# Read the index.html file
index_path = Path("site/index.html")
if not index_path.exists():
    print("Error: site/index.html not found. Run example_raman.py first.")
    exit(1)

html_content = index_path.read_text(encoding='utf-8')

# Find all technique cards
pattern = r'<h3><a href="[^"]+">([^<]+)</a></h3>'
techniques = re.findall(pattern, html_content)

print(f"Found {len(techniques)} techniques on the main page:\n")
for i, tech in enumerate(techniques, 1):
    print(f"{i:2d}. {tech}")

# Also check registered techniques
print("\n" + "="*60)
print("Registered techniques in module:")
from techniques import list_techniques
registered = sorted(list_techniques())
print(f"Total: {len(registered)}")
for i, tech in enumerate(registered, 1):
    print(f"{i:2d}. {tech}")

# Compare
print("\n" + "="*60)
print("Comparison:")
missing_on_page = set(registered) - set(techniques)
extra_on_page = set(techniques) - set(registered)

if missing_on_page:
    print(f"\nMissing on page ({len(missing_on_page)}):")
    for tech in sorted(missing_on_page):
        print(f"  - {tech}")

if extra_on_page:
    print(f"\nExtra on page ({len(extra_on_page)}):")
    for tech in sorted(extra_on_page):
        print(f"  - {tech}")

if not missing_on_page and not extra_on_page:
    print("\n[OK] All techniques match!")

