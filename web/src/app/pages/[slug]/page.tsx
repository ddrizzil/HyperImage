import { notFound } from 'next/navigation'
import fs from 'fs'
import path from 'path'
import { BlockMath } from 'react-katex'
import 'katex/dist/katex.min.css'
import Link from 'next/link'

// Get all available page slugs
export async function generateStaticParams() {
  const pagesDir = path.join(process.cwd(), 'src', 'content', 'pages')
  if (!fs.existsSync(pagesDir)) {
    return []
  }
  
  const files = fs.readdirSync(pagesDir)
  return files
    .filter((file) => file.endsWith('.mdx'))
    .map((file) => ({
      slug: file.replace(/\.mdx$/, ''),
    }))
}

// Metadata generation
export async function generateMetadata({ params }: { params: { slug: string } }) {
  const pagesDir = path.join(process.cwd(), 'src', 'content', 'pages')
  const filePath = path.join(pagesDir, `${params.slug}.mdx`)
  
  if (!fs.existsSync(filePath)) {
    return {
      title: 'Page Not Found',
    }
  }
  
  const fileContent = fs.readFileSync(filePath, 'utf-8')
  const titleMatch = fileContent.match(/title:\s*"([^"]+)"/)
  const title = titleMatch ? titleMatch[1] : params.slug
  
  return {
    title: `${title} | HyperImage`,
    description: `Chemical and pigment information for ${title}`,
  }
}

// Simple MDX parser
function parseMDX(content: string) {
  const frontmatter: Record<string, string> = {}
  let body = content
  
  // Extract frontmatter
  const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/)
  if (frontmatterMatch) {
    const frontmatterText = frontmatterMatch[1]
    body = frontmatterMatch[2]
    
    // Parse frontmatter
    frontmatterText.split('\n').forEach((line) => {
      const match = line.match(/^(\w+):\s*"([^"]+)"/)
      if (match) {
        frontmatter[match[1]] = match[2]
      }
    })
  }
  
  return { frontmatter, body }
}

// Render MDX content with LaTeX support
function renderMDX(body: string) {
  const parts: JSX.Element[] = []
  let key = 0
  
  // Split by sections (## headings)
  const sections = body.split(/^##\s+(.+)$/gm)
  
  sections.forEach((section, idx) => {
    if (idx === 0 && section.trim()) {
      // Overview section (before first ##)
      parts.push(
        <div key={key++} className="mb-8">
          <h2 className="text-3xl font-bold mb-4">Overview</h2>
          {renderSection(section)}
        </div>
      )
    } else if (idx % 2 === 1) {
      // This is a heading
      const heading = section.trim()
      const content = sections[idx + 1] || ''
      
      if (heading) {
        parts.push(
          <div key={key++} className="mb-8">
            <h2 className="text-3xl font-bold mb-4">{heading}</h2>
            {renderSection(content)}
          </div>
        )
      }
    }
  })
  
  return parts
}

function renderSection(content: string) {
  const elements: JSX.Element[] = []
  let key = 0
  
  // Process LaTeX equations ($$...$$)
  const equationRegex = /\$\$([\s\S]*?)\$\$/g
  const parts = content.split(equationRegex)
  
  parts.forEach((part, idx) => {
    if (idx % 2 === 0) {
      // Regular text
      if (part.trim()) {
        // Process links [text](/pages/slug)
        const linkRegex = /\[([^\]]+)\]\(\/pages\/([^)]+)\)/g
        let lastIndex = 0
        let match
        
        while ((match = linkRegex.exec(part)) !== null) {
          // Add text before link
          if (match.index > lastIndex) {
            const text = part.substring(lastIndex, match.index)
            elements.push(<span key={`text-${key++}`}>{text}</span>)
          }
          
          // Add link
          elements.push(
            <Link
              key={`link-${key++}`}
              href={`/pages/${match[2]}`}
              className="text-primary-600 hover:text-primary-800 underline"
            >
              {match[1]}
            </Link>
          )
          
          lastIndex = match.index + match[0].length
        }
        
        // Add remaining text
        if (lastIndex < part.length) {
          elements.push(<span key={`text-${key++}`}>{part.substring(lastIndex)}</span>)
        }
        
        // If no links, add whole text
        if (elements.length === 0 || !linkRegex.test(part)) {
          const lines = part.split('\n').filter((l) => l.trim())
          lines.forEach((line) => {
            elements.push(
              <p key={`p-${key++}`} className="mb-4">
                {line.trim()}
              </p>
            )
          })
        }
      }
    } else {
      // LaTeX equation
      elements.push(
        <div key={`eq-${key++}`} className="my-6 p-4 bg-gray-50 rounded-lg overflow-x-auto">
          <BlockMath math={part.trim()} />
        </div>
      )
    }
  })
  
  return <div>{elements}</div>
}

export default async function Page({ params }: { params: { slug: string } }) {
  const pagesDir = path.join(process.cwd(), 'src', 'content', 'pages')
  const filePath = path.join(pagesDir, `${params.slug}.mdx`)
  
  if (!fs.existsSync(filePath)) {
    notFound()
  }
  
  const source = fs.readFileSync(filePath, 'utf-8')
  const { frontmatter, body } = parseMDX(source)
  
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-4xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-6">
          <Link
            href="/pages"
            className="inline-flex items-center text-primary-600 hover:text-primary-800 mb-4"
          >
            ← Back to Pages
          </Link>
        </div>
        
        <article className="bg-white rounded-lg shadow-sm border border-gray-200 p-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            {frontmatter.title || params.slug}
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
