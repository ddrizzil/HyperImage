import Link from 'next/link'

export function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-300">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
          <div>
            <h3 className="text-lg font-semibold text-white mb-4">HyperImage</h3>
            <p className="text-sm">
              Comprehensive reference documentation for scientific analysis techniques
              in conservation science and artwork analysis.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-white mb-4">Resources</h3>
            <ul className="space-y-2 text-sm">
              <li>
                <Link href="/techniques" className="hover:text-white transition-colors">
                  All Techniques
                </Link>
              </li>
              <li>
                <Link href="/multimodal" className="hover:text-white transition-colors">
                  Multimodal Combinations
                </Link>
              </li>
              <li>
                <Link href="/ml" className="hover:text-white transition-colors">
                  Machine Learning
                </Link>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-white mb-4">About</h3>
            <p className="text-sm">
              Built for conservators, researchers, and scientists working with cultural
              heritage materials.
            </p>
          </div>
        </div>
        
        <div className="disclaimer mt-8 border-t border-gray-800 pt-8">
          <p className="text-sm text-gray-400 mb-4">
            <strong>Disclaimer:</strong> HyperImage is a personal learning tool shared publicly. 
            Content represents the author's current understanding and should not be considered 
            authoritative. Verify information against primary sources for critical applications.{' '}
            <Link href="/about#accuracy" className="text-primary-400 hover:text-primary-300 underline">
              Learn more about this resource →
            </Link>
          </p>
        </div>
        
        <div className="mt-6 border-t border-gray-800 pt-6 text-center text-sm text-gray-400">
          <p className="mb-2">
            Built by <Link href="/about" className="text-primary-400 hover:text-primary-300 underline">Daniel Webb</Link> | 
            Content generated with AI assistance, reviewed and refined | 
            Last updated: {new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })} | 
            <a href="mailto:daniel@intrawebb.com" className="text-primary-400 hover:text-primary-300 underline ml-1">
              Feedback welcome
            </a>
          </p>
          <p className="text-xs text-gray-500">
            <Link href="/" className="hover:text-gray-400">Home</Link> | 
            <Link href="/about" className="hover:text-gray-400 ml-1">About</Link> | 
            <a href="https://github.com/ddrizzil/HyperImage" target="_blank" rel="noopener noreferrer" className="hover:text-gray-400 ml-1">
              GitHub
            </a>
          </p>
        </div>
      </div>
    </footer>
  )
}

