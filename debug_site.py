"""Debug which techniques are actually being added to the site."""

from framework import SiteGenerator
from pathlib import Path
from techniques import get_technique_data, list_techniques

site = SiteGenerator(output_dir=Path("site"), base_url="")

print("Checking each technique:\n")
all_techniques = list_techniques()
added = []
failed = []

for technique_name in sorted(all_techniques):
    technique_data = get_technique_data(technique_name)
    if technique_data:
        try:
            # Check if it has required fields
            has_summary = bool(technique_data.get("one_line_summary", "").strip())
            has_abstract = bool(technique_data.get("abstract", "").strip())
            
            site.add_technique(technique_name, technique_data)
            status = "OK"
            if not has_summary:
                status += " (no summary)"
            added.append((technique_name, status))
            print(f"  [+] {technique_name} - {status}")
        except Exception as e:
            failed.append((technique_name, str(e)))
            print(f"  [-] {technique_name} - FAILED: {e}")
    else:
        failed.append((technique_name, "No data"))
        print(f"  [-] {technique_name} - No data")

print(f"\n\nSummary:")
print(f"  Successfully added: {len(added)}")
print(f"  Failed: {len(failed)}")
print(f"  Total in site.techniques: {len(site.techniques)}")

if failed:
    print("\nFailed techniques:")
    for name, reason in failed:
        print(f"  - {name}: {reason}")

