"""
HyperImage Framework: Generate hyperphysics-style reference pages for scientific analysis techniques.

This framework creates structured HTML documentation pages for conservation science techniques
with interlinking and navigation.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Set
from pathlib import Path
import json
import re
import html


@dataclass
class TechniqueReference:
    """Data structure for a scientific analysis technique reference page."""
    
    technique_name: str
    one_line_summary: str
    abstract: str
    physics_principle: str
    instruments_components: str
    resolution_detection: str
    sample_requirements: str
    measurement_protocol: Dict[str, List[str]]  # e.g., {"preparation": [...], "calibration": [...]}
    data_outputs: str
    data_analysis_pipeline: Dict[str, str]  # e.g., {"preprocessing": "...", "feature_extraction": "..."}
    artifacts_troubleshooting: str
    multimodal_pairings: str
    strengths_limitations: Dict[str, List[str]]  # {"strengths": [...], "limitations": [...]}
    references: List[Dict[str, str]]  # [{"citation": "...", "doi": "..."}]
    lab_checklist: List[str]
    keywords: List[str]
    
    def to_markdown(self) -> str:
        """Convert the technique reference to markdown format."""
        
        md = f"# {self.technique_name}\n\n"
        
        # Section 2: One-line summary
        md += f"## One-line Summary\n\n{self.one_line_summary}\n\n"
        
        # Section 3: Abstract
        md += f"## Abstract\n\n{self.abstract}\n\n"
        
        # Section 4: Physics & Principle
        md += f"## Physics & Principle\n\n{self.physics_principle}\n\n"
        
        # Section 5: Typical Instruments & Components
        md += f"## Typical Instruments & Components\n\n{self.instruments_components}\n\n"
        
        # Section 6: Spatial / Spectral / Temporal Resolution
        md += f"## Spatial / Spectral / Temporal Resolution\n\n{self.resolution_detection}\n\n"
        
        # Section 7: Sample Requirements & Invasiveness
        md += f"## Sample Requirements & Invasiveness\n\n{self.sample_requirements}\n\n"
        
        # Section 8: Step-by-step Measurement Protocol
        md += "## Step-by-step Measurement Protocol\n\n"
        for section_name, steps in self.measurement_protocol.items():
            md += f"### {section_name.title()}\n\n"
            for i, step in enumerate(steps, 1):
                md += f"{i}. {step}\n"
            md += "\n"
        
        # Section 9: Data Outputs & File Formats
        md += f"## Data Outputs & File Formats\n\n{self.data_outputs}\n\n"
        
        # Section 10: Data Analysis Pipeline
        md += "## Data Analysis Pipeline\n\n"
        for section_name, content in self.data_analysis_pipeline.items():
            md += f"### {section_name.replace('_', ' ').title()}\n\n{content}\n\n"
        
        # Section 11: Common Instrument Artifacts & Troubleshooting
        md += f"## Common Instrument Artifacts & Troubleshooting\n\n{self.artifacts_troubleshooting}\n\n"
        
        # Section 12: Typical Multimodal Pairings
        md += f"## Typical Multimodal Pairings\n\n{self.multimodal_pairings}\n\n"
        
        # Section 13: Strengths & Limitations
        md += "## Strengths & Limitations\n\n"
        md += "### Strengths\n\n"
        for strength in self.strengths_limitations.get("strengths", []):
            md += f"- {strength}\n"
        md += "\n### Limitations\n\n"
        for limitation in self.strengths_limitations.get("limitations", []):
            md += f"- {limitation}\n"
        md += "\n"
        
        # Section 14: Representative References
        md += "## Representative References\n\n"
        for ref in self.references:
            citation = ref.get("citation", "")
            doi = ref.get("doi", "")
            if doi:
                md += f"- {citation} DOI: [{doi}](https://doi.org/{doi})\n"
            else:
                md += f"- {citation}\n"
        md += "\n"
        
        # Section 15: Lab Checklist
        md += "## Lab Checklist\n\n"
        for i, item in enumerate(self.lab_checklist, 1):
            md += f"{i}. [ ] {item}\n"
        md += "\n"
        
        # Section 16: Keywords & Tags
        md += "## Keywords & Tags\n\n"
        md += ", ".join(self.keywords) + "\n"
        
        return md
    
    def to_html(self, all_techniques: Optional[Dict[str, str]] = None, base_url: str = "") -> str:
        """Convert the technique reference to HTML format with cross-linking."""
        if all_techniques is None:
            all_techniques = {}
        
        def markdown_to_html(text: str) -> str:
            """Convert markdown-like text to HTML with cross-linking."""
            if not text:
                return ""
            
            # Escape HTML first
            text = html.escape(text)
            
            # Convert code blocks
            text = re.sub(r'```(\w+)?\n(.*?)```', 
                         lambda m: f'<pre><code class="language-{m.group(1) or ""}">{m.group(2)}</code></pre>', 
                         text, flags=re.DOTALL)
            
            # Convert inline code
            text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
            
            # Convert bold
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            
            # Convert italic
            text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
            
            # Convert links
            text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
            
            # Convert line breaks to paragraphs, handling lists
            # First, split by double newlines
            paragraphs = text.split('\n\n')
            html_paras = []
            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue
                
                # Check if paragraph contains list items
                lines = para.split('\n')
                first_line = lines[0].strip()
                
                # Check if it's a list
                if first_line.startswith('- ') or first_line.startswith('* '):
                    # Convert to unordered list
                    list_html = '<ul>\n'
                    for line in lines:
                        line = line.strip()
                        if line.startswith('- ') or line.startswith('* '):
                            item = re.sub(r'^[-*]\s+', '', line)
                            list_html += f'  <li>{item}</li>\n'
                    list_html += '</ul>'
                    html_paras.append(list_html)
                elif re.match(r'^\d+\.\s', first_line):
                    # Convert to ordered list
                    list_html = '<ol>\n'
                    for line in lines:
                        line = line.strip()
                        if re.match(r'^\d+\.\s', line):
                            item = re.sub(r'^\d+\.\s+', '', line)
                            list_html += f'  <li>{item}</li>\n'
                    list_html += '</ol>'
                    html_paras.append(list_html)
                else:
                    # Regular paragraph - check for inline lists
                    if '\n- ' in para or '\n* ' in para:
                        # Has list items within, split them
                        parts = re.split(r'\n(?=[-*]\s)', para)
                        for part in parts:
                            part = part.strip()
                            if part.startswith('- ') or part.startswith('* '):
                                # List item
                                items = re.split(r'\n(?=[-*]\s)', part)
                                list_html = '<ul>\n'
                                for item in items:
                                    item = re.sub(r'^[-*]\s+', '', item.strip())
                                    list_html += f'  <li>{item}</li>\n'
                                list_html += '</ul>'
                                html_paras.append(list_html)
                            else:
                                # Regular text
                                if part:
                                    html_paras.append(f'<p>{part}</p>')
                    else:
                        # Regular paragraph
                        html_paras.append(f'<p>{para}</p>')
            
            # Cross-link technique names
            for tech_name, tech_url in all_techniques.items():
                if tech_name != self.technique_name:
                    pattern = re.compile(r'\b' + re.escape(tech_name) + r'\b', re.IGNORECASE)
                    html_paras = [pattern.sub(
                        lambda m: f'<a href="{base_url}{tech_url}" class="technique-link">{m.group(0)}</a>',
                        para) for para in html_paras]
            
            return '\n'.join(html_paras)
        
        def format_code_block(code: str, language: str = "python") -> str:
            """Format code block with syntax highlighting class."""
            code = html.escape(code)
            return f'<pre><code class="language-{language}">{code}</code></pre>'
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(self.technique_name)} - HyperImage</title>
    <link rel="stylesheet" href="{base_url}assets/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="{base_url}index.html" class="nav-logo">HyperImage</a>
            <ul class="nav-menu">
                <li><a href="{base_url}index.html">Home</a></li>
                <li><a href="{base_url}index.html#techniques">Techniques</a></li>
            </ul>
        </div>
    </nav>
    
    <main class="container">
        <article class="technique-page">
            <header class="page-header">
                <h1>{html.escape(self.technique_name)}</h1>
                <p class="summary">{html.escape(self.one_line_summary)}</p>
            </header>
            
            <section id="abstract" class="section">
                <h2>Abstract</h2>
                {markdown_to_html(self.abstract)}
            </section>
            
            <section id="physics" class="section">
                <h2>Physics & Principle</h2>
                {markdown_to_html(self.physics_principle)}
            </section>
            
            <section id="instruments" class="section">
                <h2>Typical Instruments & Components</h2>
                {markdown_to_html(self.instruments_components)}
            </section>
            
            <section id="resolution" class="section">
                <h2>Spatial / Spectral / Temporal Resolution</h2>
                {markdown_to_html(self.resolution_detection)}
            </section>
            
            <section id="sample-requirements" class="section">
                <h2>Sample Requirements & Invasiveness</h2>
                {markdown_to_html(self.sample_requirements)}
            </section>
            
            <section id="protocol" class="section">
                <h2>Step-by-step Measurement Protocol</h2>"""
        
        for section_name, steps in self.measurement_protocol.items():
            html_content += f"""
                <h3>{html.escape(section_name.title())}</h3>
                <ol>"""
            for step in steps:
                html_content += f"""
                    <li>{markdown_to_html(step)}</li>"""
            html_content += """
                </ol>"""
        
        html_content += f"""
            </section>
            
            <section id="data-outputs" class="section">
                <h2>Data Outputs & File Formats</h2>
                {markdown_to_html(self.data_outputs)}
            </section>
            
            <section id="analysis" class="section">
                <h2>Data Analysis Pipeline</h2>"""
        
        for section_name, content in self.data_analysis_pipeline.items():
            html_content += f"""
                <h3>{html.escape(section_name.replace('_', ' ').title())}</h3>
                {markdown_to_html(content)}"""
        
        html_content += f"""
            </section>
            
            <section id="troubleshooting" class="section">
                <h2>Common Instrument Artifacts & Troubleshooting</h2>
                {markdown_to_html(self.artifacts_troubleshooting)}
            </section>
            
            <section id="multimodal" class="section">
                <h2>Typical Multimodal Pairings</h2>
                {markdown_to_html(self.multimodal_pairings)}
            </section>
            
            <section id="strengths-limitations" class="section">
                <h2>Strengths & Limitations</h2>
                <h3>Strengths</h3>
                <ul>"""
        
        for strength in self.strengths_limitations.get("strengths", []):
            html_content += f"""
                    <li>{markdown_to_html(strength)}</li>"""
        
        html_content += """
                </ul>
                <h3>Limitations</h3>
                <ul>"""
        
        for limitation in self.strengths_limitations.get("limitations", []):
            html_content += f"""
                    <li>{markdown_to_html(limitation)}</li>"""
        
        html_content += """
                </ul>
            </section>
            
            <section id="references" class="section">
                <h2>Representative References</h2>
                <ul class="references">"""
        
        for ref in self.references:
            citation = ref.get("citation", "")
            doi = ref.get("doi", "")
            if doi:
                html_content += f"""
                    <li>{html.escape(citation)} <a href="https://doi.org/{doi}" target="_blank" rel="noopener">DOI: {doi}</a></li>"""
            else:
                html_content += f"""
                    <li>{html.escape(citation)}</li>"""
        
        html_content += """
                </ul>
            </section>
            
            <section id="checklist" class="section">
                <h2>Lab Checklist</h2>
                <div class="checklist">"""
        
        for i, item in enumerate(self.lab_checklist, 1):
            html_content += f"""
                    <label class="checklist-item">
                        <input type="checkbox">
                        <span>{html.escape(item)}</span>
                    </label>"""
        
        html_content += """
                </div>
            </section>
            
            <section id="keywords" class="section">
                <h2>Keywords & Tags</h2>
                <div class="keywords">"""
        
        for keyword in self.keywords:
            html_content += f"""
                    <span class="keyword-tag">{html.escape(keyword)}</span>"""
        
        html_content += """
                </div>
            </section>
        </article>
    </main>
    
    <footer class="footer">
        <p>&copy; 2024 HyperImage Framework. Scientific analysis techniques for conservation science.</p>
    </footer>
</body>
</html>"""
        
        return html_content
    
    def save(self, output_path: Path):
        """Save the reference page to a markdown file."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(self.to_markdown(), encoding='utf-8')
    
    def save_html(self, output_path: Path, all_techniques: Optional[Dict[str, str]] = None, base_url: str = ""):
        """Save the reference page as an HTML file."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        html_content = self.to_html(all_techniques, base_url)
        output_path.write_text(html_content, encoding='utf-8')
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TechniqueReference':
        """Create a TechniqueReference from a dictionary."""
        return cls(**data)


