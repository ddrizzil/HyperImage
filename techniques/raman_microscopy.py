"""
Raman Microscopy technique data definition.
"""

# Data for Raman microscopy reference page
raman_data = {
    "one_line_summary": "Vibrational spectroscopy technique for molecular identification and characterization of materials in artworks, providing non-destructive chemical fingerprinting.",
    
    "abstract": "Raman microscopy combines Raman spectroscopy with optical microscopy to provide spatially resolved molecular information from samples. The technique relies on inelastic scattering of monochromatic light, typically from a laser, to identify chemical bonds and molecular structures. In conservation science, it is widely used for pigment identification, degradation product analysis, and authentication of artworks without requiring sample removal.",
    
    "physics_principle": """Raman spectroscopy is based on the inelastic scattering of photons by molecular vibrations. When monochromatic laser light (typically 532 nm, 785 nm, or 1064 nm) interacts with a sample, most photons are elastically scattered (Rayleigh scattering) at the same frequency. A small fraction (~1 in 10^7 photons) undergoes inelastic scattering, shifting in frequency by an amount equal to the vibrational energy of the molecule.

The Raman shift (Δν) is measured in wavenumbers (cm⁻¹) and is calculated as:
```
Δν = (1/λ₀ - 1/λᵣ) × 10⁷
```
where λ₀ is the excitation wavelength and λᵣ is the scattered wavelength.

The technique provides a molecular fingerprint through characteristic vibrational modes:
- Stretching vibrations (1000-4000 cm⁻¹): C-H, O-H, N-H bonds
- Bending vibrations (400-1500 cm⁻¹): molecular framework
- Lattice modes (<400 cm⁻¹): crystal structures

Raman microscopy adds spatial resolution by coupling the spectrometer to an optical microscope, enabling mapping of chemical distributions with micron-scale resolution.""",
    
    "instruments_components": """**Lab-based systems:**
- Confocal Raman microscope (e.g., Horiba LabRAM, Renishaw inVia)
- Laser sources: 532 nm (green, high sensitivity), 785 nm (NIR, reduced fluorescence), 1064 nm (FT-Raman, minimal fluorescence)
- Spectrometer: dispersive (CCD detector) or FT-based (interferometer)
- Objective lenses: 10×, 50×, 100× (NA 0.9-0.95)
- Motorized stage for mapping
- Temperature-controlled sample stage (optional)

**Portable/handheld systems:**
- Battery-powered Raman spectrometer (e.g., B&W Tek, Ocean Optics)
- Fiber-optic probe with focusing optics
- Integrated laser (typically 785 nm)
- Compact CCD or CMOS detector
- Tablet/phone interface for data collection

**Key specifications:**
- Spectral range: 200-4000 cm⁻¹ (typical)
- Spectral resolution: 1-4 cm⁻¹
- Spatial resolution: ~1-2 μm (confocal), ~10-50 μm (portable)
- Laser power: 1-50 mW (surface), adjustable to prevent damage
- Integration time: 1-60 seconds per spectrum""",
    
    "resolution_detection": """**Spatial resolution:**
- Confocal systems: ~1-2 μm lateral, ~2-5 μm axial (depends on NA and wavelength)
- Portable systems: ~10-50 μm spot size
- Mapping step size: typically 1-10 μm for high-resolution maps

**Spectral resolution:**
- Dispersive systems: 1-4 cm⁻¹ (depends on grating and slit width)
- FT-Raman: 0.5-2 cm⁻¹
- Wavenumber accuracy: ±1 cm⁻¹ (calibrated)

**Temporal resolution:**
- Single spectrum: 1-60 seconds (depends on signal strength)
- Mapping speed: 10-1000 spectra/hour (depends on step size and integration time)

**Detection limits:**
- Concentration: ~0.1-1% for most compounds (depends on Raman cross-section)
- Absolute amount: ~1-10 pg for strong scatterers
- Penetration depth: ~1-100 μm (depends on material transparency and wavelength)

**Common measurement units:**
- Wavenumber (cm⁻¹) for spectral axis
- Intensity (counts or arbitrary units) for signal
- Spatial coordinates (μm or mm) for mapping""",
    
    "sample_requirements": """**Non-destructive analysis:**
- No sample preparation required for most solid samples
- Can analyze through glass coverslips or protective layers
- Minimal risk of photodamage with appropriate laser power settings
- Suitable for fragile or valuable objects

**Sample considerations:**
- Flat surfaces preferred for optimal focus
- Rough surfaces may require longer integration times
- Dark or highly absorbing materials may heat up (use lower power or NIR excitation)
- Fluorescent materials may require longer wavelength excitation (785 nm or 1064 nm)

**Micro-sampling (if needed):**
- Cross-sections: can analyze embedded samples in resin
- Powder samples: can be pressed into pellets or analyzed directly
- Liquid samples: require special cuvettes or capillary tubes

**Safety & ethical notes:**
- Laser safety: Class 3B or 4 lasers require appropriate eye protection
- Sample damage risk: monitor for discoloration or heating, especially with high laser power
- Use lowest power necessary to obtain adequate signal
- Document laser power and exposure time for reproducibility
- For artworks: obtain proper permissions and follow conservation guidelines""",
    
    "measurement_protocol": {
        "preparation": [
            "Clean sample surface if necessary (use appropriate solvents, avoid abrasives)",
            "Mount sample securely on microscope stage or in sample holder",
            "Ensure sample is level and in focus under white light illumination",
            "Select appropriate objective lens based on desired spatial resolution",
            "For portable systems, position probe at correct working distance (typically 5-10 mm)"
        ],
        "calibration": [
            "Perform wavenumber calibration using standard reference (e.g., silicon peak at 520.7 cm⁻¹, neon lamp, or polystyrene)",
            "Verify calibration accuracy: check known peaks are within ±1 cm⁻¹ of expected values",
            "Perform intensity calibration if quantitative analysis is required (use NIST-traceable standards)",
            "Record calibration date and reference used in metadata"
        ],
        "typical_settings": [
            "Laser wavelength: 532 nm (visible pigments), 785 nm (reduced fluorescence), or 1064 nm (FT-Raman)",
            "Laser power: Start at 10-25% of maximum, adjust based on signal and sample response",
            "Integration time: 1-10 seconds per spectrum (increase for weak signals)",
            "Number of accumulations: 1-10 scans (average to improve signal-to-noise)",
            "Spectral range: 200-4000 cm⁻¹ (adjust based on region of interest)",
            "Grating: 600-1800 lines/mm (higher for better resolution, lower for wider range)",
            "Slit width: 50-200 μm (narrower for better resolution, wider for more signal)"
        ],
        "data_collection": [
            "Focus on area of interest using white light or low-power laser",
            "Acquire reference spectrum from clean area or standard material",
            "Collect spectrum from sample area",
            "Verify signal quality: check for adequate intensity and absence of saturation",
            "If mapping: define grid area and step size, set total acquisition time",
            "Document measurement conditions: laser power, integration time, objective, date, operator",
            "Save raw spectra with metadata (instrument settings, sample info, coordinates)"
        ]
    },
    
    "data_outputs": """**File formats:**
- Raw spectra: `.spc` (GRAMS), `.txt` (ASCII), `.csv`, `.wdf` (Renishaw), `.wxd` (Horiba)
- Maps/hyperspectral data: `.hdf5`, `.mat` (MATLAB), `.hspy` (HyperSpy), `.ome.tiff`
- Metadata: JSON, XML, or embedded in file headers

**Data structure:**
- Single spectrum: 2D array (wavenumber, intensity)
- Map: 3D array (x, y, wavenumber) or 4D (x, y, z, wavenumber) for depth profiling
- Typical file size: 1-100 MB per map (depends on spatial and spectral resolution)

**Archiving for reproducibility:**
- Save raw data before any processing
- Include instrument settings and calibration data
- Document sample preparation and measurement conditions
- Use standardized naming: `SampleID_Date_Technique_Location.extension`
- Store metadata in machine-readable format (JSON/YAML)
- Follow FAIR data principles: Findable, Accessible, Interoperable, Reusable
- Recommended: Archive in institutional repository with DOI""",
    
    "data_analysis_pipeline": {
        "preprocessing": """**Remove cosmic rays:**
```python
import numpy as np
from scipy import signal
from scipy.ndimage import median_filter

# Method 1: Median filter
cleaned = median_filter(spectrum, size=3)

# Method 2: Detect and replace spikes
def remove_cosmic_rays(spectrum, threshold=5):
    median = np.median(spectrum)
    mad = np.median(np.abs(spectrum - median))
    spikes = np.abs(spectrum - median) > threshold * mad
    spectrum[spikes] = np.interp(np.where(spikes)[0], 
                                  np.where(~spikes)[0], 
                                  spectrum[~spikes])
    return spectrum
```

**Baseline correction:**
```python
from scipy import sparse
from scipy.sparse.linalg import spsolve

def baseline_als(y, lam=1e4, p=0.001, niter=10):
    '''Asymmetric Least Squares baseline correction'''
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z

corrected = spectrum - baseline_als(spectrum)
```

**Normalization:**
```python
# Min-max normalization
normalized = (spectrum - np.min(spectrum)) / (np.max(spectrum) - np.min(spectrum))

# Vector normalization
normalized = spectrum / np.linalg.norm(spectrum)

# Standard normal variate (SNV)
normalized = (spectrum - np.mean(spectrum)) / np.std(spectrum)
```""",
        
        "artifact_removal": """**Fluorescence background removal:**
```python
# Polynomial fitting
from numpy.polynomial import Polynomial

def remove_fluorescence(spectrum, wavenumber, degree=5):
    poly = Polynomial.fit(wavenumber, spectrum, degree)
    background = poly(wavenumber)
    corrected = spectrum - background
    return corrected, background

# Or use rolling ball/median filter
from scipy.ndimage import uniform_filter1d
background = uniform_filter1d(spectrum, size=100, mode='nearest')
corrected = spectrum - background
```

**Noise reduction:**
```python
# Savitzky-Golay smoothing
from scipy.signal import savgol_filter
smoothed = savgol_filter(spectrum, window_length=11, polyorder=3)

# Wavelet denoising
import pywt
coeffs = pywt.wavedec(spectrum, 'db4', level=4)
coeffs[1:] = [pywt.threshold(c, value=0.1, mode='soft') for c in coeffs[1:]]
denoised = pywt.waverec(coeffs, 'db4')
```""",
        
        "feature_extraction": """**Peak finding:**
```python
from scipy.signal import find_peaks

peaks, properties = find_peaks(intensity, 
                               height=threshold,
                               distance=10,  # minimum distance between peaks
                               prominence=0.1 * max(intensity))

# Get peak positions in wavenumbers
peak_wavenumbers = wavenumber[peaks]
peak_intensities = intensity[peaks]
```

**Peak fitting:**
```python
from scipy.optimize import curve_fit

def gaussian(x, amp, center, width):
    return amp * np.exp(-((x - center) / width)**2)

# Fit single peak
popt, pcov = curve_fit(gaussian, wavenumber, intensity, 
                       p0=[max(intensity), peak_center, 5])

# Multi-peak fitting with lmfit
from lmfit import Model
gmodel = Model(gaussian)
result = gmodel.fit(intensity, x=wavenumber, 
                    amp=max(intensity), center=peak_center, width=5)
```

**Spectral matching:**
```python
# Correlation coefficient
from scipy.stats import pearsonr
correlation, p_value = pearsonr(reference_spectrum, sample_spectrum)

# Euclidean distance
distance = np.linalg.norm(reference_spectrum - sample_spectrum)

# Spectral angle mapper (SAM)
def spectral_angle(s1, s2):
    return np.arccos(np.dot(s1, s2) / (np.linalg.norm(s1) * np.linalg.norm(s2)))
```""",
        
        "statistical_analysis_visualization": """**Principal Component Analysis (PCA):**
```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Reshape map data: (n_pixels, n_wavenumbers)
data_2d = map_data.reshape(-1, map_data.shape[-1])

# Apply PCA
pca = PCA(n_components=10)
pca_scores = pca.fit_transform(data_2d)

# Visualize loadings
plt.figure()
for i in range(3):
    plt.plot(wavenumber, pca.components_[i], label=f'PC{i+1}')
plt.xlabel('Wavenumber (cm⁻¹)')
plt.ylabel('Loading')
plt.legend()

# Visualize score maps
fig, axes = plt.subplots(1, 3)
for i, ax in enumerate(axes):
    score_map = pca_scores[:, i].reshape(map_data.shape[:2])
    im = ax.imshow(score_map, cmap='viridis')
    ax.set_title(f'PC{i+1} ({pca.explained_variance_ratio_[i]:.1%})')
    plt.colorbar(im, ax=ax)
```

**Cluster analysis:**
```python
from sklearn.cluster import KMeans

# K-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(data_2d)

# Visualize cluster map
cluster_map = labels.reshape(map_data.shape[:2])
plt.imshow(cluster_map, cmap='tab10')
plt.colorbar(label='Cluster')
```

**Visualization:**
```python
# Single spectrum
plt.plot(wavenumber, intensity)
plt.xlabel('Wavenumber (cm⁻¹)')
plt.ylabel('Intensity')
plt.title('Raman Spectrum')

# Map visualization
plt.imshow(intensity_map, cmap='hot', aspect='auto')
plt.colorbar(label='Intensity')
plt.xlabel('X (μm)')
plt.ylabel('Y (μm)')

# False-color composite
from matplotlib.colors import Normalize
rgb = np.stack([pc1_map, pc2_map, pc3_map], axis=-1)
rgb_norm = Normalize()(rgb)
plt.imshow(rgb_norm)
```"""
    },
    
    "artifacts_troubleshooting": """**Common artifacts:**

1. **Fluorescence background:**
   - *Cause:* Organic materials, binders, or impurities fluoresce under laser excitation
   - *Solution:* Use longer wavelength laser (785 nm or 1064 nm), increase integration time, or apply background subtraction algorithms

2. **Cosmic ray spikes:**
   - *Cause:* High-energy particles hitting the detector
   - *Solution:* Use median filter, collect multiple accumulations, or use spike removal algorithms

3. **Saturation:**
   - *Cause:* Laser power too high or integration time too long
   - *Solution:* Reduce laser power or integration time, check detector linearity

4. **Sample heating/photodamage:**
   - *Cause:* Excessive laser power, especially on dark or absorbing materials
   - *Solution:* Reduce laser power, use defocused beam, or move sample during measurement

5. **Poor signal-to-noise ratio:**
   - *Cause:* Low concentration, weak scatterer, or insufficient integration time
   - *Solution:* Increase integration time, use higher NA objective, increase laser power (if safe), or use surface-enhanced Raman (SERS)

6. **Wavenumber drift:**
   - *Cause:* Temperature changes, instrument instability
   - *Solution:* Regular calibration checks, temperature stabilization, use internal standard

7. **Spatial resolution degradation:**
   - *Cause:* Out of focus, wrong objective, or sample too thick
   - *Solution:* Check focus, use appropriate objective, use confocal pinhole, or prepare thinner sample

**Troubleshooting checklist:**
- [ ] Verify laser is properly aligned and focused
- [ ] Check wavenumber calibration (use silicon or polystyrene standard)
- [ ] Ensure sample is in focus and at correct working distance
- [ ] Verify detector is not saturated (check maximum counts)
- [ ] Check for fluorescence (try different excitation wavelength)
- [ ] Verify spectral range covers region of interest
- [ ] Check for sample movement or drift during measurement
- [ ] Ensure proper background subtraction
- [ ] Verify file saving and metadata recording""",
    
    "multimodal_pairings": """**Common technique combinations:**

1. **Raman + FTIR:**
   - *Rationale:* Complementary vibrational techniques; Raman detects symmetric vibrations, FTIR detects asymmetric vibrations
   - *Alignment:* Spatial registration using common features or fiducial markers
   - *Fusion:* Combine spectral libraries, use both for molecular identification, cross-validate findings

2. **Raman + XRF:**
   - *Rationale:* Raman provides molecular information, XRF provides elemental composition
   - *Alignment:* Same sample area, use XRF map to guide Raman point measurements
   - *Fusion:* Correlate elements (XRF) with compounds (Raman), identify pigments from both signals

3. **Raman + Optical Microscopy:**
   - *Rationale:* Visual context for spectral data
   - *Alignment:* Same field of view, use optical image to select measurement points
   - *Fusion:* Overlay Raman maps on optical images, correlate morphology with chemistry

4. **Raman + SEM-EDS:**
   - *Rationale:* High-resolution elemental (EDS) and molecular (Raman) information
   - *Alignment:* Use same sample coordinates, register using common features
   - *Fusion:* Combine elemental maps with molecular identification, identify phases

**Data fusion recipe:**
```python
# Example: Align and fuse Raman and XRF data
import numpy as np
from scipy.ndimage import affine_transform

# 1. Spatial alignment (if needed)
# Use feature-based registration or manual alignment
transformation_matrix = compute_alignment(raman_map, xrf_map)

# 2. Resample to common grid
xrf_aligned = affine_transform(xrf_map, transformation_matrix)

# 3. Weight signals based on confidence/relevance
raman_weight = 0.6  # Higher weight for molecular ID
xrf_weight = 0.4    # Lower weight for elemental confirmation

# 4. Fused analysis
# Option A: Concatenate features
fused_features = np.concatenate([raman_features, xrf_features], axis=-1)

# Option B: Weighted combination for visualization
fused_map = raman_weight * raman_intensity + xrf_weight * xrf_intensity

# 5. Joint classification/analysis
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(fused_features, labels)
```""",
    "strengths_limitations": {
        "strengths": [
            "Non-destructive analysis (with appropriate laser power settings)",
            "High spatial resolution (1-2 μm with confocal systems)",
            "Molecular identification through characteristic vibrational fingerprints",
            "Minimal sample preparation required",
            "Can analyze through glass or protective layers",
            "Portable systems available for in-situ measurements",
            "Suitable for a wide range of materials (pigments, binders, degradation products)",
            "Fast data acquisition (seconds per spectrum)",
            "Can be combined with microscopy for visual context",
            "Sensitive to both organic and inorganic materials"
        ],
        "limitations": [
            "Fluorescence interference from organic materials can overwhelm signal",
            "Weak signal for some materials (low Raman cross-section)",
            "Limited penetration depth (~1-100 μm depending on material)",
            "Potential for photodamage with high laser power or sensitive materials",
            "Requires relatively flat surfaces for optimal focus",
            "Spectral libraries may be incomplete for historical materials",
            "Quantification is challenging (requires calibration standards)",
            "Water and moisture can interfere with measurements",
            "Dark or highly absorbing materials may heat up",
            "Portable systems have lower spatial resolution than lab systems"
        ]
    }, "lab_checklist": [
        "Verify laser alignment and power settings",
        "Perform wavenumber calibration with standard reference (Si or polystyrene)",
        "Check sample focus and working distance",
        "Set appropriate integration time and accumulations",
        "Verify detector is not saturated (check max counts)",
        "Record all instrument settings and sample information",
        "Acquire background/reference spectrum if needed",
        "Check for fluorescence interference",
        "Verify spectral range covers region of interest",
        "Save raw data with metadata before processing",
        "Document measurement location and coordinates",
        "Check for sample damage after measurement"
    ],
    
    "keywords": [
        "Raman spectroscopy",
        "Raman microscopy",
        "vibrational spectroscopy",
        "molecular identification",
        "non-destructive analysis",
        "pigment identification",
        "conservation science",
        "cultural heritage",
        "confocal microscopy",
        "spectral imaging",
        "chemical mapping",
        "artwork analysis"
    ]
}

