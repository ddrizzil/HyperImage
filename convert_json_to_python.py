"""
Convert JSON technique files to Python technique modules for the HyperImage framework.
"""

import json
from pathlib import Path
import re

def convert_json_to_python_format(json_data):
    """Convert JSON technique format to Python framework format."""
    
    # Map JSON fields to Python framework fields
    python_data = {
        "one_line_summary": json_data.get("summary", ""),
        "abstract": json_data.get("summary", ""),  # Use summary as abstract if no separate abstract
        "physics_principle": json_data.get("fundamentalPhysics", {}).get("principle", ""),
        "instruments_components": format_instrumentation(json_data.get("instrumentation", {})),
        "resolution_detection": format_resolution(json_data.get("fundamentalPhysics", {})),
        "sample_requirements": format_sample_requirements(json_data),
        "measurement_protocol": format_measurement_protocol(json_data.get("methodology", {})),
        "data_outputs": format_data_outputs(json_data.get("dataAnalysis", {})),
        "data_analysis_pipeline": format_analysis_pipeline(json_data.get("dataAnalysis", {})),
        "artifacts_troubleshooting": format_troubleshooting(json_data.get("methodology", {})),
        "multimodal_pairings": format_multimodal(json_data.get("multimodal", {})),
        "strengths_limitations": format_strengths_limitations(json_data),
        "references": format_references(json_data.get("references", {})),
        "lab_checklist": format_checklist(json_data.get("methodology", {})),
        "keywords": json_data.get("tags", [])
    }
    
    return python_data

def format_instrumentation(instrumentation):
    """Format instrumentation section."""
    if not instrumentation:
        return "**Instrumentation details not available.**"
    
    parts = []
    
    if instrumentation.get("source"):
        parts.append(f"**Source:**\n{instrumentation['source']}")
    
    if instrumentation.get("detector"):
        detector = instrumentation["detector"]
        if isinstance(detector, dict):
            parts.append(f"**Detector:**\n{detector.get('type', 'N/A')}")
        else:
            parts.append(f"**Detector:**\n{detector}")
    
    if instrumentation.get("opticalSystem"):
        optical = instrumentation["opticalSystem"]
        if isinstance(optical, dict):
            components = optical.get("components", [])
            if components:
                parts.append(f"**Optical System Components:**\n" + "\n".join(f"- {c}" for c in components))
        else:
            parts.append(f"**Optical System:**\n{optical}")
    
    if instrumentation.get("criticalComponents"):
        parts.append(f"**Critical Components:**\n" + "\n".join(f"- {c}" for c in instrumentation["criticalComponents"]))
    
    if instrumentation.get("typicalConfiguration"):
        parts.append(f"**Typical Configuration:**\n{instrumentation['typicalConfiguration']}")
    
    return "\n\n".join(parts) if parts else "**Instrumentation details not available.**"

def format_resolution(fundamental_physics):
    """Format resolution and detection information."""
    parts = []
    
    if fundamental_physics.get("spatialResolution"):
        parts.append(f"**Spatial Resolution:**\n{fundamental_physics['spatialResolution']}")
    
    if fundamental_physics.get("interactionDepth"):
        depth = fundamental_physics["interactionDepth"]
        if isinstance(depth, dict):
            parts.append(f"**Interaction Depth:**\n{depth.get('description', 'N/A')}")
        else:
            parts.append(f"**Interaction Depth:**\n{depth}")
    
    if fundamental_physics.get("detectionLimit") or fundamental_physics.get("sensitivity"):
        sens = fundamental_physics.get("detectionLimit") or fundamental_physics.get("sensitivity", {})
        if isinstance(sens, dict):
            parts.append(f"**Detection Limits:**\n{sens.get('detectionLimits', 'N/A')}")
        else:
            parts.append(f"**Detection Limits:**\n{sens}")
    
    return "\n\n".join(parts) if parts else "**Resolution and detection information not available.**"

