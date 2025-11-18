import { ReactNode } from 'react'

/**
 * Simple markdown-like content renderer
 * Handles basic formatting like **bold**, *italic*, and line breaks
 */
export function MarkdownContent({ content }: { content: string | undefined | null }) {
  // Handle non-string content gracefully
  if (!content) {
    return null
  }

  // Convert to string if it's not already
  const contentString = typeof content === 'string' ? content : String(content)

  // If empty string, return null
  if (!contentString.trim()) {
    return null
  }

  const parts: ReactNode[] = []
  let currentIndex = 0
  let key = 0

  // Simple regex-based parsing for **bold** and *italic*
  const boldRegex = /\*\*(.+?)\*\*/g
  const italicRegex = /\*(.+?)\*/g
  const codeRegex = /`(.+?)`/g

  // Split by double newlines for paragraphs
  const paragraphs = contentString.split('\n\n')

  return (
    <div className="space-y-4">
      {paragraphs.map((paragraph, pIdx) => {
        if (!paragraph.trim()) return null

        const elements: ReactNode[] = []
        let lastIndex = 0

        // Find all matches
        const matches: Array<{
          type: 'bold' | 'italic' | 'code'
          start: number
          end: number
          content: string
        }> = []

        let match
        while ((match = boldRegex.exec(paragraph)) !== null) {
          matches.push({
            type: 'bold',
            start: match.index,
            end: match.index + match[0].length,
            content: match[1],
          })
        }
        boldRegex.lastIndex = 0

        while ((match = italicRegex.exec(paragraph)) !== null) {
          // Don't match if it's part of a bold match
          const isInBold = matches.some(
            (m) => m.type === 'bold' && match!.index >= m.start && match!.index < m.end
          )
          if (!isInBold) {
            matches.push({
              type: 'italic',
              start: match.index,
              end: match.index + match[0].length,
              content: match[1],
            })
          }
        }
        italicRegex.lastIndex = 0

        while ((match = codeRegex.exec(paragraph)) !== null) {
          matches.push({
            type: 'code',
            start: match.index,
            end: match.index + match[0].length,
            content: match[1],
          })
        }
        codeRegex.lastIndex = 0

        // Sort matches by position
        matches.sort((a, b) => a.start - b.start)

        // Build elements
        matches.forEach((m) => {
          // Add text before match
          if (m.start > lastIndex) {
            elements.push(paragraph.substring(lastIndex, m.start))
          }

          // Add formatted content
          if (m.type === 'bold') {
            elements.push(<strong key={`${pIdx}-${m.start}`}>{m.content}</strong>)
          } else if (m.type === 'italic') {
            elements.push(<em key={`${pIdx}-${m.start}`}>{m.content}</em>)
          } else if (m.type === 'code') {
            elements.push(
              <code key={`${pIdx}-${m.start}`} className="bg-gray-100 px-1.5 py-0.5 rounded">
                {m.content}
              </code>
            )
          }

          lastIndex = m.end
        })

        // Add remaining text
        if (lastIndex < paragraph.length) {
          elements.push(paragraph.substring(lastIndex))
        }

        // Handle line breaks
        const processedElements: ReactNode[] = []
        elements.forEach((el, idx) => {
          if (typeof el === 'string' && el.includes('\n')) {
            const lines = el.split('\n')
            lines.forEach((line, lineIdx) => {
              if (lineIdx > 0) processedElements.push(<br key={`br-${pIdx}-${idx}-${lineIdx}`} />)
              if (line) processedElements.push(line)
            })
          } else {
            processedElements.push(el)
          }
        })

        return <p key={pIdx}>{processedElements}</p>
      })}
    </div>
  )
}

