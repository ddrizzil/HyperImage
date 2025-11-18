import { getAllRFTechniques, getAllRFCategories } from '@/lib/rf-techniques'
import Link from 'next/link'
import { Radio, Wifi } from 'lucide-react'

export default function RFTechniquesPage() {
  const techniques = getAllRFTechniques()
  const categories = getAllRFCategories()

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-3 bg-blue-100 rounded-lg">
              <Radio className="w-8 h-8 text-blue-600" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-gray-900">RF Techniques</h1>
              <p className="text-lg text-gray-600 mt-1">
                Radio frequency, radar, and microwave analysis techniques
              </p>
            </div>
          </div>
          
          {/* Link to Imaging Techniques */}
          <div className="bg-blue-50 border-l-4 border-blue-500 rounded-r-lg p-4 mb-6">
            <div className="flex items-center gap-2">
              <Wifi className="w-5 h-5 text-blue-600" />
              <p className="text-sm text-blue-800">
                Looking for imaging techniques?{' '}
                <Link href="/techniques" className="font-semibold hover:underline">
                  View Imaging Techniques →
                </Link>
              </p>
            </div>
          </div>
        </div>

        {/* Results */}
        {techniques.length > 0 ? (
          <>
            <div className="mb-4 text-sm text-gray-600">
              Showing {techniques.length} RF technique{techniques.length !== 1 ? 's' : ''}
            </div>

            <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
              {techniques.map((technique) => (
                <div
                  key={technique.id}
                  className="bg-white rounded-lg shadow-sm border border-gray-200 p-6"
                >
                  <div className="flex items-start justify-between mb-3">
                    <h3 className="text-xl font-semibold text-primary-800">{technique.name}</h3>
                    {technique.acronym && (
                      <span className="text-sm font-mono bg-blue-100 text-blue-800 px-2 py-1 rounded">
                        {technique.acronym}
                      </span>
                    )}
                  </div>
                  <p className="text-gray-600 text-sm mb-4 line-clamp-2">{technique.summary}</p>
                  <div className="flex flex-wrap gap-2 mb-3">
                    <span className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded">
                      {technique.category}
                    </span>
                    <span className="text-xs bg-green-100 text-green-700 px-2 py-1 rounded">
                      {technique.destructiveness}
                    </span>
                    <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded">
                      {technique.portability}
                    </span>
                  </div>
                  <div className="flex flex-wrap gap-1">
                    {(technique.tags || []).slice(0, 3).map((tag, idx) => (
                      <span
                        key={idx}
                        className="text-xs bg-gray-50 text-gray-600 px-2 py-0.5 rounded"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </>
        ) : (
          <div className="text-center py-12 bg-white rounded-lg shadow-sm border border-gray-200">
            <Radio className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-900 mb-2">No RF Techniques Yet</h3>
            <p className="text-gray-600 mb-6 max-w-md mx-auto">
              RF techniques are being prepared in a separate branch. This section will contain
              radio frequency, radar, and microwave analysis techniques for cultural heritage.
            </p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Link
                href="/techniques"
                className="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
              >
                View Imaging Techniques
              </Link>
              <Link
                href="/"
                className="inline-flex items-center px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors"
              >
                Back to Home
              </Link>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
