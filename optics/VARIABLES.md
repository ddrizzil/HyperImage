# Global Variable & Symbol Dictionary for Fundamentals of Optics

This dictionary provides a **unified reference** for all symbols used across the *Fundamentals of Optics* content and related imaging pages (e.g. OCT, SIM, photoacoustic imaging, Raman, etc.).

For each entry:

- **Symbol** – Latin or Greek variable or tensor notation  
- **Name** – Standard name in optics / imaging  
- **Definition** – Clear physical meaning  
- **SI Units** – Base / derived units (with common practical units if different)  
- **Typical Range** – Order-of-magnitude values in optical systems  
- **Context / Example Use** – Where and how it appears in this project  
- **Related Equations** – Key representative equations (in LaTeX)

> **Context conflicts:** Several symbols (e.g. \( \phi, L, n \)) appear in **multiple domains** with different meanings. These are explicitly noted in each entry with domain context tags such as *(phase)*, *(optical power)*, *(radiance)*, etc.

---

## SECTION A — FUNDAMENTAL CONSTANTS

### General space–time variables
- **Symbol**: \( \mathbf{r},\, x, y, z,\, t \)  
- **Name**: Position vector and Cartesian coordinates; time  
- **Definition**:  
  - \( \mathbf{r} = (x,y,z) \) gives spatial position.  
  - \( t \) is time.  
- **SI Units**:  
  - \( x,y,z \): \( \mathrm{m} \)  
  - \( t \): \( \mathrm{s} \)  
- **Typical Range**:  
  - Spatial: \( 10^{-7} - 10^1\,\mathrm{m} \) in optical systems  
  - Time: \( 10^{-15} - 10^2\,\mathrm{s} \) depending on context  
- **Context / Example Use**:  
  - Fields \( \mathbf{E}(\mathbf{r},t) \), \( \psi(\mathbf{r},t) \) in `/optics/fundamentals/nature-of-light` and `/optics/wave_optics/*`  
  - Depth coordinate \( z \) in OCT and PA imaging in `/optics/applications/*`  
- **Related Equations**:  
  - \( \mathbf{E}(\mathbf{r},t) = \Re\{ \mathbf{E}_0 e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)} \} \)  
  - \( z = c_s t / 2 \) in pulse–echo geometries

### c — Speed of light in vacuum
- **Symbol**: \( c \)  
- **Name**: Speed of light in vacuum  
- **Definition**: Universal propagation speed of electromagnetic waves in vacuum.  
- **SI Units**: \( \mathrm{m\,s^{-1}} \)  
- **Typical Range**: Exactly \( c = 2.99792458 \times 10^8 \,\mathrm{m\,s^{-1}} \)  
- **Context / Example Use**:  
  - Wave equation and Maxwell’s equations in `/optics/fundamentals/nature-of-light`  
  - Dispersion and refractive index via \( v_p = c/n \) in `/optics/fundamentals/complex-refractive-index`  
- **Related Equations**:  
  - \( c = \dfrac{1}{\sqrt{\mu_0 \varepsilon_0}} \)  
  - \( v_p = \dfrac{c}{n} \)  
  - \( E = h \nu = \dfrac{h c}{\lambda_0} \)

---

### h — Planck constant
- **Symbol**: \( h \)  
- **Name**: Planck constant  
- **Definition**: Quantum of action; relates photon energy to frequency.  
- **SI Units**: \( \mathrm{J\,s} \)  
- **Typical Range**: \( h \approx 6.62607015 \times 10^{-34}\,\mathrm{J\,s} \) (exact by definition)  
- **Context / Example Use**:  
  - Photon energy and quantum optics in `/optics/fundamentals/nature-of-light`  
  - Spectroscopy and Raman shift energy conversions in `/optics/spectroscopy/*`  
- **Related Equations**:  
  - \( E = h \nu \)  
  - \( \lambda = \dfrac{h}{p} \) (de Broglie wavelength)

---

### \(\hbar\) — Reduced Planck constant
- **Symbol**: \( \hbar = \dfrac{h}{2\pi} \)  
- **Name**: Reduced Planck constant  
- **Definition**: Planck constant divided by \( 2\pi \); appears naturally in angular-frequency formulations.  
- **SI Units**: \( \mathrm{J\,s} \)  
- **Typical Range**: \( \hbar \approx 1.0545718 \times 10^{-34}\,\mathrm{J\,s} \)  
- **Context / Example Use**:  
  - Quantum field formulations and angular-frequency optics in advanced sections `/optics/advanced_methods/*`  
- **Related Equations**:  
  - \( E = \hbar \omega \)  
  - \( \Delta x\,\Delta p \ge \dfrac{\hbar}{2} \)

---

### \(\varepsilon_0\) — Permittivity of free space
- **Symbol**: \( \varepsilon_0 \)  
- **Name**: Vacuum permittivity  
- **Definition**: Proportionality constant between electric displacement and electric field in vacuum.  
- **SI Units**: \( \mathrm{F\,m^{-1}} = \mathrm{C^2\,N^{-1}\,m^{-2}} \)  
- **Typical Range**: \( \varepsilon_0 \approx 8.8541878128 \times 10^{-12}\,\mathrm{F\,m^{-1}} \)  
- **Context / Example Use**:  
  - Maxwell’s equations in `/optics/fundamentals/nature-of-light`  
  - Relation \( c = 1/\sqrt{\mu_0 \varepsilon_0} \) in the same pages  
- **Related Equations**:  
  - \( \nabla \cdot \mathbf{E} = \dfrac{\rho}{\varepsilon_0} \)  
  - \( c = \dfrac{1}{\sqrt{\mu_0 \varepsilon_0}} \)

---

### \(\mu_0\) — Permeability of free space
- **Symbol**: \( \mu_0 \)  
- **Name**: Vacuum permeability  
- **Definition**: Proportionality constant between magnetic flux density and magnetic field in vacuum.  
- **SI Units**: \( \mathrm{H\,m^{-1}} = \mathrm{N\,A^{-2}} \)  
- **Typical Range**: \( \mu_0 = 4\pi \times 10^{-7}\,\mathrm{H\,m^{-1}} \)  
- **Context / Example Use**:  
  - Maxwell’s equations; wave equation derivations in `/optics/fundamentals/nature-of-light`  
- **Related Equations**:  
  - \( \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \dfrac{\partial \mathbf{E}}{\partial t} \)  
  - \( c = 1 / \sqrt{\mu_0 \varepsilon_0} \)

---

### \(k_B\) — Boltzmann constant
- **Symbol**: \( k_B \)  
- **Name**: Boltzmann constant  
- **Definition**: Relates thermal energy to temperature.  
- **SI Units**: \( \mathrm{J\,K^{-1}} \)  
- **Typical Range**: \( k_B \approx 1.380649 \times 10^{-23}\,\mathrm{J\,K^{-1}} \)  
- **Context / Example Use**:  
  - Thermal radiation (Planck law, blackbody) in `/optics/radiometry/*`  
  - Noise in detectors, NEP and SNR modeling in `/optics/detection/*`  
- **Related Equations**:  
  - \( \langle E \rangle = k_B T \)  
  - Appears in Planck spectral radiance \( B_\lambda(T) \)

---

### \(q_e\) — Elementary charge
- **Symbol**: \( q_e \) or \( e \)  
- **Name**: Electron charge (magnitude)  
- **Definition**: Magnitude of the charge of a single electron.  
- **SI Units**: \( \mathrm{C} \)  
- **Typical Range**: \( q_e \approx 1.602176634 \times 10^{-19}\,\mathrm{C} \)  
- **Context / Example Use**:  
  - Photodetector responsivity and quantum efficiency in `/optics/detection/photodetectors`  
  - Shot noise and current noise models.  
- **Related Equations**:  
  - \( I = q_e \, \Phi_{\text{photon}} \, \mathrm{QE} \)  
  - Shot noise \( i_n = \sqrt{2 q_e I \Delta f} \)

---

### \(\lambda_0\) — Free-space wavelength
- **Symbol**: \( \lambda_0 \)  
- **Name**: Wavelength in vacuum / air  
- **Definition**: Spatial period of the optical field in free space.  
- **SI Units**: \( \mathrm{m} \) (often nm or µm in practice)  
- **Typical Range**:  
  - UV: \( 200{-}400\,\mathrm{nm} \)  
  - Visible: \( 400{-}700\,\mathrm{nm} \)  
  - NIR: \( 700{-}2500\,\mathrm{nm} \)  
- **Context / Example Use**:  
  - Dispersion and refractive index in `/optics/fundamentals/complex-refractive-index`  
  - Diffraction and interference in `/optics/wave_optics/*`  
- **Related Equations**:  
  - \( \lambda_0 = \dfrac{c}{\nu} = \dfrac{2\pi c}{\omega} \)  
  - \( k_0 = \dfrac{2\pi}{\lambda_0} \)

---

### \(\nu\) — Frequency
- **Symbol**: \( \nu \)  
- **Name**: Optical frequency  
- **Definition**: Temporal oscillation frequency of the electromagnetic field.  
- **SI Units**: \( \mathrm{Hz} \)  
- **Typical Range**:  
  - Visible light: \( \sim 4 \times 10^{14} - 7.5 \times 10^{14}\,\mathrm{Hz} \)  
- **Context / Example Use**:  
  - Photon energy \( E = h\nu \) in `/optics/fundamentals/nature-of-light`  
  - Spectroscopic line positions in `/optics/spectroscopy/*`  
- **Related Equations**:  
  - \( \nu = \dfrac{c}{\lambda_0} \)  
  - \( E = h \nu \)

---

### \(\omega\) — Angular frequency
- **Symbol**: \( \omega \)  
- **Name**: Angular frequency  
- **Definition**: \( 2\pi \) times the temporal frequency of the field.  
- **SI Units**: \( \mathrm{rad\,s^{-1}} \)  
- **Typical Range**:  
  - Visible: \( \sim 2.5 \times 10^{15} - 4.7 \times 10^{15}\,\mathrm{rad\,s^{-1}} \)  
