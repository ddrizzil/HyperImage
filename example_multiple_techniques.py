"""
Example: Generate a site with multiple techniques using the HyperImage framework.
This demonstrates how to use the modular technique file structure.
"""

from framework import SiteGenerator
from pathlib import Path
from techniques import get_technique_data, list_techniques

if __name__ == "__main__":
    # Create site generator
    site = SiteGenerator(output_dir=Path("site"), base_url="")
    
    # List all available techniques
    print("Available techniques:")
    for technique_name in list_techniques():
        print(f"  - {technique_name}")
    print()
    
    # Add all available techniques to the site
    for technique_name in list_techniques():
        technique_data = get_technique_data(technique_name)
        if technique_data:
            site.add_technique(technique_name, technique_data)
            print(f"Added: {technique_name}")
    
    # Generate all pages (HTML site with index, CSS, etc.)
    print("\nGenerating site...")
    site.generate_all_pages()
    
    print("\nGenerated HTML site:")
    print(f"  - Index page: site/index.html")
    print(f"  - CSS stylesheet: site/assets/style.css")
    print(f"  - Technique pages: {len(list_techniques())} pages")
    print("\nOpen site/index.html in a web browser to view the site!")

