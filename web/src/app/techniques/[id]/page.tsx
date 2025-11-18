import { notFound } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, ExternalLink, CheckCircle2, BarChart3 } from 'lucide-react'
import { getTechniqueById, getRelatedTechniques } from '@/lib/techniques'
import { TechniqueContent } from '@/components/TechniqueContent'
import { TableOfContents } from '@/components/TableOfContents'

export async function generateMetadata({ params }: { params: { id: string } }) {
  const technique = getTechniqueById(params.id)

  if (!technique) {
    return {
      title: 'Technique Not Found',
    }
  }

  return {
    title: `${technique.name} - HyperImage`,
    description: technique.summary,
  }
}

export async function generateStaticParams() {
  const { getAllTechniques } = await import('@/lib/techniques')
  const techniques = getAllTechniques()
  return techniques.map((technique) => ({
    id: technique.id,
  }))
}

export default function TechniquePage({ params }: { params: { id: string } }) {
  const technique = getTechniqueById(params.id)
  const relatedTechniques = technique ? getRelatedTechniques(technique) : []

  if (!technique) {
    notFound()
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="bg-white border-b">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
          <Link
            href="/techniques"
            className="inline-flex items-center text-primary-600 hover:text-primary-800 mb-4"
          >
            <ArrowLeft className="h-4 w-4 mr-2" />
            Back to Techniques
          </Link>

          <div className="flex items-start justify-between">
            <div>
              <div className="flex items-center gap-3 mb-2">
                <h1 className="text-4xl font-bold text-gray-900">{technique.name}</h1>
                {technique.acronym && (
                  <span className="text-2xl font-mono text-gray-500">({technique.acronym})</span>
                )}
              </div>
              <p className="text-lg text-gray-600 mb-4">{technique.summary}</p>
              <div className="flex flex-wrap gap-2 mb-4">
                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-primary-100 text-primary-800">
                  {technique.category}
                </span>
                {technique.subcategory && (
                  <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
                    {technique.subcategory}
                  </span>
                )}
                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
                  {technique.destructiveness}
                </span>
                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
                  {technique.portability}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-4">
          {/* Table of Contents Sidebar */}
          <aside className="lg:col-span-1">
            <div className="sticky top-20">
              <TableOfContents technique={technique} />
              {/* Comparison Link for Nonlinear Microscopy */}
              {(technique.id === 'shg-microscopy' || 
                technique.id === 'thg-microscopy' || 
                technique.id === 'tpef-microscopy' ||
                technique.id === 'cars-microscopy') && (
                <div className="mt-8 bg-gradient-to-br from-indigo-50 to-purple-50 p-4 rounded-lg shadow-sm border border-indigo-200">
                  <div className="flex items-start gap-2 mb-2">
                    <BarChart3 className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
                    <h3 className="font-semibold text-indigo-900">Compare Techniques</h3>
                  </div>
                  <p className="text-sm text-indigo-800 mb-3">
                    {technique.id === 'cars-microscopy' 
                      ? "CARS is related to other nonlinear microscopy techniques. Compare SHG, THG, and TPEF to understand the broader family of label-free imaging methods."
                      : "See how this technique compares to other nonlinear microscopy methods."}
                  </p>
                  <Link
                    href="/comparisons/nonlinear-microscopy"
                    className="inline-flex items-center text-sm font-medium text-indigo-600 hover:text-indigo-800 hover:underline"
                  >
                    View Comparison
                    <ExternalLink className="w-3 h-3 ml-1" />
                  </Link>
                </div>
              )}

              {relatedTechniques.length > 0 && (
                <div className="mt-8 bg-white p-4 rounded-lg shadow-sm border border-gray-200">
                  <h3 className="font-semibold mb-3 text-gray-900">Related Techniques</h3>
                  <ul className="space-y-2">
                    {relatedTechniques.map((related) => (
                      <li key={related.id}>
                        <Link
                          href={`/techniques/${related.id}`}
                          className="text-sm text-primary-600 hover:text-primary-800 hover:underline"
                        >
                          {related.name}
                        </Link>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </aside>

          {/* Main Content */}
          <div className="lg:col-span-3">
            <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-8">
              <TechniqueContent technique={technique} />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

