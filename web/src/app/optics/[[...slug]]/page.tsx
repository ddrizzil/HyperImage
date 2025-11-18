import { notFound } from 'next/navigation'
import fs from 'fs'
import path from 'path'
import { BlockMath, InlineMath } from 'react-katex'
import 'katex/dist/katex.min.css'
import Link from 'next/link'

interface OpticsPage {
  slug: string[]
  title: string
  category: string
  path: string
}

function getAllOpticsPages(): Record<string, OpticsPage[]> {
  const opticsDir = path.join(process.cwd(), 'src', 'content', 'optics')
  if (!fs.existsSync(opticsDir)) {
    return {}
  }
  
  const pages: OpticsPage[] = []
  
  function scanDirectory(dir: string, basePath: string[] = []) {
    const entries = fs.readdirSync(dir, { withFileTypes: true })
    
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name)
      
      if (entry.isDirectory()) {
        scanDirectory(fullPath, [...basePath, entry.name])
      } else if (entry.isFile() && entry.name.endsWith('.mdx')) {
        const slug = entry.name.replace(/\.mdx$/, '')
        const fileContent = fs.readFileSync(fullPath, 'utf-8')
        const titleMatch = fileContent.match(/title:\s*"([^"]+)"/)
        const categoryMatch = fileContent.match(/category:\s*"([^"]+)"/)
        
        pages.push({
          slug: [...basePath, slug],
          title: titleMatch ? titleMatch[1] : slug,
          category: categoryMatch ? categoryMatch[1] : basePath[0] || 'Other',
          path: [...basePath, slug].join('/'),
        })
      }
    }
  }
  
  scanDirectory(opticsDir)
  
  // Group by category
  const grouped = pages.reduce((acc, page) => {
    if (!acc[page.category]) {
      acc[page.category] = []
    }
    acc[page.category].push(page)
    return acc
  }, {} as Record<string, OpticsPage[]>)
  
  return grouped
}

// Get all available optics pages for static generation
export async function generateStaticParams() {
  const opticsDir = path.join(process.cwd(), 'src', 'content', 'optics')
  if (!fs.existsSync(opticsDir)) {
    return []
  }
  
  const pages: Array<{ slug: string[] }> = []
  
  function scanDirectory(dir: string, basePath: string[] = []) {
    const entries = fs.readdirSync(dir, { withFileTypes: true })
    
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name)
      
      if (entry.isDirectory()) {
        scanDirectory(fullPath, [...basePath, entry.name])
      } else if (entry.isFile() && entry.name.endsWith('.mdx')) {
        const slug = entry.name.replace(/\.mdx$/, '')
        pages.push({ slug: [...basePath, slug] })
      }
    }
  }
  
  scanDirectory(opticsDir)
  return pages
}

// Metadata generation
export async function generateMetadata({ params }: { params: { slug?: string[] } }) {
  const slug = params.slug || []
  
  // Index page metadata
  if (slug.length === 0) {
    return {
      title: 'Fundamentals of Optics | HyperImage',
      description: 'Comprehensive reference for optical principles, equations, materials, and advanced techniques',
    }
  }
  
  const opticsDir = path.join(process.cwd(), 'src', 'content', 'optics')
  const filePath = path.join(opticsDir, ...slug.slice(0, -1), `${slug[slug.length - 1]}.mdx`)
  
  if (!fs.existsSync(filePath)) {
    return { title: 'Page Not Found' }
  }
  
  const fileContent = fs.readFileSync(filePath, 'utf-8')
  const titleMatch = fileContent.match(/title:\s*"([^"]+)"/)
  const title = titleMatch ? titleMatch[1] : slug[slug.length - 1]
  
  return {
    title: `${title} | Optics Reference`,
    description: `Optical principles and equations for ${title}`,
  }
}

// Simple MDX parser
function parseMDX(content: string) {
  const frontmatter: Record<string, string> = {}
  let body = content
  
  const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/)
  if (frontmatterMatch) {
    const frontmatterText = frontmatterMatch[1]
    body = frontmatterMatch[2]
    
    frontmatterText.split('\n').forEach((line) => {
      const match = line.match(/^(\w+):\s*"([^"]+)"/)
      if (match) {
        frontmatter[match[1]] = match[2]
      }
    })
  }
  
  return { frontmatter, body }
}

