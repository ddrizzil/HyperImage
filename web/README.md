# HyperImage Web Application

Modern web application for browsing and searching scientific analysis techniques in conservation science.

## Features

- **Comprehensive Technique Documentation**: Detailed pages for each technique with physics, instrumentation, protocols, and data analysis
- **Search & Filter**: Search across all techniques and filter by category, destructiveness, and portability
- **Multimodal Combinations**: Explore how techniques can be combined
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Fast & SEO-Friendly**: Optimized for static hosting

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn

### Installation

```bash
cd web
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
npm run build
```

This generates a static site in the `out/` directory, ready for deployment to Vercel, Netlify, or GitHub Pages.

## Project Structure

```
web/
├── src/
│   ├── app/              # Next.js app router pages
│   │   ├── page.tsx      # Home page
│   │   ├── techniques/   # Technique pages
│   │   └── multimodal/   # Multimodal combinations page
│   ├── components/       # React components
│   ├── data/            # Technique JSON data files
│   ├── lib/             # Utility functions
│   └── types/           # TypeScript type definitions
├── public/              # Static assets
└── package.json
```

## Adding New Techniques

1. Create a JSON file in `src/data/techniques/` following the `Technique` interface
2. Update `src/lib/techniques.ts` to load the new technique
3. The technique will automatically appear in listings and search

## Tech Stack

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **KaTeX** - LaTeX equation rendering
- **Fuse.js** - Fuzzy search (for future enhancement)

## License

MIT

