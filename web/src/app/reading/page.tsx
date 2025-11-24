'use client'

import { useEffect, useState } from 'react'
import { BookOpen, ExternalLink, Calendar, User, Tag } from 'lucide-react'
import Link from 'next/link'

interface RSSItem {
  title: string
  link: string
  description: string
  pubDate: string
  author?: string
  category?: string
}

export default function ReadingPage() {
  const [items, setItems] = useState<RSSItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [filter, setFilter] = useState<string>('all')

  useEffect(() => {
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
        
        const parseError = xmlDoc.querySelector('parsererror')
        if (parseError) {
          throw new Error('Failed to parse RSS feed')
        }
        
        const itemElements = xmlDoc.querySelectorAll('item')
        const parsedItems: RSSItem[] = []
        
        itemElements.forEach((item) => {
          const title = item.querySelector('title')?.textContent || 'Untitled'
          const link = item.querySelector('link')?.textContent || ''
          const description = item.querySelector('description')?.textContent || ''
          const pubDate = item.querySelector('pubDate')?.textContent || ''
          const author = item.querySelector('author')?.textContent || ''
          const category = item.querySelector('category')?.textContent || ''
          
          const descriptionParts = description.split(' | ')
          const summary = descriptionParts[0] || description
          
          parsedItems.push({
            title,
            link,
            description: summary,
            pubDate,
            author,
            category,
          })
        })
        
        // Sort by date, newest first
        parsedItems.sort((a, b) => {
          const dateA = new Date(a.pubDate).getTime()
          const dateB = new Date(b.pubDate).getTime()
          return dateB - dateA
        })
        
        setItems(parsedItems)
        setLoading(false)
      } catch (err) {
        console.error('Error fetching RSS feed:', err)
        setError('Unable to load papers')
        setLoading(false)
      }
    }
    
    fetchRSS()
  }, [])

  const categories = Array.from(new Set(items.map(item => item.category).filter((cat): cat is string => Boolean(cat))))
  const filteredItems = filter === 'all' 
    ? items 
    : items.filter(item => item.category === filter)

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50">
        <div className="mx-auto max-w-4xl px-4 py-16 sm:px-6 lg:px-8">
          <div className="bg-white rounded-lg shadow-md border border-gray-200 p-8 text-center">
            <div className="animate-pulse">
              <BookOpen className="w-12 h-12 text-primary-600 mx-auto mb-4" />
              <p className="text-gray-600">Loading papers...</p>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50">
        <div className="mx-auto max-w-4xl px-4 py-16 sm:px-6 lg:px-8">
          <div className="bg-white rounded-lg shadow-md border border-red-200 p-8 text-center">
            <p className="text-red-600">{error}</p>
            <Link 
              href="/"
              className="mt-4 inline-block text-primary-600 hover:text-primary-800"
            >
              Return to home
            </Link>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-4xl px-4 py-16 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-md border border-gray-200 p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <BookOpen className="w-8 h-8 text-primary-600" />
            <h1 className="text-3xl font-bold text-gray-900">What I'm Reading</h1>
          </div>
          
          {/* Reading Notice */}
          <div className="reading-notice mb-4 bg-gray-50 p-4 rounded-lg border border-gray-200">
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

          {/* Filter */}
          {categories.length > 0 && (
            <div className="flex flex-wrap gap-2">
              <button
                onClick={() => setFilter('all')}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                  filter === 'all'
                    ? 'bg-primary-600 text-white'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                All ({items.length})
              </button>
              {categories.map((category) => {
                const count = items.filter(item => item.category === category).length
                return (
                  <button
                    key={category}
                    onClick={() => setFilter(category)}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                      filter === category
                        ? 'bg-primary-600 text-white'
                        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                  >
                    {category} ({count})
                  </button>
                )
              })}
            </div>
          )}
        </div>

        {/* Papers List */}
        <div className="space-y-4">
          {filteredItems.length === 0 ? (
            <div className="bg-white rounded-lg shadow-md border border-gray-200 p-8 text-center">
              <p className="text-gray-600">No papers found.</p>
            </div>
          ) : (
            filteredItems.map((item, index) => (
              <div 
                key={index} 
                className="bg-white rounded-lg shadow-md border border-gray-200 p-6 hover:shadow-lg transition-shadow"
              >
                <a
                  href={item.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block group"
                >
                  <h2 className="text-xl font-semibold text-gray-900 group-hover:text-primary-600 transition-colors mb-3">
                    {item.title}
                  </h2>
                  
                  {item.description && (
                    <p className="text-gray-600 mb-4 line-clamp-3">
                      {item.description}
                    </p>
                  )}
                  
                  <div className="flex flex-wrap items-center gap-4 text-sm text-gray-500">
                    {item.category && (
                      <span className="flex items-center gap-1">
                        <Tag className="w-4 h-4" />
                        <span className="bg-primary-100 text-primary-700 px-2 py-1 rounded font-medium">
                          {item.category}
                        </span>
                      </span>
                    )}
                    
                    {item.author && (
                      <span className="flex items-center gap-1">
                        <User className="w-4 h-4" />
                        <span>{item.author}</span>
                      </span>
                    )}
                    
                    {item.pubDate && (
                      <span className="flex items-center gap-1">
                        <Calendar className="w-4 h-4" />
                        <span>
                          {new Date(item.pubDate).toLocaleDateString('en-US', {
                            month: 'long',
                            day: 'numeric',
                            year: 'numeric',
                          })}
                        </span>
                      </span>
                    )}
                    
                    <span className="ml-auto flex items-center gap-1 text-primary-600 group-hover:text-primary-800">
                      Read paper
                      <ExternalLink className="w-4 h-4" />
                    </span>
                  </div>
                </a>
              </div>
            ))
          )}
        </div>

        {/* Back to Home */}
        <div className="mt-8 text-center">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-primary-600 hover:text-primary-800 font-medium"
          >
            ← Back to home
          </Link>
        </div>
      </div>
    </div>
  )
}