- **Context / Example Use**:  
  - Complex exponential representations \( e^{-i\omega t} \) in `/optics/wave_optics/*`  
  - Nonlinear optics \( \chi^{(n)}(\omega) \) in `/optics/interactions/nonlinear-optics`  
- **Related Equations**:  
  - \( \omega = 2\pi \nu \)  
  - \( E = \hbar \omega \)

---

### \(k\) — Wavevector magnitude
- **Symbol**: \( k \)  
- **Name**: Wave number / wavevector magnitude  
- **Definition**: Spatial frequency of the wave; \( k = 2\pi / \lambda \).  
- **SI Units**: \( \mathrm{m^{-1}} \)  
- **Typical Range**:  
  - Visible: \( k \sim 10^7\,\mathrm{m^{-1}} \)  
- **Context / Example Use**:  
  - Plane waves in `/optics/wave_optics/propagation`  
  - Diffraction and grating equations in `/optics/wave_optics/diffraction`  
- **Related Equations**:  
  - \( k_0 = \dfrac{2\pi}{\lambda_0} \)  
  - Helmholtz equation: \( (\nabla^2 + k^2) \psi = 0 \)

> **Note on symbol conflict**:  
> In **optical constants**, \( k \) is also used for the **extinction coefficient** (see below). Always check context:  
> - \( k \) (wave number) in propagation and diffraction;  
> - \( k \) (extinction coefficient) in material optical constants \( \tilde{n} = n + i k \).

---

### \(n\) — Refractive index (real part)
- **Symbol**: \( n \)  
- **Name**: Refractive index (real part of complex index)  
- **Definition**: Ratio of speed of light in vacuum to phase velocity in medium: \( n = c/v_p \).  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Air: \( \approx 1.000 - 1.001 \)  
  - Glasses: \( 1.4 - 1.8 \)  
  - Pigments / semiconductors: up to \( \sim 3 - 4 \)  
- **Context / Example Use**:  
  - Snell’s law and Fresnel equations in `/optics/geometric_optics/refraction`  
  - Complex index \( \tilde{n} = n + i k \) in `/optics/fundamentals/complex-refractive-index`  
- **Related Equations**:  
  - \( v_p = c/n \)  
  - \( \tilde{n}^2 = \varepsilon_r \mu_r \)

---

### \(k\) (optical constant) — Extinction coefficient
- **Symbol**: \( k \) (context: **optical constant**)  
- **Name**: Extinction coefficient  
- **Definition**: Imaginary part of complex refractive index \( \tilde{n} = n + i k \); quantifies absorption.  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Weakly absorbing dielectrics: \( k \sim 10^{-5} - 10^{-2} \)  
  - Strongly absorbing pigments / metals: \( k \sim 10^{-1} - 10^{1} \)  
- **Context / Example Use**:  
  - Optical constants for pigments and metals in `/optics/materials/optical-constants`  
  - Thin-film absorption and reflectance modeling.  
- **Related Equations**:  
  - \( \tilde{n}(\omega) = n(\omega) + i k(\omega) \)  
  - Absorption coefficient: \( \alpha = \dfrac{4\pi k}{\lambda_0} \)

---

### \(\sigma_{\mathrm{sc}}, \sigma_{\mathrm{abs}}, \sigma_{\mathrm{ext}}\) — Cross-sections
- **Symbol**: \( \sigma_{\mathrm{sc}}, \sigma_{\mathrm{abs}}, \sigma_{\mathrm{ext}} \)  
- **Name**: Scattering, absorption, and extinction cross-sections  
- **Definition**: Effective area quantifying probability of scattering, absorption, or total extinction for a single particle or feature.  
- **SI Units**: \( \mathrm{m^2} \) (often reported in \( \mathrm{cm^2} \) or normalized per particle)  
- **Typical Range**:  
  - Single nanoparticles: \( 10^{-16} - 10^{-12}\,\mathrm{m^2} \)  
  - Micron-scale particles: \( 10^{-12} - 10^{-10}\,\mathrm{m^2} \)  
- **Context / Example Use**:  
  - Light scattering by pigment particles in `/optics/interactions/scattering`  
  - Radiative transfer and turbidity in diffusive media.  
- **Related Equations**:  
  - Extinction: \( \sigma_{\mathrm{ext}} = \sigma_{\mathrm{sc}} + \sigma_{\mathrm{abs}} \)  
  - Macroscopic coefficients: \( \mu_s = N \sigma_{\mathrm{sc}},\; \mu_a = N \sigma_{\mathrm{abs}} \)

---

### \(\varepsilon_r, \mu_r\) — Relative permittivity and permeability
- **Symbol**: \( \varepsilon_r,\, \mu_r \)  
- **Name**: Relative permittivity and relative permeability  
- **Definition**: Material parameters relating fields in a medium to those in vacuum: \( \varepsilon = \varepsilon_r \varepsilon_0 \), \( \mu = \mu_r \mu_0 \).  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Optical dielectrics: \( \varepsilon_r \sim 1 - 10 \), \( \mu_r \approx 1 \)  
- **Context / Example Use**:  
  - Relation between refractive index and material properties in `/optics/fundamentals/complex-refractive-index`  
- **Related Equations**:  
  - \( \tilde{n}^2 = \varepsilon_r \mu_r \) (non-magnetic media: \( \mu_r \approx 1 \))

---

### \(v_p\) — Phase velocity
- **Symbol**: \( v_p \)  
- **Name**: Phase velocity  
- **Definition**: Speed at which a point of constant phase propagates in a medium.  
- **SI Units**: \( \mathrm{m\,s^{-1}} \)  
- **Typical Range**:  
  - In dielectrics: \( v_p = c/n \sim 10^8\,\mathrm{m\,s^{-1}} \)  
- **Context / Example Use**:  
  - Relation between \( c \), \( n \), and \( v_p \) in `/optics/fundamentals/nature-of-light`  
- **Related Equations**:  
  - \( v_p = \dfrac{c}{n} \)

---

### \(\rho, \mathbf{J}\) — Charge density and current density
- **Symbol**: \( \rho,\, \mathbf{J} \)  
- **Name**: Charge density, electric current density  
- **Definition**:  
  - \( \rho \): free charge per unit volume  
  - \( \mathbf{J} \): current per unit area  
- **SI Units**:  
  - \( \rho \): \( \mathrm{C\,m^{-3}} \)  
  - \( \mathbf{J} \): \( \mathrm{A\,m^{-2}} \)  
- **Typical Range**: Small or zero in most optical media (dielectrics assumed charge-free).  
- **Context / Example Use**:  
  - Full Maxwell equations in `/optics/fundamentals/nature-of-light`  
- **Related Equations**:  
  - \( \nabla \cdot \mathbf{E} = \rho / \varepsilon_0 \)  
  - \( \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \partial_t \mathbf{E} \)

---

### \(m_e\) — Electron mass
- **Symbol**: \( m_e \)  
- **Name**: Electron rest mass  
- **Definition**: Mass of a free electron at rest.  
- **SI Units**: \( \mathrm{kg} \)  
- **Typical Range**: \( m_e \approx 9.10938356 \times 10^{-31}\,\mathrm{kg} \)  
- **Context / Example Use**:  
  - Plasma frequency in `/optics/materials/drude-model`  
- **Related Equations**:  
  - \( \omega_p = \sqrt{\dfrac{N q_e^2}{\varepsilon_0 m_e}} \)

---

## SECTION B — GEOMETRIC OPTICS VARIABLES

### f — Focal length
- **Symbol**: \( f \)  
- **Name**: Focal length  
- **Definition**: Distance from lens (or mirror) principal plane to focal point where collimated rays converge.  
- **SI Units**: \( \mathrm{m} \) (often mm)  
- **Typical Range**: \( 1\,\mathrm{mm} - 2\,\mathrm{m} \) for imaging optics  
- **Context / Example Use**:  
  - Thin-lens formula in `/optics/geometric_optics/lenses`  
