import Link from 'next/link'

export default function AboutPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-6">About HyperImage</h1>
          
          <div className="prose prose-lg max-w-none">
            <p className="text-gray-700 mb-4">
              HyperImage is a comprehensive technical reference for scientific analysis techniques 
              used in cultural heritage conservation, artwork analysis, and related measurement science 
              domains. This resource systematically documents imaging techniques, RF methods, optical 
              principles, and multimodal combinations across these fields.
            </p>

            <p className="text-gray-700 mb-4">
              The project aims to bridge knowledge gaps between domains—connecting heritage science 
              with RF/imaging techniques, signal processing with material characterization, and 
              established methods with emerging applications.
            </p>

            <h2 id="accuracy" className="text-2xl font-bold mt-8 mb-4 text-primary-800">
              A Note on Accuracy and Authority
            </h2>

            <p className="text-gray-700 mb-4">
              <strong>This is a learning tool, not an authoritative reference.</strong> While I strive 
              for technical accuracy and verify information against primary literature, this site 
              represents my current understanding as I learn. Content is generated with AI assistance 
              (Claude, Anthropic), then reviewed and refined, but may contain errors or oversimplifications.
            </p>

            <p className="text-gray-700 mb-4">
              <strong>You're welcome to use this resource if you find it helpful.</strong> Many sections 
              provide comprehensive technical overviews that may be useful for students, researchers, 
              or professionals. However, for critical applications (research publications, conservation 
              decisions, engineering specifications), please verify information against:
            </p>

            <ul className="list-disc ml-6 mb-4 text-gray-700">
              <li>Primary scientific literature (papers, textbooks)</li>
              <li>Established technical standards (ASTM, ISO, etc.)</li>
              <li>Manufacturer specifications and documentation</li>
              <li>Domain experts in your specific application</li>
            </ul>

            <h2 className="text-2xl font-bold mt-8 mb-4 text-primary-800">
              How This Is Built
            </h2>

            <p className="text-gray-700 mb-4">
              Content development process:
            </p>

            <ol className="list-decimal ml-6 mb-4 text-gray-700 space-y-2">
              <li>
                <strong>AI-assisted research:</strong> I use Claude (Anthropic) to generate initial 
                technical writeups based on scientific literature
              </li>
              <li>
                <strong>Verification:</strong> I review generated content against primary sources, 
                correct errors, adjust emphasis
              </li>
              <li>
                <strong>Integration:</strong> I add domain-specific insights from my RF/signal 
                processing background
              </li>
              <li>
                <strong>Cross-domain connections:</strong> I identify how techniques transfer across 
                fields (my unique contribution)
              </li>
            </ol>

            <p className="text-gray-700 mb-4">
              This approach allows rapid documentation while maintaining technical depth, but means 
              some content may lack the nuance of resources written entirely by domain experts.
            </p>

            <h2 className="text-2xl font-bold mt-8 mb-4 text-primary-800">
              Feedback Welcome
            </h2>

            <p className="text-gray-700 mb-4">
              If you notice errors, have suggestions for techniques to add, or want to discuss 
              cross-domain applications, I welcome your feedback: <a href="mailto:daniel@intrawebb.com" className="text-primary-600 hover:text-primary-800 underline">daniel@intrawebb.com</a>. 
              This is a learning project—corrections and insights help me improve both the resource 
              and my own understanding.
            </p>

            <div className="mt-8 pt-6 border-t border-gray-200">
              <p className="text-sm text-gray-500">
                Last updated: {new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

