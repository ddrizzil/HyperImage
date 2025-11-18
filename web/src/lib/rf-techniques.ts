/**
 * Utility functions for loading and working with RF technique data
 * This is a separate branch from imaging techniques
 */

import type { Technique } from '@/types/technique'

// RF techniques cache - separate from imaging techniques
const rfTechniquesCache = new Map<string, Technique>()

/**
 * Load all available RF techniques
 * RF techniques are those related to radio frequency, radar, microwave, and RF signal processing
 */
export function getAllRFTechniques(): Technique[] {
  // For now, return empty array - RF techniques will be added here
  // In production, this would load RF technique JSON files or fetch from API
  return Array.from(rfTechniquesCache.values())
}

/**
 * Get an RF technique by ID
 */
export function getRFTechniqueById(id: string): Technique | undefined {
  const all = getAllRFTechniques()
  return all.find((t) => t.id === id)
}

/**
 * Get RF techniques by category
 */
export function getRFTechniquesByCategory(category: string): Technique[] {
  return getAllRFTechniques().filter((t) => t.category === category)
}

/**
 * Get all unique categories for RF techniques
 */
export function getAllRFCategories(): string[] {
  const categories = new Set<string>()
  getAllRFTechniques().forEach((t) => categories.add(t.category))
  return Array.from(categories).sort()
}

/**
 * Search RF techniques by query string
 */
export function searchRFTechniques(query: string): Technique[] {
  if (!query.trim()) return getAllRFTechniques()

  const lowerQuery = query.toLowerCase()
  return getAllRFTechniques().filter((technique) => {
    const searchableText = [
      technique.name,
      technique.acronym,
      technique.summary,
      technique.category,
      technique.subcategory,
      ...(technique.keyApplications || []),
      ...(technique.tags || []),
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    return searchableText.includes(lowerQuery)
  })
}

/**
 * Register an RF technique (for future use when RF techniques are added)
 */
export function registerRFTechnique(technique: Technique): void {
  rfTechniquesCache.set(technique.id, technique)
}

/**
 * Check if a technique is an RF technique based on category/tags
 */
export function isRFTechnique(technique: Technique): boolean {
  const rfKeywords = [
    'rf',
    'radio frequency',
    'radar',
    'microwave',
    'ground penetrating radar',
    'gpr',
    'harmonic radar',
    'nonlinear radar',
    'rf fingerprinting',
    'intermodulation',
    'passive intermodulation',
    'pim',
    'volterra',
  ]
  
  const searchableText = [
    technique.category,
    technique.subcategory,
    technique.name,
    ...(technique.tags || []),
  ]
    .filter(Boolean)
    .join(' ')
    .toLowerCase()

  return rfKeywords.some((keyword) => searchableText.includes(keyword))
}

