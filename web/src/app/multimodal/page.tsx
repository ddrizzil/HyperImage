import { getAllTechniques } from '@/lib/techniques'
import Link from 'next/link'

export default function MultimodalPage() {
  const techniques = getAllTechniques()

  // Collect all multimodal combinations
  const combinations = new Map<string, Array<{ technique: string; rationale: string }>>()

  techniques.forEach((tech) => {
    if (tech.multimodal?.commonCombinations) {
      tech.multimodal.commonCombinations.forEach((combo) => {
        const key = combo.techniques.sort().join('+')
        if (!combinations.has(key)) {
          combinations.set(key, [])
        }
        combinations.get(key)!.push({
          technique: tech.id,
          rationale: combo.rationale,
        })
      })
    }
  })

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Multimodal Combinations</h1>
          <p className="text-lg text-gray-600">
            Explore how different techniques can be combined for comprehensive material
            characterization
          </p>
        </div>

        <div className="space-y-6">
          {Array.from(combinations.entries()).map(([key, combos]) => {
            const techniqueIds = key.split('+')
            return (
              <div key={key} className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
                <h2 className="text-2xl font-semibold mb-4">
                  {techniqueIds.map((id) => id.toUpperCase()).join(' + ')}
                </h2>
                <div className="mb-4">
                  <h3 className="font-semibold mb-2">Techniques:</h3>
                  <div className="flex flex-wrap gap-2">
                    {techniqueIds.map((id) => {
                      const tech = techniques.find((t) => t.id === id)
                      return tech ? (
                        <Link
                          key={id}
                          href={`/techniques/${id}`}
                          className="text-primary-600 hover:text-primary-800 underline"
                        >
                          {tech.name}
                        </Link>
                      ) : (
                        <span key={id} className="text-gray-600">
                          {id}
                        </span>
                      )
                    })}
                  </div>
                </div>
                <div>
                  <h3 className="font-semibold mb-2">Rationale:</h3>
                  <p className="text-gray-700">{combos[0].rationale}</p>
                </div>
              </div>
            )
          })}
        </div>

        {combinations.size === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-600">No multimodal combinations documented yet.</p>
          </div>
        )}
      </div>
    </div>
  )
}

