# Foundations of Optics: A Comprehensive Study Guide

## Introduction

This study guide provides a rigorous treatment of the fundamental principles of optics, bridging undergraduate and graduate-level physics. The material is organized into two major sections: Basic Wave Optics and Geometrical Optics Essentials. Each section includes detailed derivations, physical intuition, and connections to classical optical theory.

---

# SECTION 1 — BASIC WAVE OPTICS (Module 1.1)

## 1.1 Electromagnetic Foundations

### 1.1.1 Maxwell's Equations and the Wave Equation

The foundation of classical optics rests on Maxwell's equations, which describe how electric and magnetic fields interact. In a source-free region ($\rho = 0$, $\mathbf{J} = 0$), Maxwell's equations in vacuum are:

**Gauss's Law (Electric):**
$$\nabla \cdot \mathbf{E} = 0$$

**Gauss's Law (Magnetic):**
$$\nabla \cdot \mathbf{B} = 0$$

**Faraday's Law:**
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

**Ampère's Law (with displacement current):**
$$\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

To derive the wave equation, we take the curl of Faraday's law:

$$\nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t}(\nabla \times \mathbf{B})$$

Using the vector identity $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ and substituting from Ampère's law:

$$\nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E} = -\mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$

Since $\nabla \cdot \mathbf{E} = 0$ in vacuum, we obtain the **3D electromagnetic wave equation**:

$$\nabla^2 \mathbf{E} - \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0$$

Similarly, for the magnetic field:

$$\nabla^2 \mathbf{B} - \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{B}}{\partial t^2} = 0$$

The speed of light in vacuum is:

$$c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} \approx 2.998 \times 10^8 \text{ m/s}$$

**Physical Interpretation:** These equations show that electric and magnetic fields propagate as waves through space. The fields are coupled: a changing electric field generates a magnetic field (Ampère's law), and a changing magnetic field generates an electric field (Faraday's law). This mutual generation sustains the wave propagation.

### 1.1.2 Plane Wave Solutions

A **plane wave** is the simplest solution to the wave equation. For a wave propagating in the $z$-direction:

$$\mathbf{E}(\mathbf{r}, t) = \mathbf{E}_0 e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)}$$

where:
- $\mathbf{k} = k\hat{\mathbf{z}}$ is the wave vector ($k = 2\pi/\lambda = \omega/c$)
- $\omega = 2\pi\nu$ is the angular frequency
- $\mathbf{E}_0$ is the complex amplitude vector

The physical field is the real part: $\text{Re}[\mathbf{E}(\mathbf{r}, t)]$.

**Dispersion relation:**
$$\omega = ck$$

For a wave in a medium with refractive index $n$:
$$\omega = \frac{ck}{n}$$

**Transverse nature:** From $\nabla \cdot \mathbf{E} = 0$, we find $\mathbf{k} \cdot \mathbf{E}_0 = 0$, meaning the electric field is perpendicular to the propagation direction. Similarly, $\mathbf{B}$ is also transverse and perpendicular to $\mathbf{E}$.

**Magnetic field relation:**
$$\mathbf{B} = \frac{1}{\omega}\mathbf{k} \times \mathbf{E} = \frac{1}{c}\hat{\mathbf{k}} \times \mathbf{E}$$

### 1.1.3 Spherical Waves

For a point source, the wavefronts are spherical. The solution is:

$$E(r, t) = \frac{E_0}{r} e^{i(kr - \omega t)}$$

where $r$ is the distance from the source. The $1/r$ factor ensures energy conservation (intensity $\propto 1/r^2$).

**Near-field vs. far-field:**
- Near field: $r \ll \lambda$ (evanescent waves, complex behavior)
- Far field: $r \gg \lambda$ (spherical wave approximation valid)

### 1.1.4 Boundary Conditions at Interfaces

At an interface between two media, the fields must satisfy boundary conditions derived from Maxwell's equations:

**Tangential E-field:**
$$E_{1t} = E_{2t}$$

**Tangential H-field:**
$$H_{1t} = H_{2t} \quad \text{(if no surface current)}$$

**Normal D-field:**
$$D_{1n} - D_{2n} = \sigma_{\text{free}}$$

**Normal B-field:**
$$B_{1n} = B_{2n}$$

