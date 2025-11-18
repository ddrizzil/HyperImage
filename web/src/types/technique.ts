/**
 * TypeScript interfaces for the HyperImage technique data model
 */

export type Destructiveness =
  | 'non-destructive'
  | 'minimally-invasive'
  | 'micro-destructive'
  | 'destructive'

export type Portability =
  | 'field-portable'
  | 'transportable'
  | 'laboratory-only'
  | 'synchrotron/facility'

export interface EquationVariable {
  symbol: string
  meaning: string
  units: string
}

export interface Equation {
  latex: string
  description: string
  variables: EquationVariable[]
}

export interface FundamentalPhysics {
  principle: string // Markdown with LaTeX
  physicalPhenomenon: string
  equations: Equation[] // LaTeX equations with variable definitions
  interactionDepth: string
  spatialResolution: string
  detectionLimit?: string
}

export interface CommercialSystem {
  name: string
  vendor: string
  notes?: string
}

export interface Instrumentation {
  source: string
  detector: string
  optics?: string
  criticalComponents: string[]
  typicalConfiguration: string // Markdown
  commercialSystems?: CommercialSystem[]
}

export interface TypicalParameter {
  parameter: string
  value: string
  notes?: string
}

export interface Methodology {
  samplePreparation: string[]
  measurementProtocol: string // Markdown, step-by-step
  typicalParameters: TypicalParameter[]
  calibration: string
  qualityControl: string[]
}

export interface SoftwareTool {
  name: string
  url?: string
  notes?: string
}

export interface DataAnalysis {
  rawDataFormat: string
  preprocessing: string[]
  analysisWorkflow: string // Markdown
  softwareTools: SoftwareTool[]
  interpretationGuidelines: string
  commonPitfalls: string[]
}

export interface CaseStudy {
  title: string
  description: string
  reference?: string
  imageUrl?: string
}

export interface Applications {
  primaryUses: string[]
  materialTypes: string[]
  caseStudies: CaseStudy[]
}

export interface MultimodalCombination {
  techniques: string[] // IDs of other techniques
  rationale: string
  examples?: string
}

export interface Multimodal {
  complementaryTechniques: string[] // IDs of other techniques
  commonCombinations: MultimodalCombination[]
}

export interface KeyPaper {
  citation: string
  doi?: string
  notes?: string
}

export interface Review {
  citation: string
  doi?: string
}

export interface OnlineResource {
  title: string
  url: string
}

export interface References {
  keyPapers: KeyPaper[]
  reviews: Review[]
  onlineResources: OnlineResource[]
}

/**
 * Complete technique data structure
 */
export interface Technique {
  id: string
  name: string
  acronym?: string
  category: string
  subcategory?: string

  // Overview
  summary: string
  keyApplications: string[]
  destructiveness: Destructiveness
  portability: Portability

  // Physics & Theory
  fundamentalPhysics: FundamentalPhysics

  // Instrumentation
  instrumentation: Instrumentation

  // Methodology
  methodology: Methodology

  // Data Analysis
  dataAnalysis: DataAnalysis

  // Applications & Examples
  applications: Applications

  // Multimodal Synergies
  multimodal: Multimodal

  // References & Resources
  references: References

  // Metadata
  tags: string[]
  relatedTechniques: string[] // IDs
  lastUpdated: string
}