- **Related Equations**:  
  - Thin lens: \( \dfrac{1}{f} = \dfrac{1}{s} + \dfrac{1}{s'} \)  
  - Lensmaker’s equation: \( \dfrac{1}{f} = (n - 1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right) \)

---

### \(R_1, R_2\) — Radii of curvature
- **Symbol**: \( R_1, R_2 \)  
- **Name**: Radii of curvature of lens surfaces  
- **Definition**: Radii of the spherical surfaces of a lens; sign convention depends on surface orientation.  
- **SI Units**: \( \mathrm{m} \)  
- **Typical Range**: \( 1\,\mathrm{mm} - 1\,\mathrm{m} \)  
- **Context / Example Use**:  
  - Lens design and lensmaker’s equation in `/optics/geometric_optics/lensmaker`  
- **Related Equations**:  
  - \( \dfrac{1}{f} = (n - 1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right) \)

---

### \(n_1, n_2\) — Refractive indices of media
- **Symbol**: \( n_1, n_2 \)  
- **Name**: Refractive indices of incident and transmitted media  
- **Definition**: Ratio \( c/v_p \) for each medium; used in refraction and reflection.  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Air: \( \approx 1.0 \)  
  - Glass: \( 1.4 - 1.8 \)  
- **Context / Example Use**:  
  - Snell’s law in `/optics/geometric_optics/refraction`  
- **Related Equations**:  
  - Snell: \( n_1 \sin\theta_i = n_2 \sin\theta_t \)

---

### \(\theta_i, \theta_t\) — Incident & transmitted angles
- **Symbol**: \( \theta_i, \theta_t \)  
- **Name**: Angle of incidence, angle of transmission (refraction)  
- **Definition**: Angles measured from the interface normal for incoming and refracted rays.  
- **SI Units**: Radians (often degrees in practice)  
- **Typical Range**: \( 0 - \pi/2 \)  
- **Context / Example Use**:  
  - Refraction and TIR in `/optics/geometric_optics/refraction`  
- **Related Equations**:  
  - \( n_1 \sin\theta_i = n_2 \sin\theta_t \)  
  - Critical angle: \( \theta_c = \arcsin\left(\dfrac{n_2}{n_1}\right) \) for \( n_1>n_2 \)

---

### s, s′ — Object and image distances
- **Symbol**: \( s, s' \)  
- **Name**: Object distance, image distance  
- **Definition**: Distances from lens principal plane to object and to image.  
- **SI Units**: \( \mathrm{m} \) (often mm)  
- **Typical Range**: \( 10\,\mathrm{mm} - 10\,\mathrm{m} \)  
- **Context / Example Use**:  
  - Imaging geometry in `/optics/geometric_optics/lenses`  
- **Related Equations**:  
  - \( \dfrac{1}{f} = \dfrac{1}{s} + \dfrac{1}{s'} \)  
  - Magnification: \( M = - \dfrac{s'}{s} \)

---

### M — Magnification
- **Symbol**: \( M \)  
- **Name**: Lateral magnification  
- **Definition**: Ratio of image height to object height (or image distance to object distance with sign).  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Macroscopic imaging: \( |M| \sim 0.1 - 10 \)  
  - Microscopy: \( |M| \sim 10 - 100 \)  
- **Context / Example Use**:  
  - Lens and microscope design in `/optics/geometric_optics/imaging-systems`  
- **Related Equations**:  
  - \( M = - \dfrac{s'}{s} \)  
  - For multi-lens systems: \( M_{\text{total}} = \prod_i M_i \)

---

### NA — Numerical aperture
- **Symbol**: \( \mathrm{NA} \)  
- **Name**: Numerical aperture  
- **Definition**: Dimensionless measure of light-gathering ability; \( \mathrm{NA} = n \sin\theta_{\max} \).  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Macroscopic lenses: \( 0.1 - 0.3 \)  
  - Microscope objectives: \( 0.1 - 1.4 \)  
- **Context / Example Use**:  
  - Resolution and depth of field in `/optics/geometric_optics/resolution`  
  - Confocal and nonlinear microscopy in `/optics/applications/microscopy`  
- **Related Equations**:  
  - Lateral resolution: \( \delta x \approx 0.61 \dfrac{\lambda}{\mathrm{NA}} \)  
  - Depth of focus \( \propto \dfrac{\lambda}{\mathrm{NA}^2} \)

---

### \(\phi\) (geometric optics) — Optical power
- **Symbol**: \( \phi \) (context: **optical power of a lens**)  
- **Name**: Optical power  
- **Definition**: Reciprocal of focal length: \( \phi = 1/f \).  
- **SI Units**: \( \mathrm{m^{-1}} \) (practically diopters, \( \mathrm{D} = \mathrm{m^{-1}} \))  
- **Typical Range**: \( -20\,\mathrm{D} \) to \( +20\,\mathrm{D} \) for eyeglass lenses; up to \( 100\,\mathrm{D} \) for microscope objectives.  
- **Context / Example Use**:  
  - Lens design in `/optics/geometric_optics/lensmaker`  
- **Related Equations**:  
  - \( \phi = \dfrac{1}{f} \)  
  - For thin lenses in contact: \( \phi_{\text{total}} = \sum_i \phi_i \)

> **Symbol conflict note:**  
> \( \phi \) is also used for **phase** in wave optics (see Section C). Context determines meaning:  
> - Geometric optics: \( \phi \) in diopters (optical power)  
> - Wave optics: \( \phi \) (phase) is dimensionless angle.

---

### L — Optical path length
- **Symbol**: \( L \)  
- **Name**: Physical length / optical path length (context-dependent)  
- **Definition**:  
  - Physical length of medium segment;  
  - Optical path length (OPL) when combined with refractive index: \( \mathrm{OPL} = n L \).  
- **SI Units**: \( \mathrm{m} \)  
- **Typical Range**:  
  - Lab interferometers: \( 10^{-3} - 10^2\,\mathrm{m} \)  
- **Context / Example Use**:  
  - Interferometers in `/optics/wave_optics/interference`  
- **Related Equations**:  
  - Optical path difference: \( \mathrm{OPD} = n_1 L_1 - n_2 L_2 \)

---

### OPD — Optical path difference
- **Symbol**: \( \mathrm{OPD} \)  
- **Name**: Optical path difference  
- **Definition**: Difference in optical path between two beams or rays: \( \mathrm{OPD} = n_1 L_1 - n_2 L_2 \).  
- **SI Units**: \( \mathrm{m} \) (often expressed in wavelengths)  
- **Typical Range**:  
  - Interferometry: \( 10^{-9} - 10^{-3}\,\mathrm{m} \)  
- **Context / Example Use**:  
  - Coherence and interference fringes in `/optics/wave_optics/interference`  
- **Related Equations**:  
  - Phase difference: \( \Delta \phi = \dfrac{2\pi}{\lambda_0} \,\mathrm{OPD} \)

---

## SECTION C — WAVE OPTICS VARIABLES

### \(\mathbf{E}(\mathbf{r}, t)\) — Electric field
- **Symbol**: \( \mathbf{E}(\mathbf{r}, t) \)  
- **Name**: Electric field vector  
- **Definition**: Time- and space-dependent electric field of the electromagnetic wave.  
- **SI Units**: \( \mathrm{V\,m^{-1}} \)  
- **Typical Range**:  
  - In lab beams: \( 10^2 - 10^6\,\mathrm{V\,m^{-1}} \) (implied from intensity)  
- **Context / Example Use**:  
  - Maxwell’s equations & wave equation in `/optics/fundamentals/nature-of-light`  
  - Polarization and Jones/Stokes formalism in `/optics/wave_optics/polarization`  
- **Related Equations**:  
  - Wave equation: \( \nabla^2 \mathbf{E} - \dfrac{1}{c^2} \dfrac{\partial^2 \mathbf{E}}{\partial t^2} = 0 \)  
  - Intensity: \( I \propto \langle |\mathbf{E}|^2 \rangle \)

---

### \(\mathbf{B}(\mathbf{r}, t)\) — Magnetic field
- **Symbol**: \( \mathbf{B}(\mathbf{r}, t) \)  
- **Name**: Magnetic flux density / magnetic field  
- **Definition**: Time- and space-dependent magnetic component of the electromagnetic wave.  
- **SI Units**: \( \mathrm{T} \) (tesla)  
- **Typical Range**: Much smaller magnitude than \( \mathbf{E} \) in free-space waves; linked by \( |\mathbf{B}| = |\mathbf{E}|/c \).  
- **Context / Example Use**:  
  - Maxwell’s equations in `/optics/fundamentals/nature-of-light`  
- **Related Equations**:  
  - \( \nabla \times \mathbf{E} = - \dfrac{\partial \mathbf{B}}{\partial t} \)  
  - \( |\mathbf{B}| = |\mathbf{E}|/c \)

---

### A — Complex amplitude
- **Symbol**: \( A \) or \( A_0 \)  
- **Name**: Complex field amplitude  
- **Definition**: Complex-valued amplitude of optical field; includes magnitude and initial phase.  
- **SI Units**: Same dimensions as field (e.g. \( \mathrm{V\,m^{-1}} \)) but commonly used in normalized units.  
- **Typical Range**: Arbitrary; usually normalized so that \( |A|^2 \) is proportional to intensity.  
- **Context / Example Use**:  
  - Scalar wave optics and Fourier optics in `/optics/wave_optics/fourier-optics`  
- **Related Equations**:  
  - \( E(\mathbf{r}, t) = \Re\{ A(\mathbf{r}) e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)} \} \)

---

### \(\psi(\mathbf{r}, t)\) — Optical field (scalar)
- **Symbol**: \( \psi(\mathbf{r}, t) \)  
- **Name**: Scalar optical field  
- **Definition**: Scalar representation of one polarization component of the field, used in paraxial and scalar diffraction approximations.  
- **SI Units**: Proportional to electric field; often normalized.  
- **Typical Range**: Arbitrary; normalized in simulations.  
- **Context / Example Use**:  
  - Fresnel and Fraunhofer diffraction in `/optics/wave_optics/diffraction`  
- **Related Equations**:  
  - Helmholtz equation: \( (\nabla^2 + k^2)\psi = 0 \)  
  - Paraxial wave equation.

---

### \(\mathbf{k}, k_x, k_y, k_z\) — Wavevector
- **Symbol**: \( \mathbf{k} \)  
- **Name**: Wavevector  
- **Definition**: Vector indicating propagation direction and spatial frequency; \( \mathbf{k} = k \hat{\mathbf{k}} \).  
- **SI Units**: \( \mathrm{m^{-1}} \)  
- **Typical Range**: See \( k \) in Section A.  
- **Context / Example Use**:  
  - Plane waves and dispersion relations in `/optics/wave_optics/propagation`  
  - Fourier-domain formulations in `/optics/computational/fourier-domain-imaging`  
- **Related Equations**:  
  - \( \psi(\mathbf{r}) \propto e^{i\mathbf{k}\cdot\mathbf{r}} \)  
  - \( |\mathbf{k}| = 2\pi/\lambda \)

---

### \(\phi\) (wave optics) — Phase
- **Symbol**: \( \phi \) (context: **phase**)  
- **Name**: Optical phase  
- **Definition**: Argument of the complex field or wave; determines interference and fringe position.  
- **SI Units**: Radians (dimensionless)  
- **Typical Range**: \( 0 - 2\pi \) (often modulo \( 2\pi \))  
- **Context / Example Use**:  
  - Interference and wavefront aberrations in `/optics/wave_optics/interference`  
  - Wavefront function \( W(x,y) \) where phase \( \phi = 2\pi W/\lambda \).  
- **Related Equations**:  
  - Plane wave: \( \phi(\mathbf{r}, t) = \mathbf{k}\cdot\mathbf{r} - \omega t + \phi_0 \)  
  - Interference: \( I \propto 1 + \cos\Delta\phi \)

---

### I — Intensity
- **Symbol**: \( I \)  
- **Name**: Optical intensity (also radiant intensity in some contexts)  
- **Definition**: Power per unit area carried by the beam.  
- **SI Units**: \( \mathrm{W\,m^{-2}} \)  
- **Typical Range**:  
  - Low-power beams: \( 10^{-3} - 10^{2}\,\mathrm{W\,m^{-2}} \)  
  - Focused lasers: up to \( 10^{9}\,\mathrm{W\,m^{-2}} \) and above  
- **Context / Example Use**:  
  - Diffraction, interference visibility in `/optics/wave_optics/*`  
  - Nonlinear optics (intensity-dependent effects) in `/optics/interactions/nonlinear-optics`  
- **Related Equations**:  
  - \( I \propto \langle |\mathbf{E}|^2 \rangle \)  
  - For a Gaussian beam on axis: \( I(0) = \dfrac{2P}{\pi w_0^2} \)

---

### \(\gamma(\tau)\) — Degree of coherence
- **Symbol**: \( \gamma(\tau) \)  
- **Name**: Complex degree of temporal coherence  
- **Definition**: Normalized correlation function of the field at time delay \( \tau \).  
- **SI Units**: Dimensionless  
- **Typical Range**: \( |\gamma(\tau)| \in [0,1] \)  
- **Context / Example Use**:  
  - Temporal coherence and interferometry in `/optics/wave_optics/coherence`  
- **Related Equations**:  
  - \( \gamma(\tau) = \dfrac{\langle E^*(t) E(t+\tau)\rangle}{\langle |E(t)|^2\rangle} \)

---

### \(\mathcal{F}\{\cdot\}\) — Fourier transform operator
- **Symbol**: \( \mathcal{F}\{\cdot\},\, \mathcal{F}^{-1}\{\cdot\} \)  
- **Name**: Fourier transform, inverse Fourier transform  
- **Definition**: Operator mapping between spatial and spatial-frequency (or time and frequency) domains.  
- **SI Units**: Maps physical units to reciprocal-space units (e.g. \( x \leftrightarrow k_x \)).  
- **Typical Range**: N/A (operator)  
- **Context / Example Use**:  
  - Fourier optics, OTF/MTF, PSF in `/optics/wave_optics/fourier-optics`  
  - Computational imaging in `/optics/computational/*`  
- **Related Equations**:  
  - \( \tilde{U}(k_x, k_y) = \mathcal{F}\{ U(x,y)\} \)  
  - Convolution theorem: \( \mathcal{F}\{f \otimes g\} = \mathcal{F}\{f\}\, \mathcal{F}\{g\} \)

---

### OTF, MTF, PSF — Transfer and point spread functions
- **Symbols**:  
  - \( \mathrm{OTF}(\mathbf{f}) \): Optical transfer function  
  - \( \mathrm{MTF}(\mathbf{f}) \): Modulation transfer function (magnitude of OTF)  
  - \( \mathrm{PSF}(\mathbf{r}) \): Point spread function  
- **Name**: System transfer and impulse responses  
- **Definition**:  
  - PSF: intensity distribution from a point object.  
  - OTF: Fourier transform of PSF (complex).  
  - MTF: \( |\mathrm{OTF}| \) describing contrast transfer vs spatial frequency.  
- **SI Units**:  
  - PSF: \( \mathrm{m^{-2}} \) up to scaling  
  - OTF/MTF: Dimensionless  
- **Typical Range**:  
  - \( \mathrm{MTF} \in [0,1] \)  
- **Context / Example Use**:  
  - Imaging performance in `/optics/wave_optics/fourier-optics` and `/optics/applications/microscopy`  
- **Related Equations**:  
  - \( \mathrm{OTF}(\mathbf{f}) = \mathcal{F}\{\mathrm{PSF}(\mathbf{r})\} \)  
  - \( \mathrm{MTF}(\mathbf{f}) = |\mathrm{OTF}(\mathbf{f})| \)

---

### \(W(x,y)\) — Wavefront function
- **Symbol**: \( W(x,y) \)  
- **Name**: Wavefront aberration / optical path deviation  
- **Definition**: Optical path deviation from an ideal spherical wavefront at pupil coordinates \( (x,y) \).  
- **SI Units**: \( \mathrm{m} \) (often reported in wavelengths)  
- **Typical Range**:  
  - Well-corrected systems: \( |W| < \lambda/14 \) RMS  
- **Context / Example Use**:  
  - Aberrations, Zernike polynomials in `/optics/geometric_optics/aberrations` and `/optics/wave_optics/wavefronts`  
- **Related Equations**:  
  - Phase: \( \phi(x,y) = \dfrac{2\pi}{\lambda_0} W(x,y) \)

---

### \(z_R\) — Rayleigh range
- **Symbol**: \( z_R \)  
- **Name**: Rayleigh range  
- **Definition**: Distance from the beam waist where area doubles and intensity drops by half; depth of focus of a Gaussian beam.  
- **SI Units**: \( \mathrm{m} \)  
- **Typical Range**:  
  - Microscopy beams: \( 10{-}500\,\mu\mathrm{m} \)  
- **Context / Example Use**:  
  - Gaussian beam propagation in `/optics/wave_optics/gaussian-beams`  
- **Related Equations**:  
  - \( z_R = \dfrac{\pi w_0^2}{\lambda_0} \)  
  - Beam radius: \( w(z) = w_0 \sqrt{1 + (z/z_R)^2} \)

---

### \(w_0\) — Beam waist
- **Symbol**: \( w_0 \)  
- **Name**: Beam waist radius  
- **Definition**: Minimum \( 1/e^2 \) intensity radius of a Gaussian beam.  
- **SI Units**: \( \mathrm{m} \) (often µm)  
- **Typical Range**:  
  - Microscope focus: \( 0.3{-}5\,\mu\mathrm{m} \)  
  - Macroscopic beams: \( 0.1{-}5\,\mathrm{mm} \)  
- **Context / Example Use**:  
  - Two-photon and nonlinear microscopy in `/optics/applications/nonlinear-microscopy`  
- **Related Equations**:  
  - \( z_R = \pi w_0^2 / \lambda_0 \)  
  - On-axis intensity: \( I(0) = 2P/(\pi w_0^2) \)

---

## SECTION D — POLARIZATION VARIABLES

### \(E_x, E_y\) — Field components
- **Symbol**: \( E_x, E_y \)  
- **Name**: Cartesian components of the electric field  
- **Definition**: Complex amplitudes of the field along x and y axes.  
- **SI Units**: \( \mathrm{V\,m^{-1}} \)  
- **Typical Range**: Relative magnitudes determine polarization state; absolute values depend on intensity.  
- **Context / Example Use**:  
  - Jones vector and Stokes parameter derivations in `/optics/wave_optics/polarization`  
- **Related Equations**:  
  - Jones vector: \( \mathbf{J} = \begin{bmatrix} E_x \\ E_y \end{bmatrix} \)

---

### \(\delta\) — Phase retardance
- **Symbol**: \( \delta \)  
- **Name**: Phase difference / retardance  
- **Definition**: Phase delay between orthogonal polarization components, often introduced by birefringent elements.  
- **SI Units**: Radians  
- **Typical Range**:  
  - Quarter-wave plate: \( \delta = \pi/2 \)  
  - Half-wave plate: \( \delta = \pi \)  
- **Context / Example Use**:  
  - Waveplates and birefringence in `/optics/materials/birefringence`  
- **Related Equations**:  
  - \( \delta = \dfrac{2\pi \Delta n L}{\lambda_0} \)

---

### \(S_0, S_1, S_2, S_3\) — Stokes parameters
- **Symbol**: \( S_0, S_1, S_2, S_3 \)  
- **Name**: Stokes parameters  
- **Definition**: Set of four real numbers describing intensity and polarization state.  
- **SI Units**:  
  - \( S_0 \): \( \mathrm{W\,m^{-2}} \) (total intensity)  
  - \( S_1, S_2, S_3 \): same scale, often normalized by \( S_0 \)  
- **Typical Range**:  
  - \( S_0 > 0 \), \( S_1, S_2, S_3 \in [-S_0, S_0] \)  
- **Context / Example Use**:  
  - Polarimetry and Mueller calculus in `/optics/wave_optics/polarization`  
- **Related Equations**:  
  - \( S_0 = |E_x|^2 + |E_y|^2 \)  
  - \( S_1 = |E_x|^2 - |E_y|^2 \)  
  - \( S_2 = 2\Re(E_x E_y^*) \)  
  - \( S_3 = 2\Im(E_x E_y^*) \)

---

### \(\mathbf{J}\) — Jones vector
- **Symbol**: \( \mathbf{J} \)  
- **Name**: Jones vector  
- **Definition**: Complex 2D vector representing fully polarized light in a given basis.  
- **SI Units**: Proportional to electric field  
- **Typical Range**: Normalization arbitrary; often scaled such that \( |\mathbf{J}|^2 = 1 \) or intensity.  
- **Context / Example Use**:  
  - Polarization calculations in `/optics/wave_optics/polarization`  
- **Related Equations**:  
  - \( \mathbf{J}_{\text{out}} = \hat{J} \, \mathbf{J}_{\text{in}} \)

---

### \(\hat{J}\) — Jones matrix
- **Symbol**: \( \hat{J} \)  
- **Name**: Jones matrix  
- **Definition**: \( 2 \times 2 \) complex matrix describing action of an optical element on polarization.  
- **SI Units**: Dimensionless (linear transformation)  
- **Typical Range**: Elements typically complex numbers with magnitude \(\leq 1\).  
- **Context / Example Use**:  
  - Linear polarizers, waveplates, retarders in `/optics/wave_optics/polarization`  
- **Related Equations**:  
  - \( \mathbf{J}_{\text{out}} = \hat{J} \mathbf{J}_{\text{in}} \)

---

### \(\chi\) — Ellipticity
- **Symbol**: \( \chi \) (context: **ellipticity**)  
- **Name**: Ellipticity angle  
- **Definition**: Parameter describing the shape of polarization ellipse; \( \tan\chi = b/a \) where \( a,b \) are semi-axes.  
- **SI Units**: Radians  
- **Typical Range**: \( -\pi/4 \le \chi \le \pi/4 \)  
- **Context / Example Use**:  
  - Polarization ellipse representation in `/optics/wave_optics/polarization`  
- **Related Equations**:  
  - Stokes relation: \( \tan 2\chi = \dfrac{S_3}{\sqrt{S_1^2 + S_2^2}} \)

---

### \(\psi\) — Azimuth (polarization)
- **Symbol**: \( \psi \) (context: **polarization azimuth**)  
- **Name**: Azimuth angle of polarization ellipse  
- **Definition**: Orientation angle of major axis of polarization ellipse relative to reference axis.  
- **SI Units**: Radians  
- **Typical Range**: \( -\pi/2 \le \psi < \pi/2 \)  
- **Context / Example Use**:  
  - Polarization ellipse parametrization in `/optics/wave_optics/polarization`  
- **Related Equations**:  
  - \( \tan 2\psi = \dfrac{S_2}{S_1} \)

---

## SECTION E — MATERIAL INTERACTION VARIABLES

### \(\alpha\) — Absorption coefficient
- **Symbol**: \( \alpha \)  
- **Name**: Absorption coefficient  
- **Definition**: Exponential attenuation coefficient in Beer–Lambert law.  
- **SI Units**: \( \mathrm{m^{-1}} \) (often \( \mathrm{cm^{-1}} \))  
- **Typical Range**:  
  - Weak absorbers: \( 10^{-2} - 10^{1}\,\mathrm{m^{-1}} \)  
  - Strong pigments: \( 10^{3} - 10^{6}\,\mathrm{m^{-1}} \)  
- **Context / Example Use**:  
  - Beer–Lambert law in `/optics/spectroscopy/beer-lambert-law`  
- **Related Equations**:  
  - \( I(z) = I_0 e^{-\alpha z} \)  
  - \( \alpha = 4\pi k / \lambda_0 \)

---

### \(\sigma\) — Scattering coefficient (microscopic)
- **Symbol**: \( \sigma \)  
- **Name**: Scattering cross-section (single scatterer)  
- **Definition**: Effective area representing scattering strength of a particle.  
- **SI Units**: \( \mathrm{m^2} \)  
- **Typical Range**: See cross-sections in Section A; used to build macroscopic \( \mu_s \).  
- **Context / Example Use**:  
  - Mie/Rayleigh scattering in `/optics/interactions/scattering`  
- **Related Equations**:  
  - \( \mu_s = N \sigma \)

---

### g — Anisotropy factor
- **Symbol**: \( g \)  
- **Name**: Scattering anisotropy factor  
- **Definition**: Mean cosine of scattering angle: \( g = \langle \cos\theta \rangle \).  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Isotropic: \( g \approx 0 \)  
  - Forward scattering biological tissues: \( g \approx 0.8 - 0.95 \)  
- **Context / Example Use**:  
  - Diffusion approximation and reduced scattering in `/optics/interactions/turbid-media`  
- **Related Equations**:  
  - Reduced scattering: \( \mu_s' = \mu_s (1-g) \)

---

### \(\mu_a, \mu_s, \mu_t\) — Macroscopic optical coefficients
- **Symbol**: \( \mu_a, \mu_s, \mu_t \)  
- **Name**: Absorption, scattering, and total attenuation coefficients  
- **Definition**:  
  - \( \mu_a \): macroscopic absorption coefficient  
  - \( \mu_s \): macroscopic scattering coefficient  
  - \( \mu_t = \mu_a + \mu_s \): total attenuation  
- **SI Units**: \( \mathrm{m^{-1}} \)  
- **Typical Range**:  
  - Tissues, paints: \( \mu_a \sim 1{-}10^3\,\mathrm{m^{-1}} \), \( \mu_s \sim 10^2{-}10^4\,\mathrm{m^{-1}} \)  
- **Context / Example Use**:  
  - Diffusion theory, OCT, and photoacoustic imaging in `/optics/applications/pa-imaging` and `/optics/applications/oct`  
- **Related Equations**:  
  - Radiative transport: \( \dfrac{dI}{dz} = -\mu_t I \)  
  - Diffusion length and penetration depth formulas.

---

### \(\tau\) — Lifetime
- **Symbol**: \( \tau \)  
- **Name**: Lifetime (e.g. fluorescence, excited-state)  
- **Definition**: Mean time an excited state persists before relaxation.  
- **SI Units**: \( \mathrm{s} \)  
- **Typical Range**:  
  - Fluorescence: \( 10^{-9} - 10^{-6}\,\mathrm{s} \)  
- **Context / Example Use**:  
  - Time-resolved fluorescence and excited-state decay in `/optics/interactions/fluorescence`  
- **Related Equations**:  
  - Exponential decay: \( N(t) = N_0 e^{-t/\tau} \)

---

### N — Population density
- **Symbol**: \( N \)  
- **Name**: Population number density  
- **Definition**: Number of particles (atoms, molecules, centers) per unit volume.  
- **SI Units**: \( \mathrm{m^{-3}} \)  
- **Typical Range**: \( 10^{20} - 10^{28}\,\mathrm{m^{-3}} \) depending on medium.  
- **Context / Example Use**:  
  - Gain and stimulated emission in lasers `/optics/interactions/laser-gain`  
- **Related Equations**:  
  - Gain coefficient: \( g = N \sigma_{\mathrm{stim}} \)

---

### \(\sigma_{\text{stim}}\) — Stimulated emission cross-section
- **Symbol**: \( \sigma_{\text{stim}} \)  
- **Name**: Stimulated emission cross-section  
- **Definition**: Effective area characterizing probability of stimulated emission per photon.  
- **SI Units**: \( \mathrm{m^2} \)  
- **Typical Range**: \( 10^{-25} - 10^{-19}\,\mathrm{m^2} \)  
- **Context / Example Use**:  
  - Laser gain and amplification in `/optics/interactions/laser-gain`  
- **Related Equations**:  
  - \( g(\nu) = N_2 \sigma_{\text{stim}}(\nu) - N_1 \sigma_{\text{abs}}(\nu) \)

---

### \(\chi^{(1)}, \chi^{(2)}, \chi^{(3)}\) — Nonlinear susceptibilities
- **Symbol**: \( \chi^{(1)}, \chi^{(2)}, \chi^{(3)} \)  
- **Name**: Linear and nonlinear electric susceptibilities  
- **Definition**: Tensors relating polarization \( \mathbf{P} \) to powers of electric field \( \mathbf{E} \).  
- **SI Units**: Dimensionless (in Gaussian units) or \( \mathrm{m\,V^{-1}} \), \( \mathrm{m^2\,V^{-2}} \) depending on convention; in this project we treat them as effective dimensionless coefficients with context-dependent scaling.  
- **Typical Range**:  
  - \( \chi^{(1)} \sim 1 - 10 \)  
  - \( \chi^{(2)} \sim 10^{-12} - 10^{-8}\,\mathrm{m\,V^{-1}} \)  
  - \( \chi^{(3)} \sim 10^{-22} - 10^{-18}\,\mathrm{m^2\,V^{-2}} \)  
- **Context / Example Use**:  
  - SHG, THG, CARS microscopy in `/optics/applications/nonlinear-microscopy` and nonlinear sections.  
- **Related Equations**:  
  - \( \mathbf{P} = \varepsilon_0 \left( \chi^{(1)} \mathbf{E} + \chi^{(2)} : \mathbf{E}^2 + \chi^{(3)} : \mathbf{E}^3 + \cdots \right) \)

---

## SECTION F — RADIOMETRY & DETECTION VARIABLES

> **Note on symbol L:**  
> In **radiometry**, \( L \) denotes **radiance** (not path length). Context section clarifies which meaning is active.

### \(\Phi\) — Radiant flux
- **Symbol**: \( \Phi \)  
- **Name**: Radiant flux / optical power  
- **Definition**: Total radiant energy per unit time.  
- **SI Units**: \( \mathrm{W} \)  
- **Typical Range**:  
  - Lab sources: \( 10^{-3} - 10^2\,\mathrm{W} \)  
- **Context / Example Use**:  
  - Radiometric balances in `/optics/radiometry/fundamentals`  
- **Related Equations**:  
  - \( \Phi = \iint I(\mathbf{r})\, dA \)

---

### L — Radiance (radiometry)
- **Symbol**: \( L \) (context: **radiance**)  
- **Name**: Radiance  
- **Definition**: Power per unit projected area per unit solid angle.  
- **SI Units**: \( \mathrm{W\,m^{-2}\,sr^{-1}} \)  
- **Typical Range**:  
  - Display screens, daylight scenes: \( 10^0 - 10^4\,\mathrm{W\,m^{-2}\,sr^{-1}} \)  
- **Context / Example Use**:  
  - Imaging system throughput and etendue in `/optics/radiometry/imaging-radiometry`  
- **Related Equations**:  
  - Etendue: \( G = \iint n^2 \cos\theta\, dA\, d\Omega \) with radiance invariance.

---

### E — Irradiance
- **Symbol**: \( E \) (context: **irradiance**)  
- **Name**: Irradiance  
- **Definition**: Radiant flux per unit area incident on a surface.  
- **SI Units**: \( \mathrm{W\,m^{-2}} \)  
- **Typical Range**:  
  - Sunlight at Earth: \( \sim 10^3\,\mathrm{W\,m^{-2}} \)  
  - Lab beams: \( 10^{-3} - 10^3\,\mathrm{W\,m^{-2}} \)  
- **Context / Example Use**:  
  - Detector exposure and damage thresholds in `/optics/detection/photodetectors`  
- **Related Equations**:  
  - \( E = \int L(\theta,\phi) \cos\theta\, d\Omega \)

---

### \(B_\lambda(T)\) — Spectral radiance
- **Symbol**: \( B_\lambda(T) \)  
- **Name**: Spectral radiance of a blackbody  
- **Definition**: Radiance per unit wavelength of an ideal blackbody at temperature \( T \).  
- **SI Units**: \( \mathrm{W\,m^{-3}\,sr^{-1}} \) (per m of wavelength)  
- **Typical Range**: Depends strongly on \( T \) and \( \lambda \).  
- **Context / Example Use**:  
  - Thermal emitters and illumination models in `/optics/radiometry/blackbody`  
- **Related Equations**:  
  - Planck’s law:  
    \[
    B_\lambda(T) = \frac{2 h c^2}{\lambda^5} \frac{1}{\exp\left(\frac{h c}{\lambda k_B T}\right) - 1}
    \]

---

### R — Responsivity
- **Symbol**: \( R \)  
- **Name**: Detector responsivity  
- **Definition**: Ratio of output electrical signal (current or voltage) to incident optical power at a given wavelength.  
- **SI Units**: \( \mathrm{A\,W^{-1}} \) or \( \mathrm{V\,W^{-1}} \)  
- **Typical Range**: \( 0.1 - 1\,\mathrm{A\,W^{-1}} \) for silicon photodiodes in visible.  
- **Context / Example Use**:  
  - Detector modeling in `/optics/detection/photodetectors`  
- **Related Equations**:  
  - \( I_{\text{out}} = R(\lambda) \, \Phi_{\text{in}} \)

---

### \(I_d\) — Dark current
- **Symbol**: \( I_d \)  
- **Name**: Dark current  
- **Definition**: Current produced by a detector in absence of light (thermal + leakage).  
- **SI Units**: \( \mathrm{A} \)  
- **Typical Range**: \( 10^{-15} - 10^{-9}\,\mathrm{A} \) for cooled devices; higher for uncooled.  
- **Context / Example Use**:  
  - Noise analysis and SNR calculations in `/optics/detection/noise`  
- **Related Equations**:  
  - Dark-noise current: \( i_{n,\text{dark}} \approx \sqrt{2 q_e I_d \Delta f} \)

---

### NEP — Noise-equivalent power
- **Symbol**: \( \mathrm{NEP} \)  
- **Name**: Noise-equivalent power  
- **Definition**: Incident optical power that yields SNR = 1 in a 1 Hz bandwidth.  
- **SI Units**: \( \mathrm{W\,Hz^{-1/2}} \)  
- **Typical Range**: \( 10^{-17} - 10^{-12}\,\mathrm{W\,Hz^{-1/2}} \)  
- **Context / Example Use**:  
  - Detector performance comparison in `/optics/detection/noise`  
- **Related Equations**:  
  - \( \mathrm{SNR} = \dfrac{P_{\text{signal}}}{\mathrm{NEP} \sqrt{\Delta f}} \)

---

### SNR — Signal-to-noise ratio
- **Symbol**: \( \mathrm{SNR} \)  
- **Name**: Signal-to-noise ratio  
- **Definition**: Ratio of mean signal level to standard deviation of noise.  
- **SI Units**: Dimensionless (often expressed in dB)  
- **Typical Range**: \( 1 - 10^4 \) (0–80 dB) depending on measurement.  
- **Context / Example Use**:  
  - All detection and imaging performance discussions; e.g. `/optics/detection/noise` and `/optics/applications/pa-imaging`  
- **Related Equations**:  
  - \( \mathrm{SNR} = \frac{P_{\text{signal}}}{P_{\text{noise}}} \) (or in power spectral terms)  
  - \( \mathrm{SNR}_{\mathrm{dB}} = 10 \log_{10}(\mathrm{SNR}) \)

---

### \(\Delta\lambda\) — Spectral bandwidth
- **Symbol**: \( \Delta\lambda \)  
- **Name**: Spectral bandwidth / FWHM  
- **Definition**: Width of source or filter spectrum (often full-width at half-maximum).  
- **SI Units**: \( \mathrm{m} \) (practical: nm)  
- **Typical Range**:  
  - Narrowband lasers: \( < 0.01\,\mathrm{nm} \)  
  - LEDs: \( 10 - 50\,\mathrm{nm} \)  
  - Supercontinuum / broadband sources: \( 100 - 1000\,\mathrm{nm} \)  
- **Context / Example Use**:  
  - OCT axial resolution and coherence length in `/optics/applications/oct`  
- **Related Equations**:  
  - Coherence length: \( L_c \approx \dfrac{2 \ln 2}{\pi}\dfrac{\lambda_0^2}{\Delta\lambda} \)

---

### QE — Quantum efficiency
- **Symbol**: \( \mathrm{QE} \)  
- **Name**: Quantum efficiency  
- **Definition**: Fraction of incident photons that generate a useful signal (e.g. electron–hole pairs).  
- **SI Units**: Dimensionless (0–1) or percentage  
- **Typical Range**:  
  - Silicon detectors: \( 0.3 - 0.9 \) in visible  
  - EMCCD, sCMOS have high QE near peak wavelengths.  
- **Context / Example Use**:  
  - Detector efficiency and SNR in `/optics/detection/photodetectors`  
- **Related Equations**:  
  - Responsivity: \( R(\lambda) = \dfrac{q_e}{h c} \lambda \,\mathrm{QE}(\lambda) \)

---

## SECTION G — SPECTROSCOPY VARIABLES

### \(\tilde{\nu}\) — Wavenumber
- **Symbol**: \( \tilde{\nu} \)  
- **Name**: Wavenumber (spectroscopy)  
- **Definition**: Reciprocal of wavelength in centimeters; used widely in IR/Raman.  
- **SI Units**: \( \mathrm{m^{-1}} \) (practical: \( \mathrm{cm^{-1}} \))  
- **Typical Range**:  
  - Vibrational spectroscopy: \( 100 - 4000\,\mathrm{cm^{-1}} \)  
- **Context / Example Use**:  
  - FTIR and Raman in `/optics/spectroscopy/ftir` and `/optics/spectroscopy/raman`  
- **Related Equations**:  
  - \( \tilde{\nu} = \dfrac{1}{\lambda_{\mathrm{cm}}} = \dfrac{10^7}{\lambda_{\mathrm{nm}}} \)

---

### \(\Delta \nu\) — Linewidth
- **Symbol**: \( \Delta \nu \)  
- **Name**: Spectral linewidth (frequency domain)  
- **Definition**: Width of a spectral line, often FWHM in frequency.  
- **SI Units**: \( \mathrm{Hz} \) (or \( \mathrm{cm^{-1}} \) via conversion)  
- **Typical Range**:  
  - Gas-phase transitions: kHz–MHz  
  - Solid-state, inhomogeneous: MHz–THz  
- **Context / Example Use**:  
  - Laser linewidth, spectral resolution in `/optics/spectroscopy/line-shapes`  
- **Related Equations**:  
  - Lifetime–linewidth relation: \( \Delta \nu \approx \dfrac{1}{2\pi \tau} \)

---

### \(A(\lambda)\) — Absorbance
- **Symbol**: \( A(\lambda) \)  
- **Name**: Absorbance  
- **Definition**: Logarithmic measure of attenuation: \( A = -\log_{10} T \).  
- **SI Units**: Dimensionless  
- **Typical Range**: \( 0 - 2 \) for many measurements; higher for strong absorbers.  
- **Context / Example Use**:  
  - Beer–Lambert law in `/optics/spectroscopy/beer-lambert-law`  
- **Related Equations**:  
  - \( A(\lambda) = \varepsilon(\lambda) c \ell \)  
  - \( T = 10^{-A} \)

---

### \(T(\lambda)\) — Transmittance
- **Symbol**: \( T(\lambda) \)  
- **Name**: Transmittance  
- **Definition**: Fraction of incident power transmitted: \( T = I/I_0 \).  
- **SI Units**: Dimensionless (0–1) or percentage  
- **Typical Range**: \( 0 - 1 \)  
- **Context / Example Use**:  
  - Filter characterization and sample transmission in `/optics/spectroscopy/beer-lambert-law`  
- **Related Equations**:  
  - \( T(\lambda) = 10^{-A(\lambda)} \)  
  - \( I(z) = I_0 e^{-\alpha z} \Rightarrow T = e^{-\alpha \ell} \)

---

### \(\varepsilon\) — Molar absorptivity
- **Symbol**: \( \varepsilon(\lambda) \)  
- **Name**: Molar extinction / absorptivity coefficient  
- **Definition**: Proportionality constant in Beer–Lambert law relating absorbance to concentration and path length.  
- **SI Units**: \( \mathrm{L\,mol^{-1}\,cm^{-1}} \) (chemistry convention)  
- **Typical Range**: \( 10^1 - 10^5\,\mathrm{L\,mol^{-1}\,cm^{-1}} \)  
- **Context / Example Use**:  
  - Solution-phase spectroscopy in `/optics/spectroscopy/beer-lambert-law`  
- **Related Equations**:  
  - \( A(\lambda) = \varepsilon(\lambda) c \ell \)

---

### \(\ell\) — Path length
- **Symbol**: \( \ell \)  
- **Name**: Optical path length in cuvette / sample thickness  
- **Definition**: Length of beam path through sample for Beer–Lambert law.  
- **SI Units**: \( \mathrm{m} \) (often cm in lab)  
- **Typical Range**: \( 0.1 - 10\,\mathrm{cm} \)  
- **Context / Example Use**:  
  - UV–Vis, NIR absorption in `/optics/spectroscopy/beer-lambert-law`  
- **Related Equations**:  
  - \( A = \varepsilon c \ell \)

---

### Raman shift — Frequency/wavenumber shift
- **Symbol**: \( \Delta \tilde{\nu}_{\mathrm{Raman}} \) or simply “Raman shift”  
- **Name**: Raman shift  
- **Definition**: Difference between excitation and scattered wavenumber.  
- **SI Units**: \( \mathrm{cm^{-1}} \)  
- **Typical Range**: \( 50 - 4000\,\mathrm{cm^{-1}} \)  
- **Context / Example Use**:  
  - Raman and CARS spectroscopy in `/optics/spectroscopy/raman` and technique pages for Raman microscopy.  
- **Related Equations**:  
  - \( \Delta \tilde{\nu}_{\mathrm{Raman}} = \tilde{\nu}_{\text{exc}} - \tilde{\nu}_{\text{scattered}} \)

---

### \(\omega_p\) — Plasma frequency
- **Symbol**: \( \omega_p \)  
- **Name**: Plasma frequency  
- **Definition**: Natural oscillation frequency of free electron gas in a material.  
- **SI Units**: \( \mathrm{rad\,s^{-1}} \)  
- **Typical Range**: \( 10^{15} - 10^{16}\,\mathrm{rad\,s^{-1}} \) for metals.  
- **Context / Example Use**:  
  - Drude model of metals in `/optics/materials/drude-model`  
- **Related Equations**:  
  - \( \omega_p = \sqrt{\dfrac{N q_e^2}{\varepsilon_0 m_e}} \)

---

## SECTION H — COMPUTATIONAL VARIABLES

### H — Transfer function
- **Symbol**: \( H(\mathbf{f}) \) or \( H \)  
- **Name**: System transfer function  
- **Definition**: Mapping from object spectrum to image spectrum (frequency-domain representation of PSF).  
- **SI Units**: Dimensionless (gain factor)  
- **Typical Range**: \( |H| \in [0,1] \) for normalized systems.  
- **Context / Example Use**:  
  - Reconstruction and deconvolution in `/optics/computational/deconvolution`  
- **Related Equations**:  
  - \( G(\mathbf{f}) = H(\mathbf{f}) O(\mathbf{f}) + N(\mathbf{f}) \)

---

### O — Object function
- **Symbol**: \( O(\mathbf{r}) \) or \( O(\mathbf{f}) \)  
- **Name**: Object / sample distribution  
- **Definition**: Spatial distribution of sample property (e.g. refractive index, absorption, phase) being imaged.  
- **SI Units**: Depends on modality (e.g. dimensionless amplitude, absorption coefficient).  
- **Typical Range**: Normalized between 0–1 for many models.  
- **Context / Example Use**:  
  - Imaging model in `/optics/computational/forward-models`  
- **Related Equations**:  
  - \( G = H \otimes O \) (in real space)  
  - \( G(\mathbf{f}) = H(\mathbf{f}) O(\mathbf{f}) \)

---

### G — Measured data
- **Symbol**: \( G(\mathbf{r}) \) or \( G(\mathbf{f}) \)  
- **Name**: Measured image / data  
- **Definition**: Recorded signal after passing through imaging system and detector.  
- **SI Units**: Detector counts, intensity, or arbitrary units.  
- **Typical Range**: 0–\( 2^{N_{\text{bits}}}-1 \) for digital images.  
- **Context / Example Use**:  
  - Inverse problems and reconstruction in `/optics/computational/inverse-problems`  
- **Related Equations**:  
  - \( G = H \otimes O + \eta \)  
  - \( G(\mathbf{f}) = H(\mathbf{f}) O(\mathbf{f}) + N(\mathbf{f}) \)

---

### \(\eta\) — Regularization parameter / noise term
- **Symbol**: \( \eta \)  
- **Name**: Regularization parameter (or noise term, depending on context)  
- **Definition**:  
  - In optimization: parameter controlling strength of regularization.  
  - In some models: additive noise term.  
- **SI Units**: Depends on cost functional; often dimensionless.  
- **Typical Range**: Chosen empirically, e.g. \( 10^{-6} - 10^{2} \).  
- **Context / Example Use**:  
  - Tikhonov or sparsity-regularized inversion in `/optics/computational/regularization`  
- **Related Equations**:  
  - Cost functional: \( \mathcal{J}(O) = \|H O - G\|^2 + \eta \, R(O) \)

---

### \(\nabla\) — Gradient operator
- **Symbol**: \( \nabla \)  
- **Name**: Gradient (vector differential operator)  
- **Definition**: Operator giving spatial derivatives: \( \nabla = (\partial_x, \partial_y, \partial_z) \).  
- **SI Units**: \( \mathrm{m^{-1}} \) when applied to scalar fields.  
- **Typical Range**: N/A (operator)  
- **Context / Example Use**:  
  - PDE-based regularization and phase retrieval in `/optics/computational/variational-methods`  
- **Related Equations**:  
  - Laplacian: \( \nabla^2 = \nabla\cdot\nabla \)

---

### \(\otimes\) — Convolution
- **Symbol**: \( \otimes \)  
- **Name**: Convolution operator  
- **Definition**: Integral combining two functions with a reversed and shifted kernel.  
- **SI Units**: Units of the product of the two convolved fields.  
- **Typical Range**: N/A (operator)  
- **Context / Example Use**:  
  - Imaging forward model \( G = H \otimes O \) in `/optics/computational/forward-models`  
- **Related Equations**:  
  - \( (f \otimes g)(x) = \int f(u) g(x-u)\,du \)

---

### * — Correlation
- **Symbol**: \( * \) (context: **correlation**)  
- **Name**: Correlation operator  
- **Definition**: Similar to convolution but without kernel reversal.  
- **SI Units**: As for convolution.  
- **Typical Range**: N/A  
- **Context / Example Use**:  
  - Autocorrelation in coherence / speckle analysis `/optics/wave_optics/coherence`  
- **Related Equations**:  
  - \( (f * g)(x) = \int f(u) g(u+x)\,du \)

---

### \(A^\mathrm{T}\) — Adjoint / transpose operator
- **Symbol**: \( A^\mathrm{T}, A^\ast, A^\dagger \) (depending on context)  
- **Name**: Adjoint / transpose operator  
- **Definition**: Linear operator adjoint to \( A \) under chosen inner product; used in gradient computations.  
- **SI Units**: Same mapping units as \( A \).  
- **Typical Range**: N/A  
- **Context / Example Use**:  
  - Iterative reconstruction algorithms in `/optics/computational/inverse-problems`  
- **Related Equations**:  
  - Gradient: \( \nabla_O \|A O - G\|^2 = 2 A^\mathrm{T}(A O - G) \)

---

## SECTION I — ADVANCED IMAGING VARIABLES (OCT, SIM, PA IMAGING)

### \(k_0\) — Central wavenumber
- **Symbol**: \( k_0 \)  
- **Name**: Central (mean) wavenumber of broadband source  
- **Definition**: \( 2\pi / \lambda_0 \) evaluated at central wavelength of source spectrum.  
- **SI Units**: \( \mathrm{m^{-1}} \)  
- **Typical Range**:  
  - OCT at \( \lambda_0 \sim 800\,\mathrm{nm} \): \( k_0 \sim 7.8 \times 10^6\,\mathrm{m^{-1}} \)  
- **Context / Example Use**:  
  - OCT axial resolution in `/optics/applications/oct`  
- **Related Equations**:  
  - \( k_0 = 2\pi / \lambda_0 \)

---

### \(\Delta k\) — Spectral bandwidth (wavenumber)
- **Symbol**: \( \Delta k \)  
- **Name**: Source bandwidth in wavenumber domain  
- **Definition**: Standard deviation or FWHM of \( k \)-space spectrum.  
- **SI Units**: \( \mathrm{m^{-1}} \)  
- **Typical Range**: For broadband OCT, \( \Delta k \sim 10^5 - 10^6\,\mathrm{m^{-1}} \).  
- **Context / Example Use**:  
  - Axial resolution and coherence length in `/optics/applications/oct`  
- **Related Equations**:  
  - Axial resolution: \( \delta z \approx \dfrac{2\ln 2}{\pi} \dfrac{1}{\Delta k} \)

---

### z — Depth coordinate
- **Symbol**: \( z \)  
- **Name**: Depth / axial coordinate  
- **Definition**: Coordinate along beam propagation direction, used for layer depth in imaging.  
- **SI Units**: \( \mathrm{m} \)  
- **Typical Range**:  
  - OCT, PA imaging in tissues/paintings: \( 10^{-5} - 10^{-2}\,\mathrm{m} \) (10 µm–10 mm)  
- **Context / Example Use**:  
  - A-scan depth profiles in OCT `/optics/applications/oct`  
  - PA initial pressure distribution \( p_0(z) \) in `/optics/applications/pa-imaging`  
- **Related Equations**:  
  - Time-of-flight: \( z = c_s t / 2 \) (for reflection geometries)

---

### \(p(t)\) — Acoustic pressure (time-domain)
- **Symbol**: \( p(t) \) or \( p(\mathbf{r}, t) \)  
- **Name**: Acoustic pressure signal  
- **Definition**: Pressure variation measured by ultrasonic transducer due to photoacoustic or ultrasonic waves.  
- **SI Units**: \( \mathrm{Pa} \)  
- **Typical Range**:  
  - Photoacoustic signals: \( 10^{-3} - 10^{3}\,\mathrm{Pa} \) at detector, depending on fluence and geometry.  
- **Context / Example Use**:  
  - Photoacoustic imaging & spectroscopy in `/optics/applications/pa-imaging` and the PAS / PAI technique pages.  
- **Related Equations**:  
  - Initial pressure: \( p_0(\mathbf{r}) = \Gamma(\mathbf{r}) \mu_a(\mathbf{r}) F(\mathbf{r}) \)  
  - Wave equation: \( \nabla^2 p - \dfrac{1}{c_s^2}\dfrac{\partial^2 p}{\partial t^2} = \text{source} \)

---

### \(\Gamma\) — Grüneisen parameter
- **Symbol**: \( \Gamma \)  
- **Name**: Grüneisen parameter  
- **Definition**: Dimensionless coefficient converting absorbed optical energy density into initial pressure rise in photoacoustics (\( \Gamma = \beta c_s^2 / C_p \)).  
- **SI Units**: Dimensionless  
- **Typical Range**:  
  - Soft tissue and paints: \( \Gamma \sim 0.1 - 1 \)  
- **Context / Example Use**:  
  - Photoacoustic imaging and spectroscopy in `/optics/applications/pa-imaging` and PAS technique page.  
- **Related Equations**:  
  - \( p_0 = \Gamma \mu_a F \)

---

### \(\mu_a\) — Optical absorption coefficient (imaging)
- **Symbol**: \( \mu_a \)  
- **Name**: Absorption coefficient (photoacoustic / diffusive imaging)  
- **Definition**: Same as in Section E, but specifically used to parameterize contrast in PA and diffuse optical imaging.  
- **SI Units**: \( \mathrm{m^{-1}} \)  
- **Typical Range**: See Section E.  
- **Context / Example Use**:  
  - Contrast source in PA imaging `/optics/applications/pa-imaging`  
- **Related Equations**:  
  - \( p_0(\mathbf{r}) = \Gamma(\mathbf{r}) \mu_a(\mathbf{r}) F(\mathbf{r}) \)

---

### \(c_s\) — Speed of sound
- **Symbol**: \( c_s \)  
- **Name**: Speed of sound in medium  
- **Definition**: Propagation speed of acoustic waves in the medium.  
- **SI Units**: \( \mathrm{m\,s^{-1}} \)  
- **Typical Range**:  
  - Air: \( \sim 340\,\mathrm{m\,s^{-1}} \)  
  - Soft tissue / paints / water: \( 1400 - 1700\,\mathrm{m\,s^{-1}} \)  
- **Context / Example Use**:  
  - Time-of-flight to depth conversion in PA imaging `/optics/applications/pa-imaging` and ultrasound-related sections.  
- **Related Equations**:  
  - Travel time: \( t = z / c_s \)  
  - Acoustic wave equation: \( \nabla^2 p - \dfrac{1}{c_s^2}\dfrac{\partial^2 p}{\partial t^2} = 0 \)

---

### F — Optical fluence
- **Symbol**: \( F \) (also written \( \Phi \) in some texts; here we use \( F \) for fluence)  
- **Name**: Optical fluence  
- **Definition**: Time-integrated optical energy delivered per unit area by a pulse or pulse sequence.  
- **SI Units**: \( \mathrm{J\,m^{-2}} \) (often quoted in \( \mathrm{mJ\,cm^{-2}} \))  
- **Typical Range**:  
  - Photoacoustic imaging / spectroscopy: \( 1{-}20\,\mathrm{mJ\,cm^{-2}} \) at the sample  
- **Context / Example Use**:  
  - Initial pressure generation in PAS and PAT, see `/optics/applications/pa-imaging` and photoacoustic technique pages.  
- **Related Equations**:  
  - \( p_0(\mathbf{r}) = \Gamma(\mathbf{r}) \mu_a(\mathbf{r}) F(\mathbf{r}) \)

---

### \(\beta\) — Volumetric thermal expansion coefficient
- **Symbol**: \( \beta \)  
- **Name**: Thermal expansion coefficient (volumetric)  
- **Definition**: Relative change in volume per unit temperature change at constant pressure.  
- **SI Units**: \( \mathrm{K^{-1}} \)  
- **Typical Range**: \( 10^{-5} - 10^{-3}\,\mathrm{K^{-1}} \) for most solids and liquids.  
- **Context / Example Use**:  
  - Enters the Grüneisen parameter \( \Gamma = \beta c_s^2 / C_p \) in photoacoustic physics.  
- **Related Equations**:  
  - \( \Gamma = \beta c_s^2 / C_p \)

---

### \(C_p\) — Specific heat capacity at constant pressure
- **Symbol**: \( C_p \)  
- **Name**: Specific heat capacity (constant pressure)  
- **Definition**: Heat required to raise the temperature of a unit mass by one kelvin at constant pressure.  
- **SI Units**: \( \mathrm{J\,kg^{-1}\,K^{-1}} \)  
- **Typical Range**: \( 10^2 - 10^4\,\mathrm{J\,kg^{-1}\,K^{-1}} \) depending on material.  
- **Context / Example Use**:  
- Appears in \( \Gamma = \beta c_s^2 / C_p \) and in temperature rise estimates in photoacoustic imaging/spectroscopy.  
- **Related Equations**:  
  - \( \Delta T = \dfrac{E_{\text{abs}}}{\rho C_p} \)

---

### BW — Detector bandwidth
- **Symbol**: \( BW \)  
- **Name**: Detector (acoustic) bandwidth  
- **Definition**: Effective frequency range over which an ultrasonic detector or system has significant sensitivity.  
- **SI Units**: \( \mathrm{Hz} \)  
- **Typical Range**: \( 1{-}50\,\mathrm{MHz} \) for PAT / ultrasound arrays.  
- **Context / Example Use**:  
  - Axial resolution in photoacoustic tomography `/optics/applications/pa-imaging`.  
- **Related Equations**:  
  - \( d_{\text{axial}} \approx \dfrac{c_s}{2\,BW} \)

---

### \(f_{\text{center}}\) — Transducer center frequency
- **Symbol**: \( f_{\text{center}} \)  
- **Name**: Center frequency of an ultrasonic transducer  
- **Definition**: Frequency at which the transducer has maximum sensitivity.  
- **SI Units**: \( \mathrm{Hz} \)  
- **Typical Range**: \( 1{-}20\,\mathrm{MHz} \) for typical PAT / ultrasound probes.  
- **Context / Example Use**:  
  - Lateral resolution estimates in photoacoustic tomography `/optics/applications/pa-imaging`.  
- **Related Equations**:  
  - \( d_{\text{lateral}} \approx \dfrac{c_s}{f_{\text{center}}} \)

---

### \(\mu_{\text{eff}}\) — Effective attenuation coefficient
- **Symbol**: \( \mu_{\text{eff}} \)  
- **Name**: Effective attenuation coefficient  
- **Definition**: Combined absorption–scattering coefficient in diffusion theory, often \( \mu_{\text{eff}} = \sqrt{3 \mu_a \mu_s'} \).  
- **SI Units**: \( \mathrm{m^{-1}} \) (often \( \mathrm{cm^{-1}} \))  
- **Typical Range**: \( \mu_{\text{eff}} \sim 1{-}10\,\mathrm{cm^{-1}} \) for turbid media.  
- **Context / Example Use**:  
  - Penetration depth in photoacoustic tomography and diffuse optics `/optics/applications/pa-imaging`.  
- **Related Equations**:  
  - \( z_{\max} \approx 1/\mu_{\text{eff}} \)  
  - \( \mu_{\text{eff}} = \sqrt{3 \mu_a \mu_s'} \)

---

### \(\mu_s'\) — Reduced scattering coefficient
- **Symbol**: \( \mu_s' \)  
- **Name**: Reduced scattering coefficient  
- **Definition**: Effective scattering coefficient that accounts for anisotropy: \( \mu_s' = \mu_s (1-g) \).  
- **SI Units**: \( \mathrm{m^{-1}} \) (often \( \mathrm{cm^{-1}} \))  
- **Typical Range**: \( \mu_s' \sim 10 - 100\,\mathrm{cm^{-1}} \) for many turbid media (tissues, paints).  
- **Context / Example Use**:  
  - Diffusion approximation and PAT penetration depth `/optics/interactions/turbid-media`, `/optics/applications/pa-imaging`.  
- **Related Equations**:  
  - \( \mu_s' = \mu_s (1-g) \)  
  - \( \mu_{\text{eff}} = \sqrt{3 \mu_a \mu_s'} \)

---

### \(\alpha_{\text{US}}\) — Ultrasound attenuation coefficient
- **Symbol**: \( \alpha_{\text{US}} \)  
- **Name**: Ultrasound attenuation coefficient  
- **Definition**: Rate of acoustic amplitude reduction per unit distance and frequency.  
- **SI Units**: Commonly \( \mathrm{dB/(cm\cdot MHz)} \); in linear units, \( \mathrm{Np\,m^{-1}} \).  
- **Typical Range**:  
- Soft tissue: \( 0.5{-}1\,\mathrm{dB/(cm\cdot MHz)} \); wood / dense media: \( \lesssim 0.1{-}1\,\mathrm{dB/(cm\cdot MHz)} \).  
- **Context / Example Use**:  
  - Limits PAT penetration depth in `/optics/applications/pa-imaging`.  
- **Related Equations**:  
  - Acoustic penetration (linear units): \( z_{\text{acoustic}} \approx 1/\alpha_{\text{US}} \)

---

### Cross-linking and Usage Notes

- Whenever a variable appears on an **optics page** (e.g. `/optics/fundamentals/*`, `/optics/wave_optics/*`, `/optics/applications/*`) or a **technique page** (e.g. Raman, OCT, PA imaging, PAS), its meaning follows the closest matching definition from this dictionary.  
- If a symbol is **overloaded** (e.g. \( \phi, L, n, k \)), each page should clarify in the local text which meaning is in force and, when needed, link back to this file for disambiguation:
  - Example: “Here \( \phi \) denotes **phase** (see *Section C — Wave Optics Variables* in `VARIABLES.md`).”
- When adding new equations or pages, **extend this dictionary first** if a new symbol is introduced, then reference it from the page.


