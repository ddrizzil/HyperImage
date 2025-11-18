/**
 * Utility functions for loading and working with technique data
 */

import type { Technique } from '@/types/technique'
import maXrfData from '@/data/techniques/ma-xrf.json'
import xRayRadiographyData from '@/data/techniques/x-ray-radiography-film.json'
import digitalXRayData from '@/data/techniques/digital-x-ray-radiography.json'
import shgMicroscopyData from '@/data/techniques/shg-microscopy.json'
import thgMicroscopyData from '@/data/techniques/thg-microscopy.json'
import carsMicroscopyData from '@/data/techniques/cars-microscopy.json'
import photoacousticImagingData from '@/data/techniques/photoacoustic-imaging.json'
import photoacousticTomographyData from '@/data/techniques/photoacoustic-tomography.json'
import xRayHolographyData from '@/data/techniques/x-ray-holography.json'
import pixeData from '@/data/techniques/pixe.json'
import semSecondaryElectronsData from '@/data/techniques/sem-secondary-electrons.json'
import fibSemTomographyData from '@/data/techniques/fib-sem-tomography.json'
import coherenceScanningInterferometryData from '@/data/techniques/coherence-scanning-interferometry.json'
import stereoPhotogrammetryData from '@/data/techniques/stereo-photogrammetry.json'
import thzTdsData from '@/data/techniques/thz-tds.json'
import gcMsData from '@/data/techniques/gc-ms.json'
import pyGcMsData from '@/data/techniques/py-gc-ms.json'
import visiblePhotographyData from '@/data/techniques/visible-photography.json'
import rakingLightData from '@/data/techniques/raking-light.json'
import ramanSpectroscopyData from '@/data/techniques/raman-spectroscopy.json'
import microRamanSpectroscopyData from '@/data/techniques/micro-raman-spectroscopy.json'
import photoacousticSpectroscopyData from '@/data/techniques/photoacoustic-spectroscopy.json'
import orPamData from '@/data/techniques/or-pam.json'
import crossPolarizedPhotographyData from '@/data/techniques/cross-polarized-photography.json'
import macroPhotographyData from '@/data/techniques/macro-photography.json'
import uvFluorescenceLongwaveData from '@/data/techniques/uv-fluorescence-longwave.json'
import xanesData from '@/data/techniques/xanes.json'
import synchrotronXrfMappingData from '@/data/techniques/synchrotron-xrf-mapping.json'
import opticalCoherenceTomographyData from '@/data/techniques/optical-coherence-tomography.json'

// In a real application, this would load from a database or API
// For now, we'll use a simple in-memory store
const techniquesCache = new Map<string, Technique>()

/**
 * Normalize technique data to handle both flat and metadata-wrapped formats
 */
function normalizeTechnique(data: any): Technique {
  // If data has a metadata wrapper, flatten it
  if (data.metadata) {
    const { metadata, ...rest } = data
    return {
      ...rest,
      tags: metadata.tags || metadata.tag || [],
      relatedTechniques: metadata.relatedTechniques || metadata.relatedTechniqueIds || [],
      lastUpdated: metadata.lastUpdated || data.lastUpdated || new Date().toISOString().split('T')[0],
      // Normalize references.reviews to handle null doi values
      references: {
        ...rest.references,
        reviews: (rest.references?.reviews || []).map((r: any) => ({
          citation: r.citation,
          doi: r.doi === null ? undefined : r.doi,
        })),
      },
    } as Technique
  }
  
  // Normalize reviews with null doi values
  if (data.references?.reviews) {
    data.references.reviews = data.references.reviews.map((r: any) => ({
      citation: r.citation,
      doi: r.doi === null ? undefined : r.doi,
    }))
  }
  
  return data as Technique
}

/**
 * Load all available techniques
 * In production, this would fetch from an API or database
 */
