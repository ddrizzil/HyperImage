'use client'

import React, { useState, useMemo } from 'react'
import { CheckCircle, XCircle, AlertCircle, Info, ChevronDown, ChevronUp } from 'lucide-react'
import comparisonData from '@/data/comparisons/nonlinear-microscopy-comparison.json'

type TabId = 'overview' | 'technical' | 'applications' | 'practical'
type TechniqueId = 'shg' | 'thg' | 'tpef'

interface TechniqueFeature {
  shg: string | boolean | number
  thg: string | boolean | number
  tpef: string | boolean | number
}

interface Feature {
  name: string
  description?: string
  values: TechniqueFeature
}

interface Category {
  id: string
  title: string
  features: Feature[]
}

interface Technique {
  id: string
  name: string
  color: string
  icon: string
  summary: string
  keyAdvantage: string
  typicalUseCase: string
  signalStrength: string
  typicalPower: string
}

interface ComparisonData {
  comparisonId: string
  title: string
  subtitle: string
  lastUpdated: string
  techniques: Technique[]
  categories: Category[]
  decisionHelper: {
    whenToUseSHG: string[]
    whenToUseTHG: string[]
    whenToUseTPEF: string[]
    bestCombinations: Array<{
      techniques: string[]
      rationale: string
      example: string
    }>
  }
}

const data = comparisonData as ComparisonData

function getRating(value: string | boolean | number): 'excellent' | 'good' | 'moderate' | 'poor' | 'none' {
  if (typeof value === 'boolean') {
    return value ? 'excellent' : 'none'
  }
  
  const str = String(value).toLowerCase()
  if (str.includes('excellent') || str.includes('strong') || str === 'yes' || str === 'true') {
    return 'excellent'
  }
  if (str.includes('good') || str.includes('moderate')) {
    return 'good'
  }
  if (str.includes('poor') || str.includes('weak') || str.includes('no signal') || str === 'no' || str === 'false') {
    return 'poor'
  }
  if (str.includes('moderate')) {
    return 'moderate'
  }
  return 'good'
}

function RatingIcon({ rating }: { rating: 'excellent' | 'good' | 'moderate' | 'poor' | 'none' }) {
  switch (rating) {
    case 'excellent':
      return <CheckCircle className="w-5 h-5 text-green-600" />
    case 'good':
      return <AlertCircle className="w-5 h-5 text-yellow-600" />
    case 'moderate':
      return <AlertCircle className="w-5 h-5 text-orange-600" />
    case 'poor':
    case 'none':
      return <XCircle className="w-5 h-5 text-red-600" />
    default:
      return null
  }
}

function formatValue(value: string | boolean | number): string {
  if (typeof value === 'boolean') {
    return value ? 'Yes' : 'No'
  }
  return String(value)
}