These conditions determine the reflection and transmission coefficients (Fresnel equations) and are fundamental to understanding refraction, reflection, and total internal reflection.

### 1.1.5 Polarization States

**Linear polarization:** Electric field oscillates in a fixed direction:
$$\mathbf{E} = E_0 (\cos\theta \hat{\mathbf{x}} + \sin\theta \hat{\mathbf{y}}) e^{i(kz - \omega t)}$$

**Circular polarization:** Two orthogonal components with $\pi/2$ phase difference:
$$\mathbf{E} = \frac{E_0}{\sqrt{2}} (\hat{\mathbf{x}} \pm i\hat{\mathbf{y}}) e^{i(kz - \omega t)}$$

The $+$ sign gives right-circular (RCP), $-$ gives left-circular (LCP).

**Elliptical polarization:** General case with arbitrary phase difference and amplitude ratio.

### 1.1.6 Jones Vectors and Matrices

**Jones vector** represents fully polarized light as a 2D complex vector:

$$\mathbf{J} = \begin{pmatrix} E_x e^{i\phi_x} \\ E_y e^{i\phi_y} \end{pmatrix} = \begin{pmatrix} J_x \\ J_y \end{pmatrix}$$

**Normalized examples:**
- Horizontal: $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$
- Vertical: $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$
- 45°: $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$
- RCP: $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix}$
- LCP: $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix}$

**Jones matrices** describe polarization-changing elements:

**Linear polarizer (horizontal):**
$$\mathbf{M} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$$

**Quarter-wave plate (fast axis horizontal):**
$$\mathbf{M} = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

**Rotation matrix:**
$$\mathbf{R}(\theta) = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}$$

**Output:** $\mathbf{J}_{\text{out}} = \mathbf{M} \mathbf{J}_{\text{in}}$

### 1.1.7 Mueller Calculus

For partially polarized light, we use **Stokes parameters**:

$$\mathbf{S} = \begin{pmatrix} S_0 \\ S_1 \\ S_2 \\ S_3 \end{pmatrix} = \begin{pmatrix} I \\ I_H - I_V \\ I_{+45} - I_{-45} \\ I_R - I_L \end{pmatrix}$$

where $I$ is total intensity, subscripts indicate polarization components.

**Mueller matrix** (4×4) describes polarization-changing elements:
$$\mathbf{S}_{\text{out}} = \mathbf{M} \mathbf{S}_{\text{in}}$$

**Degree of polarization:**
$$P = \frac{\sqrt{S_1^2 + S_2^2 + S_3^2}}{S_0}$$

## 1.2 Refractive Index & Dispersion

### 1.2.1 Phase and Group Velocity

**Phase velocity:** Speed at which wavefronts (surfaces of constant phase) propagate:
$$v_p = \frac{\omega}{k} = \frac{c}{n}$$

**Group velocity:** Speed at which wave packets (information, energy) propagate:
$$v_g = \frac{d\omega}{dk} = \frac{c}{n + \omega \frac{dn}{d\omega}} = \frac{c}{n_g}$$

where $n_g = n - \lambda \frac{dn}{d\lambda}$ is the group index.

**Physical significance:** In dispersive media, different frequencies travel at different speeds. The group velocity represents the speed of the envelope of a wave packet, while phase velocity is the speed of individual wavefronts.

### 1.2.2 Dispersion Relations

**Normal dispersion:** $dn/d\lambda < 0$ (most common, visible to IR)

**Anomalous dispersion:** $dn/d\lambda > 0$ (near absorption resonances)

**Dispersion relation** connects frequency and wave number:
$$\omega = \omega(k)$$

For non-dispersive medium: $\omega = ck/n$ (linear).

For dispersive medium: $\omega(k)$ is nonlinear, leading to pulse broadening.

### 1.2.3 Sellmeier Equation

Most accurate model for transparent materials:

$$n^2(\lambda) = 1 + \sum_{i=1}^{N} \frac{B_i \lambda^2}{\lambda^2 - C_i}$$

where $B_i$ and $C_i$ are material-specific coefficients. Typically $N=3$ for glasses (three resonances: UV, visible, IR).

