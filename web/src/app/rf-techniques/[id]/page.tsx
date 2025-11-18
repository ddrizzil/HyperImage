import { notFound } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, ExternalLink, Radio } from 'lucide-react'
import { getRFTechniqueById, getAllRFTechniques } from '@/lib/rf-techniques'
import { TechniqueContent } from '@/components/TechniqueContent'
import { TableOfContents } from '@/components/TableOfContents'

export async function generateMetadata({ params }: { params: { id: string } }) {
  const technique = getRFTechniqueById(params.id)

  if (!technique) {
    return {
      title: 'RF Technique Not Found',
    }
  }

  return {
    title: `${technique.name} - HyperImage RF Techniques`,
    description: technique.summary,
  }
}

export async function generateStaticParams() {
  const techniques = getAllRFTechniques()
  return techniques.map((technique) => ({
    id: technique.id,
  }))
}

export default function RFTechniquePage({ params }: { params: { id: string } }) {
  const technique = getRFTechniqueById(params.id)

  if (!technique) {
    notFound()
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="bg-white border-b">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
          <Link
            href="/rf-techniques"
            className="inline-flex items-center text-primary-600 hover:text-primary-800 mb-4"
          >
            <ArrowLeft className="h-4 w-4 mr-2" />
            Back to RF Techniques
          </Link>

          <div className="flex items-start justify-between">
            <div>
              <div className="flex items-center gap-3 mb-2">
                <Radio className="w-6 h-6 text-blue-600" />
                <h1 className="text-4xl font-bold text-gray-900">{technique.name}</h1>
                {technique.acronym && (
                  <span className="text-2xl font-mono text-gray-500">({technique.acronym})</span>
                )}
              </div>
              <p className="text-lg text-gray-600 mb-4">{technique.summary}</p>
              <div className="flex flex-wrap gap-2 mb-4">
                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
                  RF Technique
                </span>
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
              
              {/* Link to Imaging Techniques */}
              <div className="mt-8 bg-blue-50 p-4 rounded-lg shadow-sm border border-blue-200">
                <div className="flex items-start gap-2 mb-2">
                  <Radio className="w-5 h-5 text-blue-600 flex-shrink-0 mt-0.5" />
                  <h3 className="font-semibold text-blue-900">RF Techniques</h3>
                </div>
                <p className="text-sm text-blue-800 mb-3">
                  This is an RF technique. View imaging techniques for optical, X-ray, and other imaging methods.
                </p>
                <Link
                  href="/techniques"
                  className="inline-flex items-center text-sm font-medium text-blue-600 hover:text-blue-800 hover:underline"
                >
                  View Imaging Techniques
                  <ExternalLink className="w-3 h-3 ml-1" />
                </Link>
              </div>
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

