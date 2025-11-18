import type { Technique } from '@/types/technique'
import { MarkdownContent } from './MarkdownContent'
import { Equation } from './Equation'
import { ExternalLink, BarChart3 } from 'lucide-react'
import Link from 'next/link'
import { getAllTechniques } from '@/lib/techniques'

export function TechniqueContent({ technique }: { technique: Technique }) {
  return (
    <div className="prose prose-lg max-w-none">
      {/* Overview Section */}
      <section id="overview" className="scroll-mt-20">
        <h2>Overview</h2>
        <p>{technique.summary}</p>

        {/* Comparison Link for Nonlinear Microscopy Techniques */}
        {(technique.id === 'shg-microscopy' || 
          technique.id === 'thg-microscopy' || 
          technique.id === 'tpef-microscopy') && (
          <div className="bg-gradient-to-r from-indigo-50 to-purple-50 border-l-4 border-indigo-500 rounded-r-lg p-4 my-6">
            <div className="flex items-start gap-3">
              <BarChart3 className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-semibold text-indigo-900 mb-1">
                  Compare with Related Techniques
                </h4>
                <p className="text-sm text-indigo-800 mb-2">
                  See how {technique.acronym || technique.name} compares to other nonlinear optical microscopy techniques.
                </p>
                <Link
                  href="/comparisons/nonlinear-microscopy"
                  className="inline-flex items-center text-sm font-medium text-indigo-600 hover:text-indigo-800 hover:underline"
                >
                  View Comparison: SHG vs THG vs TPEF
                  <ExternalLink className="w-4 h-4 ml-1" />
                </Link>
              </div>
            </div>
          </div>
        )}

        <h3>Key Applications</h3>
        <ul>
          {(technique.keyApplications || []).map((app, idx) => (
            <li key={idx}>{app}</li>
          ))}
        </ul>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="font-semibold mb-2">Destructiveness</h4>
            <p className="text-gray-700">{technique.destructiveness}</p>
          </div>
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="font-semibold mb-2">Portability</h4>
            <p className="text-gray-700">{technique.portability}</p>
          </div>
        </div>
      </section>

      {/* Physics & Theory Section */}
      {technique.fundamentalPhysics && (
        <section id="physics" className="scroll-mt-20 mt-12">
          <h2>Physics & Theory</h2>

          <h3>Fundamental Principle</h3>
          <MarkdownContent content={technique.fundamentalPhysics?.principle || ''} />

          <h3>Physical Phenomenon</h3>
          <p>{technique.fundamentalPhysics?.physicalPhenomenon || ''}</p>

          {technique.fundamentalPhysics?.equations && technique.fundamentalPhysics.equations.length > 0 && (
            <>
              <h3>Key Equations</h3>
              <div className="space-y-4">
                {technique.fundamentalPhysics.equations.map((eq, idx) => (
                  <Equation key={idx} equation={eq} />
                ))}
              </div>
            </>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
            <div className="bg-gray-50 p-4 rounded-lg">
              <h4 className="font-semibold mb-2">Interaction Depth</h4>
              {typeof technique.fundamentalPhysics?.interactionDepth === 'string' ? (
                <p className="text-gray-700">{technique.fundamentalPhysics.interactionDepth}</p>
              ) : (() => {
                const interactionDepth = technique.fundamentalPhysics?.interactionDepth
                if (interactionDepth && typeof interactionDepth === 'object' && !Array.isArray(interactionDepth) && 'description' in interactionDepth) {
                  const depthObj = interactionDepth as { description?: string; materialSpecific?: Array<{ material: string; penetrationDepth?: string; visualizedFeatures?: string }> }
                  return (
                    <div className="space-y-3">
                      {depthObj.description && (
                        <MarkdownContent content={depthObj.description} />
                      )}
                      {depthObj.materialSpecific && Array.isArray(depthObj.materialSpecific) && (
                        <div className="mt-4">
                          <strong className="text-sm">Material-Specific Information:</strong>
                          <div className="mt-2 space-y-3">
                            {depthObj.materialSpecific.map((material: any, idx: number) => (
                              <div key={idx} className="border-l-2 border-blue-400 pl-3">
                                <strong className="text-sm">{material.material}:</strong>
                                {material.penetrationDepth && (
                                  <p className="text-sm text-gray-700 mt-1">
                                    <strong>Penetration Depth:</strong> {material.penetrationDepth}
                                  </p>
                                )}
                                {material.visualizedFeatures && (
                                  <p className="text-sm text-gray-700 mt-1">
                                    <strong>Visualized Features:</strong> {material.visualizedFeatures}
                                  </p>
                                )}
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  )
                }
                return <p className="text-gray-700">No interaction depth information available.</p>
              })()}
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h4 className="font-semibold mb-2">Spatial Resolution</h4>
              {typeof technique.fundamentalPhysics?.spatialResolution === 'string' ? (
                <p className="text-gray-700">{technique.fundamentalPhysics.spatialResolution}</p>
              ) : technique.fundamentalPhysics?.spatialResolution && typeof technique.fundamentalPhysics.spatialResolution === 'object' ? (
                <div className="space-y-3">
                  {technique.fundamentalPhysics.spatialResolution.lateral && (
                    <div>
                      <strong>Lateral:</strong> {technique.fundamentalPhysics.spatialResolution.lateral}
                    </div>
                  )}
                  {technique.fundamentalPhysics.spatialResolution.depth && (
                    <div>
                      <strong>Depth:</strong> {technique.fundamentalPhysics.spatialResolution.depth}
                    </div>
                  )}
                  {technique.fundamentalPhysics.spatialResolution.limitingFactors && Array.isArray(technique.fundamentalPhysics.spatialResolution.limitingFactors) && (
                    <div className="mt-3">
                      <strong className="text-sm">Limiting Factors:</strong>
                      <ul className="list-disc list-inside mt-1 text-sm text-gray-700">
                        {technique.fundamentalPhysics.spatialResolution.limitingFactors.map((factor: string, idx: number) => (
                          <li key={idx}>{factor}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              ) : (
                <p className="text-gray-700">No spatial resolution information available.</p>
              )}
            </div>
            {technique.fundamentalPhysics?.detectionLimit && (
              <div className="bg-gray-50 p-4 rounded-lg">
                <h4 className="font-semibold mb-2">Detection Limit</h4>
                {typeof technique.fundamentalPhysics.detectionLimit === 'string' ? (
                  <p className="text-gray-700">{technique.fundamentalPhysics.detectionLimit}</p>
                ) : typeof technique.fundamentalPhysics.detectionLimit === 'object' && technique.fundamentalPhysics.detectionLimit.description ? (
                  <MarkdownContent content={technique.fundamentalPhysics.detectionLimit.description} />
                ) : (
                  <p className="text-gray-700">{String(technique.fundamentalPhysics.detectionLimit)}</p>
                )}
              </div>
            )}
            {technique.fundamentalPhysics?.sensitivity && (
              <div className="bg-gray-50 p-4 rounded-lg">
                <h4 className="font-semibold mb-2">Sensitivity</h4>
                {typeof technique.fundamentalPhysics.sensitivity === 'string' ? (
                  <p className="text-gray-700">{technique.fundamentalPhysics.sensitivity}</p>
                ) : typeof technique.fundamentalPhysics.sensitivity === 'object' && technique.fundamentalPhysics.sensitivity.description ? (
                  <MarkdownContent content={technique.fundamentalPhysics.sensitivity.description} />
                ) : (
                  <p className="text-gray-700">{String(technique.fundamentalPhysics.sensitivity)}</p>
                )}
              </div>
            )}
          </div>
        </section>
      )}

      {/* Instrumentation Section */}
      {technique.instrumentation && (
        <section id="instrumentation" className="scroll-mt-20 mt-12">
          <h2>Instrumentation</h2>

          <h3>Source</h3>
          {typeof technique.instrumentation.source === 'string' ? (
            <p>{technique.instrumentation.source}</p>
          ) : technique.instrumentation.source && typeof technique.instrumentation.source === 'object' ? (
            <div className="space-y-3">
              {technique.instrumentation.source.type && typeof technique.instrumentation.source.type === 'string' && (
                <div>
                  <strong>Type:</strong>
                  <MarkdownContent content={technique.instrumentation.source.type} />
                </div>
              )}
              {technique.instrumentation.source.specifications && typeof technique.instrumentation.source.specifications === 'string' && (
                <div>
                  <strong>Specifications:</strong>
                  <MarkdownContent content={technique.instrumentation.source.specifications} />
                </div>
              )}
              {technique.instrumentation.source.powerRange && typeof technique.instrumentation.source.powerRange === 'string' && (
                <div>
                  <strong>Power Range:</strong>
                  <MarkdownContent content={technique.instrumentation.source.powerRange} />
                </div>
              )}
            </div>
          ) : (
            <p>No source information available.</p>
          )}

          <h3>Detector</h3>
          {typeof technique.instrumentation.detector === 'string' ? (
            <p>{technique.instrumentation.detector}</p>
          ) : technique.instrumentation.detector && typeof technique.instrumentation.detector === 'object' ? (
            <div className="space-y-3">
              {technique.instrumentation.detector.type && typeof technique.instrumentation.detector.type === 'string' && (
                <div>
                  <strong>Type:</strong>
                  <MarkdownContent content={technique.instrumentation.detector.type} />
                </div>
              )}
              {technique.instrumentation.detector.spectralRange && (
                <div>
                  <strong>Spectral Range:</strong> {technique.instrumentation.detector.spectralRange}
                </div>
              )}
              {technique.instrumentation.detector.efficiency && typeof technique.instrumentation.detector.efficiency === 'string' && (
                <div>
                  <strong>Efficiency:</strong>
                  <MarkdownContent content={technique.instrumentation.detector.efficiency} />
                </div>
              )}
              {technique.instrumentation.detector.resolution && typeof technique.instrumentation.detector.resolution === 'string' && (
                <div>
                  <strong>Resolution:</strong>
                  <MarkdownContent content={technique.instrumentation.detector.resolution} />
                </div>
              )}
            </div>
          ) : (
            <p>No detector information available.</p>
          )}

          {(technique.instrumentation.optics || technique.instrumentation.opticalSystem) && (
            <>
              <h3>Optical System</h3>
              {(() => {
                const optics = technique.instrumentation.optics || technique.instrumentation.opticalSystem
                return typeof optics === 'string' ? (
                  <p>{optics}</p>
                ) : optics && typeof optics === 'object' && !Array.isArray(optics) && 'components' in optics ? (
                  <div className="space-y-4">
                    {optics.components && Array.isArray(optics.components) && (
                      <div>
                        <strong>Components:</strong>
                        <ul className="list-disc list-inside mt-2 ml-4 space-y-2">
                          {optics.components.map((component: string, idx: number) => (
                            <li key={idx}>
                              <MarkdownContent content={component} />
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}
                    {optics.beamPath && typeof optics.beamPath === 'string' && (
                      <div>
                        <strong>Beam Path:</strong>
                        <MarkdownContent content={optics.beamPath} />
                      </div>
                    )}
                    {optics.focusing && typeof optics.focusing === 'string' && (
                      <div>
                        <strong>Focusing:</strong>
                        <MarkdownContent content={optics.focusing} />
                      </div>
                    )}
                  </div>
                ) : null
              })()}
            </>
          )}

          <h3>Critical Components</h3>
          <ul>
            {(technique.instrumentation.criticalComponents || []).map((component, idx) => (
              <li key={idx}>{component}</li>
            ))}
          </ul>

          <h3>Typical Configuration</h3>
          <MarkdownContent content={technique.instrumentation.typicalConfiguration || ''} />

          {technique.instrumentation.commercialSystems &&
            technique.instrumentation.commercialSystems.length > 0 && (
              <>
                <h3>Commercial Systems</h3>
                <div className="overflow-x-auto">
                  <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-gray-50">
                      <tr>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                          System
                        </th>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                          Vendor
                        </th>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                          Notes
                        </th>
                      </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                      {technique.instrumentation.commercialSystems.map((system, idx) => (
                        <tr key={idx}>
                          <td className="px-4 py-3 text-sm font-medium text-gray-900">
                            {system.name}
                          </td>
                          <td className="px-4 py-3 text-sm text-gray-700">{system.vendor}</td>
                          <td className="px-4 py-3 text-sm text-gray-700">{system.notes || '-'}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </>
            )}
        </section>
      )}

      {/* Methodology Section */}
      {technique.methodology && (
        <section id="methodology" className="scroll-mt-20 mt-12">
          <h2>Methodology</h2>

          <h3>Sample Preparation</h3>
          {Array.isArray(technique.methodology.samplePreparation) ? (
            <ul>
              {technique.methodology.samplePreparation.map((step, idx) => (
                <li key={idx}>{step}</li>
              ))}
            </ul>
          ) : technique.methodology.samplePreparation && typeof technique.methodology.samplePreparation === 'object' ? (
            <div className="space-y-4">
              {technique.methodology.samplePreparation.samplingRequired !== undefined && (
                <div>
                  <strong>Sampling Required:</strong>{' '}
                  {technique.methodology.samplePreparation.samplingRequired ? 'Yes' : 'No'}
                </div>
              )}
              {technique.methodology.samplePreparation.sampleSize && (
                <div>
                  <strong>Sample Size:</strong> {technique.methodology.samplePreparation.sampleSize}
                </div>
              )}
              {technique.methodology.samplePreparation.mountingProcedure && (
                <div>
                  <strong>Mounting Procedure:</strong>{' '}
                  {technique.methodology.samplePreparation.mountingProcedure}
                </div>
              )}
              {technique.methodology.samplePreparation.surfacePreparation && (
                <div>
                  <strong>Surface Preparation:</strong>{' '}
                  {technique.methodology.samplePreparation.surfacePreparation}
                </div>
              )}
              {technique.methodology.samplePreparation.contaminationConcerns && (
                <div>
                  <strong>Contamination Concerns:</strong>{' '}
                  {technique.methodology.samplePreparation.contaminationConcerns}
                </div>
              )}
            </div>
          ) : (
            <p>No sample preparation information available.</p>
          )}

          <h3>Measurement Protocol</h3>
          {typeof technique.methodology.measurementProtocol === 'string' ? (
            <MarkdownContent content={technique.methodology.measurementProtocol} />
          ) : technique.methodology.measurementProtocol && typeof technique.methodology.measurementProtocol === 'object' && Array.isArray(technique.methodology.measurementProtocol.steps) ? (
            <div className="space-y-6">
              {technique.methodology.measurementProtocol.steps.map((step: any, idx: number) => (
                <div key={idx} className="border-l-4 border-blue-500 pl-4">
                  <h4 className="font-semibold text-lg mb-2">
                    Step {step.stepNumber || idx + 1}: {step.title || `Step ${idx + 1}`}
                  </h4>
                  {step.description && (
                    <MarkdownContent content={step.description} />
                  )}
                  {step.duration && (
                    <p className="text-sm text-gray-600 mt-2">
                      <strong>Duration:</strong> {step.duration}
                    </p>
                  )}
                  {step.criticalParameters && Array.isArray(step.criticalParameters) && step.criticalParameters.length > 0 && (
                    <div className="mt-3">
                      <strong className="text-sm">Critical Parameters:</strong>
                      <ul className="list-disc list-inside mt-1 text-sm text-gray-700">
                        {step.criticalParameters.map((param: string, paramIdx: number) => (
                          <li key={paramIdx}>{param}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <p>No measurement protocol information available.</p>
          )}

          {((technique.methodology.typicalParameters && technique.methodology.typicalParameters.length > 0) ||
            (technique.methodology.operatingParameters && technique.methodology.operatingParameters.length > 0)) && (
            <>
              <h3>Operating Parameters</h3>
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Parameter
                      </th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Typical Value
                      </th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Range
                      </th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Notes
                      </th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {(technique.methodology.operatingParameters || technique.methodology.typicalParameters || []).map((param: any, idx: number) => (
                      <tr key={idx}>
                        <td className="px-4 py-3 text-sm font-medium text-gray-900">
                          {param.parameter}
                        </td>
                        <td className="px-4 py-3 text-sm text-gray-700">
                          {param.typicalValue || param.value || '-'}
                        </td>
                        <td className="px-4 py-3 text-sm text-gray-700">
                          {param.range || '-'}
                        </td>
                        <td className="px-4 py-3 text-sm text-gray-700">{param.notes || '-'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          )}

          {technique.methodology.calibration && (
            <>
              <h3>Calibration</h3>
              {typeof technique.methodology.calibration === 'string' ? (
                <MarkdownContent content={technique.methodology.calibration} />
              ) : typeof technique.methodology.calibration === 'object' ? (
                <div className="space-y-4">
                  {technique.methodology.calibration.standards && Array.isArray(technique.methodology.calibration.standards) && (
                    <div>
                      <strong>Standards:</strong>
                      <ul className="list-disc list-inside mt-2 ml-4">
                        {technique.methodology.calibration.standards.map((standard: string, idx: number) => (
                          <li key={idx}>{standard}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                  {technique.methodology.calibration.frequency && (
                    <div>
                      <strong>Frequency:</strong> {technique.methodology.calibration.frequency}
                    </div>
                  )}
                  {technique.methodology.calibration.procedure && (
                    <div>
                      <strong>Procedure:</strong>
                      <MarkdownContent content={technique.methodology.calibration.procedure} />
                    </div>
                  )}
                </div>
              ) : null}
            </>
          )}

          {technique.methodology.qualityControl && (
            <>
              <h3>Quality Control</h3>
              {Array.isArray(technique.methodology.qualityControl) ? (
                <ul>
                  {technique.methodology.qualityControl.map((item, idx) => (
                    <li key={idx}>{item}</li>
                  ))}
                </ul>
              ) : typeof technique.methodology.qualityControl === 'object' ? (
                <div className="space-y-4">
                  {technique.methodology.qualityControl.checkpoints && Array.isArray(technique.methodology.qualityControl.checkpoints) && (
                    <div>
                      <strong>Checkpoints:</strong>
                      <ul className="list-disc list-inside mt-2 ml-4">
                        {technique.methodology.qualityControl.checkpoints.map((checkpoint: string, idx: number) => (
                          <li key={idx}>{checkpoint}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                  {technique.methodology.qualityControl.commonArtifacts && Array.isArray(technique.methodology.qualityControl.commonArtifacts) && (
                    <div>
                      <strong>Common Artifacts:</strong>
                      <div className="mt-2 space-y-3">
                        {technique.methodology.qualityControl.commonArtifacts.map((artifact: any, idx: number) => (
                          <div key={idx} className="border-l-2 border-yellow-400 pl-3">
                            <strong>{artifact.artifact || `Artifact ${idx + 1}`}:</strong>
                            {artifact.cause && (
                              <p className="text-sm text-gray-600 mt-1">
                                <strong>Cause:</strong> {artifact.cause}
                              </p>
                            )}
                            {artifact.mitigation && (
                              <p className="text-sm text-gray-700 mt-1">
                                <strong>Mitigation:</strong> {artifact.mitigation}
                              </p>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                  {technique.methodology.qualityControl.troubleshooting && Array.isArray(technique.methodology.qualityControl.troubleshooting) && (
                    <div>
                      <strong>Troubleshooting:</strong>
                      <div className="mt-2 space-y-3">
                        {technique.methodology.qualityControl.troubleshooting.map((item: any, idx: number) => (
                          <div key={idx} className="border-l-2 border-blue-400 pl-3">
                            <strong>{item.problem || `Problem ${idx + 1}`}:</strong>
                            {item.solution && (
                              <p className="text-sm text-gray-700 mt-1">
                                <strong>Solution:</strong> {item.solution}
                              </p>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              ) : null}
            </>
          )}
        </section>
      )}

      {/* Data Analysis Section */}
      {technique.dataAnalysis && (
        <section id="data-analysis" className="scroll-mt-20 mt-12">
          <h2>Data Analysis</h2>

          <h3>Raw Data Format</h3>
          {typeof technique.dataAnalysis.rawDataFormat === 'string' ? (
            <MarkdownContent content={technique.dataAnalysis.rawDataFormat} />
          ) : technique.dataAnalysis.rawDataFormat && typeof technique.dataAnalysis.rawDataFormat === 'object' ? (
            <div className="space-y-3">
              {technique.dataAnalysis.rawDataFormat.fileFormats && Array.isArray(technique.dataAnalysis.rawDataFormat.fileFormats) && (
                <div>
                  <strong>File Formats:</strong>
                  <ul className="list-disc list-inside mt-2 ml-4">
                    {technique.dataAnalysis.rawDataFormat.fileFormats.map((format: string, idx: number) => (
                      <li key={idx}>{format}</li>
                    ))}
                  </ul>
                </div>
              )}
              {technique.dataAnalysis.rawDataFormat.dataStructure && (
                <div>
                  <strong>Data Structure:</strong> {technique.dataAnalysis.rawDataFormat.dataStructure}
                </div>
              )}
              {technique.dataAnalysis.rawDataFormat.typicalFileSize && (
                <div>
                  <strong>Typical File Size:</strong> {technique.dataAnalysis.rawDataFormat.typicalFileSize}
                </div>
              )}
            </div>
          ) : (
            <p>No raw data format information available.</p>
          )}

          <h3>Preprocessing</h3>
          {Array.isArray(technique.dataAnalysis.preprocessing) && technique.dataAnalysis.preprocessing.length > 0 ? (
            (() => {
              const firstItem = technique.dataAnalysis.preprocessing[0]
              return typeof firstItem === 'string' ? (
                <ul>
                  {(technique.dataAnalysis.preprocessing as string[]).map((step: string, idx: number) => (
                    <li key={idx}>{step}</li>
                  ))}
                </ul>
              ) : (
                <div className="space-y-4">
                  {(technique.dataAnalysis.preprocessing as Array<{ step?: string; description?: string; software?: string }>).map((item: any, idx: number) => (
                    <div key={idx} className="border-l-4 border-blue-500 pl-4">
                      <h4 className="font-semibold text-lg mb-2">
                        {item.step || `Step ${idx + 1}`}
                      </h4>
                      {item.description && (
                        <MarkdownContent content={item.description} />
                      )}
                      {item.software && (
                        <p className="text-sm text-gray-600 mt-2">
                          <strong>Software:</strong> {item.software}
                        </p>
                      )}
                    </div>
                  ))}
                </div>
              )
            })()
          ) : (
            <p>No preprocessing information available.</p>
          )}

          <h3>Analysis Workflow</h3>
          {typeof technique.dataAnalysis.analysisWorkflow === 'string' ? (
            <MarkdownContent content={technique.dataAnalysis.analysisWorkflow} />
          ) : technique.dataAnalysis.analysisWorkflow && typeof technique.dataAnalysis.analysisWorkflow === 'object' && Array.isArray(technique.dataAnalysis.analysisWorkflow.steps) ? (
            <div className="space-y-6">
              {technique.dataAnalysis.analysisWorkflow.steps.map((step: any, idx: number) => (
                <div key={idx} className="border-l-4 border-blue-500 pl-4">
                  <h4 className="font-semibold text-lg mb-2">
                    Step {step.stepNumber || idx + 1}: {step.title || `Step ${idx + 1}`}
                  </h4>
                  {step.description && (
                    <MarkdownContent content={step.description} />
                  )}
                  {step.software && (
                    <p className="text-sm text-gray-600 mt-2">
                      <strong>Software:</strong> {step.software}
                    </p>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <p>No analysis workflow information available.</p>
          )}

          {technique.dataAnalysis.softwareTools && technique.dataAnalysis.softwareTools.length > 0 && (
            <>
              <h3>Software Tools</h3>
              <div className="space-y-2">
                {technique.dataAnalysis.softwareTools.map((tool, idx) => (
                  <div key={idx} className="flex items-start gap-2">
                    <span className="font-medium">{tool.name}</span>
                    {tool.url && (
                      <a
                        href={tool.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-primary-600 hover:text-primary-800 inline-flex items-center gap-1"
                      >
                        <ExternalLink className="h-3 w-3" />
                      </a>
                    )}
                    {tool.notes && <span className="text-gray-600 text-sm">— {tool.notes}</span>}
                  </div>
                ))}
              </div>
            </>
          )}

          <h3>Interpretation Guidelines</h3>
          {typeof technique.dataAnalysis.interpretationGuidelines === 'string' ? (
            <MarkdownContent content={technique.dataAnalysis.interpretationGuidelines} />
          ) : Array.isArray(technique.dataAnalysis.interpretationGuidelines) ? (
            <ul className="space-y-2">
              {technique.dataAnalysis.interpretationGuidelines.map((guideline: string, idx: number) => (
                <li key={idx}>{guideline}</li>
              ))}
            </ul>
          ) : (
            <p>No interpretation guidelines available.</p>
          )}

          <h3>Common Pitfalls</h3>
          <ul>
            {(technique.dataAnalysis.commonPitfalls || []).map((pitfall, idx) => (
              <li key={idx}>{pitfall}</li>
            ))}
          </ul>
        </section>
      )}

      {/* Applications Section */}
      {technique.applications && (
        <section id="applications" className="scroll-mt-20 mt-12">
          <h2>Applications & Examples</h2>

          <h3>Primary Uses</h3>
          <ul>
            {(technique.applications.primaryUses || []).map((use, idx) => (
              <li key={idx}>{use}</li>
            ))}
          </ul>

          <h3>Material Types</h3>
          <ul>
            {(technique.applications.materialTypes || []).map((material, idx) => {
              if (typeof material === 'string') {
                return <li key={idx}>{material}</li>
              } else if (material && typeof material === 'object' && 'material' in material) {
                const mat = material as { material?: string; suitability?: string; notes?: string }
                return (
                  <li key={idx}>
                    <strong>{mat.material}</strong>
                    {mat.suitability && <span className="ml-2 text-sm text-gray-600">({mat.suitability})</span>}
                    {mat.notes && <p className="text-sm text-gray-700 mt-1 ml-4">{mat.notes}</p>}
                  </li>
                )
              }
              return null
            })}
          </ul>

          {technique.applications.caseStudies && technique.applications.caseStudies.length > 0 && (
            <>
              <h3>Case Studies</h3>
              <div className="space-y-6">
                {technique.applications.caseStudies.map((study, idx) => (
                  <div key={idx} className="bg-gray-50 p-6 rounded-lg">
                    <h4 className="font-semibold mb-2">{study.title}</h4>
                    <p className="text-gray-700 mb-2">{study.description}</p>
                    {study.reference && (() => {
                      const ref = study.reference as any
                      const citation = typeof ref === 'string' 
                        ? ref 
                        : typeof ref === 'object' && ref && 'citation' in ref
                        ? ref.citation
                        : JSON.stringify(ref)
                      const doi = typeof ref === 'object' && ref && 'doi' in ref ? ref.doi : null
                      return (
                        <p className="text-sm text-gray-600 italic">
                          {citation}
                          {doi && (
                            <a
                              href={`https://doi.org/${doi}`}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-primary-600 hover:text-primary-800 ml-2 inline-flex items-center gap-1"
                            >
                              DOI: {doi}
                              <ExternalLink className="h-3 w-3" />
                            </a>
                          )}
                        </p>
                      )
                    })()}
                  </div>
                ))}
              </div>
            </>
          )}
        </section>
      )}

      {/* Multimodal Section */}
      <section id="multimodal" className="scroll-mt-20 mt-12">
        <h2>Multimodal Synergies</h2>

        {/* Comparison Link for Nonlinear Microscopy Techniques */}
        {(technique.id === 'shg-microscopy' || 
          technique.id === 'thg-microscopy' || 
          technique.id === 'tpef-microscopy') && (
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
            <div className="flex items-start gap-3">
              <BarChart3 className="w-5 h-5 text-blue-600 flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-semibold text-blue-900 mb-1">
                  Detailed Technique Comparison
                </h4>
                <p className="text-sm text-blue-800 mb-2">
                  Compare {technique.acronym || technique.name} side-by-side with SHG, THG, and TPEF across technical specifications, applications, and practical considerations.
                </p>
                <Link
                  href="/comparisons/nonlinear-microscopy"
                  className="inline-flex items-center text-sm font-medium text-blue-600 hover:text-blue-800 hover:underline"
                >
                  View Full Comparison
                  <ExternalLink className="w-4 h-4 ml-1" />
                </Link>
              </div>
            </div>
          </div>
        )}

        {/* Related Techniques Comparison Link for CARS */}
        {technique.id === 'cars-microscopy' && (
          <div className="bg-indigo-50 border border-indigo-200 rounded-lg p-4 mb-6">
            <div className="flex items-start gap-3">
              <BarChart3 className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-semibold text-indigo-900 mb-1">
                  Related Nonlinear Microscopy Techniques
                </h4>
                <p className="text-sm text-indigo-800 mb-2">
                  CARS is part of the nonlinear optical microscopy family. Compare SHG, THG, and TPEF techniques to understand how CARS complements other label-free imaging methods.
                </p>
                <Link
                  href="/comparisons/nonlinear-microscopy"
                  className="inline-flex items-center text-sm font-medium text-indigo-600 hover:text-indigo-800 hover:underline"
                >
                  View Nonlinear Microscopy Comparison
                  <ExternalLink className="w-4 h-4 ml-1" />
                </Link>
              </div>
            </div>
          </div>
        )}

        {technique.multimodal?.complementaryTechniques && technique.multimodal.complementaryTechniques.length > 0 && (
          <>
            <h3>Complementary Techniques</h3>
            <ul>
              {technique.multimodal.complementaryTechniques.map((item, idx) => {
                // Handle both string format and object format
                let techId: string;
                if (typeof item === 'string') {
                  techId = item;
                } else if (item && typeof item === 'object' && 'techniqueId' in item) {
                  techId = String((item as any).techniqueId || '');
                } else {
                  // Fallback: try to extract ID from object if it has an 'id' property
                  techId = String((item as any)?.id || '');
                }
                
                // Ensure techId is a valid string, skip if not
                if (!techId || typeof techId !== 'string') {
                  console.warn('Invalid technique ID in complementaryTechniques:', item);
                  return null;
                }
                
                const rationale = typeof item === 'object' && (item as any).rationale ? (item as any).rationale : null;
                const relatedTech = getAllTechniques().find(t => t.id === techId);
                
                return (
                  <li key={idx}>
                    <Link
                      href={`/techniques/${techId}`}
                      className="text-primary-600 hover:text-primary-800"
                    >
                      {relatedTech?.name || techId}
                    </Link>
                    {rationale && (
                      <p className="text-sm text-gray-600 mt-1 ml-4">{rationale}</p>
                    )}
                  </li>
                );
              })}
            </ul>
          </>
        )}

        {(technique.multimodal?.standardCombinations || technique.multimodal?.commonCombinations) && 
         (technique.multimodal.standardCombinations || technique.multimodal.commonCombinations || []).length > 0 && (
          <>
            <h3>Standard Combinations</h3>
            <div className="space-y-4">
              {(technique.multimodal.standardCombinations || technique.multimodal.commonCombinations || []).map((combo: any, idx: number) => {
                // Ensure techniques is an array of strings
                const techniques = Array.isArray(combo.techniques) 
                  ? combo.techniques.map((t: any) => typeof t === 'string' ? t : String(t || ''))
                  : [];
                
                return (
                  <div key={idx} className="bg-gray-50 p-4 rounded-lg">
                    <h4 className="font-semibold mb-2">
                      {combo.name || techniques.map((t: string) => t.toUpperCase()).join(' + ')}
                    </h4>
                    {combo.workflow && (
                      <div className="mb-2">
                        <p className="text-sm font-medium text-gray-700 mb-1">Workflow:</p>
                        <p className="text-gray-700 whitespace-pre-line">{combo.workflow}</p>
                      </div>
                    )}
                    {combo.rationale && (
                      <p className="text-gray-700 mb-2">{combo.rationale}</p>
                    )}
                    {combo.exampleApplication && (
                      <div className="mt-2">
                        <p className="text-sm font-medium text-gray-700 mb-1">Example Application:</p>
                        <p className="text-sm text-gray-600 italic whitespace-pre-line">{combo.exampleApplication}</p>
                      </div>
                    )}
                    {combo.examples && (
                      <p className="text-sm text-gray-600 italic">{combo.examples}</p>
                    )}
                    {combo.timeInvestment && (
                      <p className="text-xs text-gray-500 mt-2">Time investment: {combo.timeInvestment}</p>
                    )}
                  </div>
                );
              })}
            </div>
          </>
        )}
      </section>

      {/* References Section */}
      {technique.references && (
        <section id="references" className="scroll-mt-20 mt-12">
          <h2>References & Resources</h2>

          {technique.references.foundationalPapers && technique.references.foundationalPapers.length > 0 && (
            <>
              <h3>Foundational Papers</h3>
              <ul className="space-y-2">
                {technique.references.foundationalPapers.map((paper: any, idx) => {
                  const citation = typeof paper === 'string' ? paper : (typeof paper.citation === 'string' ? paper.citation : JSON.stringify(paper.citation || paper))
                  const doi = typeof paper === 'object' && paper ? paper.doi : null
                  const notes = typeof paper === 'object' && paper && 'significance' in paper ? paper.significance : null
                  return (
                    <li key={idx} className="text-sm">
                      {citation}
                      {doi && (
                        <a
                          href={`https://doi.org/${doi}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-primary-600 hover:text-primary-800 ml-2 inline-flex items-center gap-1"
                        >
                          DOI: {doi}
                          <ExternalLink className="h-3 w-3" />
                        </a>
                      )}
                      {notes && <span className="text-gray-600 ml-2">— {notes}</span>}
                    </li>
                  )
                })}
              </ul>
            </>
          )}

          {technique.references.keyPapers && technique.references.keyPapers.length > 0 && (
            <>
              <h3>Key Papers</h3>
              <ul className="space-y-2">
                {technique.references.keyPapers.map((paper: any, idx) => {
                  const citation = typeof paper === 'string' ? paper : (typeof paper.citation === 'string' ? paper.citation : JSON.stringify(paper.citation || paper))
                  const doi = typeof paper === 'object' && paper ? paper.doi : null
                  const notes = typeof paper === 'object' && paper && 'notes' in paper ? paper.notes : null
                  return (
                    <li key={idx} className="text-sm">
                      {citation}
                      {doi && (
                        <a
                          href={`https://doi.org/${doi}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-primary-600 hover:text-primary-800 ml-2 inline-flex items-center gap-1"
                        >
                          DOI: {doi}
                          <ExternalLink className="h-3 w-3" />
                        </a>
                      )}
                      {notes && <span className="text-gray-600 ml-2">— {notes}</span>}
                    </li>
                  )
                })}
              </ul>
            </>
          )}

          {technique.references.methodologyReviews && technique.references.methodologyReviews.length > 0 && (
            <>
              <h3>Methodology Reviews</h3>
              <ul className="space-y-2">
                {technique.references.methodologyReviews.map((review: any, idx) => {
                  const citation = typeof review === 'string' ? review : (typeof review.citation === 'string' ? review.citation : JSON.stringify(review.citation || review))
                  const doi = typeof review === 'object' && review ? review.doi : null
                  const notes = typeof review === 'object' && review && 'scope' in review ? review.scope : null
                  return (
                    <li key={idx} className="text-sm">
                      {citation}
                      {doi && (
                        <a
                          href={`https://doi.org/${doi}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-primary-600 hover:text-primary-800 ml-2 inline-flex items-center gap-1"
                        >
                          DOI: {doi}
                          <ExternalLink className="h-3 w-3" />
                        </a>
                      )}
                      {notes && <span className="text-gray-600 ml-2">— {notes}</span>}
                    </li>
                  )
                })}
              </ul>
            </>
          )}

          {technique.references.reviews && technique.references.reviews.length > 0 && (
            <>
              <h3>Reviews</h3>
              <ul className="space-y-2">
                {technique.references.reviews.map((review: any, idx) => {
                  const citation = typeof review === 'string' ? review : (typeof review.citation === 'string' ? review.citation : JSON.stringify(review.citation || review))
                  const doi = typeof review === 'object' && review ? review.doi : null
                  const notes = typeof review === 'object' && review && 'notes' in review ? review.notes : null
                  return (
                    <li key={idx} className="text-sm">
                      {citation}
                      {doi && (
                        <a
                          href={`https://doi.org/${doi}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-primary-600 hover:text-primary-800 ml-2 inline-flex items-center gap-1"
                        >
                          DOI: {doi}
                          <ExternalLink className="h-3 w-3" />
                        </a>
                      )}
                      {notes && <span className="text-gray-600 ml-2">— {notes}</span>}
                    </li>
                  )
                })}
              </ul>
            </>
          )}

          {technique.references.recentApplications && technique.references.recentApplications.length > 0 && (
            <>
              <h3>Recent Applications</h3>
              <ul className="space-y-2">
                {technique.references.recentApplications.map((paper: any, idx) => {
                  const citation = typeof paper === 'string' ? paper : (typeof paper.citation === 'string' ? paper.citation : JSON.stringify(paper.citation || paper))
                  const doi = typeof paper === 'object' && paper ? paper.doi : null
                  const notes = typeof paper === 'object' && paper && 'summary' in paper ? paper.summary : null
                  return (
                    <li key={idx} className="text-sm">
                      {citation}
                      {doi && (
                        <a
                          href={`https://doi.org/${doi}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-primary-600 hover:text-primary-800 ml-2 inline-flex items-center gap-1"
                        >
                          DOI: {doi}
                          <ExternalLink className="h-3 w-3" />
                        </a>
                      )}
                      {notes && <span className="text-gray-600 ml-2">— {notes}</span>}
                    </li>
                  )
                })}
              </ul>
            </>
          )}

          {technique.references.onlineResources && technique.references.onlineResources.length > 0 && (
            <>
              <h3>Online Resources</h3>
              <ul className="space-y-2">
                {technique.references.onlineResources.map((resource, idx) => (
                  <li key={idx} className="text-sm">
                    <a
                      href={resource.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-primary-600 hover:text-primary-800 inline-flex items-center gap-1"
                    >
                      {resource.title}
                      <ExternalLink className="h-3 w-3" />
                    </a>
                  </li>
                ))}
              </ul>
            </>
          )}
        </section>
      )}

      {/* Tags */}
      <section className="mt-12 pt-8 border-t">
        <div className="flex flex-wrap gap-2">
          {(technique.tags || []).map((tag, idx) => (
            <span
              key={idx}
              className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800"
            >
              {tag}
            </span>
          ))}
        </div>
        <p className="text-sm text-gray-500 mt-4">
          Last updated: {new Date(technique.lastUpdated).toLocaleDateString()}
        </p>
      </section>
    </div>
  )
}

