---
title: "Foundations of Optics: Deep Dive"
slug: "01-foundations-of-optics-deep"
category: "Fundamentals"
---

# Foundations of Optics: Deep Dive

This comprehensive guide covers the fundamental principles of optical physics, bridging the gap between undergraduate and graduate-level understanding. We begin with electromagnetic wave theory and progress through polarization, coherence, Gaussian beams, and geometric optics foundations.

---

## Section 1: Basic Wave Optics (Module 1.1)

### 1.1 Electromagnetic Wave Derivation

Electromagnetic waves arise naturally as solutions to Maxwell's equations, which describe how electric and magnetic fields interact. The complete set of Maxwell's equations in their differential form are:

**Gauss's Law (Electric):**
$$\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$$

**Gauss's Law (Magnetic):**
$$\nabla \cdot \vec{B} = 0$$

**Faraday's Law:**
$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$

**Ampère's Law (with displacement current):**
$$\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$$

In free space, where there are no charges ($\rho = 0$) or currents ($\vec{J} = 0$), these simplify to:

$$\nabla \cdot \vec{E} = 0, \quad \nabla \cdot \vec{B} = 0$$

$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{B} = \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$$

To derive the wave equation, we take the curl of Faraday's law:

$$\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B}) = -\mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

Using the vector identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$ and noting that $\nabla \cdot \vec{E} = 0$ in free space, we obtain the three-dimensional wave equation:

$$\nabla^2 \vec{E} - \mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2} = 0$$

The magnetic field $\vec{B}$ satisfies an identical wave equation. The wave speed is determined by the material constants:

$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$$

which, in vacuum, equals approximately $3 \times 10^8$ m/s—the speed of light.

**Plane Wave Solution:**

The simplest solution to the wave equation is a plane wave, which has constant amplitude and phase on planes perpendicular to the propagation direction:

$$\vec{E}(\vec{r}, t) = \vec{E}_0 e^{i(\vec{k} \cdot \vec{r} - \omega t)}, \quad \vec{B} = \frac{1}{\omega} \vec{k} \times \vec{E}$$

Here, $\vec{k}$ is the wave vector, and its magnitude is $|\vec{k}| = k = \omega/c$, where $\omega$ is the angular frequency. The wave vector points in the direction of propagation, and its magnitude is related to the wavelength by $k = 2\pi/\lambda$.

### 1.2 Polarization

Polarization describes the orientation and time evolution of the electric field vector as a wave propagates. Understanding polarization is crucial for many optical applications, from 3D cinema to fiber-optic communications.

**Linear Polarization:** The electric field $\vec{E}$ oscillates in a single plane perpendicular to the propagation direction. This is the simplest form of polarization.

**Circular Polarization:** The electric field rotates in a circle as the wave propagates:

$$\vec{E}(t) = E_0(\hat{x} \cos \omega t + \hat{y} \sin \omega t)$$

Circular polarization can be right-handed or left-handed, depending on the rotation direction relative to the propagation direction.

**Elliptical Polarization:** This is the most general form, where the electric field traces an ellipse. Circular and linear polarizations are special cases of elliptical polarization.

**Jones Vector Representation:**

The Jones calculus provides a convenient matrix method for describing fully polarized light. The electric field is represented as a two-component complex vector:

$$\vec{E} = \begin{bmatrix} E_x \\ E_y \end{bmatrix} e^{i\omega t}$$

Optical elements are represented by $2 \times 2$ matrices. For example, a linear polarizer that transmits only the $x$-component is:

$$J_{\text{pol}} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$

**Mueller Calculus and Stokes Parameters:**

For partially polarized or unpolarized light, the Mueller calculus is more appropriate. It uses the four-component Stokes vector:

$$\vec{S} = \begin{bmatrix} S_0 \\ S_1 \\ S_2 \\ S_3 \end{bmatrix}$$

where $S_0$ represents the total intensity, $S_1$ and $S_2$ describe linear polarization, and $S_3$ describes circular polarization. This formalism can handle any degree of polarization, from fully polarized to completely unpolarized light.