def create_reference_page(technique_name: str, data: Dict) -> TechniqueReference:
    """
    Create a reference page from technique name and data dictionary.
    
    Args:
        technique_name: Name of the technique
        data: Dictionary containing all section data
    
    Returns:
        TechniqueReference object
    """
    return TechniqueReference(technique_name=technique_name, **data)


def generate_page(technique_name: str, data: Dict, output_dir: Path = Path("output")) -> Path:
    """
    Generate and save a reference page.
    
    Args:
        technique_name: Name of the technique
        data: Dictionary containing all section data
        output_dir: Directory to save the output file
    
    Returns:
        Path to the generated file
    """
    ref = create_reference_page(technique_name, data)
    output_path = output_dir / f"{technique_name.lower().replace(' ', '_')}.md"
    ref.save(output_path)
    return output_path


class SiteGenerator:
    """Generate a complete HTML site with interlinked technique pages."""
    
    def __init__(self, output_dir: Path = Path("site"), base_url: str = ""):
        self.output_dir = Path(output_dir)
        self.base_url = base_url
        self.techniques: Dict[str, TechniqueReference] = {}
        self.technique_urls: Dict[str, str] = {}
    
    def add_technique(self, technique_name: str, data: Dict):
        """Add a technique to the site."""
        ref = create_reference_page(technique_name, data)
        self.techniques[technique_name] = ref
        filename = f"{technique_name.lower().replace(' ', '_')}.html"
        self.technique_urls[technique_name] = filename
    
    def generate_all_pages(self):
        """Generate all HTML pages for the site."""
        # Create output directory structure
        (self.output_dir / "assets").mkdir(parents=True, exist_ok=True)
        
        # Generate individual technique pages
        for technique_name, ref in self.techniques.items():
            filename = self.technique_urls[technique_name]
            output_path = self.output_dir / filename
            ref.save_html(output_path, self.technique_urls, self.base_url)
        
        # Generate index page
        self.generate_index()
        
        # Generate CSS
        self.generate_css()
    
    def generate_index(self):
        """Generate the index/navigation page."""
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HyperImage - Scientific Analysis Techniques</title>
    <link rel="stylesheet" href="{self.base_url}assets/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="{self.base_url}index.html" class="nav-logo">HyperImage</a>
            <ul class="nav-menu">
                <li><a href="{self.base_url}index.html">Home</a></li>
                <li><a href="#techniques">Techniques</a></li>
            </ul>
        </div>
    </nav>
    
    <main class="container">
        <header class="hero">
            <h1>HyperImage</h1>
            <p class="subtitle">Reference Documentation for Scientific Analysis Techniques in Conservation Science</p>
        </header>
        
        <section id="about" class="section">
            <h2>About</h2>
            <p>HyperImage provides comprehensive, practical reference documentation for scientific analysis techniques used in artwork analysis and conservation science. Each technique page includes detailed information on physics principles, instrumentation, protocols, data analysis, and troubleshooting.</p>
        </section>
        
        <section id="techniques" class="section">
            <h2>Available Techniques</h2>
            <div class="technique-grid">"""
        
        # Sort techniques alphabetically
        sorted_techniques = sorted(self.techniques.items())
        
        for technique_name, ref in sorted_techniques:
            filename = self.technique_urls[technique_name]
            html_content += f"""
                <div class="technique-card">
                    <h3><a href="{self.base_url}{filename}">{html.escape(technique_name)}</a></h3>
                    <p class="technique-summary">{html.escape(ref.one_line_summary)}</p>
                    <div class="technique-tags">
                        {''.join([f'<span class="keyword-tag">{html.escape(kw)}</span>' for kw in ref.keywords[:5]])}
                    </div>
                </div>"""
        
        html_content += """
            </div>
        </section>
    </main>
    
    <footer class="footer">
        <p>&copy; 2024 HyperImage Framework. Scientific analysis techniques for conservation science.</p>
    </footer>
