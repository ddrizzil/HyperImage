import Link from 'next/link'

export default function NotFound() {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="max-w-2xl mx-auto px-4 py-12 text-center">
        <h1 className="text-6xl font-bold text-gray-900 mb-4">404</h1>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">Page Not Found</h2>
        <p className="text-gray-600 mb-6">
          The page you're looking for doesn't exist yet. HyperImage is actively under construction—many placeholder 
          links point to future content.
        </p>
        
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8 text-left">
          <p className="font-semibold text-gray-900 mb-3">This might mean:</p>
          <ul className="list-disc ml-6 space-y-2 text-gray-700">
            <li>The technique you're looking for hasn't been documented yet (check back later)</li>
            <li>The link is broken (please report this: <a href="mailto:daniel@example.com" className="text-primary-600 hover:text-primary-800 underline">daniel@example.com</a>)</li>
            <li>You followed an outdated link (site structure evolves as it grows)</li>
          </ul>
        </div>
        
        <div className="flex gap-4 justify-center">
          <Link
            href="/"
            className="inline-flex items-center px-6 py-3 bg-primary-800 text-white rounded-lg hover:bg-primary-700 transition-colors"
          >
            Return to Homepage
          </Link>
          <Link
            href="/techniques"
            className="inline-flex items-center px-6 py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition-colors"
          >
            Browse Available Techniques
          </Link>
        </div>
      </div>
    </div>
  )
}

