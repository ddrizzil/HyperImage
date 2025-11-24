'use client'

import { useEffect, useState } from 'react'
import Link from 'next/link'
import { BookOpen, ExternalLink } from 'lucide-react'

interface RSSItem {
  title: string
  link: string
  description: string
  pubDate: string
  author?: string
  category?: string
}

export function ReadingFeed() {
  const [items, setItems] = useState<RSSItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    // Fetch RSS feed from paper-digest repository
    const fetchRSS = async () => {
      try {
        const response = await fetch(
          'https://raw.githubusercontent.com/ddrizzil/HyperImage/main/web/feed.xml',
          { cache: 'no-store' }
        )
        
        if (!response.ok) {
          throw new Error('Failed to fetch RSS feed')
        }
        
        const xmlText = await response.text()
        const parser = new DOMParser()
        const xmlDoc = parser.parseFromString(xmlText, 'text/xml')
        
        // Check for parsing errors
        const parseError = xmlDoc.querySelector('parsererror')
        if (parseError) {
          throw new Error('Failed to parse RSS feed')
        }
        
        // Extract items
        const itemElements = xmlDoc.querySelectorAll('item')
        const parsedItems: RSSItem[] = []
        
        itemElements.forEach((item, index) => {
          if (index >= 5) return // Only show top 5
          
          const title = item.querySelector('title')?.textContent || 'Untitled'
          const link = item.querySelector('link')?.textContent || ''
          const description = item.querySelector('description')?.textContent || ''
          const pubDate = item.querySelector('pubDate')?.textContent || ''
          const author = item.querySelector('author')?.textContent || ''
          const category = item.querySelector('category')?.textContent || ''
          
          // Parse description to extract summary (first part before " | ")
          const descriptionParts = description.split(' | ')
          const summary = descriptionParts[0] || description
          
          parsedItems.push({
            title,
            link,
            description: summary.substring(0, 200) + (summary.length > 200 ? '...' : ''),
            pubDate,
            author,
            category,
          })
        })
        
        setItems(parsedItems)
        setLoading(false)
      } catch (err) {
        console.error('Error fetching RSS feed:', err)
        setError('Unable to load reading feed')
        setLoading(false)
      }
    }
    
    fetchRSS()
  }, [])

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-md border border-gray-200 p-4">
        <div className="flex items-center gap-2 mb-3">
          <BookOpen className="w-5 h-5 text-primary-600" />
          <h3 className="text-lg font-semibold text-gray-900">What I'm Reading</h3>
        </div>
        <div className="text-sm text-gray-500">Loading...</div>
      </div>
    )
  }

  if (error || items.length === 0) {
    return (
      <div className="bg-white rounded-lg shadow-md border border-gray-200 p-4">
        <div className="flex items-center gap-2 mb-3">
          <BookOpen className="w-5 h-5 text-primary-600" />
          <h3 className="text-lg font-semibold text-gray-900">What I'm Reading</h3>
        </div>
        <div className="text-sm text-gray-500">
          {error || 'No papers available'}
        </div>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-lg shadow-md border border-gray-200 p-4">
      <div className="flex items-center gap-2 mb-3">
        <BookOpen className="w-5 h-5 text-primary-600" />
        <h3 className="text-lg font-semibold text-gray-900">What I'm Reading</h3>
      </div>
      
      {/* Reading Notice */}
      <div className="reading-notice mb-4">
        <p className="text-sm mb-2">
          <strong>About This Digest:</strong> This is my personal daily paper digest—algorithmically selected from 
          20+ journal feeds based on keyword scoring. Not all papers are equally relevant; some are highly applicable, 
          others tangential. This represents what crosses my desk each morning as I learn, shared in case others find 
          the cross-domain coverage useful.
        </p>
        <p className="text-sm">
          <strong>Selection is automated</strong> (not hand-curated), so quality and relevance vary. Consider this a 
          starting point for discovering papers across heritage science, RF/imaging, and adjacent fields—not a vetted 
          collection of "best" papers.
        </p>
      </div>
      <div className="space-y-3">
        {items.map((item, index) => (
          <div key={index} className="border-l-2 border-primary-200 pl-3 py-1">
            <a
              href={item.link}
              target="_blank"
              rel="noopener noreferrer"
              className="block group"
            >
              <h4 className="text-sm font-medium text-gray-900 group-hover:text-primary-600 transition-colors line-clamp-2 mb-1">
                {item.title}
              </h4>
              {item.description && (
                <p className="text-xs text-gray-600 line-clamp-2 mb-2">
                  {item.description}
                </p>
              )}
              <div className="flex items-center gap-2 text-xs text-gray-500 flex-wrap">
                {item.category && (
                  <span className="bg-primary-100 text-primary-700 px-2 py-0.5 rounded font-medium">
                    {item.category}
                  </span>
                )}
                {item.author && (
                  <span className="text-gray-500">
                    {item.author}
                  </span>
                )}
                {item.pubDate && (
                  <span>
                    {new Date(item.pubDate).toLocaleDateString('en-US', {
                      month: 'short',
                      day: 'numeric',
                      year: 'numeric',
                    })}
                  </span>
                )}
                <ExternalLink className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity ml-auto" />
              </div>
            </a>
          </div>
        ))}
      </div>
      <div className="mt-3 pt-3 border-t border-gray-200">
        <Link
          href="/reading"
          className="text-xs text-primary-600 hover:text-primary-800 flex items-center gap-1"
        >
          View all papers →
        </Link>
      </div>
    </div>
  )
}

