"""Check which JSON files exist vs which are registered in Python."""

import json
from pathlib import Path

# Get all JSON files
json_dir = Path("web/src/data/techniques")
json_files = list(json_dir.glob("*.json"))

print(f"Found {len(json_files)} JSON files:\n")
json_names = []
for f in sorted(json_files):
    try:
        with open(f, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            name = data.get("name", f.stem)
            json_names.append(name)
            print(f"  {f.name:50s} -> {name}")
    except Exception as e:
        print(f"  {f.name:50s} -> ERROR: {e}")

print(f"\n\nRegistered in Python techniques module:")
from techniques import list_techniques
registered = sorted(list_techniques())
for i, name in enumerate(registered, 1):
    print(f"  {i:2d}. {name}")

print(f"\n\nComparison:")
missing_in_python = set(json_names) - set(registered)
missing_json = set(registered) - set(json_names)

if missing_in_python:
    print(f"\nJSON files NOT in Python module ({len(missing_in_python)}):")
    for name in sorted(missing_in_python):
        print(f"  - {name}")

if missing_json:
    print(f"\nPython techniques WITHOUT JSON files ({len(missing_json)}):")
    for name in sorted(missing_json):
        print(f"  - {name}")

if not missing_in_python and not missing_json:
    print("\n[OK] All JSON files match Python techniques!")

