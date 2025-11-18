'use client'

import { getAllTechniques, getAllCategories, searchTechniques } from '@/lib/techniques'
import Link from 'next/link'
import { Search, Camera, Radio } from 'lucide-react'
import { useRouter, useSearchParams } from 'next/navigation'
import { useState, useEffect, Suspense } from 'react'

function TechniquesContent() {
  const router = useRouter()
  const searchParams = useSearchParams()
  const [searchQuery, setSearchQuery] = useState(searchParams.get('q') || '')
  
  const category = searchParams.get('category') || ''
  const q = searchParams.get('q') || ''

  // Sync search query with URL params
  useEffect(() => {
    setSearchQuery(searchParams.get('q') || '')
  }, [searchParams])

  let techniques = getAllTechniques()
  const categories = getAllCategories()

  // Apply filters
  if (category) {
    techniques = techniques.filter((t) => t.category === category)
  }

  if (q) {
    techniques = searchTechniques(q)
  }

  // Sort techniques alphabetically by name
  techniques = techniques.sort((a, b) => a.name.localeCompare(b.name))

  const handleCategoryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const newCategory = e.target.value
    const params = new URLSearchParams(searchParams.toString())
    
    if (newCategory) {
      params.set('category', newCategory)
    } else {
      params.delete('category')
    }
    
    router.push(`/techniques?${params.toString()}`)
  }

  const handleSearchSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const params = new URLSearchParams(searchParams.toString())
    
    if (searchQuery) {
      params.set('q', searchQuery)
    } else {
      params.delete('q')
    }
    
    router.push(`/techniques?${params.toString()}`)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-3 bg-primary-100 rounded-lg">
              <Camera className="w-8 h-8 text-primary-600" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-gray-900">Imaging Techniques</h1>
              <p className="text-lg text-gray-600 mt-1">
                Optical, X-ray, electron, and other imaging methods for conservation science
              </p>
            </div>
          </div>
          
          {/* Link to RF Techniques */}
          <div className="bg-blue-50 border-l-4 border-blue-500 rounded-r-lg p-4 mb-6">
            <div className="flex items-center gap-2">
              <Radio className="w-5 h-5 text-blue-600" />
              <p className="text-sm text-blue-800">
                Looking for RF techniques?{' '}
                <Link href="/rf-techniques" className="font-semibold hover:underline">
                  View RF Techniques →
                </Link>
              </p>
            </div>
          </div>
        </div>

        {/* Search and Filters */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <form onSubmit={handleSearchSubmit} className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
                <input
                  type="text"
                  placeholder="Search techniques..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                />
              </form>
            </div>
            <div className="flex gap-2">
              <select
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500"
                value={category}
                onChange={handleCategoryChange}
              >
                <option value="">All Categories</option>
                {categories.map((cat) => (
                  <option key={cat} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Results */}
        <div className="mb-4 text-sm text-gray-600">
          Showing {techniques.length} technique{techniques.length !== 1 ? 's' : ''}
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {techniques.map((technique) => (
            <Link
              key={technique.id}
              href={`/techniques/${technique.id}`}
              className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
            >
              <div className="flex items-start justify-between mb-3">
                <h3 className="text-xl font-semibold text-primary-800">{technique.name}</h3>
                {technique.acronym && (
                  <span className="text-sm font-mono bg-primary-100 text-primary-800 px-2 py-1 rounded">
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
            </Link>
          ))}
        </div>

        {techniques.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-600 mb-4">No techniques found matching your criteria.</p>
            <Link
              href="/techniques"
              className="text-primary-600 hover:text-primary-800 underline"
            >
              Clear filters and view all techniques
            </Link>
          </div>
        )}
      </div>
    </div>
  )
}

export default function TechniquesPage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading techniques...</p>
        </div>
      </div>
    }>
      <TechniquesContent />
    </Suspense>
  )
}