### 1.3 Refractive Index & Dispersion

The refractive index is one of the most fundamental optical properties of a material. It determines how light propagates through the medium and how it bends at interfaces.

**Complex Refractive Index:**

In general, the refractive index is complex: $n = n' + ik$, where:

- The real part $n'$ determines the phase velocity: $v_p = c/n'$. This is what we typically call "the refractive index" in everyday contexts.
- The imaginary part $k$ (the extinction coefficient) determines absorption. When $k > 0$, the wave amplitude decreases exponentially as it propagates.

**Phase and Group Velocity:**

For a wave packet (a superposition of waves with slightly different frequencies), two velocities are important:

- **Phase velocity** $v_p = \omega/k$: The speed at which individual wave crests move.
- **Group velocity** $v_g = d\omega/dk$: The speed at which the envelope (or information) travels.

In most materials, $v_g < v_p < c$, and the group velocity is what we observe when measuring the speed of light pulses.

**Dispersion and the Sellmeier Equation:**

The refractive index depends on wavelength—this is called dispersion. For optical glasses, the Sellmeier equation provides an accurate empirical model:

$$n^2(\lambda) = 1 + \sum_{i=1}^3 \frac{B_i \lambda^2}{\lambda^2 - C_i}$$

where $B_i$ and $C_i$ are material-specific coefficients. This equation captures the normal dispersion behavior where $n$ decreases with increasing wavelength (except near absorption resonances).

### 1.4 Interference & Coherence

Interference is the hallmark of wave behavior and is fundamental to many optical techniques, from interferometry to holography.

**Temporal Coherence:**

Temporal coherence describes how well a wave can interfere with a time-delayed version of itself. The coherence time $\tau_c$ and coherence length $l_c$ are related by:

$$l_c = c\tau_c, \quad \tau_c = \frac{1}{\Delta\nu}$$

where $\Delta\nu$ is the spectral bandwidth. A perfectly monochromatic source has infinite coherence length, while a broadband source has very short coherence length.

**Two-Beam Interference:**

When two waves of the same frequency interfere, the resulting intensity depends on their phase difference:

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2} \cos \delta, \quad \delta = \frac{2\pi \Delta L}{\lambda}$$

where $\Delta L$ is the path difference. The interference term $2\sqrt{I_1 I_2} \cos \delta$ oscillates between constructive and destructive interference as the path difference changes.

**Mutual Coherence Function:**

For partially coherent light, the mutual coherence function $\Gamma_{12}(\tau)$ quantifies the correlation between the electric fields at two points:

$$\Gamma_{12}(\tau) = \langle E_1(t) E_2^*(t+\tau) \rangle$$

where the angle brackets denote time averaging. This function is central to coherence theory and determines the visibility of interference fringes.

### 1.5 Gaussian Beams

Gaussian beams are the natural modes of laser cavities and are fundamental to laser optics. Unlike plane waves, they have a finite beam waist and diffract as they propagate.

**Paraxial Wave Equation:**

In the paraxial approximation (where the beam makes small angles with the optical axis), the wave equation simplifies to:

$$\nabla_T^2 u - 2ik \frac{\partial u}{\partial z} = 0$$

where $\nabla_T^2$ is the transverse Laplacian.

**Solution (TEM$_{00}$ Mode):**

The fundamental Gaussian beam mode (TEM$_{00}$) has the form:

$$u(r,z) = \frac{w_0}{w(z)} \exp\left(-\frac{r^2}{w^2(z)}\right) \exp\left(-ikz - ik\frac{r^2}{2R(z)} + i\zeta(z)\right)$$

**Beam Parameters:**

The beam width $w(z)$ expands as:

$$w(z) = w_0 \sqrt{1 + (z/z_R)^2}$$

where $w_0$ is the beam waist (minimum width) and $z_R$ is the Rayleigh range. The wavefront radius of curvature is:

$$R(z) = z[1 + (z_R/z)^2]$$

The Rayleigh range is:

