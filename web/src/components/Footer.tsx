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
                <a href="/techniques" className="hover:text-white transition-colors">
                  All Techniques
                </a>
              </li>
              <li>
                <a href="/multimodal" className="hover:text-white transition-colors">
                  Multimodal Combinations
                </a>
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
        <div className="mt-8 border-t border-gray-800 pt-8 text-center text-sm">
          <p>&copy; 2024 HyperImage. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}

