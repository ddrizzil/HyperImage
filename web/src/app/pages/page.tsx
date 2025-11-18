import Link from 'next/link'
import fs from 'fs'
import path from 'path'

type PageInfo = {
  slug: string
  title: string
  category: string
}

// Get all pages
function getAllPages(): Record<string, PageInfo[]> {
  const pagesDir = path.join(process.cwd(), 'src', 'content', 'pages')
  if (!fs.existsSync(pagesDir)) {
    return {}
  }
  
  const files = fs.readdirSync(pagesDir)
  const pages: PageInfo[] = []
  
  files
    .filter((file) => file.endsWith('.mdx'))
    .forEach((file) => {
      const filePath = path.join(pagesDir, file)
      const content = fs.readFileSync(filePath, 'utf-8')
      const titleMatch = content.match(/title:\s*"([^"]+)"/)
      const categoryMatch = content.match(/category:\s*"([^"]+)"/)
      
      pages.push({
        slug: file.replace(/\.mdx$/, ''),
        title: titleMatch ? titleMatch[1] : file.replace(/\.mdx$/, ''),
        category: categoryMatch ? categoryMatch[1] : 'Other',
      })
    })
  
  // Group by category
  const grouped = pages.reduce((acc: Record<string, PageInfo[]>, page: PageInfo) => {
    if (!acc[page.category]) {
      acc[page.category] = []
    }
    acc[page.category].push(page)
    return acc
  }, {})
  
  return grouped
}

export default function PagesIndex() {
  const pagesByCategory = getAllPages()
  const categories = Object.keys(pagesByCategory).sort()
  
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">Pigments & Chemical Equations</h1>
        <p className="text-lg text-gray-600 mb-8">
          Comprehensive reference for historic pigments, chemical processes, and degradation pathways
        </p>
        
        {categories.map((category) => (
          <div key={category} className="mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">{category}</h2>
            <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
              {pagesByCategory[category]
                .sort((a, b) => a.title.localeCompare(b.title))
                .map((page) => (
                  <Link
                    key={page.slug}
                    href={`/pages/${page.slug}`}
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