**Example (BK7 glass):**
$$n^2 = 1 + \frac{1.03961212 \lambda^2}{\lambda^2 - 0.00600069867} + \frac{0.231792344 \lambda^2}{\lambda^2 - 0.0200179144} + \frac{1.01046945 \lambda^2}{\lambda^2 - 103.560653}$$

### 1.2.4 Cauchy Equation

Simpler model, valid for limited wavelength ranges:

$$n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4} + \cdots$$

Good approximation away from resonances.

### 1.2.5 Complex Refractive Index and Absorption

When absorption is present, the refractive index becomes complex:

$$\tilde{n} = n + i\kappa$$

where:
- $n$ = real part (phase velocity)
- $\kappa$ = extinction coefficient (absorption)

**Wave in absorbing medium:**
$$E(z,t) = E_0 e^{i(kz - \omega t)} = E_0 e^{i(\tilde{n} k_0 z - \omega t)} = E_0 e^{-\kappa k_0 z} e^{i(n k_0 z - \omega t)}$$

The intensity decays as:
$$I(z) = I_0 e^{-\alpha z}$$

where $\alpha = 2\kappa k_0 = \frac{4\pi \kappa}{\lambda}$ is the absorption coefficient.

**Beer's law:** $I = I_0 e^{-\alpha z}$ describes exponential attenuation.

### 1.2.6 Kramers-Kronig Relations

These fundamental relations connect the real and imaginary parts of the complex refractive index:

$$n(\omega) - 1 = \frac{2}{\pi} \mathcal{P} \int_0^{\infty} \frac{\omega' \kappa(\omega')}{\omega'^2 - \omega^2} d\omega'$$

$$\kappa(\omega) = -\frac{2\omega}{\pi} \mathcal{P} \int_0^{\infty} \frac{n(\omega') - 1}{\omega'^2 - \omega^2} d\omega'$$

where $\mathcal{P}$ denotes the Cauchy principal value.

**Physical interpretation:** Causality (no response before stimulus) requires that absorption and dispersion are not independent. If you know the absorption spectrum, you can calculate the dispersion, and vice versa. This is a manifestation of the fact that the real and imaginary parts of any causal response function are Hilbert transform pairs.

## 1.3 Interference & Coherence

### 1.3.1 Temporal Coherence

**Coherence time:** $\tau_c$ - time over which the phase remains predictable.

**Coherence length:** $l_c = c\tau_c = \frac{\lambda^2}{\Delta\lambda}$

where $\Delta\lambda$ is the spectral bandwidth.

**Physical meaning:** Two points separated by more than $l_c$ have uncorrelated phases. For interference to occur, the path difference must be $< l_c$.

### 1.3.2 Spatial Coherence

**Coherence area:** Region over which the field is correlated.

**Van Cittert-Zernike theorem:** Spatial coherence from an extended source:
$$\gamma_{12} = \frac{\iint I(\xi, \eta) e^{ik(\mathbf{r}_1 - \mathbf{r}_2) \cdot \hat{\mathbf{s}}} d\xi d\eta}{\iint I(\xi, \eta) d\xi d\eta}$$

where $I(\xi, \eta)$ is the source intensity distribution.

**Coherence width:** For a circular source of angular size $\theta$:
$$d_c \approx \frac{\lambda}{\theta}$$

### 1.3.3 Mutual Coherence Function

**Mutual coherence:**
$$\Gamma_{12}(\tau) = \langle U_1(t) U_2^*(t+\tau) \rangle$$

**Complex degree of coherence:**
$$\gamma_{12}(\tau) = \frac{\Gamma_{12}(\tau)}{\sqrt{\Gamma_{11}(0) \Gamma_{22}(0)}}$$

**Properties:**
- $|\gamma_{12}(\tau)| \leq 1$
- $\gamma_{12}(0) = 1$ for fully coherent
- $\gamma_{12}(0) = 0$ for fully incoherent

### 1.3.4 Two-Beam Interference

**Intensity pattern:**
$$I = I_1 + I_2 + 2\sqrt{I_1 I_2} |\gamma_{12}(\tau)| \cos(\phi_1 - \phi_2 + \arg[\gamma_{12}(\tau)])$$

**Visibility (fringe contrast):**
$$V = \frac{I_{\text{max}} - I_{\text{min}}}{I_{\text{max}} + I_{\text{min}}} = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2} |\gamma_{12}(\tau)|$$

**Maximum visibility:** $V = 1$ when $I_1 = I_2$ and $|\gamma_{12}| = 1$ (fully coherent, equal intensities).

**Young's double slit:** Classic example where $|\gamma_{12}|$ determines fringe visibility.

## 1.4 Diffraction Overview

### 1.4.1 Huygens-Fresnel Principle

**Huygens' principle:** Every point on a wavefront acts as a secondary source of spherical waves.

**Fresnel's addition:** The field at a point is the coherent superposition of all secondary wavelets, with proper phase and amplitude.

**Mathematical form:**
$$U(P) = \frac{1}{i\lambda} \iint U_0(Q) \frac{e^{ikr}}{r} K(\theta) dS$$

where $K(\theta)$ is the obliquity factor (typically $\cos\theta$).

### 1.4.2 Fresnel vs Fraunhofer Diffraction

**Fresnel number:**
$$N_F = \frac{a^2}{\lambda z}$$

**Fresnel diffraction:** $N_F \gg 1$ (near field)
- Wavefront curvature important
- Complex intensity patterns
- Near-field effects

**Fraunhofer diffraction:** $N_F \ll 1$ (far field)
- Wavefronts approximately plane
- Simpler patterns (Fourier transform of aperture)
- Far-field approximation

**Transition:** Occurs when $z \approx a^2/\lambda$.

### 1.4.3 Physical Interpretation of Diffraction Limits

**Rayleigh criterion:** Two point sources are just resolved when the first minimum of one Airy disk coincides with the center of the other:

$$\theta_{\text{min}} = 1.22 \frac{\lambda}{D}$$

where $D$ is the aperture diameter.

**Spatial resolution:**
$$\delta x = 1.22 \frac{\lambda f}{D} = 1.22 \frac{\lambda}{\text{NA}}$$

where NA is the numerical aperture.

**Physical origin:** Diffraction arises from the finite size of the aperture. Even a perfect lens cannot focus light to a point - the wave nature of light sets a fundamental limit.

### 1.4.4 Airy Patterns

For a circular aperture, the intensity pattern is:

$$I(\theta) = I_0 \left[\frac{2J_1(ka\sin\theta)}{ka\sin\theta}\right]^2$$

where $J_1$ is the first-order Bessel function.

**Airy disk radius:** First zero at $\theta = 1.22\lambda/D$.

**Energy distribution:** 84% of energy in central disk, 16% in rings.

## 1.5 Gaussian Optics Introduction

### 1.5.1 Paraxial Wave Equation

Starting from the scalar wave equation and assuming a beam-like solution:

$$U(x,y,z) = A(x,y,z) e^{ikz}$$

Substituting into the wave equation and using the paraxial approximation ($\partial^2 A/\partial z^2 \ll k \partial A/\partial z$):

$$-2ik \frac{\partial A}{\partial z} + \nabla_T^2 A = 0$$

where $\nabla_T^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2$ is the transverse Laplacian.

### 1.5.2 Gaussian Beam Solution

The fundamental solution is a **Gaussian beam**:

$$U(r,z) = \frac{w_0}{w(z)} \exp\left[-\frac{r^2}{w^2(z)}\right] \exp\left[i\left(kz + \frac{kr^2}{2R(z)} - \psi(z)\right)\right]$$

where:
- $w_0$ = beam waist radius
- $w(z) = w_0\sqrt{1 + (z/z_R)^2}$ = beam radius
- $R(z) = z[1 + (z_R/z)^2]$ = wavefront radius
- $\psi(z) = \arctan(z/z_R)$ = Gouy phase
- $z_R = \pi w_0^2/\lambda$ = Rayleigh range

### 1.5.3 Complex Beam Parameter

**Complex beam parameter:**
$$q(z) = z + iz_R$$

**Reciprocal:**
$$\frac{1}{q(z)} = \frac{1}{R(z)} - i \frac{\lambda}{\pi w^2(z)}$$

**Propagation:**
$$q(z) = q_0 + z$$

where $q_0 = iz_R$ at the waist.

### 1.5.4 ABCD Law for Gaussian Beams

**Transformation through optical system:**
$$q_2 = \frac{Aq_1 + B}{Cq_1 + D}$$

where $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is the ray transfer matrix.

This elegant result connects ray optics (ABCD matrices) to wave optics (Gaussian beams).

## 1.6 Energy Flow

### 1.6.1 Poynting Vector

**Poynting vector** represents energy flux:

$$\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B} = \vec{E} \times \vec{H}$$

