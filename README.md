# HyperImage

A comprehensive reference system for imaging techniques and optical physics used in cultural heritage analysis and conservation science.

## Overview

HyperImage provides two complementary systems:

1. **Next.js Web Application** (`/web`) - Interactive web interface with search, filtering, and detailed technique pages
2. **Python Static Site Generator** (`/techniques`) - Framework for generating static HTML documentation sites

## Features

### Web Application (`/web`)
- **Interactive technique browser** - Search and filter imaging techniques
- **Detailed technique pages** - Comprehensive information on each technique
- **Optics reference library** - Graduate-level optical physics content
- **Pigments & Chemistry** - Chemical analysis reference pages
- **Responsive design** - Works on desktop, tablet, and mobile
- **TypeScript** - Type-safe development
- **MDX support** - Markdown with LaTeX equations

### Static Site Generator (`/techniques`)
- **HyperPhysics-style pages** - Standardized 16-section format
- **Interlinked HTML pages** - Automatic cross-linking between techniques
- **Navigation system** - Easy browsing between techniques
- **Professional styling** - Clean, modern interface

## Quick Start

### Web Application

```bash
cd web
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Static Site Generator

```bash
python example_raman.py
```

This generates a complete HTML site in the `site/` directory.

## Project Structure

```
hyperImage/
├── web/                    # Next.js web application
│   ├── src/
│   │   ├── app/           # Next.js app router pages
│   │   ├── components/    # React components
│   │   ├── data/          # Technique JSON data
│   │   ├── content/       # MDX content (optics, pages)
│   │   └── lib/           # Utility functions
│   └── package.json
├── techniques/            # Python technique definitions
│   ├── __init__.py
│   └── *.py              # Individual technique modules
├── optics/               # Optics reference content
│   ├── 01_FOUNDATIONS_OF_OPTICS_DEEP.md
│   └── VARIABLES.md
├── framework.py          # Static site generator framework
└── example_raman.py      # Example usage
```

## Techniques Included

The system includes comprehensive data on:

- **Molecular Spectroscopy**: Raman, FTIR, Micro-Raman
- **Elemental Analysis**: XRF, MA-XRF, Synchrotron XRF, PIXE
- **Imaging Techniques**: OCT, Macro Photography, UV Fluorescence, Raking Light
- **Hybrid Imaging**: Photoacoustic Tomography, OR-PAM
- **Advanced Techniques**: XANES, CARS, SHG, THG
- And many more...

## Development

### Adding a New Technique

1. Create a JSON file in `web/src/data/techniques/` following the TypeScript `Technique` interface
2. Register it in `web/src/lib/techniques.ts`
3. Optionally create a Python module in `techniques/` for static site generation

### Adding Optics Content

Create MDX files in `web/src/content/optics/` with frontmatter:

```mdx
---
title: "Your Title"
slug: "your-slug"
category: "Category"
---

Your content with LaTeX: $E = mc^2$
```

## Technologies

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **MDX** - Markdown with JSX
- **Python 3.7+** - Static site generator

## License

This project is designed for creating documentation and reference materials for scientific analysis techniques in conservation science and cultural heritage research.