</body>
</html>"""
        
        index_path = self.output_dir / "index.html"
        index_path.write_text(html_content, encoding='utf-8')
    
    def generate_css(self):
        """Generate the CSS stylesheet."""
        css_content = """/* HyperImage Framework Styles */

:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --background-color: #ffffff;
    --text-color: #333333;
    --border-color: #e0e0e0;
    --code-background: #f5f5f5;
    --link-color: #2980b9;
    --link-hover: #3498db;
    --navbar-bg: #2c3e50;
    --navbar-text: #ffffff;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--background-color);
}

/* Navigation */
.navbar {
    background-color: var(--navbar-bg);
    color: var(--navbar-text);
    padding: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--navbar-text);
    text-decoration: none;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    color: var(--navbar-text);
    text-decoration: none;
    transition: opacity 0.3s;
}

.nav-menu a:hover {
    opacity: 0.8;
}

/* Container */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 3rem 0;
    margin-bottom: 3rem;
}

.hero h1 {
    font-size: 3rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
}

.subtitle {
    font-size: 1.2rem;
    color: #666;
}

/* Sections */
.section {
    margin-bottom: 3rem;
}

.section h2 {
    font-size: 2rem;
    color: var(--primary-color);
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border-color);
}

.section h3 {
    font-size: 1.5rem;
    color: var(--primary-color);
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.section p {
    margin-bottom: 1rem;
}

.section ul, .section ol {
    margin-left: 2rem;
    margin-bottom: 1.5rem;
}

.section li {
    margin-bottom: 0.5rem;
}

/* Technique Page */
.technique-page {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.page-header {
    margin-bottom: 3rem;
    padding-bottom: 2rem;
    border-bottom: 3px solid var(--secondary-color);
}

.page-header h1 {
    font-size: 2.5rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
}

.summary {
    font-size: 1.2rem;
    color: #666;
    font-style: italic;
}

/* Code Blocks */
pre {
    background-color: var(--code-background);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    padding: 1rem;
    overflow-x: auto;
    margin: 1rem 0;
}

code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.9rem;
}

pre code {
    display: block;
    white-space: pre;
}

/* Links */
a {
    color: var(--link-color);
    text-decoration: none;
}

a:hover {
    color: var(--link-hover);
    text-decoration: underline;
}

.technique-link {
    font-weight: 600;
    border-bottom: 1px dotted var(--link-color);
}

.technique-link:hover {
    border-bottom: 1px solid var(--link-color);
}

/* References */
.references {
    list-style: none;
    margin-left: 0;
}

.references li {
    margin-bottom: 1rem;
    padding-left: 1.5rem;
    position: relative;
}

.references li::before {
    content: "📄";
    position: absolute;
    left: 0;
}

/* Checklist */
.checklist {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.checklist-item {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 0.75rem;
    background-color: #f9f9f9;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
}

.checklist-item:hover {
    background-color: #f0f0f0;
}

.checklist-item input[type="checkbox"] {
    margin-top: 0.25rem;
    cursor: pointer;
}

.checklist-item span {
    flex: 1;
}

/* Keywords */
.keywords {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
}

.keyword-tag {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background-color: var(--secondary-color);
    color: white;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}

/* Technique Grid (Index Page) */
.technique-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.technique-card {
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.2s, box-shadow 0.2s;
}

.technique-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.technique-card h3 {
    margin-bottom: 1rem;
}

.technique-card h3 a {
    color: var(--primary-color);
    font-size: 1.3rem;
}

.technique-summary {
    color: #666;
    margin-bottom: 1rem;
    font-size: 0.95rem;
}

.technique-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
}

/* Footer */
.footer {
    background-color: var(--primary-color);
    color: white;
    text-align: center;
    padding: 2rem;
    margin-top: 4rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-container {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-menu {
        flex-direction: column;
        gap: 0.5rem;
        text-align: center;
    }
    
    .container {
        padding: 1rem;
    }
    
    .hero h1 {
        font-size: 2rem;
    }
    
    .technique-grid {
        grid-template-columns: 1fr;
    }
    
    .technique-page {
        padding: 1rem;
    }
}

/* Print Styles */
@media print {
    .navbar, .footer {
        display: none;
    }
    
    .checklist-item input[type="checkbox"] {
        display: none;
    }
    
    .checklist-item::before {
        content: "☐ ";
    }
}
"""
        
        css_path = self.output_dir / "assets" / "style.css"
        css_path.write_text(css_content, encoding='utf-8')


if __name__ == "__main__":
    # Example usage
    print("HyperImage Framework")
    print("Use this framework to generate reference pages for scientific analysis techniques.")
    print("\nExample:")
    print("  from framework import generate_page")
    print("  generate_page('Raman microscopy', data_dict)")