export function getAllTechniques(): Technique[] {
  // For now, return the available techniques
  // In production, this would load all JSON files or fetch from API
  if (techniquesCache.size === 0) {
    techniquesCache.set('ma-xrf', normalizeTechnique(maXrfData))
    techniquesCache.set('x-ray-radiography-film', normalizeTechnique(xRayRadiographyData))
    techniquesCache.set('digital-x-ray-radiography', normalizeTechnique(digitalXRayData))
    techniquesCache.set('shg-microscopy', normalizeTechnique(shgMicroscopyData))
    techniquesCache.set('thg-microscopy', normalizeTechnique(thgMicroscopyData))
    techniquesCache.set('cars-microscopy', normalizeTechnique(carsMicroscopyData))
    techniquesCache.set('photoacoustic-imaging', normalizeTechnique(photoacousticImagingData))
    techniquesCache.set('photoacoustic-tomography', normalizeTechnique(photoacousticTomographyData))
    techniquesCache.set('x-ray-holography', normalizeTechnique(xRayHolographyData))
    techniquesCache.set('pixe', normalizeTechnique(pixeData))
    techniquesCache.set('sem-secondary-electrons', normalizeTechnique(semSecondaryElectronsData))
    techniquesCache.set('fib-sem-tomography', normalizeTechnique(fibSemTomographyData))
    techniquesCache.set('coherence-scanning-interferometry', normalizeTechnique(coherenceScanningInterferometryData))
    techniquesCache.set('stereo-photogrammetry', normalizeTechnique(stereoPhotogrammetryData))
    techniquesCache.set('thz-tds', normalizeTechnique(thzTdsData))
    techniquesCache.set('gc-ms', normalizeTechnique(gcMsData))
    techniquesCache.set('py-gc-ms', normalizeTechnique(pyGcMsData))
    techniquesCache.set('visible-photography', normalizeTechnique(visiblePhotographyData))
    techniquesCache.set('raking-light', normalizeTechnique(rakingLightData))
    techniquesCache.set('raman-spectroscopy', normalizeTechnique(ramanSpectroscopyData))
    techniquesCache.set('micro-raman-spectroscopy', normalizeTechnique(microRamanSpectroscopyData))
    techniquesCache.set('photoacoustic-spectroscopy', normalizeTechnique(photoacousticSpectroscopyData))
    techniquesCache.set('or-pam', normalizeTechnique(orPamData))
    techniquesCache.set('cross-polarized-photography', normalizeTechnique(crossPolarizedPhotographyData))
    techniquesCache.set('macro-photography', normalizeTechnique(macroPhotographyData))
    techniquesCache.set('uv-fluorescence-longwave', normalizeTechnique(uvFluorescenceLongwaveData))
    techniquesCache.set('xanes', normalizeTechnique(xanesData))
    techniquesCache.set('synchrotron-xrf-mapping', normalizeTechnique(synchrotronXrfMappingData))
    techniquesCache.set('optical-coherence-tomography', normalizeTechnique(opticalCoherenceTomographyData))
  }
  return Array.from(techniquesCache.values())
}

/**
 * Get a technique by ID
 */
export function getTechniqueById(id: string): Technique | undefined {
  const all = getAllTechniques()
  return all.find((t) => t.id === id)
}

/**
 * Get techniques by category
 */
export function getTechniquesByCategory(category: string): Technique[] {
  return getAllTechniques().filter((t) => t.category === category)
}

/**
 * Get all unique categories
 */
export function getAllCategories(): string[] {
  const categories = new Set<string>()
  getAllTechniques().forEach((t) => categories.add(t.category))
  return Array.from(categories).sort()
}

/**
 * Search techniques by query string
 */
export function searchTechniques(query: string): Technique[] {
  if (!query.trim()) return getAllTechniques()

  const lowerQuery = query.toLowerCase()
  return getAllTechniques().filter((technique) => {
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
 * Get related techniques
 */
export function getRelatedTechniques(technique: Technique): Technique[] {
  // Extract technique IDs from complementaryTechniques (handle both string and object formats)
  const complementaryIds = (technique.multimodal?.complementaryTechniques || []).map((item: any) => {
    return typeof item === 'string' ? item : (item?.techniqueId || item);
  });

  const relatedIds = new Set<string>([
    ...(technique.relatedTechniques || []),
    ...complementaryIds,
  ])

  return getAllTechniques()
    .filter((t) => relatedIds.has(t.id) && t.id !== technique.id)
    .slice(0, 6) // Limit to 6 related techniques
}