**Time-averaged (for harmonic fields):**
$$\langle \vec{S} \rangle = \frac{1}{2}\text{Re}(\vec{E} \times \vec{H}^*)$$

**For plane wave:**
$$|\langle \vec{S} \rangle| = \frac{1}{2} \epsilon_0 c n |E_0|^2 = I$$

### 1.6.2 Intensity vs Irradiance

**Intensity:** Power per unit area (often used interchangeably with irradiance).

**Irradiance:** $E = d\Phi/dA$ [W/m²] - power incident per unit area.

**Radiant exitance:** $M = d\Phi/dA$ [W/m²] - power emitted per unit area.

**Physical distinction:** Intensity often refers to power per unit solid angle, while irradiance is power per unit area. In optics, "intensity" commonly means power per unit area.

### 1.6.3 Relationship Between Fields and Measurable Quantities

**Photodetector response:** Typically proportional to $|E|^2$ (intensity), not $E$ directly.

**Coherent detection:** Can measure $E$ directly using interferometry.

**Energy density:**
$$u = \frac{1}{2}\epsilon_0 |E|^2 + \frac{1}{2\mu_0}|B|^2 = \epsilon_0 |E|^2$$

**Energy flux:** $|\vec{S}| = cu$ (for plane wave in vacuum).

---

# SECTION 2 — GEOMETRICAL OPTICS ESSENTIALS (Module 1.2)

## 2.1 Fermat's Principle

### 2.1.1 Principle of Stationary Optical Path Length

**Fermat's principle:** Light travels along the path that makes the optical path length stationary (usually a minimum):

$$\delta \int n(\mathbf{r}) \, ds = 0$$

**Optical path length (OPL):**
$$\text{OPL} = \int_{\text{path}} n(\mathbf{r}) \, ds$$

**Physical interpretation:** Among all possible paths between two points, light chooses the one that takes the least time (or, more precisely, makes the time stationary). This is the optical analog of the principle of least action in mechanics.

### 2.1.2 Derivation of Snell's Law

Consider a ray crossing an interface at point $P$:

```
        Medium 1 (n₁)
        ════════════════ Interface
                        Medium 2 (n₂)
```

The optical path length is:
$$\text{OPL} = n_1 \sqrt{x^2 + y_1^2} + n_2 \sqrt{(L-x)^2 + y_2^2}$$

Minimizing with respect to $x$:
$$\frac{d(\text{OPL})}{dx} = \frac{n_1 x}{\sqrt{x^2 + y_1^2}} - \frac{n_2 (L-x)}{\sqrt{(L-x)^2 + y_2^2}} = 0$$

This gives:
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

**Snell's law!** Fermat's principle directly yields the law of refraction.

### 2.1.3 Connection to Wave Optics: Eikonal Approximation

In the limit $\lambda \to 0$ (geometric optics), the wave equation reduces to the **eikonal equation**:

$$(\nabla S)^2 = n^2(\mathbf{r})$$

where $S(\mathbf{r})$ is the eikonal (optical path length function).

**Rays** are curves perpendicular to surfaces of constant $S$ (wavefronts):
$$\frac{d}{ds}\left(n \frac{d\mathbf{r}}{ds}\right) = \nabla n$$

This is equivalent to Fermat's principle. The eikonal approximation bridges wave and ray optics.

## 2.2 Eikonal Equation

### 2.2.1 Derivation

Starting from the scalar wave equation:
$$\nabla^2 U - \frac{n^2}{c^2} \frac{\partial^2 U}{\partial t^2} = 0$$

Assume solution: $U(\mathbf{r}, t) = A(\mathbf{r}) e^{i[k_0 S(\mathbf{r}) - \omega t]}$

Substituting and taking the limit $k_0 \to \infty$ (short wavelength):