export const NonlinearMicroscopyComparison: React.FC = () => {
  const [activeTab, setActiveTab] = useState<TabId>('overview')
  const [selectedTechniques, setSelectedTechniques] = useState<Set<TechniqueId>>(
    new Set(['shg', 'thg', 'tpef'])
  )
  const [expandedRows, setExpandedRows] = useState<Set<string>>(new Set())
  const [hoveredFeature, setHoveredFeature] = useState<string | null>(null)

  const activeCategory = useMemo(() => {
    return data.categories.find((cat) => cat.id === activeTab)
  }, [activeTab])

  const toggleTechnique = (techniqueId: TechniqueId) => {
    const newSet = new Set(selectedTechniques)
    if (newSet.has(techniqueId)) {
      newSet.delete(techniqueId)
    } else {
      newSet.add(techniqueId)
    }
    setSelectedTechniques(newSet)
  }

  const toggleRow = (featureName: string) => {
    const newSet = new Set(expandedRows)
    if (newSet.has(featureName)) {
      newSet.delete(featureName)
    } else {
      newSet.add(featureName)
    }
    setExpandedRows(newSet)
  }

  const visibleTechniques = data.techniques.filter((t) => selectedTechniques.has(t.id as TechniqueId))

  return (
    <div className="w-full">
      {/* Summary Cards */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        {data.techniques.map((technique) => {
          const isSelected = selectedTechniques.has(technique.id as TechniqueId)
          return (
            <div
              key={technique.id}
              onClick={() => toggleTechnique(technique.id as TechniqueId)}
              className={`
                bg-white rounded-lg border-2 p-6 cursor-pointer transition-all
                ${isSelected ? 'border-opacity-100 shadow-lg' : 'border-opacity-30'}
                hover:shadow-md
              `}
              style={{
                borderColor: technique.color,
              }}
            >
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                  <span className="text-2xl">{technique.icon}</span>
                  <div>
                    <h3 className="font-bold text-lg" style={{ color: technique.color }}>
                      {technique.name.split('(')[0].trim()}
                    </h3>
                    <p className="text-xs text-gray-500">{technique.name.split('(')[1]?.replace(')', '')}</p>
                  </div>
                </div>
                <input
                  type="checkbox"
                  checked={isSelected}
                  onChange={() => {}}
                  className="w-5 h-5 rounded"
                  style={{ accentColor: technique.color }}
                  onClick={(e) => e.stopPropagation()}
                />
              </div>
              <p className="text-sm text-gray-700 mb-3">{technique.summary}</p>
              <div className="space-y-2 text-sm">
                <div>
                  <span className="font-semibold">Signal: </span>
                  <span className="text-gray-600">{technique.signalStrength}</span>
                </div>
                <div>
                  <span className="font-semibold">Power: </span>
                  <span className="text-gray-600">{technique.typicalPower}</span>
                </div>
                <div>
                  <span className="font-semibold">Use: </span>
                  <span className="text-gray-600">{technique.typicalUseCase}</span>
                </div>
              </div>
            </div>
          )
        })}
      </div>

      {/* Tabs */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 mb-6">
        <div className="flex border-b border-gray-200 overflow-x-auto">
          {data.categories.map((category) => (
            <button
              key={category.id}
              onClick={() => setActiveTab(category.id as TabId)}
              className={`
                px-6 py-4 font-medium text-sm transition-colors whitespace-nowrap
                ${activeTab === category.id
                  ? 'border-b-2 border-indigo-600 text-indigo-600 bg-indigo-50'
                  : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                }
              `}
            >
              {category.title}
            </button>
          ))}
        </div>

        {/* Comparison Table */}
        {activeCategory && (
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-gray-50 sticky top-0 z-10">
                <tr>
                  <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900 w-1/3">
                    Feature
                  </th>
                  {visibleTechniques.map((technique) => (
                    <th
                      key={technique.id}
                      className="px-6 py-4 text-center text-sm font-semibold text-white"
                      style={{ backgroundColor: technique.color }}
                    >
                      {technique.name.split('(')[0].trim()}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                {activeCategory.features.map((feature, idx) => {
                  const isExpanded = expandedRows.has(feature.name)
                  return (
                    <React.Fragment key={feature.name}>
                      <tr
                        className="hover:bg-gray-50 cursor-pointer transition-colors"
                        onClick={() => toggleRow(feature.name)}
                      >
                        <td className="px-6 py-4">
                          <div className="flex items-center gap-2">
                            <button
                              className="text-gray-400 hover:text-gray-600"
                              onClick={(e) => {
                                e.stopPropagation()
                                toggleRow(feature.name)
                              }}
                            >
                              {isExpanded ? (
                                <ChevronUp className="w-4 h-4" />
                              ) : (
                                <ChevronDown className="w-4 h-4" />
                              )}
                            </button>
                            <div
                              className="relative group"
                              onMouseEnter={() => setHoveredFeature(feature.name)}
                              onMouseLeave={() => setHoveredFeature(null)}
                            >
                              <span className="font-medium text-gray-900">{feature.name}</span>
                              {feature.description && (
                                <Info className="w-4 h-4 text-gray-400 inline-block ml-2" />
                              )}
                              {hoveredFeature === feature.name && feature.description && (
                                <div className="absolute left-0 top-full mt-2 w-64 p-3 bg-gray-900 text-white text-xs rounded-lg shadow-lg z-20">
                                  {feature.description}
                                </div>
                              )}
                            </div>
                          </div>
                        </td>
                        {visibleTechniques.map((technique) => {
                          const value = feature.values[technique.id as keyof TechniqueFeature]
                          const rating = getRating(value)
                          return (
                            <td
                              key={technique.id}
                              className="px-6 py-4 text-center"
                              style={{ backgroundColor: `${technique.color}10` }}
                            >
                              <div className="flex items-center justify-center gap-2">
                                <RatingIcon rating={rating} />
                                <span className="text-sm text-gray-700">{formatValue(value)}</span>
                              </div>
                            </td>
                          )
                        })}
                      </tr>
                      {isExpanded && feature.description && (
                        <tr className="bg-gray-50">
                          <td colSpan={visibleTechniques.length + 1} className="px-6 py-4">
                            <div className="text-sm text-gray-600 italic">
                              <strong>Description:</strong> {feature.description}
                            </div>
                          </td>
                        </tr>
                      )}
                    </React.Fragment>
                  )
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Decision Helper */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Decision Helper</h2>
        
        <div className="grid md:grid-cols-3 gap-6 mb-8">
          <div className="border-l-4 pl-4" style={{ borderColor: data.techniques[0].color }}>
            <h3 className="font-semibold text-lg mb-3" style={{ color: data.techniques[0].color }}>
              When to Use SHG
            </h3>
            <ul className="space-y-2 text-sm text-gray-700">
              {data.decisionHelper.whenToUseSHG.map((item, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <CheckCircle className="w-4 h-4 text-green-600 mt-0.5 flex-shrink-0" />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="border-l-4 pl-4" style={{ borderColor: data.techniques[1].color }}>
            <h3 className="font-semibold text-lg mb-3" style={{ color: data.techniques[1].color }}>
              When to Use THG
            </h3>
            <ul className="space-y-2 text-sm text-gray-700">
              {data.decisionHelper.whenToUseTHG.map((item, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <CheckCircle className="w-4 h-4 text-purple-600 mt-0.5 flex-shrink-0" />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="border-l-4 pl-4" style={{ borderColor: data.techniques[2].color }}>
            <h3 className="font-semibold text-lg mb-3" style={{ color: data.techniques[2].color }}>
              When to Use TPEF
            </h3>
            <ul className="space-y-2 text-sm text-gray-700">
              {data.decisionHelper.whenToUseTPEF.map((item, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <CheckCircle className="w-4 h-4 text-green-600 mt-0.5 flex-shrink-0" />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div>
          <h3 className="font-semibold text-lg mb-4 text-gray-900">Best Combinations</h3>
          <div className="space-y-4">
            {data.decisionHelper.bestCombinations.map((combo, idx) => (
              <div key={idx} className="bg-gray-50 rounded-lg p-4 border border-gray-200">
                <div className="flex items-center gap-2 mb-2">
                  {combo.techniques.map((techId) => {
                    const tech = data.techniques.find((t) => t.id === techId)
                    return tech ? (
                      <span
                        key={techId}
                        className="px-3 py-1 rounded-full text-sm font-medium text-white"
                        style={{ backgroundColor: tech.color }}
                      >
                        {tech.name.split('(')[0].trim()}
                      </span>
                    ) : null
                  })}
                </div>
                <p className="text-sm text-gray-700 mb-1">
                  <strong>Rationale:</strong> {combo.rationale}
                </p>
                <p className="text-sm text-gray-600">
                  <strong>Example:</strong> {combo.example}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

