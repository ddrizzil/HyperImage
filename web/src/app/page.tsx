import Link from 'next/link'
import { Search, BookOpen, Layers, Zap, Radio, Camera, Beaker, Lightbulb } from 'lucide-react'
import { getAllTechniques, getAllCategories } from '@/lib/techniques'
import { getAllRFTechniques } from '@/lib/rf-techniques'

export default function HomePage() {
  const techniques = getAllTechniques()
  const rfTechniques = getAllRFTechniques()
  const categories = getAllCategories()
  const stats = {
    totalTechniques: techniques.length,
    rfTechniques: rfTechniques.length,
    categories: categories.length,
    references: techniques.reduce((sum, t) => sum + (t.references?.keyPapers?.length || 0), 0),
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary-800 via-primary-700 to-primary-900 text-white">
        <div className="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-5xl font-bold mb-6">HyperImage</h1>
            <p className="text-xl mb-8 text-primary-100 max-w-2xl mx-auto">
              Comprehensive reference documentation for scientific analysis techniques
              in conservation science and artwork analysis
            </p>

            {/* Search Bar */}
            <div className="max-w-2xl mx-auto">
              <Link
                href="/techniques?search=true"
                className="flex items-center justify-between w-full bg-white text-gray-900 rounded-lg px-6 py-4 shadow-lg hover:shadow-xl transition-shadow"
              >
                <div className="flex items-center space-x-3">
                  <Search className="h-5 w-5 text-gray-400" />
                  <span className="text-gray-500">Search techniques, applications, materials...</span>
                </div>
                <kbd className="hidden sm:inline-flex items-center px-2 py-1 text-xs font-semibold text-gray-500 bg-gray-100 border border-gray-200 rounded">
                  ⌘K
                </kbd>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="bg-white py-12 border-b">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 sm:grid-cols-4">
            <div className="text-center">
              <div className="text-4xl font-bold text-primary-800 mb-2">
                {stats.totalTechniques}
              </div>
              <div className="text-gray-600">Imaging Techniques</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600 mb-2">
                {stats.rfTechniques}
              </div>
              <div className="text-gray-600">RF Techniques</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-primary-800 mb-2">
                {stats.categories}
              </div>
              <div className="text-gray-600">Categories</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-primary-800 mb-2">
                {stats.references}+
              </div>
              <div className="text-gray-600">References</div>
            </div>
          </div>
        </div>
      </section>

      {/* Reference Libraries Section */}
      <section className="py-16 bg-white border-b">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-900">
            Reference Libraries
          </h2>
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 mb-12">
            {/* Optics Reference */}
            <Link
              href="/optics"
              className="bg-gradient-to-br from-purple-50 to-indigo-50 p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow border-2 border-purple-200 hover:border-purple-400"
            >
              <div className="flex items-center gap-4 mb-4">
                <div className="p-3 bg-purple-100 rounded-lg">
                  <Lightbulb className="w-8 h-8 text-purple-800" />
                </div>
                <h3 className="text-2xl font-semibold text-purple-800">Fundamentals of Optics</h3>
              </div>
              <p className="text-gray-700 mb-4">
                Comprehensive reference for optical principles, equations, materials, and advanced techniques. 
                Wave optics, geometric optics, light-matter interactions, and computational methods.
              </p>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">
                  Principles, equations & methods
                </span>
                <span className="text-purple-600 font-medium">Explore →</span>
              </div>
            </Link>

            {/* Pigments & Chemistry */}
            <Link
              href="/pages"
              className="bg-gradient-to-br from-amber-50 to-orange-50 p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow border-2 border-amber-200 hover:border-amber-400"
            >
              <div className="flex items-center gap-4 mb-4">
                <div className="p-3 bg-amber-100 rounded-lg">
                  <Beaker className="w-8 h-8 text-amber-800" />
                </div>
                <h3 className="text-2xl font-semibold text-amber-800">Pigments & Chemical Analysis</h3>
              </div>
              <p className="text-gray-700 mb-4">
                Historic pigments, chemical processes, degradation pathways, and equations. 
                Complete reference for pigment identification, aging mechanisms, and conservation chemistry.
              </p>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">
                  Chemical equations & processes
                </span>
                <span className="text-amber-600 font-medium">Explore →</span>
              </div>
            </Link>
          </div>
        </div>
      </section>

      {/* Technique Types */}
      <section className="py-16 bg-gray-50">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-900">
            Browse Techniques
          </h2>
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 mb-12">
            {/* Imaging Techniques */}
            <Link
              href="/techniques"
              className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow border-2 border-primary-200 hover:border-primary-400"
            >
              <div className="flex items-center gap-4 mb-4">
                <div className="p-3 bg-primary-100 rounded-lg">
                  <Camera className="w-8 h-8 text-primary-800" />
                </div>
                <h3 className="text-2xl font-semibold text-primary-800">Imaging Techniques</h3>
              </div>
              <p className="text-gray-600 mb-4">
                Optical, X-ray, electron, and other imaging methods for cultural heritage analysis
              </p>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-500">
                  {stats.totalTechniques} techniques available
                </span>
                <span className="text-primary-600 font-medium">View All →</span>
              </div>
            </Link>

            {/* RF Techniques */}
            <Link
              href="/rf-techniques"
              className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow border-2 border-blue-200 hover:border-blue-400"
            >
              <div className="flex items-center gap-4 mb-4">
                <div className="p-3 bg-blue-100 rounded-lg">
                  <Radio className="w-8 h-8 text-blue-800" />
                </div>
                <h3 className="text-2xl font-semibold text-blue-800">RF Techniques</h3>
              </div>
              <p className="text-gray-600 mb-4">
                Radio frequency, radar, and microwave analysis techniques for subsurface imaging and material characterization
              </p>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-500">
                  {stats.rfTechniques} techniques available
                </span>
                <span className="text-blue-600 font-medium">View All →</span>
              </div>
            </Link>
          </div>

          {/* Category Browser */}
          {categories.length > 0 && (
            <>
              <h3 className="text-2xl font-bold text-center mb-8 text-gray-900">
                Imaging Technique Categories
              </h3>
              <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {categories.map((category) => (
                  <Link
                    key={category}
                    href={`/techniques?category=${encodeURIComponent(category)}`}
                    className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow border border-gray-200"
                  >
                    <h4 className="text-xl font-semibold mb-2 text-primary-800">{category}</h4>
                    <p className="text-gray-600 text-sm">
                      {techniques.filter((t) => t.category === category).length} techniques
                    </p>
                  </Link>
                ))}
              </div>
            </>
          )}
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-900">
            What You'll Find
          </h2>
          <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
            <div className="text-center">
              <div className="inline-flex items-center justify-center w-16 h-16 bg-primary-100 rounded-full mb-4">
                <BookOpen className="h-8 w-8 text-primary-800" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Comprehensive Documentation</h3>
              <p className="text-gray-600">
                Detailed information on physics principles, instrumentation, protocols, and data
                analysis for each technique
              </p>
            </div>
            <div className="text-center">
              <div className="inline-flex items-center justify-center w-16 h-16 bg-secondary-100 rounded-full mb-4">
                <Layers className="h-8 w-8 text-secondary-800" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Multimodal Combinations</h3>
              <p className="text-gray-600">
                Learn how to combine techniques effectively for comprehensive material
                characterization
              </p>
            </div>
            <div className="text-center">
              <div className="inline-flex items-center justify-center w-16 h-16 bg-accent-100 rounded-full mb-4">
                <Zap className="h-8 w-8 text-accent-800" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Practical Protocols</h3>
              <p className="text-gray-600">
                Step-by-step measurement protocols, troubleshooting guides, and real-world case
                studies
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Techniques */}
      {techniques.length > 0 && (
        <section className="py-16 bg-gray-50">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h2 className="text-3xl font-bold text-center mb-12 text-gray-900">
              Featured Techniques
            </h2>
            <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
              {techniques.slice(0, 6).map((technique) => (
                <Link
                  key={technique.id}
                  href={`/techniques/${technique.id}`}
                  className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow border border-gray-200"
                >
                  <div className="flex items-start justify-between mb-3">
                    <h3 className="text-xl font-semibold text-primary-800">
                      {technique.name}
                    </h3>
                    {technique.acronym && (
                      <span className="text-sm font-mono bg-primary-100 text-primary-800 px-2 py-1 rounded">
                        {technique.acronym}
                      </span>
                    )}
                  </div>
                  <p className="text-gray-600 text-sm mb-4 line-clamp-2">
                    {technique.summary}
                  </p>
                  <div className="flex flex-wrap gap-2">
                    <span className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded">
                      {technique.destructiveness}
                    </span>
                    <span className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded">
                      {technique.portability}
                    </span>
                  </div>
                </Link>
              ))}
            </div>
            {techniques.length > 6 && (
              <div className="text-center mt-8">
                <Link
                  href="/techniques"
                  className="inline-flex items-center px-6 py-3 bg-primary-800 text-white rounded-lg hover:bg-primary-700 transition-colors"
                >
                  View All Techniques
                </Link>
              </div>
            )}
          </div>
        </section>
      )}
    </div>
  )
}

