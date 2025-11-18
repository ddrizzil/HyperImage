'use client'

import { BlockMath, InlineMath } from 'react-katex'
import 'katex/dist/katex.min.css'
import type { Equation as EquationType } from '@/types/technique'

/**
 * Renders a LaTeX equation using KaTeX with variable definitions
 */
export function Equation({ equation }: { equation: EquationType | string }) {
  // Handle legacy string format for backward compatibility
  if (typeof equation === 'string') {
    try {
      return (
        <div className="my-4 p-4 bg-gray-50 rounded-lg overflow-x-auto">
          <BlockMath math={equation} />
        </div>
      )
    } catch (error) {
      return (
        <div className="my-4 p-4 bg-gray-50 rounded-lg">
          <code className="font-mono text-sm">{equation}</code>
        </div>
      )
    }
  }

  // Handle new object format with variable definitions
  try {
    // Remove $$ delimiters if present (KaTeX BlockMath doesn't need them)
    const latex = equation.latex.replace(/^\$\$|\$\$$/g, '')
    
    return (
      <div className="my-4 p-4 bg-gray-50 rounded-lg">
        {equation.description && (
          <p className="text-sm text-gray-600 mb-2 italic">{equation.description}</p>
        )}
        <div className="overflow-x-auto mb-3">
          <BlockMath math={latex} />
        </div>
        {equation.variables && equation.variables.length > 0 && (
          <div className="mt-3 pt-3 border-t border-gray-300">
            <p className="text-xs font-semibold text-gray-700 mb-2">Variables:</p>
            <dl className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
              {equation.variables.map((variable, idx) => {
                // Render symbol as LaTeX if it contains LaTeX syntax, otherwise plain text
                const hasLatexSyntax = variable.symbol.includes('\\') || 
                                       variable.symbol.includes('_') || 
                                       variable.symbol.includes('^') ||
                                       variable.symbol.includes('{') ||
                                       variable.symbol.includes('}')
                
                const symbolElement = hasLatexSyntax ? (
                  <InlineMath math={variable.symbol} />
                ) : (
                  <span className="font-mono">{variable.symbol}</span>
                )
                
                return (
                  <div key={idx} className="flex items-start gap-2">
                    <dt className="font-semibold text-primary-700 min-w-[80px] flex-shrink-0">
                      {symbolElement}:
                    </dt>
                    <dd className="text-gray-700">
                      <span>{variable.meaning}</span>
                      <span className="text-gray-500 ml-1">({variable.units})</span>
                    </dd>
                  </div>
                )
              })}
            </dl>
          </div>
        )}
      </div>
    )
  } catch (error) {
    return (
      <div className="my-4 p-4 bg-gray-50 rounded-lg">
        <code className="font-mono text-sm">{equation.latex}</code>
      </div>
    )
  }
}

