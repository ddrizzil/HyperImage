"""
Main script: Generate reference pages for all techniques using the HyperImage framework.
This is the main entry point for generating the complete technique documentation site.
"""

from framework import SiteGenerator
from pathlib import Path
from techniques import get_technique_data, list_techniques

if __name__ == "__main__":
    # Create site generator
    site = SiteGenerator(output_dir=Path("site"), base_url="")
    
    # List all available techniques
    print("Loading techniques...")
    all_techniques = list_techniques()
    print(f"Found {len(all_techniques)} techniques:")
    
    # Add all available techniques to the site
    added_count = 0
    for technique_name in all_techniques:
        technique_data = get_technique_data(technique_name)
        if technique_data:
            site.add_technique(technique_name, technique_data)
            added_count += 1
            print(f"  [+] Added: {technique_name}")
        else:
            print(f"  [-] Failed to load: {technique_name}")
    
    print(f"\nSuccessfully loaded {added_count} techniques")
    
    # Generate all pages (HTML site with index, CSS, etc.)
    print("\nGenerating site...")
    site.generate_all_pages()
    
    print("\n" + "="*60)
    print("Generated HTML site:")
    print(f"  - Index page: site/index.html")
    print(f"  - CSS stylesheet: site/assets/style.css")
    print(f"  - Technique pages: {added_count} pages")
    print("="*60)
    print("\nOpen site/index.html in a web browser to view the site!")
