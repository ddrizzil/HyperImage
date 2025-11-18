"""Count and list all techniques in the generated HTML file."""

import re
from pathlib import Path

html_file = Path("site/index.html")
if not html_file.exists():
    print("Error: site/index.html not found")
    exit(1)

html_content = html_file.read_text(encoding='utf-8')

# Find all technique cards
card_pattern = r'<div class="technique-card">'
cards = re.findall(card_pattern, html_content)

# Find all technique titles
title_pattern = r'<h3><a href="[^"]+">([^<]+)</a></h3>'
titles = re.findall(title_pattern, html_content)

# Find techniques with empty summaries
empty_summary_pattern = r'<p class="technique-summary"></p>'
empty_summaries = re.findall(empty_summary_pattern, html_content)

print(f"Technique cards found: {len(cards)}")
print(f"Technique titles found: {len(titles)}")
print(f"Empty summaries: {len(empty_summaries)}")
print("\nAll techniques on the page:")
print("=" * 60)

for i, title in enumerate(titles, 1):
    # Check if this technique has an empty summary
    # Find the card for this technique
    title_escaped = re.escape(title)
    pattern = f'<h3><a href="[^"]+">{title_escaped}</a></h3>.*?<p class="technique-summary">(.*?)</p>'
    match = re.search(pattern, html_content, re.DOTALL)
    if match:
        summary = match.group(1).strip()
        if not summary:
            print(f"{i:2d}. {title} [EMPTY SUMMARY - might be hidden]")
        else:
            print(f"{i:2d}. {title}")
    else:
        print(f"{i:2d}. {title}")

print("\n" + "=" * 60)
if len(titles) != 17:
    print(f"WARNING: Expected 17 techniques, found {len(titles)}")
else:
    print("✓ All 17 techniques are present in the HTML file")
    
if empty_summaries:
    print(f"\n⚠ {len(empty_summaries)} technique(s) have empty summaries and might not be visible")