// Render MDX content with LaTeX and cross-links
function renderMDX(body: string) {
  const parts: JSX.Element[] = []
  let key = 0
  
  // Split by sections (## and ### headings)
  const sections = body.split(/^(##+\s+.+)$/gm)
  
  sections.forEach((section, idx) => {
    if (idx === 0 && section.trim()) {
      // Content before first heading
      parts.push(<div key={key++}>{renderContent(section)}</div>)
    } else if (idx % 2 === 1) {
      // This is a heading
      const heading = section.trim()
      const content = sections[idx + 1] || ''
      
      if (heading) {
        const level = heading.match(/^#+/)?.[0].length || 2
        const text = heading.replace(/^#+\s+/, '')
        const HeadingTag = `h${level}` as keyof JSX.IntrinsicElements
        
        parts.push(
          <div key={key++} className="mb-8 scroll-mt-20" id={text.toLowerCase().replace(/\s+/g, '-')}>
            <HeadingTag className={`font-bold mb-4 ${level === 2 ? 'text-3xl' : level === 3 ? 'text-2xl' : 'text-xl'}`}>
              {text}
            </HeadingTag>
            {renderContent(content)}
          </div>
        )
      }
    }
  })
  
  return parts
}

function renderContent(content: string) {
  const elements: JSX.Element[] = []
  let key = 0
  
  // Process LaTeX equations first ($$...$$ for block, $...$ for inline)
  const blockEqRegex = /\$\$([\s\S]*?)\$\$/g
  const inlineEqRegex = /\$([^\$]+)\$/g
  
  // Split by block equations
  const blockParts = content.split(blockEqRegex)
  
  blockParts.forEach((part, idx) => {
    if (idx % 2 === 0) {
      // Regular text - process inline equations and links
      const inlineParts = part.split(inlineEqRegex)
      
      inlineParts.forEach((inlinePart, inlineIdx) => {
        if (inlineIdx % 2 === 0) {
          // Regular text - process links and formatting
          const processed = processText(inlinePart, key++)
          if (Array.isArray(processed)) {
            elements.push(...processed)
          } else {
            elements.push(processed)
          }
        } else {
          // Inline equation
          elements.push(
            <InlineMath key={`inline-eq-${key++}`} math={inlinePart.trim()} />
          )
        }
      })
    } else {
      // Block equation
      elements.push(
        <div key={`block-eq-${key++}`} className="my-6 p-4 bg-gray-50 rounded-lg overflow-x-auto">
          <BlockMath math={part.trim()} />
        </div>
      )
    }
  })
  
  return <div>{elements}</div>
}

function processText(text: string, baseKey: number): JSX.Element | JSX.Element[] {
  const elements: JSX.Element[] = []
  let key = baseKey
  
  // Process links [text](/optics/path)
  const linkRegex = /\[([^\]]+)\]\(\/optics\/([^)]+)\)/g
  let lastIndex = 0
  let match
  
  while ((match = linkRegex.exec(text)) !== null) {
    // Add text before link
    if (match.index > lastIndex) {
      const beforeText = text.substring(lastIndex, match.index)
      const lines = beforeText.split('\n').filter((l) => l.trim())
      lines.forEach((line) => {
        elements.push(
          <p key={`text-${key++}`} className="mb-4 leading-relaxed">
            {line.trim()}
          </p>
        )
      })
    }
    
    // Add link
    elements.push(
      <Link
        key={`link-${key++}`}
        href={`/optics/${match[2]}`}
        className="text-primary-600 hover:text-primary-800 underline"
      >
        {match[1]}
      </Link>
    )
    
    lastIndex = match.index + match[0].length
  }
  
  // Add remaining text
  if (lastIndex < text.length) {
    const remaining = text.substring(lastIndex)
    const lines = remaining.split('\n').filter((l) => l.trim())
    lines.forEach((line) => {
      elements.push(
        <p key={`text-${key++}`} className="mb-4 leading-relaxed">
          {line.trim()}
        </p>
      )
    })
  }
  
  // If no links found, return simple paragraphs
  if (elements.length === 0) {
    const lines = text.split('\n').filter((l) => l.trim())
    return lines.map((line) => (
      <p key={`p-${key++}`} className="mb-4 leading-relaxed">
        {line.trim()}
      </p>
    ))
  }
  
  return elements
}

const categoryOrder = [
  'Fundamentals',
  'Geometric Optics',
  'Wave Optics',
  'Interactions',
  'Materials',
  'Detection',
  'Advanced Methods',
  'Computational',
  'Spectroscopy',
  'Applications',
]

export default async function OpticsPage({ params }: { params: { slug?: string[] } }) {
  const slug = params.slug || []
  
  // If no slug, show index page
  if (slug.length === 0) {
    const pagesByCategory = getAllOpticsPages()
    const categories = Object.keys(pagesByCategory).sort((a, b) => {
      const aIdx = categoryOrder.indexOf(a)
      const bIdx = categoryOrder.indexOf(b)
      if (aIdx === -1 && bIdx === -1) return a.localeCompare(b)
      if (aIdx === -1) return 1
      if (bIdx === -1) return -1
      return aIdx - bIdx
    })
    
    return (
      <div className="min-h-screen bg-gray-50">
        <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Fundamentals of Optics
          </h1>
          <p className="text-lg text-gray-600 mb-8">
            Comprehensive reference for optical principles, equations, materials, and advanced techniques
          </p>
          
          {categories.map((category) => (
            <div key={category} className="mb-12">
              <h2 className="text-2xl font-semibold text-gray-900 mb-4">{category}</h2>
              <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                {pagesByCategory[category]
                  .sort((a, b) => a.title.localeCompare(b.title))
                  .map((page) => (
                    <Link
                      key={page.path}
                      href={`/optics/${page.path}`}
                      className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
                    >
                      <h3 className="text-xl font-semibold text-primary-800 mb-2">{page.title}</h3>
                      <p className="text-sm text-gray-600">View details →</p>
                    </Link>
                  ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    )
  }
  
  // Otherwise, show content page
  const opticsDir = path.join(process.cwd(), 'src', 'content', 'optics')
  const filePath = path.join(opticsDir, ...slug.slice(0, -1), `${slug[slug.length - 1]}.mdx`)
  
  if (!fs.existsSync(filePath)) {
    notFound()
  }
  
  const source = fs.readFileSync(filePath, 'utf-8')
  const { frontmatter, body } = parseMDX(source)
  
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-5xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-6">
          <Link
            href="/optics"
            className="inline-flex items-center text-primary-600 hover:text-primary-800 mb-4"
          >
            ← Back to Optics Index
          </Link>
        </div>
        
        <article className="bg-white rounded-lg shadow-sm border border-gray-200 p-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            {frontmatter.title || slug[slug.length - 1]}
          </h1>
          {frontmatter.category && (
            <p className="text-sm text-gray-600 mb-6">
              Category: <span className="font-semibold">{frontmatter.category}</span>
            </p>
          )}
          
          <div className="prose prose-lg max-w-none">
            {renderMDX(body)}
          </div>
        </article>
      </div>
    </div>
  )
}

