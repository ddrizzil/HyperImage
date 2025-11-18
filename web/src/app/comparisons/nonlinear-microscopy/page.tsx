'use client'

import React from 'react'
import Link from 'next/link'
import { BookOpen, Download, Share2 } from 'lucide-react'
import { NonlinearMicroscopyComparison } from '@/components/comparisons/NonlinearMicroscopyComparison'

export default function NonlinearMicroscopyComparisonPage() {
  const handleExportPDF = () => {
    // TODO: Implement PDF export
    window.print()
  }

  const handleShare = () => {
    if (navigator.share) {
      navigator.share({
        title: 'Nonlinear Optical Microscopy Comparison',
        text: 'Compare SHG, THG, and TPEF techniques for cultural heritage applications',
        url: window.location.href,
      })
    } else {
      navigator.clipboard.writeText(window.location.href)
      alert('Link copied to clipboard!')
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div>
              <Link
                href="/techniques"
                className="text-indigo-600 hover:text-indigo-800 text-sm font-medium inline-flex items-center gap-1"
              >
                ← Back to Techniques
              </Link>
              <h1 className="text-3xl font-bold text-gray-900 mt-2">
                Nonlinear Optical Microscopy Comparison
              </h1>
              <p className="text-gray-600 mt-1">
                SHG vs THG vs TPEF for Cultural Heritage Science
              </p>
            </div>
            <div className="flex gap-3">
              <button
                onClick={handleExportPDF}
                className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition flex items-center gap-2 text-sm"
              >
                <Download className="w-4 h-4" />
                Export PDF
              </button>
              <button
                onClick={handleShare}
                className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition flex items-center gap-2 text-sm"
              >
                <Share2 className="w-4 h-4" />
                Share
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        {/* Introduction */}
        <div className="bg-blue-50 border-l-4 border-blue-500 rounded-r-lg p-6 mb-8">
          <div className="flex items-start gap-4">
            <BookOpen className="w-6 h-6 text-blue-600 flex-shrink-0 mt-1" />
            <div>
              <h2 className="text-lg font-semibold text-blue-900 mb-2">About This Comparison</h2>
              <p className="text-blue-800 text-sm leading-relaxed">
                Second Harmonic Generation (SHG), Third Harmonic Generation (THG), and Two-Photon
                Excited Fluorescence (TPEF) are complementary nonlinear optical microscopy techniques
                often used together for comprehensive structural and chemical characterization of
                heritage materials. This comparison helps you understand their differences and choose
                the right technique(s) for your application.
              </p>
            </div>
          </div>
        </div>

        {/* Comparison Component */}
        <NonlinearMicroscopyComparison />

        {/* Additional Resources */}
        <div className="mt-12 grid md:grid-cols-3 gap-6">
          <Link
            href="/techniques/shg-microscopy"
            className="bg-white border-2 border-blue-200 rounded-lg p-6 hover:border-blue-400 transition block"
          >
            <h3 className="text-xl font-bold text-blue-900 mb-2">Learn More: SHG</h3>
            <p className="text-gray-600 text-sm">
              Complete technical documentation for Second Harmonic Generation microscopy
            </p>
          </Link>

          <Link
            href="/techniques/thg-microscopy"
            className="bg-white border-2 border-purple-200 rounded-lg p-6 hover:border-purple-400 transition block"
          >
            <h3 className="text-xl font-bold text-purple-900 mb-2">Learn More: THG</h3>
            <p className="text-gray-600 text-sm">
              Complete technical documentation for Third Harmonic Generation microscopy
            </p>
          </Link>

          <Link
            href="/techniques/tpef-microscopy"
            className="bg-white border-2 border-green-200 rounded-lg p-6 hover:border-green-400 transition block"
          >
            <h3 className="text-xl font-bold text-green-900 mb-2">Learn More: TPEF</h3>
            <p className="text-gray-600 text-sm">
              Complete technical documentation for Two-Photon Excited Fluorescence
            </p>
          </Link>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-100 border-t border-gray-300 mt-12 py-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-sm text-gray-600">
          <p>Last updated: January 15, 2025</p>
          <p className="mt-1">
            For questions about these techniques, consult the detailed documentation pages or contact
            an expert in nonlinear microscopy.
          </p>
        </div>
      </footer>

      {/* Print Styles */}
      <style jsx global>{`
        @media print {
          header,
          footer,
          button,
          .no-print {
            display: none !important;
          }
          main {
            max-width: 100% !important;
            padding: 0 !important;
          }
          table {
            page-break-inside: avoid;
          }
        }
      `}</style>
    </div>
  )
}

