# Techniques Directory

This directory contains individual technique data definitions. Each technique has its own Python file that exports a data dictionary.

## Structure

- Each technique file (e.g., `raman_microscopy.py`) contains a single dictionary with all technique data
- The `__init__.py` file imports all techniques and provides helper functions
- Techniques are registered in the `TECHNIQUES` dictionary in `__init__.py`

## Adding a New Technique

1. Create a new file: `techniques/your_technique_name.py`
2. Define your technique data dictionary (see `raman_microscopy.py` for structure)
3. Import and register it in `techniques/__init__.py`:
   ```python
   from .your_technique_name import your_technique_data
   
   TECHNIQUES = {
       "Raman microscopy": raman_data,
       "Your Technique Name": your_technique_data,  # Add here
   }
   ```

## Using Techniques

```python
from techniques import get_technique_data, list_techniques

# List all available techniques
print(list_techniques())

# Get a specific technique's data
data = get_technique_data("Raman microscopy")
```

## Technique Data Structure

Each technique dictionary should contain these keys:
- `one_line_summary`: Brief description
- `abstract`: Detailed overview
- `physics_principle`: Physics explanation
- `instruments_components`: Equipment details
- `resolution_detection`: Resolution and detection limits
- `sample_requirements`: Sample preparation and requirements
- `measurement_protocol`: Step-by-step protocol (dict with sections)
- `data_outputs`: File formats and data structure
- `data_analysis_pipeline`: Analysis methods (dict with sections)
- `artifacts_troubleshooting`: Common issues and solutions
- `multimodal_pairings`: Compatible techniques
- `strengths_limitations`: Dict with "strengths" and "limitations" lists
- `references`: List of citation dicts with "citation" and "doi"
- `lab_checklist`: List of checklist items
- `keywords`: List of keywords/tags

