'use client'

import { useState, useEffect } from 'react'
import type { Technique } from '@/types/technique'
import { cn } from '@/lib/utils'

const sections = [
  { id: 'overview', label: 'Overview' },
  { id: 'physics', label: 'Physics & Theory' },
  { id: 'instrumentation', label: 'Instrumentation' },
  { id: 'methodology', label: 'Methodology' },
  { id: 'data-analysis', label: 'Data Analysis' },
  { id: 'applications', label: 'Applications' },
  { id: 'multimodal', label: 'Multimodal' },
  { id: 'references', label: 'References' },
]

export function TableOfContents({ technique }: { technique: Technique }) {
  const [activeSection, setActiveSection] = useState<string>('overview')

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY + 100

      for (let i = sections.length - 1; i >= 0; i--) {
        const section = document.getElementById(sections[i].id)
        if (section && section.offsetTop <= scrollPosition) {
          setActiveSection(sections[i].id)
          break
        }
      }
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <nav className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
      <h3 className="font-semibold mb-3 text-gray-900">Contents</h3>
      <ul className="space-y-1">
        {sections.map((section) => (
          <li key={section.id}>
            <a
              href={`#${section.id}`}
              onClick={(e) => {
                e.preventDefault()
                const element = document.getElementById(section.id)
                if (element) {
                  element.scrollIntoView({ behavior: 'smooth', block: 'start' })
                }
              }}
              className={cn(
                'block px-2 py-1 text-sm rounded transition-colors',
                activeSection === section.id
                  ? 'bg-primary-100 text-primary-800 font-medium'
                  : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
              )}
            >
              {section.label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  )
}