def format_sample_requirements(json_data):
    """Format sample requirements."""
    parts = []
    
    destructiveness = json_data.get("destructiveness", "")
    if destructiveness:
        parts.append(f"**Destructiveness:** {destructiveness}")
    
    portability = json_data.get("portability", "")
    if portability:
        parts.append(f"**Portability:** {portability}")
    
    methodology = json_data.get("methodology", {})
    sample_prep = methodology.get("samplePreparation", {})
    if sample_prep:
        if isinstance(sample_prep, dict):
            if sample_prep.get("samplingRequired"):
                parts.append(f"**Sampling Required:** {'Yes' if sample_prep['samplingRequired'] else 'No'}")
            if sample_prep.get("sampleSize"):
                parts.append(f"**Sample Size:** {sample_prep['sampleSize']}")
            if sample_prep.get("mountingProcedure"):
                parts.append(f"**Mounting Procedure:**\n{sample_prep['mountingProcedure']}")
        else:
            parts.append(f"**Sample Preparation:**\n{sample_prep}")
    
    return "\n\n".join(parts) if parts else "**Sample requirements not specified.**"

def format_measurement_protocol(methodology):
    """Format measurement protocol."""
    protocol = {}
    
    sample_prep = methodology.get("samplePreparation", {})
    if sample_prep:
        if isinstance(sample_prep, dict):
            prep_steps = []
            if sample_prep.get("mountingProcedure"):
                prep_steps.append(f"Mounting: {sample_prep['mountingProcedure']}")
            if sample_prep.get("surfacePreparation"):
                prep_steps.append(f"Surface preparation: {sample_prep['surfacePreparation']}")
            if prep_steps:
                protocol["preparation"] = prep_steps
        else:
            protocol["preparation"] = [str(sample_prep)]
    
    measurement = methodology.get("measurementProtocol", {})
    if measurement:
        if isinstance(measurement, dict):
            steps = measurement.get("steps", [])
            if steps:
                protocol["data_collection"] = [format_step(step) for step in steps]
        else:
            protocol["data_collection"] = [str(measurement)]
    
    calibration = methodology.get("calibration", {})
    if calibration:
        if isinstance(calibration, dict):
            standards = calibration.get("standards", [])
            if standards:
                protocol["calibration"] = [f"Standards: {', '.join(standards)}"]
            if calibration.get("procedure"):
                protocol.setdefault("calibration", []).append(calibration["procedure"])
        else:
            protocol["calibration"] = [str(calibration)]
    
    return protocol if protocol else {"preparation": ["See methodology section"], "data_collection": ["See methodology section"]}

def format_step(step):
    """Format a measurement protocol step."""
    if isinstance(step, dict):
        title = step.get("title", "")
        desc = step.get("description", "")
        return f"{title}: {desc}" if title else desc
    return str(step)

def format_data_outputs(data_analysis):
    """Format data outputs section."""
    if not data_analysis:
        return "**Data output formats not specified.**"
    
    parts = []
    
    raw_data = data_analysis.get("rawDataFormat", {})
    if raw_data:
        if isinstance(raw_data, dict):
            if raw_data.get("fileFormats"):
                parts.append(f"**File Formats:**\n" + ", ".join(raw_data["fileFormats"]))
            if raw_data.get("dataStructure"):
                parts.append(f"**Data Structure:**\n{raw_data['dataStructure']}")
        else:
            parts.append(f"**Raw Data Format:**\n{raw_data}")
    
    return "\n\n".join(parts) if parts else "**Data output formats not specified.**"

def format_analysis_pipeline(data_analysis):
    """Format data analysis pipeline."""
    pipeline = {}
    
    if data_analysis.get("preprocessing"):
        preprocessing = data_analysis["preprocessing"]
        if isinstance(preprocessing, list):
            pipeline["preprocessing"] = "\n".join(f"- {p.get('step', p.get('description', str(p)))}" if isinstance(p, dict) else f"- {p}" for p in preprocessing)
        else:
            pipeline["preprocessing"] = str(preprocessing)
    
    if data_analysis.get("analysisWorkflow"):
        workflow = data_analysis["analysisWorkflow"]
        if isinstance(workflow, dict):
            steps = workflow.get("steps", [])
            if steps:
                pipeline["analysis_workflow"] = "\n".join(f"{i+1}. {format_step(s)}" for i, s in enumerate(steps))
        else:
            pipeline["analysis_workflow"] = str(workflow)
    
    return pipeline if pipeline else {"preprocessing": "See data analysis section", "analysis_workflow": "See data analysis section"}