**Eikonal equation:**
$$(\nabla S)^2 = n^2(\mathbf{r})$$

**Transport equation:**
$$2\nabla S \cdot \nabla A + A \nabla^2 S = 0$$

### 2.2.2 Physical Meaning

**Eikonal $S(\mathbf{r})$:** Optical path length from a reference point.

**Wavefronts:** Surfaces of constant $S$ (constant phase).

**Rays:** Perpendicular to wavefronts, direction $\propto \nabla S$.

**Slowly varying amplitude:** The transport equation shows how amplitude changes along rays (conservation of energy flux).

### 2.2.3 Ray Equation

From the eikonal equation, we derive the **ray equation**:

$$\frac{d}{ds}\left(n \frac{d\mathbf{r}}{ds}\right) = \nabla n$$

This describes how rays bend in inhomogeneous media (gradient-index optics, mirages, etc.).

## 2.3 Paraxial Ray Optics

### 2.3.1 Small-Angle Approximation

**Paraxial approximation:** $\sin\theta \approx \theta$, $\cos\theta \approx 1$ (angles in radians).

Valid when $\theta \ll 1$ rad (typically $\theta < 0.1$ rad or $6°$).

### 2.3.2 Ray Transfer (ABCD) Matrices

A paraxial ray is described by its height $y$ and angle $u$:

$$\mathbf{r} = \begin{pmatrix} y \\ u \end{pmatrix}$$

**Free space propagation (distance $d$):**
$$\mathbf{M}_{\text{space}} = \begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix}$$

