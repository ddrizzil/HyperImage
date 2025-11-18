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

export interface InteractionDepthObject {
  description?: string
  materialSpecific?: Array<{
    material: string
    penetrationDepth?: string
    visualizedFeatures?: string
  }>
}

export interface SpatialResolutionObject {
  lateral?: string
  depth?: string
  limitingFactors?: string[]
}

export interface SensitivityObject {
  description?: string
}

export interface FundamentalPhysics {
  principle: string // Markdown with LaTeX
  physicalPhenomenon: string
  equations: Equation[] // LaTeX equations with variable definitions
  interactionDepth: string | InteractionDepthObject
  spatialResolution: string | SpatialResolutionObject
  detectionLimit?: string | { description?: string }
  sensitivity?: string | SensitivityObject
}

export interface CommercialSystem {
  name: string
  vendor: string
  notes?: string
}

export interface SourceObject {
  type?: string
  specifications?: string
  powerRange?: string
}

export interface DetectorObject {
  type?: string
  spectralRange?: string
  efficiency?: string
  resolution?: string
}

export interface OpticalSystemObject {
  components?: string[]
  beamPath?: string
  focusing?: string
}

export interface Instrumentation {
  source: string | SourceObject
  detector: string | DetectorObject
  optics?: string | OpticalSystemObject
  opticalSystem?: OpticalSystemObject
  criticalComponents: string[]
  typicalConfiguration: string // Markdown
  commercialSystems?: CommercialSystem[]
}

export interface TypicalParameter {
  parameter: string
  value: string
  notes?: string
}

export interface SamplePreparationObject {
  samplingRequired?: boolean
  sampleSize?: string
  mountingProcedure?: string
  surfacePreparation?: string
  contaminationConcerns?: string
}

export interface MeasurementProtocolStep {
  stepNumber?: number
  title?: string
  description?: string
  duration?: string
  criticalParameters?: string[]
}

export interface MeasurementProtocolObject {
  steps: MeasurementProtocolStep[]
}

export interface OperatingParameter {
  parameter: string
  typicalValue?: string
  value?: string
  range?: string
  notes?: string
}

export interface Methodology {
  samplePreparation: string[] | SamplePreparationObject
  measurementProtocol: string | MeasurementProtocolObject
  typicalParameters?: TypicalParameter[]
  operatingParameters?: OperatingParameter[]
  calibration: string | { standards?: string; frequency?: string; procedure?: string }
  qualityControl: string[] | { checkpoints?: string[]; commonArtifacts?: Array<{ artifact: string; cause?: string; mitigation?: string }>; troubleshooting?: Array<{ problem: string; solution: string }> }
}

export interface SoftwareTool {
  name: string
  url?: string
  notes?: string
}

export interface RawDataFormatObject {
  fileFormats?: string[]
  dataStructure?: string
  typicalFileSize?: string
}

export interface PreprocessingStep {
  step?: string
  description?: string
  software?: string
}

export interface AnalysisWorkflowObject {
  steps: Array<{
    step?: string
    description?: string
    software?: string
  }>
}

export interface DataAnalysis {
  rawDataFormat: string | RawDataFormatObject
  preprocessing: string[] | PreprocessingStep[]
  analysisWorkflow: string | AnalysisWorkflowObject
  softwareTools: SoftwareTool[]
  interpretationGuidelines: string | string[]
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
  commonCombinations?: MultimodalCombination[]
  standardCombinations?: MultimodalCombination[]
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
  foundationalPapers?: KeyPaper[]
  keyPapers?: KeyPaper[]
  methodologyReviews?: Review[]
  reviews?: Review[]
  recentApplications?: KeyPaper[]
  onlineResources?: OnlineResource[]
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