$$z_R = \frac{\pi w_0^2}{\lambda}$$

This is the distance over which the beam area doubles. Beyond the Rayleigh range, the beam diverges approximately linearly.

**ABCD Law for Gaussian Beams:**

Gaussian beams transform through optical systems according to the ABCD law, which relates the complex beam parameter $q(z) = z + iz_R$ before and after an optical element:

$$q_2 = \frac{Aq_1 + B}{Cq_1 + D}$$

where the ABCD matrix describes the optical system. This elegant formalism allows complex optical systems to be analyzed systematically.

### 1.6 Energy Flow

Understanding how energy flows in electromagnetic waves is essential for calculating intensities, power, and efficiency in optical systems.

**Poynting Vector:**

The Poynting vector $\vec{S}$ represents the direction and magnitude of energy flow:

$$\vec{S} = \vec{E} \times \vec{H}$$

For time-harmonic fields, the time-averaged Poynting vector is:

$$\langle \vec{S} \rangle = \frac{1}{2}\text{Re}[\vec{E} \times \vec{H}^*]$$

**Intensity:**

The intensity $I$ is the magnitude of the Poynting vector: $I = |\vec{S}|$. For a plane wave in a dielectric, this is proportional to $|E|^2$, with the constant of proportionality depending on the material properties. This relationship is fundamental to understanding how optical power scales with field amplitude.

---

## Section 2: Geometrical Optics Essentials (Module 1.2)

Geometrical optics provides a powerful approximation to wave optics when the wavelength is much smaller than the relevant length scales. It describes light as rays that travel in straight lines (in uniform media) and bend at interfaces according to simple rules.

### 2.1 Fermat's Principle

Fermat's principle is the fundamental law of geometrical optics. It states that light travels along the path that minimizes (or more precisely, makes stationary) the optical path length.

**Optical Path Length:**

The optical path length (OPL) is defined as:

$$\text{OPL} = \int_A^B n(\vec{r}) \, ds$$

where the integral is taken along the ray path from point $A$ to point $B$, and $n(\vec{r})$ is the refractive index at each point along the path.

**Stationary Path Condition:**

Fermat's principle states that the actual path taken by light makes the OPL stationary:

$$\delta \int_A^B n(\vec{r}) \, ds = 0$$

This variational principle is equivalent to all the laws of geometrical optics.

**Derivation of Snell's Law:**

Applying Fermat's principle to a ray crossing a planar interface between two media with refractive indices $n_1$ and $n_2$ leads directly to Snell's law:

$$n_1 \sin \theta_1 = n_2 \sin \theta_2$$

where $\theta_1$ and $\theta_2$ are the angles of incidence and refraction, measured from the surface normal. This elegant result explains why light bends when entering a different medium.

### 2.2 Eikonal Equation

The eikonal equation connects wave optics to ray optics through the high-frequency (short-wavelength) limit.

**Derivation:**

Starting from the wave equation and taking the limit where the wavelength approaches zero, we obtain the eikonal equation:

$$|\nabla S(\vec{r})|^2 = n^2(\vec{r})$$

where $S(\vec{r})$ is the eikonal function, which represents the phase of the wave in the geometric optics limit.

**Physical Interpretation:**

The eikonal equation shows that:
- The surfaces of constant $S$ are the wavefronts.
- The gradient $\nabla S$ points in the direction of the rays.
- The magnitude of $\nabla S$ equals the local refractive index.

**Ray Direction:**

The unit vector tangent to a ray is:

$$\hat{t} = \frac{\nabla S}{|\nabla S|}$$

This means rays are always perpendicular to wavefronts, providing a geometric picture of wave propagation.

### 2.3 Paraxial Ray Optics & ABCD Matrices

The paraxial approximation simplifies optical system analysis by assuming all rays make small angles with the optical axis. This leads to linear relationships that can be expressed using matrix methods.

**Ray Vector:**

A ray is described by its height $y$ above the optical axis and its angle $\theta$ relative to the axis:

$$\begin{bmatrix} y \\ \theta \end{bmatrix}$$