**Refraction at interface (radius $R$, indices $n$, $n'$):**
$$\mathbf{M}_{\text{refract}} = \begin{pmatrix} 1 & 0 \\ -\frac{n'-n}{n'R} & \frac{n}{n'} \end{pmatrix}$$

**Thin lens (focal length $f$):**
$$\mathbf{M}_{\text{lens}} = \begin{pmatrix} 1 & 0 \\ -\frac{1}{f} & 1 \end{pmatrix}$$

**Spherical mirror (radius $R$):**
$$\mathbf{M}_{\text{mirror}} = \begin{pmatrix} 1 & 0 \\ \frac{2}{R} & 1 \end{pmatrix}$$

### 2.3.3 System Matrix

For a system with $N$ elements:

$$\mathbf{M}_{\text{sys}} = \mathbf{M}_N \mathbf{M}_{\text{space},N-1} \cdots \mathbf{M}_2 \mathbf{M}_{\text{space},1} \mathbf{M}_1$$

**Effective focal length:**
$$f_{\text{eff}} = -\frac{1}{C}$$

where $C$ is the (2,1) element of $\mathbf{M}_{\text{sys}}$.

### 2.3.4 Gaussian Beams and Ray Matrices

The **ABCD law** for Gaussian beams:

$$q_2 = \frac{Aq_1 + B}{Cq_1 + D}$$

connects ray optics (matrices) to wave optics (Gaussian beams). This elegant unification shows that Gaussian beams transform through optical systems exactly as rays do, but with complex parameters.

## 2.4 Cardinal Points of an Optical System

### 2.4.1 The Six Cardinal Points

1. **First principal point $H_1$:** Reference point for object distances
2. **Second principal point $H_2$:** Reference point for image distances
3. **First focal point $F_1$:** Object at infinity focuses here
4. **Second focal point $F_2$:** Image of object at infinity
5. **First nodal point $N_1$:** Rays through $N_1$ emerge parallel
6. **Second nodal point $N_2$:** Parallel rays appear to come from $N_2$

**For systems in air:** $N_1 = H_1$ and $N_2 = H_2$.

### 2.4.2 Imaging Equations

**Gaussian lens equation:**
$$\frac{1}{s'} - \frac{1}{s} = \frac{1}{f}$$

where $s$ and $s'$ are measured from $H_1$ and $H_2$.

**Newtonian form:**
$$xx' = f^2$$

where $x$ and $x'$ are measured from focal points.

**Magnification:**
$$M = \frac{y'}{y} = -\frac{s'}{s} = -\frac{x'}{f} = -\frac{f}{x}$$

### 2.4.3 Diagram Illustration

```
Object Space          Optical System          Image Space
─────────────────────────────────────────────────────────
  F₁  H₁                    H₂  F₂
   ●──┼──────────────────────┼──●
      │                      │
      │                      │
      s                      s'
      │                      │
      │                      │
      ● Object               ● Image
```

## 2.5 Optical Invariants

### 2.5.1 Lagrange Invariant

**2D Lagrange invariant:**
$$H = n y \sin u = n' y' \sin u'$$

**3D form:**
$$H^2 = n^2 A \Omega = \frac{G}{\pi^2}$$

where $G$ is the étendue.

**Conservation:** $H$ is conserved through any optical system (in the paraxial approximation).

### 2.5.2 Connection to Étendue

**Étendue:**
$$G = n^2 A \Omega = \pi^2 H^2$$

**Conservation:** In a lossless system, $G_{\text{in}} = G_{\text{out}}$.

**Physical meaning:** You cannot collect more light than the étendue allows. This sets fundamental limits on:
- Light collection efficiency
- Concentration ratios (solar concentrators)
- Field of view vs. aperture trade-offs

### 2.5.3 System Limits

**Resolution limit:** Diffraction + étendue conservation:
$$\delta x \geq 1.22 \frac{\lambda}{\text{NA}}$$

**Light collection:** Maximum étendue of system is minimum étendue of any element (stop, fiber, detector).

## 2.6 Stops & Pupils

### 2.6.1 Aperture Stop

**Aperture stop:** Physical element that limits the cone of rays from an on-axis object point.

**Location:** Found by tracing chief rays from object through all apertures; the one with smallest angular subtense is the stop.

### 2.6.2 Field Stop

**Field stop:** Limits the field of view (off-axis extent).

**Location:** Usually at an intermediate image plane.

### 2.6.3 Entrance and Exit Pupils

**Entrance pupil:** Image of the aperture stop as seen from object space.

**Exit pupil:** Image of the aperture stop as seen from image space.

**Location:** Found by tracing rays through the system.

### 2.6.4 Chief Rays and Marginal Rays

**Chief ray:** Passes through center of aperture stop (and pupils).

**Marginal ray:** Passes through edge of aperture stop.

**Significance:**
- Chief ray: Determines image position
- Marginal ray: Determines image size and resolution

### 2.6.5 Telecentricity

**Object-space telecentric:** Entrance pupil at infinity.

**Properties:**
- Chief rays parallel in object space
- Magnification constant with defocus
- Important for metrology

**Image-space telecentric:** Exit pupil at infinity.

**Properties:**
- Chief rays parallel in image space
- No focus shift with detector position
- Important for machine vision

**Double telecentric:** Both pupils at infinity.

**Properties:**
- Constant magnification regardless of object/image position
- Ideal for measurement applications

---

## Summary and Connections

This study guide has established the fundamental principles of optics:

**Wave Optics (Section 1):**
- Electromagnetic wave equation from Maxwell's equations
- Plane, spherical, and Gaussian wave solutions
- Polarization (Jones, Mueller)
- Refractive index, dispersion, absorption
- Coherence (temporal, spatial)
- Diffraction (Huygens-Fresnel, limits)
- Energy flow (Poynting vector)

**Geometrical Optics (Section 2):**
- Fermat's principle → Snell's law
- Eikonal equation (wave → ray limit)
- Paraxial ray tracing (ABCD matrices)
- Cardinal points (imaging equations)
- Optical invariants (étendue limits)
- Stops and pupils (system design)

**Key Unifications:**
- Eikonal approximation connects waves to rays
- ABCD law connects rays to Gaussian beams
- Étendue conservation connects radiometry to imaging
- Fermat's principle unifies all of geometric optics

These foundations prepare you for advanced topics: aberration theory, Fourier optics, interferometry, and optical design.

---

## References

- Born, M. & Wolf, E. *Principles of Optics* (7th ed.). Cambridge University Press, 1999.
- Hecht, E. *Optics* (5th ed.). Pearson, 2017.
- Goodman, J. W. *Introduction to Fourier Optics* (4th ed.). W. H. Freeman, 2017.
- Saleh, B. E. A. & Teich, M. C. *Fundamentals of Photonics* (2nd ed.). Wiley, 2007.

---

*End of Study Guide*