def format_troubleshooting(methodology):
    """Format troubleshooting section."""
    qc = methodology.get("qualityControl", {})
    
    # Handle case where qualityControl is a list
    if isinstance(qc, list):
        return "**Troubleshooting:**\n" + "\n".join(f"- {item}" if isinstance(item, str) else str(item) for item in qc)
    
    if not qc or not isinstance(qc, dict):
        return "**Troubleshooting information not available.**"
    
    parts = []
    
    if qc.get("commonArtifacts"):
        artifacts = qc["commonArtifacts"]
        if isinstance(artifacts, list):
            parts.append("**Common Artifacts:**\n" + "\n".join(f"- {a}" if isinstance(a, str) else f"- {a.get('problem', a.get('cause', str(a)))}" for a in artifacts))
        else:
            parts.append(f"**Common Artifacts:**\n{artifacts}")
    
    if qc.get("troubleshooting"):
        troubleshooting = qc["troubleshooting"]
        if isinstance(troubleshooting, list):
            parts.append("**Troubleshooting:**\n" + "\n".join(f"- {t}" if isinstance(t, str) else f"- {t.get('problem', t.get('cause', str(t)))}" for t in troubleshooting))
        else:
            parts.append(f"**Troubleshooting:**\n{troubleshooting}")
    
    return "\n\n".join(parts) if parts else "**Troubleshooting information not available.**"

def format_multimodal(multimodal):
    """Format multimodal pairings."""
    if not multimodal:
        return "**Multimodal pairings not specified.**"
    
    parts = []
    
    complementary = multimodal.get("complementaryTechniques", [])
    if complementary:
        parts.append("**Complementary Techniques:**")
        for tech in complementary:
            if isinstance(tech, dict):
                name = tech.get("techniqueName", tech.get("techniqueId", "Unknown"))
                rationale = tech.get("rationale", "")
                parts.append(f"- {name}: {rationale}")
            else:
                parts.append(f"- {tech}")
    
    standard = multimodal.get("standardCombinations", [])
    if standard:
        parts.append("\n**Standard Combinations:**")
        for combo in standard:
            if isinstance(combo, dict):
                name = combo.get("name", "Combination")
                rationale = combo.get("rationale", "")
                parts.append(f"- {name}: {rationale}")
            else:
                parts.append(f"- {combo}")
    
    return "\n\n".join(parts) if parts else "**Multimodal pairings not specified.**"

def format_strengths_limitations(json_data):
    """Format strengths and limitations."""
    advantages = json_data.get("advantages", {})
    limitations = json_data.get("limitations", {})
    
    strengths = []
    limitations_list = []
    
    if isinstance(advantages, dict):
        if advantages.get("advantages"):
            strengths = advantages["advantages"] if isinstance(advantages["advantages"], list) else [advantages["advantages"]]
    elif isinstance(advantages, list):
        strengths = advantages
    
    if isinstance(limitations, dict):
        if limitations.get("limitations"):
            limitations_list = limitations["limitations"] if isinstance(limitations["limitations"], list) else [limitations["limitations"]]
    elif isinstance(limitations, list):
        limitations_list = limitations
    
    return {
        "strengths": strengths if strengths else ["See technique documentation"],
        "limitations": limitations_list if limitations_list else ["See technique documentation"]
    }

def format_references(references):
    """Format references."""
    if not references:
        return []
    
    refs = []
    
    if isinstance(references, dict):
        key_papers = references.get("keyPapers", [])
        for paper in key_papers:
            if isinstance(paper, dict):
                refs.append({
                    "citation": paper.get("citation", paper.get("title", "Unknown")),
                    "doi": paper.get("doi", "")
                })
            else:
                refs.append({"citation": str(paper), "doi": ""})
    elif isinstance(references, list):
        for ref in references:
            if isinstance(ref, dict):
                refs.append({
                    "citation": ref.get("citation", ref.get("title", "Unknown")),
                    "doi": ref.get("doi", "")
                })
            else:
                refs.append({"citation": str(ref), "doi": ""})
    
    return refs if refs else [{"citation": "See technique documentation", "doi": ""}]