**Free Space Propagation:**

A ray traveling a distance $L$ in free space (or uniform medium) transforms as:

$$M = \begin{bmatrix} 1 & L \\ 0 & 1 \end{bmatrix}$$

This matrix simply adds $L \theta$ to the height while keeping the angle unchanged.

**Thin Lens:**

A thin lens of focal length $f$ changes the ray angle according to:

$$M = \begin{bmatrix} 1 & 0 \\ -1/f & 1 \end{bmatrix}$$

The negative sign indicates that a converging lens (positive $f$) decreases the ray angle for positive heights.

**System Matrix:**

For a system of multiple elements, the total transformation is found by multiplying the individual matrices in reverse order:

$$M_{\text{total}} = M_2 \cdot M_{\text{space}} \cdot M_1$$

For example, with two lenses separated by distance $d$, we multiply the lens matrices with a free-space matrix between them. This matrix method makes complex optical systems tractable to analyze.

### 2.4 Cardinal Points

The cardinal points provide a complete description of any optical system's imaging properties, even without knowing the internal details.

**Principal Planes ($H_1$, $H_2$):** These are reference planes where refraction appears to occur for a thick lens or complex system. They allow a thick system to be treated as a thin lens.

**Focal Points ($F$, $F'$):** The object-space and image-space focal points. Parallel rays entering the system converge to (or appear to diverge from) these points.

**Nodal Points ($N$, $N'$):** Points where rays appear to pass through undeviated. For systems in air, the nodal points coincide with the principal points.

**Imaging Formula:**

Using the cardinal points, the imaging relationship becomes:

$$\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}, \quad M = -\frac{s'}{s}$$

where $s$ and $s'$ are measured from the principal planes, $f$ is the focal length, and $M$ is the magnification. This is the familiar thin-lens equation, but it applies to any optical system when distances are measured from the appropriate cardinal points.

### 2.5 Optical Invariants

Certain quantities are conserved as light propagates through an optical system, providing powerful constraints and simplifications.

**Lagrange Invariant:**

The Lagrange invariant (also called the optical invariant) is:

$$H = n y \sin \theta = \text{constant along optical system}$$

This quantity remains unchanged as a ray propagates through any rotationally symmetric optical system. It relates the object and image heights and angles, and is fundamental to understanding field of view and magnification limits.

**Conservation of Étendue:**

Étendue (also called throughput or light-gathering power) is conserved in lossless optical systems:

$$n^2 A \Omega = \text{constant}$$

where $A$ is the area and $\Omega$ is the solid angle. This fundamental limit means you cannot increase both the area and the angular spread of a light beam simultaneously—there's no free lunch in optics. This principle limits the brightness of images and the efficiency of light collection systems.

### 2.6 Stops, Pupils & Telecentricity

Understanding how optical systems control the cone of rays is essential for designing systems with the desired field of view and resolution.

**Aperture Stop:** The physical opening that limits the cone of rays from an on-axis object point. It determines the system's light-gathering power and affects depth of field.

**Field Stop:** The opening that limits the angular extent of the object that can be imaged. It determines the field of view.

**Entrance and Exit Pupils:** These are the images of the aperture stop, as seen from object space and image space, respectively. They are the effective apertures that determine the ray bundles entering and leaving the system.

**Telecentric Systems:**

In a telecentric system, the chief rays (rays passing through the center of the aperture stop) are parallel to the optical axis. This has important advantages:

- **Object-space telecentricity:** The magnification doesn't change with object distance, which is crucial for metrology and machine vision.
- **Image-space telecentricity:** The exit pupil is at infinity, which is important for sensors and fiber coupling.

**Ray Diagram Example:**

```
          |\
          | \
   Object |  \  Chief Ray
          |   \
          |    \
          O-----Aperture Stop
```

This simple diagram illustrates how the aperture stop limits the cone of rays from an object point, with the chief ray passing through the center of the stop.

---

*This completes the detailed coverage of Modules 1.1 and 1.2, providing the essential foundations for understanding both wave and geometric optics.*
