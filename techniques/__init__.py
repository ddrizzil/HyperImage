"""
Techniques module - contains individual technique data definitions.
"""

# Import all technique data modules
from .coherent_anti_stokes_raman_scattering_cars_microscopy import coherent_anti_stokes_raman_scattering_cars_microscopy_data
from .coherence_scanning_interferometry_csi import coherence_scanning_interferometry_csi_data
from .digital_x_ray_radiography_dr import digital_x_ray_radiography_dr_data
from .fib_sem_dual_beam_tomography import fib_sem_dual_beam_tomography_data
from .gas_chromatography_mass_spectrometry import gas_chromatography_mass_spectrometry_data
from .macro_x_ray_fluorescence_scanning import macro_x_ray_fluorescence_scanning_data
from .micro_raman_spectroscopy import micro_raman_spectroscopy_data
from .photoacoustic_imaging_pai import photoacoustic_imaging_pai_data
from .photoacoustic_spectroscopy import photoacoustic_spectroscopy_data
from .photoacoustic_tomography_optoacoustic_tomography import photoacoustic_tomography_optoacoustic_tomography_data
from .particle_induced_x_ray_emission_pixe import particle_induced_x_ray_emission_pixe_data
from .pyrolysis_gas_chromatography_mass_spectrometry import pyrolysis_gas_chromatography_mass_spectrometry_data
from .raking_light_photography import raking_light_photography_data
from .raman_spectroscopy_visible_excitation import raman_spectroscopy_visible_excitation_data
from .scanning_electron_microscopy_sem_secondary_electrons import scanning_electron_microscopy_sem_secondary_electrons_data
from .second_harmonic_generation_shg_microscopy import second_harmonic_generation_shg_microscopy_data
from .stereo_photogrammetry import stereo_photogrammetry_data
from .third_harmonic_generation_thg_microscopy import third_harmonic_generation_thg_microscopy_data
from .terahertz_time_domain_spectroscopy_thz_tds import terahertz_time_domain_spectroscopy_thz_tds_data
from .high_resolution_visible_photography import high_resolution_visible_photography_data
from .x_ray_holography import x_ray_holography_data
from .x_ray_radiography_film import x_ray_radiography_film_data

# Dictionary mapping technique names to their data
TECHNIQUES = {
    "Coherent Anti-Stokes Raman Scattering (CARS) Microscopy": coherent_anti_stokes_raman_scattering_cars_microscopy_data,
    "Coherence Scanning Interferometry (CSI)": coherence_scanning_interferometry_csi_data,
    "Digital X-ray Radiography (DR)": digital_x_ray_radiography_dr_data,
    "FIB-SEM Dual-Beam Tomography": fib_sem_dual_beam_tomography_data,
    "Gas Chromatography-Mass Spectrometry": gas_chromatography_mass_spectrometry_data,
    "Macro X-ray Fluorescence Scanning": macro_x_ray_fluorescence_scanning_data,
    "Micro-Raman Spectroscopy": micro_raman_spectroscopy_data,
    "Photoacoustic Imaging (PAI)": photoacoustic_imaging_pai_data,
    "Photoacoustic Spectroscopy": photoacoustic_spectroscopy_data,
    "Photoacoustic Tomography / Optoacoustic Tomography": photoacoustic_tomography_optoacoustic_tomography_data,
    "Particle-Induced X-ray Emission (PIXE)": particle_induced_x_ray_emission_pixe_data,
    "Pyrolysis-Gas Chromatography-Mass Spectrometry": pyrolysis_gas_chromatography_mass_spectrometry_data,
    "Raking Light Photography": raking_light_photography_data,
    "Raman Spectroscopy (Visible Excitation)": raman_spectroscopy_visible_excitation_data,
    "Scanning Electron Microscopy (SEM) - Secondary Electrons": scanning_electron_microscopy_sem_secondary_electrons_data,
    "Second Harmonic Generation (SHG) Microscopy": second_harmonic_generation_shg_microscopy_data,
    "Stereo Photogrammetry": stereo_photogrammetry_data,
    "Third Harmonic Generation (THG) Microscopy": third_harmonic_generation_thg_microscopy_data,
    "Terahertz Time-Domain Spectroscopy (THz-TDS)": terahertz_time_domain_spectroscopy_thz_tds_data,
    "High-Resolution Visible Photography": high_resolution_visible_photography_data,
    "X-ray Holography": x_ray_holography_data,
    "X-ray Radiography (Film)": x_ray_radiography_film_data,
}

def get_technique_data(technique_name: str):
    """Get technique data by name."""
    return TECHNIQUES.get(technique_name)

def list_techniques():
    """List all available techniques."""
    return list(TECHNIQUES.keys())