def format_checklist(methodology):
    """Format lab checklist."""
    qc = methodology.get("qualityControl", {})
    
    # Handle case where qualityControl is a list
    if isinstance(qc, list):
        return [str(item) for item in qc]
    
    if not qc or not isinstance(qc, dict):
        return ["See methodology section"]
    
    checklist = []
    
    if qc.get("checkpoints"):
        checkpoints = qc["checkpoints"]
        if isinstance(checkpoints, list):
            checklist = [str(cp) for cp in checkpoints]
        else:
            checklist = [str(checkpoints)]
    
    return checklist if checklist else ["See methodology section"]

def sanitize_filename(name):
    """Convert technique name to valid Python filename."""
    # Convert to lowercase, replace spaces and special chars with underscores
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    name = re.sub(r'_+', '_', name)  # Remove multiple underscores
    name = name.strip('_')  # Remove leading/trailing underscores
    return name

def convert_all_techniques():
    """Convert all JSON technique files to Python modules."""
    json_dir = Path("web/src/data/techniques")
    techniques_dir = Path("techniques")
    
    if not json_dir.exists():
        print(f"Error: JSON directory not found: {json_dir}")
        return
    
    json_files = list(json_dir.glob("*.json"))
    print(f"Found {len(json_files)} JSON technique files")
    
    converted = []
    
    for json_file in json_files:
        try:
            print(f"\nProcessing: {json_file.name}")
            
            # Load JSON (handle UTF-8 BOM)
            with open(json_file, 'r', encoding='utf-8-sig') as f:
                json_data = json.load(f)
            
            # Get technique name
            technique_name = json_data.get("name", json_data.get("id", json_file.stem))
            
            # Convert to Python format
            python_data = convert_json_to_python_format(json_data)
            
            # Create Python file
            filename = sanitize_filename(technique_name)
            python_file = techniques_dir / f"{filename}.py"
            
            # Generate Python code
            python_code = f'''"""
{technique_name} technique data definition.
"""

# Data for {technique_name} reference page
{filename}_data = {repr(python_data)}
'''
            
            # Write Python file
            python_file.write_text(python_code, encoding='utf-8')
            print(f"  Created: {python_file}")
            
            converted.append((technique_name, filename))
            
        except Exception as e:
            print(f"  Error processing {json_file.name}: {e}")
            import traceback
            traceback.print_exc()
    
    # Update __init__.py
    update_init_file(converted)
    
    print(f"\n\nConverted {len(converted)} techniques!")
    print("\nTechniques converted:")
    for name, filename in converted:
        print(f"  - {name} -> {filename}.py")

def update_init_file(converted):
    """Update the __init__.py file with all converted techniques."""
    init_file = Path("techniques/__init__.py")
    
    # Generate imports and TECHNIQUES dict
    imports = []
    techniques_dict_items = []
    
    for technique_name, filename in converted:
        var_name = f"{filename}_data"
        imports.append(f"from .{filename} import {var_name}")
        techniques_dict_items.append(f'    "{technique_name}": {var_name},')
    
    # Generate __init__.py content
    init_content = f'''"""
Techniques module - contains individual technique data definitions.
"""

# Import all technique data modules
{chr(10).join(imports)}

# Dictionary mapping technique names to their data
TECHNIQUES = {{
{chr(10).join(techniques_dict_items)}
}}

def get_technique_data(technique_name: str):
    """Get technique data by name."""
    return TECHNIQUES.get(technique_name)

def list_techniques():
    """List all available techniques."""
    return list(TECHNIQUES.keys())
'''
    
    init_file.write_text(init_content, encoding='utf-8')
    print(f"\nUpdated: {init_file}")

if __name__ == "__main__":
    convert_all_techniques()

