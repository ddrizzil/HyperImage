import Link from 'next/link'
import { Brain, Layers, Target, BookOpen, Code, AlertCircle } from 'lucide-react'

export default function MLPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-3 bg-purple-100 rounded-lg">
              <Brain className="w-8 h-8 text-purple-600" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-gray-900">Machine Learning for Measurement Science</h1>
              <p className="text-lg text-gray-600 mt-1">
                Practical ML architectures for analyzing measurement data across domains
              </p>
            </div>
          </div>
        </div>

        {/* Table of Contents */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
          <h2 className="text-xl font-semibold mb-4 text-gray-900">Contents</h2>
          <ul className="space-y-2 text-gray-700">
            <li><a href="#introduction" className="text-primary-600 hover:text-primary-800">1. Introduction</a></li>
            <li><a href="#architecture-reference" className="text-primary-600 hover:text-primary-800">2. Architecture Quick Reference</a></li>
            <li><a href="#multi-task-learning" className="text-primary-600 hover:text-primary-800">3. Multi-Task Learning Deep Dive</a></li>
            <li><a href="#measurement-considerations" className="text-primary-600 hover:text-primary-800">4. Measurement-Specific Considerations</a></li>
            <li><a href="#key-papers" className="text-primary-600 hover:text-primary-800">5. Key Papers by Domain</a></li>
            <li><a href="#resources" className="text-primary-600 hover:text-primary-800">6. Resources & Next Steps</a></li>
          </ul>
        </div>

        {/* Section 1: Introduction */}
        <section id="introduction" className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">1. Introduction</h2>
          
          <p className="text-gray-700 mb-4">
            Machine learning has become essential for analyzing measurement data across scientific domains. 
            Whether identifying pigments from XRF spectra, detecting component degradation in RF systems, 
            or classifying materials from hyperspectral images, ML architectures provide powerful tools 
            for extracting insights from complex measurement datasets.
          </p>

          <p className="text-gray-700 mb-4">
            This section focuses on <strong>practical ML applications to measurement data</strong>, not 
            generic machine learning theory. We emphasize architectures and techniques that have proven 
            effective for measurement science applications, with particular attention to cross-domain 
            transfer—how techniques developed in one domain (e.g., RF signal processing) can solve 
            problems in another (e.g., heritage science).
          </p>

          <div className="bg-blue-50 border-l-4 border-blue-500 p-4 my-6">
            <p className="text-sm text-blue-800">
              <strong>Note:</strong> This is a practical reference focused on measurement applications. 
              For comprehensive ML fundamentals, see the <a href="#resources" className="underline">Resources section</a>.
            </p>
          </div>

          <h3 className="text-2xl font-semibold text-gray-900 mt-6 mb-3">Cross-Domain Approach</h3>
          <p className="text-gray-700 mb-4">
            A central theme of HyperImage is recognizing patterns that transfer across domains. 
            Multi-task learning architectures developed for RF component testing have direct 
            applications in heritage science pigment analysis. Spectral classification techniques 
            from remote sensing inform hyperspectral imaging of artworks. This cross-domain 
            thinking is not just theoretical—it's how real breakthroughs happen.
          </p>

          <p className="text-gray-700">
            The progression from <strong>Aygul et al.'s RF component identification</strong> → 
            <strong> Webb's degradation localization</strong> → <strong>potential heritage pigment 
            analysis</strong> demonstrates this pattern in action. Each application builds on 
            insights from the previous, adapted to new measurement contexts.
          </p>
        </section>

        {/* Section 2: Architecture Quick Reference */}
        <section id="architecture-reference" className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">2. Architecture Quick Reference</h2>
          
          <p className="text-gray-700 mb-6">
            This table provides a quick reference for selecting ML architectures based on your 
            measurement task and data type. Each entry includes recommended architectures, 
            when to use them, and example applications.
          </p>

          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200 border border-gray-300">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-4 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider border border-gray-300">
                    Task
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider border border-gray-300">
                    Data Type
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider border border-gray-300">
                    Recommended Architecture
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider border border-gray-300">
                    When to Use
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider border border-gray-300">
                    Example Applications
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                <tr>
                  <td className="px-4 py-3 text-sm text-gray-900 border border-gray-300">
                    Spectral Classification
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    1D spectra (XRF, Raman, FTIR)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    1D CNN or MLP
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Single-point measurements, spectral features
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Pigment ID from XRF/Raman spectra
                  </td>
                </tr>
                <tr className="bg-gray-50">
                  <td className="px-4 py-3 text-sm text-gray-900 border border-gray-300">
                    Image Classification
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    2D images (RGB, grayscale)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    2D CNN (ResNet, VGG)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Spatial features, texture, style
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Artwork analysis, brushstroke style, condition assessment
                  </td>
                </tr>
                <tr>
                  <td className="px-4 py-3 text-sm text-gray-900 border border-gray-300">
                    Hyperspectral Analysis
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    3D cubes (spatial × spectral)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    3D CNN
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Spatial-spectral features, material mapping
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Hyperspectral pigment mapping, mineral identification
                  </td>
                </tr>
                <tr className="bg-purple-50">
                  <td className="px-4 py-3 text-sm text-gray-900 border border-gray-300 font-semibold">
                    Multi-Task Learning
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Any (1D, 2D, 3D, multi-modal)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Shared features + dual/multi heads
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Related tasks, limited data, shared features
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    <strong>Component ID + degradation (Aygul et al.)</strong>, pigment ID + condition, tumor detection + segmentation
                  </td>
                </tr>
                <tr>
                  <td className="px-4 py-3 text-sm text-gray-900 border border-gray-300">
                    Anomaly Detection
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Any (1D, 2D, 3D)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Autoencoder (variational or standard)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Unbalanced data, rare events, unknown anomalies
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Forgery detection, fault detection, quality control
                  </td>
                </tr>
                <tr className="bg-gray-50">
                  <td className="px-4 py-3 text-sm text-gray-900 border border-gray-300">
                    Multi-Modal Fusion
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Multiple data types (XRF + hyperspectral + OCT)
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Multi-input CNN, late fusion, attention
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Complementary information, comprehensive analysis
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Combining XRF + hyperspectral + OCT for pigment analysis
                  </td>
                </tr>
                <tr>
                  <td className="px-4 py-3 text-sm text-gray-900 border border-gray-300">
                    Time Series
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Temporal sequences
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    RNN/LSTM, Transformer
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Temporal dependencies, monitoring
                  </td>
                  <td className="px-4 py-3 text-sm text-gray-700 border border-gray-300">
                    Acoustic emission monitoring, degradation tracking
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        {/* Section 3: Multi-Task Learning Deep Dive */}
        <section id="multi-task-learning" className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">3. Multi-Task Learning Deep Dive</h2>
          
          <p className="text-gray-700 mb-6">
            Multi-task learning is a powerful approach where a single model learns to perform 
            multiple related tasks simultaneously. This section provides a detailed exploration 
            of multi-task architectures, with emphasis on applications in measurement science.
          </p>

          <h3 className="text-2xl font-semibold text-gray-900 mt-6 mb-3">What is Multi-Task Learning?</h3>
          <p className="text-gray-700 mb-4">
            In multi-task learning, a neural network shares feature extraction layers across 
            multiple tasks, then branches into task-specific output heads. The key insight: 
            features learned for one task often contain information useful for related tasks.
          </p>

          <div className="bg-gray-50 border border-gray-300 rounded-lg p-6 my-6">
            <h4 className="font-semibold text-gray-900 mb-3">Architecture Pattern:</h4>
            <pre className="text-sm text-gray-700 font-mono whitespace-pre-wrap">
{`Input Data → Shared Feature Extraction (CNN/MLP) → Branch into:
    ├─→ Task 1 Head (e.g., component identification)
    └─→ Task 2 Head (e.g., degradation detection)`}
            </pre>
          </div>

          <p className="text-gray-700 mb-4">
            <strong>Why it works:</strong> Shared representations act as a form of regularization, 
            preventing overfitting when training data is limited. The model must learn features 
            that are useful for both tasks, leading to more generalizable representations. This is 
            particularly valuable in measurement science, where labeled datasets are often small.
          </p>

          <h3 className="text-2xl font-semibold text-gray-900 mt-8 mb-4">Cross-Domain Examples</h3>

          {/* Example 1: Aygul et al. */}
          <div className="bg-purple-50 border-l-4 border-purple-500 p-6 my-6">
            <h4 className="text-xl font-semibold text-gray-900 mb-3">
              Example 1: RF Component Testing (Aygul et al.)
            </h4>
            <ul className="space-y-2 text-gray-700 mb-4">
              <li><strong>Input:</strong> RF spectral response measurements</li>
              <li><strong>Task 1:</strong> Component identification (capacitor, inductor, resistor, etc.)</li>
              <li><strong>Task 2:</strong> Degradation detection (healthy vs. degraded)</li>
              <li><strong>Architecture:</strong> 1D CNN with shared feature extraction → dual classification heads</li>
              <li><strong>Result:</strong> Better accuracy than separate single-task networks</li>
            </ul>
            <p className="text-sm text-gray-600 italic">
              <strong>Key Insight:</strong> The spectral features that identify which component 
              is present also contain information about its condition. By learning both tasks 
              together, the model discovers more robust feature representations.
            </p>
            <p className="text-sm text-gray-600 mt-2">
              <strong>Paper reference:</strong> Aygul et al. [Citation details to be added]
            </p>
          </div>

          {/* Example 2: Webb dissertation */}
          <div className="bg-blue-50 border-l-4 border-blue-500 p-6 my-6">
            <h4 className="text-xl font-semibold text-gray-900 mb-3">
              Example 2: RF Component Degradation Localization (Webb dissertation)
            </h4>
            <ul className="space-y-2 text-gray-700 mb-4">
              <li><strong>Input:</strong> Multi-dimensional RF measurements</li>
              <li><strong>Task 1:</strong> Detect degradation presence (binary classification)</li>
              <li><strong>Task 2:</strong> Localize which component is degraded (multi-class classification)</li>
              <li><strong>Task 3:</strong> (Optional) Classify degradation type</li>
              <li><strong>Architecture:</strong> Multi-task CNN with 2-3 output heads</li>
              <li><strong>Result:</strong> 99% accuracy on both detection and localization</li>
            </ul>
            <p className="text-sm text-gray-700 mb-4">
              <strong>Inspiration:</strong> This work adapted Aygul et al.'s approach to include 
              localization as an additional task. The innovation was recognizing that degradation 
              detection and component localization are naturally related—if you can detect degradation, 
              you should also be able to identify where it occurs.
            </p>
            <p className="text-sm text-gray-700">
              <strong>Innovation:</strong> Extended multi-task learning from simple classification 
              to include spatial localization, demonstrating how the approach scales to more complex 
              problem formulations.
            </p>
          </div>

          {/* The Story */}
          <div className="bg-yellow-50 border-l-4 border-yellow-500 p-6 my-6">
            <p className="text-gray-700 italic">
              "The inspiration for applying multi-task learning to component degradation came from 
              Aygul et al.'s work on RF component identification. Their insight—that the features 
              learned for identifying which component is present are also relevant for assessing 
              its condition—proved highly transferable. By adapting their architecture to include 
              localization as an additional task, the approach achieved 99% accuracy on both 
              detection and localization, outperforming separate single-task models. This same 
              pattern could apply to heritage science: the spectral features that identify a 
              pigment likely also contain information about its degradation state."
            </p>
          </div>

          {/* Example 3: Potential Heritage Application */}
          <div className="bg-green-50 border-l-4 border-green-500 p-6 my-6">
            <h4 className="text-xl font-semibold text-gray-900 mb-3">
              Example 3: Potential Heritage Application
            </h4>
            <ul className="space-y-2 text-gray-700 mb-4">
              <li><strong>Input:</strong> Hyperspectral cube of painting (spatial × spectral dimensions)</li>
              <li><strong>Task 1:</strong> Identify pigment type (azurite, ultramarine, smalt, etc.)</li>
              <li><strong>Task 2:</strong> Detect pigment degradation or alteration</li>
              <li><strong>Hypothesis:</strong> Spectral features for pigment ID also contain degradation signatures</li>
              <li><strong>Architecture:</strong> 3D CNN (spatial-spectral features) → dual classification heads</li>
              <li><strong>Status:</strong> Potential application (not yet implemented, but architecture proven in RF domain)</li>
            </ul>
            <p className="text-sm text-gray-700">
              This represents a direct transfer of the multi-task learning pattern from RF component 
              analysis to heritage science. The underlying principle—that identification and condition 
              assessment share feature representations—should hold across domains.
            </p>
          </div>

          {/* Example 4: Medical Imaging */}
          <div className="bg-indigo-50 border-l-4 border-indigo-500 p-6 my-6">
            <h4 className="text-xl font-semibold text-gray-900 mb-3">
              Example 4: Medical Imaging (Established Application)
            </h4>
            <ul className="space-y-2 text-gray-700 mb-4">
              <li><strong>Input:</strong> CT or MRI scan (3D medical image)</li>
              <li><strong>Task 1:</strong> Tumor detection (binary classification)</li>
              <li><strong>Task 2:</strong> Tumor segmentation (pixel-level localization)</li>
              <li><strong>Task 3:</strong> Malignancy classification</li>
              <li><strong>Architecture:</strong> U-Net or similar with multiple output heads</li>
              <li><strong>Status:</strong> State-of-art, widely used in clinical practice</li>
            </ul>
            <p className="text-sm text-gray-700">
              Medical imaging demonstrates that multi-task learning is well-established in some 
              domains. The challenge is recognizing when these patterns can transfer to measurement 
              science applications.
            </p>
          </div>

          <h3 className="text-2xl font-semibold text-gray-900 mt-8 mb-4">When to Use Multi-Task Learning</h3>
          <ul className="list-disc list-inside space-y-2 text-gray-700 mb-6">
            <li><strong>Tasks are related:</strong> They share underlying features or information</li>
            <li><strong>Limited training data:</strong> Shared representations improve generalization</li>
            <li><strong>Real-time requirements:</strong> One forward pass produces multiple outputs</li>
            <li><strong>Tasks benefit from mutual information:</strong> Learning one task helps the other</li>
          </ul>

          <h3 className="text-2xl font-semibold text-gray-900 mt-8 mb-4">Implementation Considerations</h3>
          <div className="space-y-4 text-gray-700">
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Loss Function Balancing</h4>
              <p>
                Multi-task learning requires balancing losses from different tasks. Common approaches:
              </p>
              <ul className="list-disc list-inside ml-4 mt-2 space-y-1">
                <li>Weighted sum: <code className="bg-gray-100 px-1 rounded">L_total = w1*L1 + w2*L2</code></li>
                <li>Dynamic weighting: Adjust weights during training</li>
                <li>Uncertainty weighting: Learn task-specific uncertainty</li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Monitor Individual Task Performance</h4>
              <p>
                Track metrics for each task separately. One task improving doesn't guarantee the 
                other is also improving. May need to adjust architecture or loss weights.
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Architecture Decisions</h4>
              <p>
                How much to share vs. task-specific layers? Start with more sharing, add 
                task-specific layers if needed. For heritage science with small datasets, 
                more sharing (regularization) is often beneficial.
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Heritage-Specific Considerations</h4>
              <p>
                Small datasets favor multi-task learning due to regularization effect. However, 
                need to ensure tasks are truly related—forcing unrelated tasks together can hurt performance.
              </p>
            </div>
          </div>
        </section>

        {/* Section 4: Measurement-Specific Considerations */}
        <section id="measurement-considerations" className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">4. Measurement-Specific Considerations</h2>

          <div className="space-y-6">
            <div>
              <h3 className="text-2xl font-semibold text-gray-900 mb-3">Small Dataset Challenge</h3>
              <p className="text-gray-700 mb-3">
                <strong>Problem:</strong> Heritage science often has &lt;100 labeled samples per class. 
                Standard deep learning approaches require thousands of examples.
              </p>
              <p className="text-gray-700 mb-3"><strong>Solutions:</strong></p>
              <ul className="list-disc list-inside ml-4 space-y-1 text-gray-700">
                <li><strong>Transfer learning:</strong> Pre-train on large datasets (ImageNet, spectral libraries), fine-tune on heritage data</li>
                <li><strong>Data augmentation:</strong> Rotation, flipping, noise injection, spectral shifting</li>
                <li><strong>Physics-guided architectures:</strong> Incorporate domain knowledge (e.g., known spectral peaks)</li>
                <li><strong>Multi-task learning:</strong> Shared representations act as regularization (see Section 3)</li>
              </ul>
            </div>

            <div>
              <h3 className="text-2xl font-semibold text-gray-900 mb-3">Interpretability Requirements</h3>
              <p className="text-gray-700 mb-3">
                <strong>Problem:</strong> Conservators and analysts need to understand WHY the model 
                made a decision. Black-box predictions are insufficient for scientific validation.
              </p>
              <p className="text-gray-700 mb-3"><strong>Solutions:</strong></p>
              <ul className="list-disc list-inside ml-4 space-y-1 text-gray-700">
                <li><strong>Attention maps:</strong> Visualize which regions/features the model focuses on</li>
                <li><strong>Gradient visualization (GradCAM):</strong> Highlight important input regions</li>
                <li><strong>Physics-guided ML:</strong> Constrain models to respect known physical relationships</li>
                <li><strong>Example:</strong> Attention map showing model focused on Cu K-alpha peak in XRF spectrum for copper pigment identification</li>
              </ul>
            </div>

            <div>
              <h3 className="text-2xl font-semibold text-gray-900 mb-3">Calibration Transfer</h3>
              <p className="text-gray-700 mb-3">
                <strong>Problem:</strong> Model trained on Instrument A, deployed on Instrument B. 
                Spectral shifts, different resolutions, varying noise characteristics.
              </p>
              <p className="text-gray-700 mb-3"><strong>Solutions:</strong></p>
              <ul className="list-disc list-inside ml-4 space-y-1 text-gray-700">
                <li><strong>Domain adaptation:</strong> Fine-tune on target instrument data</li>
                <li><strong>Normalization:</strong> Standardize inputs (SNV, min-max, z-score)</li>
                <li><strong>Ensemble models:</strong> Combine predictions from multiple models trained on different instruments</li>
                <li><strong>Robust features:</strong> Use features less sensitive to instrument differences</li>
              </ul>
            </div>

            <div>
              <h3 className="text-2xl font-semibold text-gray-900 mb-3">Physics Integration</h3>
              <p className="text-gray-700 mb-3">
                <strong>Advantage:</strong> Unlike many ML applications, we know the underlying physics. 
                We can incorporate this knowledge into models.
              </p>
              <p className="text-gray-700 mb-3"><strong>Approaches:</strong></p>
              <ul className="list-disc list-inside ml-4 space-y-1 text-gray-700">
                <li><strong>Physics-guided loss functions:</strong> Penalize predictions that violate physical constraints</li>
                <li><strong>Hybrid models:</strong> Neural network + physics simulator (e.g., radiative transfer model)</li>
                <li><strong>Example:</strong> Spectral unmixing with non-negativity constraints (concentrations must be ≥ 0)</li>
                <li><strong>Constrained architectures:</strong> Build physical relationships into network structure</li>
              </ul>
            </div>
          </div>
        </section>

        {/* Section 5: Key Papers by Domain */}
        <section id="key-papers" className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">5. Key Papers by Domain</h2>

          <div className="space-y-6">
            <div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Heritage Science</h3>
              <ul className="list-disc list-inside space-y-2 text-gray-700">
                <li>[Paper 1]: CNN for XRF pigment classification - [Citation to be added]</li>
                <li>[Paper 2]: Hyperspectral + ML for pigment mapping - [Citation to be added]</li>
                <li>[Paper 3]: Autoencoder for forgery detection - [Citation to be added]</li>
                <li>Additional papers to be added as references are compiled</li>
              </ul>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">RF & Remote Sensing</h3>
              <ul className="list-disc list-inside space-y-2 text-gray-700">
                <li>
                  <strong>Aygul et al.:</strong> Multi-task learning for RF component identification and degradation 
                  [Citation details to be added]
                </li>
                <li>
                  <strong>Webb dissertation:</strong> Multi-task CNN for component degradation localization 
                  [Your work - citation to be added]
                </li>
                <li>[Paper on satellite hyperspectral classification] - [Citation to be added]</li>
                <li>[Paper on SAR image analysis] - [Citation to be added]</li>
              </ul>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Medical Imaging</h3>
              <ul className="list-disc list-inside space-y-2 text-gray-700">
                <li>Multi-task learning for tumor detection + segmentation - [Citation to be added]</li>
                <li>Transfer learning for limited medical datasets - [Citation to be added]</li>
                <li>Additional medical imaging papers to be added</li>
              </ul>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Cross-Domain</h3>
              <ul className="list-disc list-inside space-y-2 text-gray-700">
                <li>Papers demonstrating technique transfer between domains - [Citations to be added]</li>
                <li>Multi-task learning across measurement domains - [Citations to be added]</li>
              </ul>
            </div>
          </div>

          <div className="bg-yellow-50 border-l-4 border-yellow-500 p-4 mt-6">
            <p className="text-sm text-yellow-800">
              <strong>Note:</strong> This reference list is being expanded. Citations will be added 
              as papers are reviewed and incorporated into the guide.
            </p>
          </div>
        </section>

        {/* Section 6: Resources & Next Steps */}
        <section id="resources" className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">6. Resources & Next Steps</h2>

          <div className="space-y-6">
            <div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">For Learning ML Fundamentals</h3>
              <ul className="list-disc list-inside space-y-2 text-gray-700">
                <li>
                  <strong>Fast.ai:</strong> Practical deep learning course with focus on real applications
                  <br />
                  <a href="https://www.fast.ai" target="_blank" rel="noopener noreferrer" className="text-primary-600 hover:text-primary-800 text-sm">
                    https://www.fast.ai
                  </a>
                </li>
                <li>
                  <strong>Deep Learning Book (Goodfellow et al.):</strong> Comprehensive theoretical foundation
                </li>
                <li>
                  <strong>PyTorch/TensorFlow tutorials:</strong> Framework-specific implementation guides
                </li>
              </ul>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">For Measurement-Specific Applications</h3>
              <ul className="list-disc list-inside space-y-2 text-gray-700">
                <li>Papers referenced throughout this guide (see Section 5)</li>
                <li>
                  <strong>Spectral Python (SPy):</strong> Library for hyperspectral image processing
                </li>
                <li>
                  <strong>Scikit-learn:</strong> Classical ML baselines and preprocessing tools
                </li>
                <li>
                  <strong>Related HyperImage sections:</strong>
                  <ul className="list-disc list-inside ml-6 mt-2 space-y-1">
                    <li><Link href="/multimodal" className="text-primary-600 hover:text-primary-800">Multimodal Techniques</Link> - ML for data fusion</li>
                    <li><Link href="/techniques" className="text-primary-600 hover:text-primary-800">Imaging Techniques</Link> - Techniques that generate ML-ready data</li>
                  </ul>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Coming Soon</h3>
              <div className="bg-gray-50 border border-gray-300 rounded-lg p-4">
                <ul className="list-disc list-inside space-y-2 text-gray-700">
                  <li>Code examples for common tasks (spectral classification, multi-task learning)</li>
                  <li>More detailed implementation guides</li>
                  <li>Expanded cross-domain examples</li>
                  <li>Case studies with real data</li>
                  <li>Architecture diagrams and visualizations</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="bg-blue-50 border-l-4 border-blue-500 p-4 mt-6">
            <p className="text-sm text-blue-800">
              <strong>Version Note:</strong> This is v0.1 of the Machine Learning section. Content 
              will be expanded with more architectures, detailed examples, and code implementations 
              over time. The multi-task learning section represents the current focus and unique 
              contribution to measurement science ML applications.
            </p>
          </div>
        </section>

        {/* Footer Navigation */}
        <div className="mt-8 pt-8 border-t border-gray-200">
          <div className="flex flex-wrap gap-4 justify-center">
            <Link
              href="/multimodal"
              className="text-primary-600 hover:text-primary-800 font-medium"
            >
              ← Multimodal Techniques
            </Link>
            <span className="text-gray-400">|</span>
            <Link
              href="/techniques"
              className="text-primary-600 hover:text-primary-800 font-medium"
            >
              Imaging Techniques →
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}

