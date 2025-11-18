# HyperImage Web Application - Setup Guide

## Quick Start

1. **Install Dependencies**
   ```bash
   cd hyperImage/web
   npm install
   ```

2. **Run Development Server**
   ```bash
   npm run dev
   ```

3. **Open in Browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## What's Included

### ✅ Complete Project Structure
- Next.js 14 with App Router
- TypeScript configuration
- Tailwind CSS styling
- ESLint and Prettier setup

### ✅ Data Model
- Complete TypeScript interfaces in `src/types/technique.ts`
- MA-XRF example technique with full data in `src/data/techniques/ma-xrf.json`

### ✅ Core Pages
- **Home Page** (`/`) - Hero section, search bar, category browser, stats, featured techniques
- **Techniques List** (`/techniques`) - Browseable, filterable, searchable list
- **Technique Detail** (`/techniques/[id]`) - Complete detail page with all sections
- **Multimodal** (`/multimodal`) - Browse technique combinations

### ✅ Components
- `Navigation` - Sticky navbar with mobile menu
- `Footer` - Site footer
- `TableOfContents` - Sticky TOC for technique pages
- `TechniqueContent` - Renders all technique sections
- `MarkdownContent` - Simple markdown renderer
- `Equation` - LaTeX equation renderer using KaTeX

### ✅ Features Implemented
- ✅ Responsive design (mobile-first)
- ✅ Search functionality
- ✅ Category filtering
- ✅ Sticky navigation
- ✅ Table of contents with active section highlighting
- ✅ LaTeX equation rendering
- ✅ Markdown content rendering
- ✅ Related techniques sidebar
- ✅ Multimodal combinations page
- ✅ SEO-friendly metadata
- ✅ Static export ready

## Next Steps

### Adding More Techniques

1. Create a new JSON file in `src/data/techniques/` (e.g., `raman-microscopy.json`)
2. Follow the `Technique` interface from `src/types/technique.ts`
3. Update `src/lib/techniques.ts` to load the new technique:

```typescript
import ramanData from '@/data/techniques/raman-microscopy.json'

// In getAllTechniques():
techniquesCache.set('raman-microscopy', ramanData as Technique)
```

### Enhancing Search

Currently using simple string matching. To add fuzzy search:

1. Import Fuse.js (already in dependencies)
2. Update `searchTechniques()` in `src/lib/techniques.ts`:

```typescript
import Fuse from 'fuse.js'

const fuse = new Fuse(techniques, {
  keys: ['name', 'summary', 'keyApplications', 'tags'],
  threshold: 0.3,
})
return fuse.search(query).map(result => result.item)
```

### Adding Interactive Features (Phase 2)

- Interactive spectra visualizations (D3.js or Plotly)
- Technique comparison tool
- Decision tree ("Which technique should I use?")
- Cost estimator
- Network graph for multimodal relationships

## Deployment

### Static Export (Recommended)

The app is configured for static export:

```bash
npm run build
```

This creates an `out/` directory with static HTML files ready for:
- Vercel
- Netlify
- GitHub Pages
- Any static hosting service

### Environment Variables

Currently none required. For future API integration, create `.env.local`:

```
NEXT_PUBLIC_API_URL=https://api.example.com
```

## Project Structure

```
web/
├── src/
│   ├── app/                    # Next.js pages
│   │   ├── layout.tsx         # Root layout
│   │   ├── page.tsx           # Home page
│   │   ├── globals.css        # Global styles
│   │   ├── techniques/       # Technique pages
│   │   │   ├── page.tsx      # List page
│   │   │   └── [id]/page.tsx # Detail page
│   │   └── multimodal/       # Multimodal page
│   ├── components/            # React components
│   ├── data/                 # JSON data files
│   │   └── techniques/
│   ├── lib/                  # Utilities
│   │   ├── techniques.ts     # Data loading
│   │   └── utils.ts          # Helper functions
│   └── types/                # TypeScript types
│       └── technique.ts      # Technique interface
├── public/                   # Static assets
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.js
```

## Troubleshooting

### Port Already in Use
```bash
# Use a different port
npm run dev -- -p 3001
```

### Type Errors
```bash
# Check types
npm run type-check
```

### Build Errors
```bash
# Clear cache and rebuild
rm -rf .next out node_modules
npm install
npm run build
```

## Support

For issues or questions, check the main README.md or create an issue in the repository.

