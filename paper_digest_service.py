"""
paper_digest_service.py
Daily Paper Digest with NLP-enhanced scoring, citation-aware ranking,
learning-based personalization, trending detection, and HTML email digest.
"""
import csv
import html
import logging
import math
import os
import re
import time
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from itertools import islice
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import quote_plus

import feedparser
import numpy as np
import requests
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Attempt to import scholarly + proxy support; continue gracefully if absent.
try:
    from scholarly import ProxyGenerator, scholarly  # type: ignore
except ImportError:
    scholarly = None
    ProxyGenerator = None

try:
    from sentence_transformers import SentenceTransformer  # type: ignore
except ImportError:
    SentenceTransformer = None

# ---------------- CONFIG ----------------
SENDER = "dailypapersender@intrawebb.com"
DEFAULT_RECIPIENT = "daniel@intrawebb.com"

FEEDS = [
    # ============ AREAS: CULTURAL HERITAGE & IMAGING ============
    "https://heritagesciencejournal.springeropen.com/articles/rss.xml",
    "https://www.sciencedirect.com/journal/journal-of-cultural-heritage/rss",
    "https://www.osapublishing.org/ao/rss.cfm",
    "https://www.osapublishing.org/oe/rss.cfm",
    "https://www.osapublishing.org/boe/rss.cfm",
    "https://www.osapublishing.org/josaa/rss.cfm",
    "https://www.osapublishing.org/josab/rss.cfm",
    "https://www.osapublishing.org/ol/rss.cfm",
    "https://www.osapublishing.org/optica/rss.cfm",
    "https://www.nature.com/lsa.rss",
    "https://www.spiedigitallibrary.org/journals/journal-of-electronic-imaging/rss",
    "https://www.sciencedirect.com/journal/optics-and-lasers-in-engineering/rss",
    "https://www.sciencedirect.com/journal/optics-communications/rss",
    "https://www.sciencedirect.com/journal/studies-in-conservation/rss",
    "https://www.mdpi.com/journal/heritage/rss",
    "https://brill.com/view/journals/ins/ins-overview.xml",
    "https://www.mdpi.com/journal/arts/rss",
    "https://journals.sagepub.com/action/showFeed?ui=0&mi=ehikzz&ai=2b4&jc=dsaa&type=etoc&feed=rss",

    # ============ RF SYSTEMS, MICROWAVE, RADAR ============
    "https://ieeexplore.ieee.org/rss/TOC78.XML",
    "https://ieeexplore.ieee.org/rss/TOC5.XML",
    "https://ieeexplore.ieee.org/rss/TOC7361.XML",
    "https://ieeexplore.ieee.org/rss/TOC10376.XML",
    "https://ieeexplore.ieee.org/rss/TOC22.XML",
    "https://ieeexplore.ieee.org/rss/TOC8.XML",
    "https://ieeexplore.ieee.org/rss/TOC4234.XML",
    "https://ieeexplore.ieee.org/rss/TOC6668.XML",
    "https://ieeexplore.ieee.org/rss/TOC87.XML",
    "https://ieeexplore.ieee.org/rss/TOC8859.XML",
    "https://ieeexplore.ieee.org/rss/TOC36.XML",
    "https://ieeexplore.ieee.org/rss/TOC4609.XML",

    # ============ SIGNAL PROCESSING & MACHINE LEARNING ============
    "https://ieeexplore.ieee.org/rss/TOC97.XML",
    "https://ieeexplore.ieee.org/rss/TOC4200.XML",
    "https://ieeexplore.ieee.org/rss/TOC6046.XML",
    "https://ieeexplore.ieee.org/rss/TOC6287.XML",
    "https://ieeexplore.ieee.org/rss/TOC34.XML",
    "https://ieeexplore.ieee.org/rss/TOC6221.XML",
    "https://www.sciencedirect.com/journal/signal-processing/rss",
    "https://www.sciencedirect.com/journal/digital-signal-processing/rss",

    # ============ CLIMATE, ENVIRONMENT, AGRICULTURE ============
    "https://www.nature.com/subjects/remote-sensing/rss",
    "https://www.nature.com/nclimate.rss",
    "https://www.nature.com/natrevearth.rss",
    "https://www.mdpi.com/journal/atmosphere/rss",
    "https://www.mdpi.com/journal/climate/rss",
    "https://journals.ametsoc.org/rss/bams.xml",
    "https://agupubs.onlinelibrary.wiley.com/feed/19448007/most-recent",
  #3  "https://www.sciencedirect.com/journal/agricultural-and-forest-meteorology/rss",
    "https://www.mdpi.com/journal/land/rss",
    "https://www.mdpi.com/journal/sustainability/rss",
    "https://nhess.copernicus.org/xml/rss2_0.xml",
    "https://www.mdpi.com/journal/geosciences/rss",

    # ============ MATERIALS SCIENCE & SPECTROSCOPY ============
    "https://www.mdpi.com/journal/photonics/rss",
    "https://www.nature.com/nphoton.rss",
    "https://www.sciencedirect.com/journal/spectrochimica-acta-part-a-molecular-and-biomolecular-spectroscopy/rss",
    "https://pubs.rsc.org/en/journals/rss/ja",
    "https://www.mdpi.com/journal/materials/rss",
    # "https://pubs.acs.org/action/showFeed?type=axatoc&feed=rss&jc=ancham",

    # ============ APPLIED PHYSICS & INSTRUMENTATION ============
    "https://aip.scitation.org/rss/content/aip/journal/rsi?sc_cid=rss",
    "https://www.nature.com/scientificreports.rss",
    "https://iopscience.iop.org/journal/rss/0957-0233",
    "https://www.mdpi.com/journal/applsci/rss",
    "https://www.mdpi.com/journal/instruments/rss",

    # ============ WIRELESS COMMUNICATIONS & IOT ============
    "https://ieeexplore.ieee.org/rss/TOC26.XML",
    "https://ieeexplore.ieee.org/rss/TOC35.XML",
    "https://ieeexplore.ieee.org/rss/TOC6570650.XML",
    "https://ieeexplore.ieee.org/rss/TOC9739572.XML",

    # ============ COMPUTER VISION & IMAGING ============
    "https://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=11263&channel-name=International+Journal+of+Computer+Vision",
    "https://www.mdpi.com/journal/jimaging/rss",

    # ============ MULTIDISCIPLINARY & HIGH-IMPACT ============
    "https://www.science.org/rss/news_current.xml",
    "https://www.nature.com/nature.rss",
    "https://www.pnas.org/rss/latest.xml",

    # ============ ARXIV FEEDS ============
    "https://arxiv.org/rss/eess.SP",
    "https://arxiv.org/rss/cs.LG",
    "https://arxiv.org/rss/cs.CV",
    "https://arxiv.org/rss/cs.AI",
    "https://arxiv.org/rss/stat.ML",
    "https://arxiv.org/rss/physics.ao-ph",
    "https://arxiv.org/rss/physics.app-ph",
    "https://arxiv.org/rss/physics.data-an",
    "https://arxiv.org/rss/physics.geo-ph",
    "https://arxiv.org/rss/cs.RO",
    "https://arxiv.org/rss/quant-ph",
    "https://arxiv.org/rss/eess.IV",
    "https://arxiv.org/rss/physics.optics",
    "https://arxiv.org/rss/physics.ins-det",
]

# Expanded keyword groups spanning commercial radar, climate, & disaster response.
KEYWORD_GROUPS = {
    "cultural_heritage": [
        "cultural heritage", "artwork preservation", "conservation science",
        "art conservation", "heritage digitization", "archaeological remote sensing",
        "museum imaging", "collection risk assessment", "preventive conservation"
    ],
    "rf_systems_core": [
        "RF component", "microwave component", "nonlinear radar", "harmonic radar",
        "ground penetrating radar", "high-power microwave", "intermodulation distortion",
        "passive intermodulation", "rf fingerprinting", "volterra series"
    ],
    "optical_techniques": [
        "optical coherence tomography", "OCT imaging", "reflectance spectroscopy",
        "multispectral imaging", "hyperspectral imaging", "infrared reflectography",
        "UV fluorescence", "x-ray fluorescence mapping", "raman spectroscopy",
        "photoacoustic imaging", "laser ultrasound", "terahertz imaging"
    ],
    "ml_methods": [
        "deep learning", "convolutional neural network", "cnn",
        "recurrent neural network", "rnn", "lstm", "transformer model",
        "attention mechanism", "generative adversarial network", "gan",
        "variational autoencoder", "vae", "reinforcement learning",
        "transfer learning", "few-shot learning", "meta-learning",
        "self-supervised learning", "contrastive learning",
        "neural architecture search", "automl", "federated learning",
        "graph neural network", "physics-informed neural network", "pinn"
    ],
    "ml_signal_processing": [
        "deep learning signal processing", "neural network denoising",
        "learned compression", "neural beamforming", "ai-based detection",
        "learned reconstruction", "model-based deep learning", "unrolled optimization",
        "differentiable signal processing", "end-to-end learning", "neural operator",
        "learned sensing"
    ],
    "advanced_dsp": [
        "sparse representation", "dictionary learning", "matrix completion",
        "low-rank approximation", "tensor decomposition", "tensor factorization",
        "blind source separation", "independent component analysis",
        "nonnegative matrix factorization", "nmf", "bayesian inference",
        "variational inference", "expectation maximization", "particle filter",
        "kalman filter", "extended kalman filter", "unscented kalman filter",
        "ensemble kalman filter"
    ],
    "nonlinear_systems": [
        "nonlinear dynamics", "nonlinear characterization", "harmonic generation",
        "intermodulation distortion", "volterra series", "polynomial modeling",
        "behavioral modeling", "digital predistortion", "power amplifier linearization",
        "nonlinear compensation", "chaos theory", "bifurcation analysis",
        "lyapunov exponent", "strange attractor"
    ],
    "rf_diagnostics": [
        "rf diagnostics", "component health monitoring", "predictive maintenance rf",
        "anomaly detection rf", "fault detection radar", "performance degradation detection",
        "automated test equipment", "ate", "rf calibration",
        "vector network analyzer", "vna", "spectrum analyzer", "signal analyzer",
        "modulation analysis", "electromagnetic interference", "emi testing",
        "rf front-end testing", "receiver sensitivity", "transmitter linearity",
        "phase noise measurement","cryogenic"
    ],
    "5g_6g_systems": [
        "5g nr", "new radio", "6g wireless", "massive mimo", "beamforming 5g",
        "millimeter wave communication", "mmwave 5g", "terahertz communication",
        "thz wireless", "reconfigurable intelligent surface", "ris", "network slicing",
        "edge computing", "ultra-reliable low-latency", "urllc",
        "enhanced mobile broadband", "embb", "o-ran", "open ran", "virtualized ran"
    ],
    "automotive_radar": [
        "automotive radar", "adas radar", "autonomous driving radar",
        "77 ghz radar", "79 ghz radar", "fmcw radar automotive", "radar sensor fusion",
        "vehicle-to-everything", "v2x", "radar point cloud", "4d radar imaging",
        "radar target classification", "pedestrian detection radar",
        "collision avoidance radar", "blind spot detection",
        "adaptive cruise control radar", "parking assist radar"
    ],
    "satellite_systems": [
        "synthetic aperture radar", "sar", "insar", "differential insar", "dinsar",
        "satellite remote sensing", "earth observation", "sentinel", "landsat",
        "modis", "sar interferometry", "polarimetric sar", "sar tomography",
        "bistatic radar", "spaceborne radar", "satellite altimetry",
        "gnss reflectometry", "gnss-r", "cubesat", "smallsat", "nanosatellite"
    ],
    "climate_methods": [
        "climate modeling", "climate projection", "downscaling", "data assimilation",
        "reanalysis", "climate feedback", "radiative forcing", "climate sensitivity",
        "tipping point", "extreme event attribution", "seasonal forecasting",
        "subseasonal prediction", "ensemble prediction", "uncertainty quantification"
    ],

    "precision_agriculture": [
        "precision agriculture", "smart farming", "crop monitoring",
        "yield prediction", "soil sensing", "irrigation management",
        "variable rate application", "site-specific management",
        "agricultural drone", "uav agriculture", "plant phenotyping",
        "canopy sensing", "nitrogen sensing", "chlorophyll fluorescence",
        "crop disease detection", "pest monitoring sensor"
    ],
    "quantum_technologies": [
        "quantum sensing", "quantum radar", "quantum illumination", "quantum imaging",
        "quantum metrology", "quantum communication", "quantum key distribution",
        "qkd", "entanglement", "squeezed state", "single photon detector",
        "superconducting qubit", "nitrogen vacancy center", "quantum computing"
    ],
    
    # ============ PHOTOACOUSTICS (for your art imaging) ============
    "photoacoustics": [
        "photoacoustic imaging", "photoacoustic spectroscopy", "optoacoustic",
        "thermoacoustic", "laser ultrasound", "acoustic microscopy",
        "photoacoustic tomography", "depth profiling photoacoustic"
    ],
    "heritage_materials": [
        "organic binder", "egg tempera", "oil paint", "acrylic paint",
        "watercolor", "gouache", "encaustic", "fresco", "tempera grassa",
        "azurite", "malachite", "cinnabar", "orpiment", "realgar",
        "verdigris", "prussian blue", "chrome yellow", "titanium white",
        "carbon black", "ivory black", "lamp black", "natural resin",
        "dammar", "mastic resin", "shellac", "copal", "beeswax"
    ],
    "digital_humanities": [
        "digital humanities", "computational humanities", "cultural analytics",
        "distant reading", "text mining humanities", "network analysis humanities",
        "gis humanities", "spatial humanities", "3d humanities",
        "virtual reconstruction", "digital archive", "linked open data",
        "semantic web humanities", "ontology cultural heritage"
    ],
    "infrastructure_monitoring": [
        "structural health monitoring", "shm", "bridge monitoring", "building monitoring",
        "pipeline inspection", "tunnel monitoring", "dam monitoring",
        "wind turbine monitoring", "railway infrastructure", "pavement condition",
        "concrete deterioration", "corrosion monitoring", "vibration monitoring",
        "modal analysis", "non-destructive evaluation", "nde",
        "acoustic emission", "guided wave"
    ],
    "iot_wsn": [
        "internet of things", "iot", "wireless sensor network", "wsn",
        "lora", "lorawan", "nb-iot", "lte-m", "zigbee", "bluetooth low energy",
        "ble", "edge ai", "tinyml", "on-device learning", "energy harvesting",
        "battery-free sensing", "backscatter communication", "ambient backscatter",
        "rfid sensor", "nfc sensor", "fog computing", "mesh network"
    ],
    "proptech_real_estate": [
        "property technology", "proptech", "real estate analytics",
        "property valuation", "automated valuation model", "avm",
        "real estate prediction", "housing market", "gentrification modeling",
        "urban development", "real estate investment", "portfolio optimization",
        "property risk assessment", "location intelligence", "spatial economics",
        "hedonic pricing", "neighborhood analysis", "walkability index"
    ],
    "optimization_control": [
        "convex optimization", "non-convex optimization", "stochastic optimization",
        "robust optimization", "distributed optimization", "online optimization",
        "optimal control", "model predictive control", "mpc", "adaptive control",
        "sliding mode control", "h-infinity control", "lqr", "lqg",
        "game theory", "nash equilibrium", "multi-agent system",
        "consensus algorithm"
    ],
    "inverse_problems": [
        "inverse problem", "ill-posed problem", "regularization",
        "tikhonov regularization", "total variation", "tv regularization",
        "iterative reconstruction", "algebraic reconstruction",
        "maximum likelihood estimation", "maximum a posteriori",
        "bayesian inversion", "compressed sensing reconstruction",
        "image deconvolution", "blind deconvolution", "super-resolution",
        "phase retrieval"
    ],
    "time_series": [
        "time series analysis", "time series forecasting", "arima",
        "autoregressive", "state space model", "kalman smoothing",
        "trend analysis", "seasonality", "changepoint detection",
        "anomaly detection time series", "outlier detection", "recurrent neural network time series",
        "lstm forecasting", "temporal convolutional network", "tcn",
        "attention-based time series"
    ],
    "optics_fundamentals": [
        "optical fiber", "fiber optic", "waveguide", "optical sensor",
        "photonic sensor", "optical filter", "dichroic", "bandpass filter",
        "optical coherence", "interferometry", "michelson interferometer",
        "fabry-perot", "diffraction", "scattering", "absorption",
        "fluorescence", "phosphorescence", "luminescence",
        "polarization", "birefringence", "dichroism"
    ],
    "sustainability_esg": [
        "sustainability monitoring", "esg reporting", "carbon footprint",
        "greenhouse gas emission", "circular economy", "life cycle assessment",
        "environmental impact", "biodiversity net gain", "nature-based solution",
        "ecosystem service", "climate adaptation", "climate resilience",
        "renewable energy", "solar", "wind energy", "energy efficiency",
        "smart grid", "sustainable agriculture", "regenerative agriculture"
    ],
}

RESEARCH_PROFILE = (
    "I research nonlinear electromagnetic phenomena in RF systems, using machine learning "
    "for component identification and damage detection in high-power RF components. "
    "I also work on multimodal optical imaging for art conservation, including OCT, "
    "hyperspectral imaging, XRF, and Raman spectroscopy for pigment analysis and brushstroke characterization. "
    "I'm interested in commercial applications of RF diagnostics in 5G/6G infrastructure and automotive radar, "
    "as well as climate monitoring using radar remote sensing."
)

SEMANTIC_MODEL = None
RESEARCH_EMBEDDING = None
if SentenceTransformer is not None:
    try:
        SEMANTIC_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
        RESEARCH_EMBEDDING = SEMANTIC_MODEL.encode(RESEARCH_PROFILE, convert_to_numpy=True)
    except Exception as exc:
        logging.getLogger(__name__).warning("Failed to load sentence transformer model: %s", exc)
        SEMANTIC_MODEL = None
        RESEARCH_EMBEDDING = None

ALL_KEYWORDS = [phrase for phrases in KEYWORD_GROUPS.values() for phrase in phrases]
KEYWORD_TO_GROUP: Dict[str, str] = {}
for group, phrases in KEYWORD_GROUPS.items():
    for phrase in phrases:
        KEYWORD_TO_GROUP[phrase.lower()] = group

GROUP_WEIGHT_RF = 1.5
GROUP_WEIGHT_HERITAGE = 1.3
GROUP_WEIGHT_DEFAULT = 1.0

DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)

ADJACENT_KEYWORDS = [
    "quantum radar", "cognitive radio", "digital twin environment",
    "satellite-ground fusion", "ESG reporting technology",
    "environmental signal processing", "climate resilience analytics",
    "sustainable infrastructure monitoring", "smart grid sensing"
]

LOG_FILE = "logs/paper_digest_log.csv"
PERSONALIZATION_FILE = "config/clicks.txt"
os.makedirs("logs", exist_ok=True)
os.makedirs("config", exist_ok=True)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Daily vs weekly digest mode toggle.
DIGEST_MODE = os.getenv("DIGEST_MODE", "daily").lower()

# Backoff / rate limit configuration.
SCHOLAR_RESULTS_PER_KEYWORD = 3
SCHOLAR_RATE_LIMIT_SECONDS = 2.5
SCHOLAR_MAX_KEYWORDS = 8
SCHOLAR_MAX_FAILURES = 3

CROSSREF_ENDPOINT = "https://api.crossref.org/works"
CROSSREF_ROWS_PER_KEYWORD = 20
CROSSREF_TIMEOUT = 10
CROSSREF_MAX_KEYWORDS = 10

ADJACENT_TARGET = 10
RECENT_TARGET = 10
DECADE_TARGET = 10
DECADE_MIN_SCORE = 6.0

ML_RF_GROUPS = {
    "rf_systems_core",
    "rf_diagnostics",
    "nonlinear_systems",
    "ml_methods",
    "ml_signal_processing",
    "advanced_dsp",
    "5g_6g_systems",
    "automotive_radar",
    "satellite_systems",
    "optimization_control",
    "inverse_problems",
    "time_series",
    "iot_wsn",
}

HERITAGE_OPTICS_GROUPS = {
    "cultural_heritage",
    "optical_techniques",
    "heritage_materials",
    "photoacoustics",
    "digital_humanities",
    "optics_fundamentals",
}

PRIORITY_ML_KEYWORDS = {
    "harmonic radar",
    "nonlinear radar",
    "harmonic generation",
    "volterra series",
    "rf diagnostics",
    "component health monitoring",
    "passive intermodulation",
}

CITATION_CACHE: Dict[str, int] = {}
SESSION = requests.Session()

# ---------------- HELPERS ----------------
def configure_scholarly_proxy() -> None:
    """Configure scholarly to use optional proxy from SCHOLAR_PROXY_URL."""
    if scholarly is None or ProxyGenerator is None:
        return
    proxy_url = os.getenv("SCHOLAR_PROXY_URL")
    if not proxy_url:
        return
    pg = ProxyGenerator()
    try:
        if proxy_url.startswith("socks5://"):
            parsed = re.sub(r"^socks5://", "", proxy_url)
            creds_host = parsed.split("@")
            if len(creds_host) == 2:
                creds, host_port = creds_host
                user, password = creds.split(":", 1)
            else:
                user = password = None
                host_port = creds_host[0]
            host, port = host_port.split(":", 1)
            success = pg.SOCKS5(
                proxy_host=host,
                proxy_port=int(port),
                username=user,
                password=password,
            )
        else:
            success = pg.SingleProxy(http=proxy_url, https=proxy_url)
        if success:
            scholarly.use_proxy(pg)
            logger.info("Configured scholarly proxy via SCHOLAR_PROXY_URL.")
        else:
            logger.warning("Failed to configure scholarly proxy; continuing without proxy.")
    except Exception as err:
        logger.warning("Error configuring scholarly proxy: %s", err)

configure_scholarly_proxy()

def ensure_file(path: str, default: str = "") -> None:
    """Create a file with default contents if it does not exist."""
    file_path = Path(path)
    if not file_path.exists():
        file_path.write_text(default, encoding="utf-8")

def request_with_backoff(url: str, *, params=None, headers=None, method: str = "GET",
                         max_attempts: int = 5, base_delay: float = 1.0):
    """HTTP helper with exponential backoff for rate-limited APIs."""
    delay = base_delay
    for attempt in range(1, max_attempts + 1):
        try:
            response = SESSION.request(method, url, params=params, headers=headers,
                                       timeout=CROSSREF_TIMEOUT)
            if response.status_code == 429 or response.status_code >= 500:
                logger.info("Rate limit (%s) on %s attempt %d/%d. Sleeping %.1fs.",
                            response.status_code, url, attempt, max_attempts, delay)
                time.sleep(delay)
                delay *= 2
                continue
            response.raise_for_status()
            return response
        except requests.RequestException as err:
            if attempt == max_attempts:
                raise
            logger.warning("Request error %s on %s attempt %d/%d. Sleeping %.1fs.",
                           err, url, attempt, max_attempts, delay)
            time.sleep(delay)
            delay *= 2
    return None


def sanitize_doi(raw: str) -> str:
    """Return a bare DOI string if the input looks like a DOI; otherwise empty."""
    if not raw:
        return ""
    candidate = raw.strip()
    candidate = candidate.replace("https://doi.org/", "").replace("http://doi.org/", "")
    candidate = re.sub(r"^doi:\s*", "", candidate, flags=re.IGNORECASE)
    candidate = candidate.strip()
    if DOI_PATTERN.match(candidate):
        return candidate
    return ""


def ensure_summary_text(paper: dict) -> None:
    """Provide a fallback summary when metadata lacks an abstract."""
    summary = (paper.get("summary") or "").strip()
    if summary:
        paper["summary"] = summary
        return
    title = paper.get("title", "This paper") or "This paper"
    published = paper.get("published")
    year = published.year if isinstance(published, datetime) else ""
    paper["summary"] = f"Summary unavailable. Refer to the full text for details. {year}".strip()

def load_recipients() -> List[str]:
    path = "config/emails.txt"
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"{DEFAULT_RECIPIENT}\n")
    with open(path, encoding="utf-8") as f:
        return [e.strip() for e in f if e.strip()]

def load_click_history() -> List[str]:
    """Load clicked paper titles for personalization."""
    ensure_file(PERSONALIZATION_FILE)
    with open(PERSONALIZATION_FILE, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def update_keyword_weights(clicked_titles: Iterable[str]) -> Tuple[Dict[str, float], Dict[str, float]]:
    """
    Learn keyword weights from click history.
    Each phrase match yields +0.1 weight; returns weight dict and normalized stats.
    """
    weights: Dict[str, float] = defaultdict(float)
    title_texts = [title.lower() for title in clicked_titles]
    for phrase in ALL_KEYWORDS:
        phrase_l = phrase.lower()
        for title in title_texts:
            if phrase_l in title:
                weights[phrase] += 0.1
    total_weight = sum(weights.values()) or 1.0
    normalized = {phrase: round(weight / total_weight, 3) for phrase, weight in weights.items()}
    return dict(weights), normalized


def nlp_score_keyword_only(text: str, learned_weights: Dict[str, float]) -> float:
    if not text or not text.strip():
        return 0.0

    tokens = [t.lower() for t in re.findall(r"\w+", text.lower())]
    score = 0.0

    for phrase in ALL_KEYWORDS:
        phrase_tokens = [t.lower() for t in phrase.lower().split()]
        for i in range(len(tokens) - len(phrase_tokens) + 1):
            if tokens[i:i + len(phrase_tokens)] == phrase_tokens:
                group = KEYWORD_TO_GROUP.get(phrase.lower(), "")
                if group in ML_RF_GROUPS or has_priority_topic({"title": phrase, "summary": ""}):
                    base_weight = GROUP_WEIGHT_RF
                elif group in HERITAGE_OPTICS_GROUPS:
                    base_weight = GROUP_WEIGHT_HERITAGE
                else:
                    base_weight = GROUP_WEIGHT_DEFAULT
                score += base_weight * (1.0 + learned_weights.get(phrase, 0.0))
                break

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text] + ALL_KEYWORDS)
    sim_score = cosine_similarity(tfidf[0:1], tfidf[1:]).max()

    keyword_score = score + sim_score * 2.0
    return max(0.0, min(10.0, keyword_score))


def semantic_similarity_score(text: str) -> float:
    if not text or not text.strip() or SEMANTIC_MODEL is None or RESEARCH_EMBEDDING is None:
        return 0.0
    try:
        truncated = " ".join(text.split()[:400])
        embedding = SEMANTIC_MODEL.encode(truncated, convert_to_numpy=True)
        ref_vec = np.asarray(RESEARCH_EMBEDDING)
        if np.linalg.norm(embedding) == 0 or np.linalg.norm(ref_vec) == 0:
            return 0.0
        similarity = float(np.dot(ref_vec, embedding) / (np.linalg.norm(ref_vec) * np.linalg.norm(embedding)))
        score = similarity * 15.0
        return max(0.0, min(10.0, score))
    except Exception as exc:
        logger.warning("Semantic scoring failed: %s", exc)
        return 0.0


def nlp_score(text: str, learned_weights: Dict[str, float]) -> float:
    keyword_only = nlp_score_keyword_only(text, learned_weights)
    semantic = semantic_similarity_score(text)
    if semantic == 0.0 and (SEMANTIC_MODEL is None or RESEARCH_EMBEDDING is None):
        return keyword_only
    return max(0.0, min(10.0, 0.7 * semantic + 0.3 * keyword_only))

def enhanced_score(paper: dict, now: datetime, learned_weights: Dict[str, float]) -> float:
    """
    Combine NLP score with citation-based boost.
    Older (>2 years) highly cited (>100) papers get additional credit,
    capped at +5 to avoid overpowering recent work.
    """
    text = f"{paper.get('title', '')} {paper.get('summary', '')}"
    base_score = nlp_score(text, learned_weights)
    citations = paper.get("citations", 0) or 0
    published: datetime = paper.get("published", now)
    age_years = max(0, (now - published).days / 365.25)
    boost = 0.0
    if age_years >= 2 and citations >= 100:
        boost = min(5.0, math.log10(citations + 1) * 1.5)
    return max(0.0, min(10.0, base_score + boost))


def generate_daily_task(current_date, papers: List[dict]) -> Dict[str, str]:
    """Return a rotating daily skill-building task informed by current papers."""
    if isinstance(current_date, datetime):
        day_index = current_date.date().toordinal()
    else:
        day_index = current_date.toordinal()

    top_papers = sorted(papers, key=lambda x: x.get("score", 0), reverse=True)[:3]
    paper_titles = [p.get("title", "Untitled")[:60] + "..." for p in top_papers if p.get("title")]

    task_keys = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    selected_key = task_keys[day_index % len(task_keys)]

    related_defaults = {
        "Monday": "See RF Systems & Nonlinear Phenomena section for signal processing papers",
        "Tuesday": "See Cultural Heritage section for imaging papers",
        "Wednesday": "See RF Systems section for nonlinear/harmonic radar papers",
        "Thursday": "See Cultural Heritage section for spectroscopy papers",
        "Friday": "See Adjacent Opportunities section for precision ag or commercial sensing",
        "Saturday": "See RF Systems section for measurement papers",
        "Sunday": "See Cultural Heritage section for advanced imaging papers",
    }

    tasks = {
        "Monday": {
            "domain": "RF Signal Processing",
            "skill": "Digital Signal Processing Fundamentals",
            "task": "Implement a matched filter for pulse compression",
            "time": "30 minutes",
            "difficulty": "Intermediate",
            "description": """
Today's focus: **RF Signal Processing Fundamentals**

**30-minute task:** Implement matched filter detection for a chirped radar pulse.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, correlate

# Generate chirped pulse (LFM waveform)
fs = 1e6  # 1 MHz sampling
duration = 10e-6  # 10 microseconds
t = np.arange(0, duration, 1/fs)
f0, f1 = 5e6, 15e6  # 5-15 MHz sweep
pulse = chirp(t, f0, duration, f1, method='linear')

# Add noise and simulate received signal
SNR_dB = -10
noise = np.random.randn(len(pulse))
signal_power = np.mean(pulse**2)
noise_power = signal_power / (10**(SNR_dB/10))
received = pulse + np.sqrt(noise_power) * noise

# Matched filter (correlate with template)
matched_output = correlate(received, pulse, mode='same')

# Plot
plt.figure(figsize=(12,4))
plt.subplot(131); plt.plot(t*1e6, pulse); plt.title('Transmitted Pulse'); plt.xlabel('Time (μs)')
plt.subplot(132); plt.plot(t*1e6, received); plt.title(f'Received (SNR={SNR_dB}dB)'); plt.xlabel('Time (μs)')
plt.subplot(133); plt.plot(t*1e6, np.abs(matched_output)); plt.title('Matched Filter Output'); plt.xlabel('Time (μs)')
plt.tight_layout(); plt.savefig('matched_filter.png'); plt.show()

# Calculate processing gain
print(f"Processing gain: {10*np.log10(len(pulse)):.1f} dB")
```

**Why this matters:** Matched filtering is fundamental to radar detection, giving you processing gain equal to the time-bandwidth product. This is the basis for pulse compression radar used in SAR, automotive radar, and GPR.

**Extensions:**
- Try different waveforms: Barker codes, Golay codes, OFDM
- Add Doppler shift to simulate moving targets
- Implement range-Doppler processing

**Related to today's papers:**
__RELATED_PAPERS__

**Resources:**
- Richards, "Fundamentals of Radar Signal Processing" Chapter 4
- MATLAB Radar Toolbox examples
- GNU Radio pulse compression tutorials
            """,
        },
        "Tuesday": {
            "domain": "Art Conservation Science",
            "skill": "Optical Imaging Fundamentals",
            "task": "Analyze multispectral reflectance data",
            "time": "30 minutes",
            "difficulty": "Intermediate",
            "description": """
Today's focus: **Art Conservation Optical Imaging**

**30-minute task:** Process multispectral image data to identify pigment candidates.
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Simulate multispectral image (or load real data)
# Real data: download from RIT Munsell Color Science Lab or use your own
wavelengths = np.array([400, 450, 500, 550, 600, 650, 700, 750, 800])  # nm
height, width = 100, 100

# Simulate different pigment spectra
ultramarine_blue = np.array([0.05, 0.08, 0.15, 0.35, 0.45, 0.40, 0.35, 0.30, 0.28])
vermillion_red = np.array([0.10, 0.12, 0.15, 0.25, 0.60, 0.80, 0.85, 0.85, 0.83])
lead_white = np.array([0.85, 0.87, 0.88, 0.89, 0.90, 0.90, 0.90, 0.89, 0.88])

# Create synthetic image with three regions
image_cube = np.zeros((height, width, len(wavelengths)))
image_cube[:40, :40, :] = ultramarine_blue
image_cube[60:, :40, :] = vermillion_red
image_cube[:, 60:, :] = lead_white
image_cube += 0.05 * np.random.randn(height, width, len(wavelengths))  # noise

# Reshape for analysis
pixels = image_cube.reshape(-1, len(wavelengths))

# PCA for dimensionality reduction
pca = PCA(n_components=3)
pca_result = pca.fit_transform(pixels)
pca_image = pca_result.reshape(height, width, 3)

# Visualize
plt.figure(figsize=(15,5))

# RGB approximation (bands 5,3,1 for R,G,B)
rgb_approx = np.dstack([image_cube[:,:,5], image_cube[:,:,3], image_cube[:,:,1]])
rgb_approx = (rgb_approx - rgb_approx.min()) / (rgb_approx.max() - rgb_approx.min())
plt.subplot(141); plt.imshow(rgb_approx); plt.title('RGB Approximation'); plt.axis('off')

# Show individual bands
plt.subplot(142); plt.imshow(image_cube[:,:,0], cmap='gray'); plt.title('400nm (UV)'); plt.axis('off')
plt.subplot(143); plt.imshow(image_cube[:,:,4], cmap='gray'); plt.title('600nm (Red)'); plt.axis('off')

# PCA false color
pca_rgb = (pca_image - pca_image.min()) / (pca_image.max() - pca_image.min())
plt.subplot(144); plt.imshow(pca_rgb); plt.title('PCA False Color'); plt.axis('off')

plt.tight_layout(); plt.savefig('multispectral_analysis.png'); plt.show()

# Plot spectral signatures
plt.figure(figsize=(10,6))
sample_spectra = [
    pixels[2000],  # blue region
    pixels[7000],  # red region  
    pixels[500]    # white region
]
for i, spectrum in enumerate(sample_spectra):
    plt.plot(wavelengths, spectrum, 'o-', label=f'Sample {i+1}', linewidth=2)
plt.xlabel('Wavelength (nm)', fontsize=12)
plt.ylabel('Reflectance', fontsize=12)
plt.title('Extracted Spectral Signatures', fontsize=14)
plt.legend(); plt.grid(True, alpha=0.3)
plt.savefig('spectral_signatures.png'); plt.show()

print(f"Explained variance: {pca.explained_variance_ratio_}")
```

**Why this matters:** Multispectral imaging reveals pigments invisible to the naked eye. UV/IR reflectance can detect underdrawings, retouching, and distinguish chemically similar pigments.

**Real-world application:**
- Identify modern vs historical pigments (TiO2 white invented 1920s)
- Detect pentimenti (artist changes) via differential spectral response
- Map pigment degradation (e.g., lead white darkening)

**Next steps:**
- Compare against reference spectral libraries (IRUG, Kremer Pigmente)
- Try spectral angle mapper (SAM) or spectral correlation mapper (SCM)
- Add spatial texture analysis for brushstroke characterization

**Related to today's papers:**
__RELATED_PAPERS__

**Resources:**
- Delaney et al., "Visible and Infrared Imaging Spectroscopy of Picasso's Harlequin Musician"
- CHARISMA project datasets: http://www.charismaproject.eu/
- RIT Munsell Color Science Lab spectral database
            """,
        },
        "Wednesday": {
            "domain": "Harmonic & Nonlinear Radar",
            "skill": "Nonlinear System Characterization",
            "task": "Model and detect harmonic generation",
            "time": "30 minutes",
            "difficulty": "Advanced",
            "description": """
Today's focus: **Harmonic Radar & Nonlinear Systems**

**30-minute task:** Characterize nonlinear RF component using harmonic balance analysis.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# Simulate nonlinear RF component (e.g., diode, amplifier in compression)
def nonlinear_device(x, coeffs):
    '''Polynomial nonlinearity: y = a1*x + a2*x**2 + a3*x**3 + ...'''
    return sum(c * x**i for i, c in enumerate(coeffs, 1))

# True device parameters (unknown in practice)
true_coeffs = [1.0, 0.15, -0.05, 0.01]  # Linear, 2nd, 3rd, 4th order

# Generate training data: multi-tone input
fs = 100e6  # 100 MHz sampling
duration = 100e-6  # 100 microseconds
t = np.arange(0, duration, 1/fs)

# Two-tone test (classic IMD measurement)
f1, f2 = 10e6, 12e6  # 10 and 12 MHz
A1, A2 = 0.5, 0.5
x_input = A1 * np.sin(2*np.pi*f1*t) + A2 * np.sin(2*np.pi*f2*t)

# Measured output (through nonlinear device + noise)
y_measured = nonlinear_device(x_input, true_coeffs)
y_measured += 0.02 * np.random.randn(len(y_measured))  # Add noise

# Identification: estimate coefficients
def model_error(coeffs, x, y):
    y_pred = nonlinear_device(x, coeffs)
    return y_pred - y

# Initial guess
x0 = [1.0, 0.0, 0.0, 0.0]

# Solve
result = least_squares(model_error, x0, args=(x_input, y_measured), verbose=0)
estimated_coeffs = result.x

print("True coefficients:", true_coeffs)
print("Estimated coefficients:", estimated_coeffs)
print("Estimation error:", np.linalg.norm(np.array(true_coeffs) - estimated_coeffs))

# Analyze spectrum
from scipy.fft import rfft, rfftfreq


def plot_spectrum(signal, fs, title):
    N = len(signal)
    spectrum = np.abs(rfft(signal))
    freqs = rfftfreq(N, 1/fs)

    plt.semilogy(freqs/1e6, spectrum)
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Magnitude')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 30)

plt.figure(figsize=(15,5))

plt.subplot(131)
plot_spectrum(x_input, fs, 'Input Spectrum (Two Tones)')
plt.axvline(f1/1e6, color='r', linestyle='--', alpha=0.5, label='f1')
plt.axvline(f2/1e6, color='r', linestyle='--', alpha=0.5, label='f2')

plt.subplot(132)
plot_spectrum(y_measured, fs, 'Output Spectrum (with Harmonics & IMD)')
# Mark harmonics and IMD products
plt.axvline(f1/1e6, color='r', linestyle='--', alpha=0.5)
plt.axvline(f2/1e6, color='r', linestyle='--', alpha=0.5)
plt.axvline(2*f1/1e6, color='orange', linestyle=':', alpha=0.5, label='2f1')
plt.axvline(2*f2/1e6, color='orange', linestyle=':', alpha=0.5, label='2f2')
plt.axvline((2*f1-f2)/1e6, color='g', linestyle=':', alpha=0.5, label='IMD3')
plt.axvline((2*f2-f1)/1e6, color='g', linestyle=':', alpha=0.5, label='IMD3')

# Reconstructed output
y_reconstructed = nonlinear_device(x_input, estimated_coeffs)
plt.subplot(133)
plot_spectrum(y_reconstructed, fs, 'Reconstructed Spectrum (Estimated Model)')

plt.tight_layout()
plt.savefig('harmonic_analysis.png')
print('Total Harmonic Distortion: analysis pending')
```

**Why this matters:**
- Characterizing nonlinear behavior is critical for RF component diagnostics
- Harmonic generation enables harmonic radar for tagging/tracking
- IMD products cause interference in wireless systems
- Your nonlinear reflections research directly applies here

**Applications:**
- Detect damaged RF components from abnormal harmonic signatures
- Design harmonic tags for wildlife tracking
- Test 5G/6G components for linearity requirements
- Identify faulty connections via passive intermodulation (PIM)

**Extensions:**
- Implement Volterra series model (memory effects)
- Try X-parameters for large-signal characterization
- Measure actual components with VNA + signal analyzer

**Related to today's papers:**
__RELATED_PAPERS__

**Resources:**
- Pedro & Carvalho, "Intermodulation Distortion in Microwave and Wireless Circuits"
- Your PhD thesis section on harmonic characterization
- Agilent AN1420: Nonlinear Vector Network Analyzer (NVNA)
            """,
        },
        "Thursday": {
            "domain": "Art Conservation Science",
            "skill": "Spectroscopy & Chemical Analysis",
            "task": "Analyze XRF/Raman spectroscopy data",
            "time": "30 minutes",
            "difficulty": "Intermediate",
            "description": """
Today's focus: **Spectroscopy & Chemical Analysis for Art**

**30-minute task:** Identify pigments from simulated XRF and Raman spectroscopy data.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Simulate XRF spectrum (Energy vs Counts)
# Common elements in historical pigments
energies = np.linspace(0, 40, 4000)  # keV


def xrf_peak(energy, center, intensity, width=0.15):
    '''Gaussian peak for XRF emission line'''
    return intensity * np.exp(-((energy - center) / width)**2)

# Lead white (Pb): Pb L-alpha at 10.55 keV, L-beta at 12.61 keV
# Ultramarine (Na, Al, Si, S): S K-alpha at 2.31 keV, Si K-alpha at 1.74 keV
# Vermillion (HgS): Hg L-alpha at 9.99 keV, S K-alpha at 2.31 keV
# Prussian blue (Fe): Fe K-alpha at 6.40 keV, Fe K-beta at 7.06 keV

spectrum = np.zeros_like(energies)

# Simulate mixture: Lead white + Ultramarine
spectrum += xrf_peak(energies, 10.55, 8000)  # Pb L-alpha (strong)
spectrum += xrf_peak(energies, 12.61, 3000)  # Pb L-beta
spectrum += xrf_peak(energies, 2.31, 1500)   # S K-alpha
spectrum += xrf_peak(energies, 1.74, 2000)   # Si K-alpha
spectrum += xrf_peak(energies, 1.49, 1000)   # Al K-alpha

# Add background and noise
background = 200 + 150 * np.exp(-energies/10)
spectrum += background
spectrum += np.random.poisson(np.sqrt(np.maximum(spectrum, 0)))

# Peak detection
peaks, _ = find_peaks(spectrum, height=500, distance=20, prominence=200)

# Further analysis here...
```

**Why this matters:**
- XRF is non-destructive and can be done on-site in museums
- Elemental composition fingerprints pigments
- Crucial for authentication (modern pigments have different elements)
- Pentimenti detection: hidden layers have different chemistry

**Related to today's papers:**
__RELATED_PAPERS__

**Resources:**
- Alfeld et al., "A mobile instrument for in situ scanning macro-XRF"
- IRUG Spectral Database: http://www.irug.org/
- Getty Conservation Institute: Analytical methods resources
            """,
        },
        "Friday": {
            "domain": "Adjacent Opportunities",
            "skill": "Cross-domain Applications",
            "task": "Explore commercial or climate applications",
            "time": "30 minutes",
            "difficulty": "Intermediate",
            "description": """
Today's focus: **Adjacent Opportunities - Commercial & Climate Applications**

**30-minute task:** Design a precision agriculture radar system concept.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Scenario: FMCW radar for crop height/biomass monitoring
# Frequency: 24 GHz ISM band (license-free for low-power applications)

# FMCW parameters
c = 3e8  # speed of light (m/s)
fc = 24e9  # center frequency (24 GHz)
B = 200e6  # bandwidth (200 MHz) → range resolution = c/(2*B) = 0.75m
T_chirp = 1e-3  # chirp duration (1 ms)
fs = 10e6  # ADC sampling rate (10 MHz)

# Additional simulation content...
```

**Why this is a good adjacent opportunity:**
1. Uses your RF signal processing expertise
2. Harmonic radar for pest tracking is a natural extension
3. Large commercial market with clear value proposition
4. Leverages defense radar technology for civilian use
5. Fundable via SBIR/STTR (USDA, NSF)

**Related to today's papers:**
__RELATED_PAPERS__

**Resources:**
- IEEE GRSS Precision agriculture papers
- Precision Agriculture journal (Springer)
- Microsoft FarmBeats platform
            """,
        },
        "Saturday": {
            "domain": "RF Test & Measurement",
            "skill": "Vector Network Analyzer Fundamentals",
            "task": "Simulate VNA S-parameter measurement",
            "time": "30 minutes",
            "difficulty": "Advanced",
            "description": """
Today's focus: **RF Test Equipment & Measurements**

**30-minute task:** Simulate VNA measurement and calibration.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# Simulate a device under test (DUT): simple filter + transmission line
# ... additional code ...
```

**Why this matters:**
- VNA is the foundational tool for RF component testing
- Accurate calibration underpins diagnostics and production testing
- Directly supports your RF health monitoring work

**Related to today's papers:**
__RELATED_PAPERS__

**Resources:**
- Keysight VNA Basics course
- Agilent AN 1287-1 application note
- Dunsmore, "Handbook of Microwave Component Measurements"
            """,
        },
        "Sunday": {
            "domain": "Art Conservation Science",
            "skill": "Advanced Imaging & Pentimenti",
            "task": "Detect and visualize hidden layers",
            "time": "30 minutes",
            "difficulty": "Advanced",
            "description": """
Today's focus: **Pentimenti & Hidden Layer Detection**

**30-minute task:** Simulate multi-layer painting analysis to reveal artist changes.
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from skimage import feature, filters

# Simulate a painting with hidden layers (pentimenti)
# ... extended code ...
```

**Why pentimenti matter:**
- Authentication: forgers rarely create convincing pentimenti
- Art history: reveals an artist's working method
- Conservation: guides treatment decisions

**Related to today's papers:**
__RELATED_PAPERS__

**Resources:**
- Getty Conservation Institute imaging workshops
- National Gallery technical bulletins
- ICOM-CC conservation imaging guidelines
            """,
        },
    }

    selected = tasks.get(selected_key, tasks["Monday"]).copy()
    related_text = ", ".join(paper_titles) if paper_titles else related_defaults.get(selected_key, "Recent papers")
    selected["description"] = selected["description"].replace("__RELATED_PAPERS__", related_text)
    selected["day"] = selected_key
    return selected

def classify_paper_topic(paper: dict) -> Tuple[str, float, List[Tuple[str, int]]]:
    """Classify a paper into RF, cultural heritage, or adjacent categories."""
    score = paper.get("score", 0)
    title = (paper.get("title", "") or "").lower()
    abstract = (paper.get("summary", "") or "").lower()
    text = f"{title} {abstract}"

    rf_indicators = {
        'nonlinear_rf': [
            'nonlinear', 'intermodulation', 'harmonic generation',
            'passive intermodulation', 'pim', 'imd', 'volterra series',
            'behavioral model', 'nonlinear distortion', 'third order intercept',
            'harmonic balance', 'nonlinear scattering', 'nonlinear reflection'
        ],
        'rf_diagnostics': [
            'rf component', 'microwave component', 'component characterization',
            'component identification', 'rf health monitoring', 'component damage',
            'rf diagnostic', 'fault detection rf', 'anomaly detection rf',
            'predictive maintenance rf', 'component aging', 'degradation detection'
        ],
        'harmonic_radar': [
            'harmonic radar', 'harmonic tag', 'harmonic transponder',
            'nonlinear radar', 'rfid harmonic', 'wildlife tracking radar',
            'harmonic scattering', 'second harmonic radar', 'third harmonic'
        ],
        'automotive_radar': [
            'automotive radar', '77 ghz', '79 ghz', 'fmcw radar automotive',
            'adas radar', 'vehicle radar', 'collision avoidance radar',
            'automotive sensor', 'radar calibration automotive', 'mimo radar automotive'
        ],
        '5g_6g_hardware': [
            '5g diagnostic', '6g infrastructure', 'base station component',
            'rf front-end test', 'mmwave diagnostic', '5g component test',
            'beamforming hardware', 'massive mimo hardware', 'rf beamformer'
        ],
        'rf_measurement': [
            'vector network analyzer', 'vna', 'automated test equipment', 'ate',
            'rf measurement', 'microwave measurement', 'scattering parameter',
            's-parameter', 'network analyzer', 'spectrum analyzer rf'
        ],
        'rf_signal_processing': [
            'rf signal processing', 'radar signal processing', 'microwave signal',
            'rf detection', 'radar detection', 'pulse compression',
            'matched filter radar', 'cfar detection', 'target detection radar'
        ],
        'power_amplifiers': [
            'power amplifier', 'high-power microwave', 'hpm', 'amplifier linearization',
            'digital predistortion', 'dpd', 'amplifier characterization',
            'power amplifier nonlinear', 'rf power', 'transmitter linearity'
        ],
        'gpr': [
            'ground penetrating radar', 'gpr', 'subsurface radar',
            'ground-probing radar', 'archaeological radar', 'utility detection radar'
        ],
    }

    heritage_indicators = {
        'cultural_heritage': [
            'cultural heritage', 'heritage conservation', 'heritage science',
            'heritage materials', 'heritage digitization', 'heritage preservation',
            'archaeological conservation', 'museum science', 'conservation science'
        ],
        'optical_techniques': [
            'optical coherence tomography art', 'oct painting', 'oct conservation',
            'hyperspectral art', 'hyperspectral cultural heritage', 'multispectral art',
            'infrared reflectography', 'uv fluorescence art', 'uv imaging art',
            'reflectance imaging spectroscopy art', 'multimodal imaging art',
            'optical imaging art', 'optical techniques art', 'optical methods conservation',
            'spectral imaging art', 'imaging spectroscopy art', 'optical characterization art'
        ],
        'spectroscopy_analysis': [
            'xrf art', 'x-ray fluorescence art', 'xrf mapping', 'macro-xrf',
            'raman spectroscopy pigment', 'raman pigment', 'raman art',
            'ftir art', 'ftir spectroscopy art', 'libs cultural heritage',
            'spectroscopy conservation', 'spectroscopy art',
            'pigment identification', 'pigment analysis', 'binder analysis',
            'material characterization art', 'chemical analysis art'
        ],
        'paint_analysis': [
            'paint layer', 'stratigraphy', 'brushstroke', 'impasto',
            'pentimenti', 'underdrawing', 'artist technique', 'painting technique',
            'canvas analysis', 'craquelure', 'surface topology painting',
            'paint layer analysis', 'layer structure art'
        ],
        'conservation_science': [
            'conservation science', 'art conservation', 'heritage conservation',
            'preventive conservation', 'condition assessment art',
            'cleaning verification', 'treatment monitoring art',
            'consolidation monitoring', 'museum conservation',
            'conservation monitoring', 'art restoration', 'heritage restoration'
        ],
        'authentication': [
            'art authentication', 'forgery detection', 'artist attribution',
            'provenance research', 'dating artwork', 'signature analysis art',
            'technical art history', 'workshop practice', 'connoisseurship',
            'artwork authentication', 'painting authentication'
        ],
        'heritage_materials': [
            # NOTE: These keywords can match general materials papers
            # The classification logic below REQUIRES art/heritage context for these to count
            'historic pigment', 'traditional pigment', 'pigment degradation',
            'varnish characterization', 'binding media', 'support material art',
            'heritage materials', 'art materials', 'painting materials',
            # Specific historical pigments (these are art-specific)
            'lead white', 'ultramarine blue', 'vermillion', 'azurite',
            'cadmium yellow', 'titanium white', 'prussian blue',
            'historical materials', 'traditional materials art',
            # Art-specific material analysis (these require art context to be meaningful)
            'pigment identification', 'pigment analysis', 'binder analysis',
            'paint layer', 'canvas analysis', 'varnish',
        ],
        'photoacoustics': [
            'photoacoustic art', 'photoacoustic imaging art', 'photoacoustic heritage',
            'photoacoustic conservation', 'photoacoustic spectroscopy art',
            'optoacoustic art', 'optoacoustic imaging art'
        ],
        'ml_heritage': [
            'machine learning art', 'deep learning art', 'neural network art',
            'ml cultural heritage', 'ai art conservation', 'machine learning heritage',
            'deep learning conservation', 'cnn art', 'transformer art',
            'ml signal processing art', 'ml image processing art',
            'artificial intelligence art', 'ai heritage', 'ml painting'
        ],
        'advanced_imaging': [
            'terahertz imaging art', 'terahertz art', 'thz imaging art',
            'confocal microscopy art', 'two-photon art',
            'second harmonic generation art', 'shg art',
            'third harmonic generation art', 'nonlinear optical microscopy art',
            'ptychography', 'ptychography art', 'digital holography art',
            'structured light art', 'fringe projection art'
        ],
        '3d_heritage': [
            'laser scanning artwork', '3d scanning heritage', 'photogrammetry art',
            'structured light 3d art', 'fringe projection art',
            'digital documentation heritage', '3d reconstruction art',
            'heritage digitization', 'virtual museum', '3d heritage',
            'digital heritage', 'heritage 3d'
        ],
        'digital_humanities': [
            'digital humanities', 'computational art history', 'digital art history',
            'heritage informatics', 'cultural heritage informatics',
            'digital archaeology', 'computational heritage',
            'heritage data', 'art data', 'museum data'
        ],
        'optics_fundamentals': [
            'optics art', 'optical properties art', 'light scattering art',
            'reflectance art', 'transmittance art', 'absorption art',
            'optical characterization art', 'spectroscopic properties art',
            'colorimetry art', 'color science art', 'optical measurements art'
        ],
        'microscopy': [
            'sem pigment', 'scanning electron microscopy art', 'optical microscopy art',
            'cross-section analysis', 'microprobe analysis art', 'afm painting',
            'atomic force microscopy art', 'electron microscopy conservation',
            'microscopy art', 'microscopy conservation'
        ],
    }

    adjacent_indicators = {
        'harmonic_applications': [
            'pollinator monitoring', 'insect tracking radar', 'wildlife telemetry',
            'animal movement tracking', 'biodiversity monitoring radar',
            'pest detection radar', 'harmonic tag wildlife'
        ],
        'climate_monitoring': [
            'climate monitoring radar', 'environmental monitoring remote sensing',
            'glacier monitoring', 'ice sheet radar', 'soil moisture radar',
            'drought monitoring', 'precipitation monitoring', 'weather radar'
        ],
        'commercial_rf': [
            'infrastructure monitoring', 'structural health monitoring',
            'bridge inspection radar', 'pipeline monitoring', 'smart city sensor',
            'iot sensor network', 'wireless sensor network', 'industrial iot'
        ],
        'autonomous_vehicles': [
            'autonomous vehicle', 'self-driving', 'lidar radar fusion',
            'sensor fusion autonomous', 'perception system', 'object detection vehicle',
            'collision avoidance', 'adas', 'autonomous navigation'
        ],
        'precision_agriculture': [
            'precision agriculture', 'smart farming', 'crop monitoring',
            'agricultural sensor', 'yield prediction', 'soil sensing',
            'irrigation management', 'variable rate application', 'farm automation'
        ],
        'ml_applications': [
            'deep learning signal processing', 'neural network rf',
            'cnn signal processing', 'transformer signal', 'machine learning radar',
            'ai signal processing', 'deep learning imaging', 'neural network imaging'
        ],
        'disaster_response': [
            'disaster response', 'search and rescue radar', 'earthquake damage',
            'flood mapping', 'wildfire detection', 'landslide monitoring',
            'through-wall radar', 'emergency response sensor'
        ],
        'sar_satellite': [
            'synthetic aperture radar', 'sar processing', 'insar', 'interferometry',
            'satellite remote sensing', 'sentinel radar', 'radar altimetry'
        ],
        'pedagogy_architecture': [
            'pedagogical tree', 'knowledge graph', 'concept mapping',
            'curriculum ontology', 'educational taxonomy', 'learning progression',
            'architectural pedagogy', 'design thinking', 'studio pedagogy'
        ],
        'advanced_dsp': [
            'compressed sensing', 'sparse representation', 'inverse problem',
            'image reconstruction', 'super-resolution', 'phase retrieval',
            'blind deconvolution', 'dictionary learning', 'matrix completion'
        ],
    }

    def compute_subscore(indicators: Dict[str, List[str]]) -> Tuple[int, List[Tuple[str, int]]]:
        subscore = 0
        subcats: List[Tuple[str, int]] = []
        for subcat, keywords in indicators.items():
            matches = sum(1 for kw in keywords if kw in text)
            if matches > 0:
                subscore += matches
                subcats.append((subcat, matches))
        return subscore, subcats

    rf_subscore, rf_subcategories = compute_subscore(rf_indicators)
    heritage_subscore, heritage_subcategories = compute_subscore(heritage_indicators)
    adjacent_subscore, adjacent_subcategories = compute_subscore(adjacent_indicators)

    # CRITICAL: Require explicit heritage context FIRST - these terms indicate heritage/art applications
    # ALL heritage papers MUST have art/heritage context - this is checked BEFORE any other processing
    heritage_context_terms = [
        # Direct heritage terms
        "cultural heritage", "heritage conservation", "heritage science",
        "heritage materials", "heritage digitization", "heritage preservation",
        "art conservation", "art restoration", "museum conservation",
        "conservation science", "conservation monitoring", "preventive conservation",
        "art authentication", "forgery detection", "artist attribution",
        "provenance research", "dating artwork", "technical art history",
        # Art-specific terms (CORE - these are required for heritage classification)
        "art ", "artwork", "artworks", "painting", "paintings", 
        "canvas", "museum", "museums", "gallery", "galleries",
        "artist", "artistic", "artists", "conservator", "conservators",
        # Painting-specific terms
        "pentimento", "pentimenti", 
        "underdrawing", "underdrawings",
        "brushstroke", "brushstrokes", "brush strokes", "brush stroke",
        # Heritage materials
        "pigment identification", "pigment analysis", "pigment degradation",
        "stratigraphy art", "paint layer", "varnish characterization", "binding media",
        "historic pigment", "traditional pigment", "heritage materials",
        # Optical techniques with heritage context
        "oct art", "oct painting", "oct conservation",
        "xrf art", "xrf painting", "xrf cultural heritage", "xrf mapping art",
        "raman art", "raman painting", "raman pigment", "raman spectroscopy art",
        "hyperspectral art", "hyperspectral cultural heritage",
        "multispectral art", "multispectral cultural heritage",
        "infrared reflectography", "uv fluorescence art", "uv imaging art",
        "photoacoustic art", "photoacoustic imaging art", "photoacoustic heritage",
        "terahertz imaging art", "terahertz art",
        # Digital humanities
        "digital humanities", "computational art history", "digital art history",
        "heritage informatics", "digital archaeology", "computational heritage",
        # 3D heritage
        "3d scanning heritage", "3d reconstruction art", "heritage digitization",
        "virtual museum", "digital heritage", "photogrammetry art",
        # ML with heritage context
        "machine learning art", "deep learning art", "ml cultural heritage",
        "ai art conservation", "machine learning heritage", "cnn art",
        # General heritage indicators
        "archaeological conservation", "museum science", "heritage restoration",
    ]
    
    # Check for heritage context - require at least one explicit heritage term
    has_heritage_context = any(term in text for term in heritage_context_terms)
    
    # CRITICAL REQUIREMENT: ALL heritage papers MUST mention paintings, artwork, art, museum, or gallery
    # Strong art terms (primary indicators - these alone are sufficient)
    strong_art_terms = [
        # Core art terms (REQUIRED for heritage classification)
        r'\bart\b', r'\bartwork\b', r'\bartworks\b', 
        r'\bpainting\b', r'\bpaintings\b', 
        r'\bmuseum\b', r'\bmuseums\b',
        # Artist and artistic terms
        r'\bgallery\b', r'\bgalleries\b', r'\bartist\b', r'\bartistic\b', r'\bartists\b',
        r'\bcanvas\b', r'\bconservator\b', r'\bconservators\b',
        # Painting-specific terms
        r'\bpentimento\b', r'\bpentimenti\b',
        r'\bunderdrawing\b', r'\bunderdrawings\b',
        r'\bbrushstroke\b', r'\bbrushstrokes\b', r'\bbrush strokes\b', r'\bbrush stroke\b',
        # Authentication and art history
        r'\bforgery detection\b', r'\bartist attribution\b', r'\bdating artwork\b',
        r'\btechnical art history\b',
        # Conservation and restoration
        r'\bart conservation\b', r'\bart restoration\b', r'\bart authentication\b',
        # Imaging techniques with art context
        r'\boct painting\b', r'\bxrf painting\b', r'\braman painting\b',
        r'\bhyperspectral art\b', r'\bmultispectral art\b', r'\bphotoacoustic art\b',
        # Digital heritage
        r'\bvirtual museum\b', r'\bcomputational art history\b', r'\bdigital art history\b',
    ]
    
    # Art context phrases (must appear with "art" in context)
    art_context_phrases = [
        r'\bart conservation\b', r'\bart restoration\b', r'\bart authentication\b',
        r'\bart materials\b', r'\bpainting materials\b', r'\bart history\b',
        r'\bart science\b', r'\bart analysis\b', r'\bart imaging\b',
        r'\bmachine learning art\b', r'\bdeep learning art\b', r'\bcnn art\b',
        r'\bphotogrammetry art\b', r'\b3d reconstruction art\b',
    ]
    
    # Check for strong art terms OR art context phrases
    has_strong_art_term = any(re.search(pattern, text) for pattern in strong_art_terms)
    has_art_context_phrase = any(re.search(pattern, text) for pattern in art_context_phrases)
    
    # Also check for standalone "art" but require it appears with heritage context
    # CRITICAL: Only accept standalone "art" if it appears with explicit heritage context terms
    # to avoid false positives (e.g., "artificial", "part", "smart", etc.)
    has_standalone_art = bool(re.search(r'\bart\b', text))
    # Require explicit heritage context for standalone "art" - be very strict
    has_explicit_heritage_for_art = any(re.search(pattern, text) for pattern in [
        r'\bcultural heritage\b', r'\bheritage conservation\b', r'\bart conservation\b',
        r'\bart restoration\b', r'\bart authentication\b', r'\bmuseum\b', r'\bgallery\b',
        r'\bartwork\b', r'\bartworks\b', r'\bpainting\b', r'\bpaintings\b', 
        r'\bartist\b', r'\bartistic\b', r'\bartists\b',
        r'\bpentimento\b', r'\bpentimenti\b', r'\bunderdrawing\b', r'\bunderdrawings\b',
        r'\bbrushstroke\b', r'\bbrushstrokes\b', r'\bbrush strokes\b', r'\bbrush stroke\b',
    ])
    has_art_painting_context = has_strong_art_term or has_art_context_phrase or (has_standalone_art and has_explicit_heritage_for_art)
    
    # ABSOLUTE REQUIREMENT: If paper lacks art/painting/heritage context, it CANNOT be classified as heritage
    # This check happens FIRST, before any other processing
    # ALL heritage papers MUST have explicit art/heritage context - no exceptions
    if not has_art_painting_context and not has_heritage_context:
        # Paper has NO art/painting/heritage context - immediately exclude from heritage
        if heritage_subscore > 0:
            logger.debug(
                "EXCLUDING from heritage (no art/heritage context): %s (heritage_subscore=%d, subcategories=%s)",
                paper.get('title', '')[:60], heritage_subscore, [sc[0] for sc in heritage_subcategories]
            )
        heritage_subscore = 0
        heritage_subcategories = []
        has_heritage_context = False
    elif not has_art_painting_context:
        # Paper has heritage context but NO art/painting context - still exclude
        # Heritage papers MUST mention art, painting, museum, gallery, artist, etc.
        if heritage_subscore > 0:
            logger.debug(
                "EXCLUDING from heritage (heritage context but NO art/painting context): %s (heritage_subscore=%d)",
                paper.get('title', '')[:60], heritage_subscore
            )
        heritage_subscore = 0
        heritage_subcategories = []
        has_heritage_context = False
    
    # CRITICAL: Check if paper matches materials keywords WITHOUT art/heritage context
    # This is a secondary check for materials papers specifically
    generic_materials_keywords = [
        'binding media', 'varnish characterization', 'pigment degradation',
        'material characterization', 'materials science', 'polymer characterization',
        'coating characterization', 'surface characterization', 'material analysis',
        'spectroscopy materials', 'xrf materials', 'raman materials',
    ]
    has_generic_materials = any(kw in text for kw in generic_materials_keywords)
    
    # Exclude papers that are clearly NOT heritage
    # Check for remote sensing without heritage context
    has_remote_sensing_no_heritage = (
        ("remote sensing" in text or "satellite" in text) and
        not has_heritage_context and
        ("weather" in text or "precipitation" in text or "atmospheric" in text or
         "water level" in text or "reservoir" in text or "glacier" in text or
         "soil moisture" in text or "crop" in text or "agricultural" in text)
    )
    
    # Check for other non-heritage contexts
    has_medical_context = any(term in text for term in [
        "medical imaging", "patient", "clinical", "diagnosis", "tumor", "cancer"
    ])
    
    has_weather_context = any(term in text for term in [
        "weather radar", "precipitation monitoring", "atmospheric sensing",
        "thunderstorm", "storm", "meteorological"
    ])
    
    has_environmental_context = any(term in text for term in [
        "water level monitoring", "reservoir monitoring", "glacier monitoring",
        "soil moisture", "crop monitoring", "agricultural sensor"
    ])
    
    # SECONDARY CHECKS: Additional validation for edge cases
    # (The primary check above already excludes papers without art/heritage context)
    
    # If paper has non-heritage context and NO heritage context, exclude from heritage
    if (has_medical_context or has_weather_context or has_environmental_context or 
        has_remote_sensing_no_heritage) and not has_heritage_context and not has_art_painting_context:
        # Force to adjacent or unrelated if there's clear non-heritage context
        if heritage_subscore > 0:
            heritage_subscore = 0
            heritage_subcategories = []
    
    # FINAL VERIFICATION: Ensure heritage_subscore is 0 if paper lacks required context
    # This is a redundant check to ensure nothing slips through
    if heritage_subscore > 0:
        if not has_art_painting_context or not has_heritage_context:
            logger.warning(
                "FINAL CHECK: Excluding paper from heritage (missing required context): %s (has_art=%s, has_heritage=%s)",
                paper.get('title', '')[:60], has_art_painting_context, has_heritage_context
            )
            heritage_subscore = 0
            heritage_subcategories = []
            has_heritage_context = False

    paper['rf_subcategories'] = rf_subcategories
    paper['heritage_subcategories'] = heritage_subcategories
    paper['adjacent_subcategories'] = adjacent_subcategories

    rf_total = rf_subscore * 1.5 + (score if rf_subscore > 0 else 0)
    # Heritage requires: subscore > 0 AND heritage context AND art/painting context
    heritage_total = (
        (heritage_subscore * 1.5 + (score if heritage_subscore > 0 else 0))
        if (heritage_subscore > 0 and has_heritage_context and has_art_painting_context)
        else 0
    )
    adjacent_total = adjacent_subscore * 1.0 + (score if adjacent_subscore > 0 else 0)

    # Classification priority: RF > Heritage (with art/painting context) > Adjacent > Unrelated
    if rf_total > heritage_total and rf_total > adjacent_total and rf_subscore > 0:
        if rf_subscore >= 3:
            score = min(10, score + 1.0)
        return 'rf_systems', score, sorted(rf_subcategories, key=lambda x: x[1], reverse=True)
    
    # Heritage requires: subscore > 0 AND heritage context AND art/painting context
    if (heritage_total > rf_total and heritage_total > adjacent_total and 
        heritage_subscore > 0 and has_heritage_context and has_art_painting_context):
        if heritage_subscore >= 3:
            score = min(10, score + 1.0)
        return 'cultural_heritage', score, sorted(heritage_subcategories, key=lambda x: x[1], reverse=True)
    
    if adjacent_subscore > 0:
        score = max(0, score - 0.5)
        return 'adjacent', score, sorted(adjacent_subcategories, key=lambda x: x[1], reverse=True)
    return 'unrelated', max(0, score - 2.0), []

def short_summary(text: str, max_sent: int = 2) -> str:
    try:
        sents = re.split(r"(?<=[.!?]) +", text)
        if len(sents) <= max_sent:
            return text
        vec = TfidfVectorizer(stop_words="english")
        tfidf = vec.fit_transform(sents)
        sims = cosine_similarity(tfidf[-1:], tfidf).flatten()
        top = sims.argsort()[-max_sent:][::-1]
        return " ".join([sents[i] for i in sorted(top)])
    except Exception:
        return (text or "")[:300] + "..."

def abstract_preview(text: str, sentences: int = 3) -> str:
    """Return the first few sentences of an abstract for high-relevance highlights."""
    if not text:
        return ""
    sents = re.split(r"(?<=[.!?]) +", text)
    return " ".join(sents[:sentences])

def parse_feed(url: str):
    try:
        return feedparser.parse(url).entries
    except Exception as e:
        logger.error("Error parsing %s: %s", url, e)
        return []

def extract_pub_date(entry) -> datetime:
    dt_struct = entry.get("published_parsed") or entry.get("updated_parsed")
    if dt_struct:
        try:
            timestamp = feedparser.mktime_tz(dt_struct)
            return datetime.fromtimestamp(timestamp, tz=timezone.utc)
        except (TypeError, OverflowError, AttributeError):
            pass
    for key in ("published", "updated"):
        val = entry.get(key)
        if not val:
            continue
        try:
            dt = parsedate_to_datetime(val)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            else:
                dt = dt.astimezone(timezone.utc)
            return dt
        except (TypeError, ValueError):
            continue
    return None

def extract_crossref_date(item: dict) -> datetime:
    for key in ("published-print", "published-online", "issued", "created", "deposited"):
        date_info = item.get(key)
        if not date_info:
            continue
        parts = date_info.get("date-parts")
        if not parts:
            continue
        date_parts = parts[0]
        if not date_parts:
            continue
        year = date_parts[0]
        month = date_parts[1] if len(date_parts) > 1 else 1
        day = date_parts[2] if len(date_parts) > 2 else 1
        try:
            return datetime(year, month, day, tzinfo=timezone.utc)
        except ValueError:
            continue
    return None

def normalize_key(paper: dict) -> Tuple[str, str]:
    """Create a normalized key for a paper to detect duplicates.
    
    Returns (normalized_title, normalized_identifier) where:
    - normalized_title: lowercase title with normalized whitespace
    - normalized_identifier: DOI (if available) or normalized link
    """
    title = re.sub(r"\s+", " ", (paper.get("title") or "").strip().lower())
    
    # Try to extract DOI first
    doi = paper.get("doi") or ""
    link = paper.get("link") or ""
    
    # Normalize DOI: extract from URL or strip prefix
    if doi:
        doi = doi.strip().lower()
        # Extract DOI from URLs like https://doi.org/10.1234/abc or doi:10.1234/abc
        doi_match = re.search(r"(?:doi\.org/|doi:)?(10\.\d+/[^\s?#]+)", doi)
        if doi_match:
            identifier = doi_match.group(1)
        else:
            identifier = doi
    elif link:
        # Normalize link: remove query params, fragments, and normalize domain
        link = link.strip().lower()
        # Extract DOI from link if present
        doi_match = re.search(r"(?:doi\.org/|doi:)(10\.\d+/[^\s?#]+)", link)
        if doi_match:
            identifier = doi_match.group(1)
        else:
            # Use normalized link (remove query params and fragments)
            identifier = re.sub(r"[?#].*$", "", link)
    else:
        identifier = ""
    
    return title, identifier

def fetch_crossref_papers(year_start: int, year_end: int, needed: int, seen_keys: set,
                          keywords: Iterable[str] = None) -> List[dict]:
    """Backfill using CrossRef with citation counts."""
    if needed <= 0:
        return []
    fetched: List[dict] = []
    search_terms = list(keywords or ALL_KEYWORDS)
    for idx, phrase in enumerate(search_terms):
        if idx >= CROSSREF_MAX_KEYWORDS:
            break
        params = {
            "query": phrase,
            "rows": CROSSREF_ROWS_PER_KEYWORD,
            "filter": f"from-pub-date:{year_start}-01-01,until-pub-date:{year_end}-12-31",
            "select": "title,abstract,DOI,URL,author,issued,created,"
                      "published-print,published-online,deposited,subtitle,"
                      "container-title,is-referenced-by-count",
            "sort": "published",
            "order": "desc"
        }
        try:
            resp = request_with_backoff(CROSSREF_ENDPOINT, params=params, base_delay=1.0)
        except requests.RequestException as err:
            logger.warning("CrossRef request failed for '%s': %s", phrase, err)
            continue
        if not resp:
            continue
        items = resp.json().get("message", {}).get("items", [])
        candidates = []
        for item in items:
            title_list = item.get("title") or []
            title = title_list[0] if title_list else None
            if not title:
                continue
            published = extract_crossref_date(item)
            if not published:
                continue
            if not (year_start <= published.year <= year_end):
                continue
            doi = item.get("DOI")
            link = item.get("URL") or (f"https://doi.org/{doi}" if doi else "")
            key = normalize_key({"title": title, "doi": doi, "link": link})
            if key in seen_keys:
                continue
            abstract = item.get("abstract") or ""
            abstract = re.sub(r"<[^>]+>", "", abstract)
            if not abstract:
                subtitles = item.get("subtitle") or []
                abstract = " ".join(subtitles).strip()
            if not abstract:
                journal = ""
                container_titles = item.get("container-title") or []
                if container_titles:
                    journal = container_titles[0]
                abstract = f"Published in {journal} ({published.year})." if journal else f"Published in {published.year}."
            authors_data = item.get("author") or []
            authors = authors = ", ".join(
                " ".join(filter(None, [a.get("given"), a.get("family")])).strip()
                for a in authors_data if a
            )
            citations = item.get("is-referenced-by-count", 0) or 0
            paper = {
                "title": title,
                "summary": abstract,
                "link": link or f"https://scholar.google.com/scholar?q={quote_plus(title)}",
                "published": published,
                "citations": citations,
                "authors": authors,
                "doi": f"https://doi.org/{doi}" if doi else link,
                "source": "crossref"
            }
            score = paper.get("citations", 0)
            candidates.append((score, paper, key))
        for _, paper, key in sorted(candidates, key=lambda x: x[0], reverse=True):
            if key in seen_keys:
                continue
            fetched.append(paper)
            seen_keys.add(key)
            if len(fetched) >= needed:
                break
        if len(fetched) >= needed:
            break
        time.sleep(1)
    return fetched

def fetch_scholar_papers(year_start: int, year_end: int, needed: int, seen_keys: set,
                         keywords: Iterable[str] = None) -> List[dict]:
    """Backfill using Google Scholar (if available) for additional coverage."""
    if needed <= 0 or scholarly is None:
        if scholarly is None:
            logger.warning("scholarly package not installed; skipping Google Scholar backfill.")
        return []
    fetched = []
    failure_count = 0
    search_terms = list(keywords or ALL_KEYWORDS)
    for idx, phrase in enumerate(search_terms):
        if idx >= SCHOLAR_MAX_KEYWORDS:
            break
        query = f'"{phrase}" after:{year_start - 1} before:{year_end + 1}'
        try:
            search = scholarly.search_pubs(query)
        except Exception as err:
            logger.warning("Scholar search failed for '%s': %s", phrase, err)
            failure_count += 1
            if failure_count >= SCHOLAR_MAX_FAILURES:
                break
            continue
        for pub in islice(search, SCHOLAR_RESULTS_PER_KEYWORD):
            try:
                detailed = scholarly.fill(pub)
            except Exception as err:
                logger.debug("Scholar fill error: %s", err)
                continue
            bib = detailed.get("bib", {})
            title = bib.get("title")
            if not title:
                continue
            try:
                year = int(bib.get("pub_year"))
            except (TypeError, ValueError):
                continue
            if not (year_start <= year <= year_end):
                continue
            link = (
                detailed.get("pub_url")
                or detailed.get("eprint_url")
                or bib.get("url")
                or f"https://scholar.google.com/scholar?q={quote_plus(title)}"
            )
            doi = bib.get("doi") or link
            key = normalize_key({"title": title, "doi": doi, "link": link})
            if key in seen_keys:
                continue
            authors_raw = bib.get("author", "")
            if isinstance(authors_raw, list):
                authors = ", ".join(authors_raw)
            else:
                authors = ", ".join(
                    a.strip() for a in authors_raw.split(" and ") if a.strip()
                ) if authors_raw else ""
            abstract = bib.get("abstract") or ""
            paper = {
             "title": title,
                "summary": abstract,
             "link": link,
                "published": datetime(year, 1, 1, tzinfo=timezone.utc),
                "citations": detailed.get("num_citations", 0) or 0,
             "authors": authors,
                "doi": doi if doi.startswith("http") else f"https://doi.org/{doi}" if doi else link,
                "source": "scholar"
            }
            fetched.append(paper)
            seen_keys.add(key)
            if len(fetched) >= needed:
                break
        if len(fetched) >= needed:
            break
        time.sleep(SCHOLAR_RATE_LIMIT_SECONDS)
    return fetched

def fetch_crossref_citation(doi: str) -> int:
    """Retrieve citation count for a DOI via CrossRef with caching."""
    if not doi:
        return 0
    doi = sanitize_doi(doi)
    if not doi:
        return 0
    if doi in CITATION_CACHE:
        return CITATION_CACHE[doi]
    url = f"https://api.crossref.org/works/{quote_plus(doi)}"
    try:
        resp = request_with_backoff(url, base_delay=1.0)
    except requests.RequestException:
        CITATION_CACHE[doi] = 0
        return 0
    if not resp:
        return 0
    count = resp.json().get("message", {}).get("is-referenced-by-count", 0) or 0
    CITATION_CACHE[doi] = count
    return count


def enrich_with_citations(paper: dict) -> None:
    """Ensure every paper has a citation count."""
    if paper.get("citations") is not None:
        return
    doi = paper.get("doi")
    citations = 0
    if doi and isinstance(doi, str):
        citations = fetch_crossref_citation(doi)
    paper["citations"] = citations


def ensure_scores(papers: Iterable[dict], now: datetime, learned_weights: Dict[str, float]) -> None:
    for paper in papers:
        if not paper:
            continue
        if paper.get("score") is None:
            paper["score"] = enhanced_score(paper, now, learned_weights)

def backfill_time_window(
    current: List[dict],
    start_year: int,
    end_year: int,
    target: int,
    seen_keys: set,
    learned_weights: Dict[str, float],
    now: datetime,
) -> Tuple[List[dict], List[dict], List[dict]]:
    current = sorted(current, key=lambda x: x["score"], reverse=True)[:target]
    for paper in current:
        ensure_summary_text(paper)
    needed = target - len(current)
    crossref_extras: List[dict] = []
    scholar_extras: List[dict] = []
    if needed > 0:
        crossref_extras = fetch_crossref_papers(start_year, end_year, needed, seen_keys)
        for paper in crossref_extras:
            ensure_summary_text(paper)
            paper["score"] = enhanced_score(paper, now, learned_weights)
            current.append(paper)
            seen_keys.add(normalize_key(paper))
        needed = target - len(current)
    if needed > 0:
        scholar_extras = fetch_scholar_papers(start_year, end_year, needed, seen_keys)
        for paper in scholar_extras:
            ensure_summary_text(paper)
            paper["score"] = enhanced_score(paper, now, learned_weights)
            current.append(paper)
            seen_keys.add(normalize_key(paper))
    current = sorted(current, key=lambda x: x["score"], reverse=True)[:target]
    return current, crossref_extras, scholar_extras

def load_history_papers(exclude_links: set) -> Tuple[List[dict], set]:
    """Load papers from CSV log. Returns (history_papers, sent_keys).
    
    sent_keys contains ALL previously sent papers (even if in current feeds).
    history_papers only contains papers NOT in current feeds (to avoid re-scoring).
    """
    if not os.path.exists(LOG_FILE):
        return [], set()
    history: List[dict] = []
    sent_keys: set = set()
    with open(LOG_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            link = row.get("link") or ""
            title = row.get("title", "")
            summary = row.get("summary", "")
            authors = row.get("authors", "")
            
            # Create minimal paper dict for key normalization (even if data is missing)
            # We need at least title or link to create a key
            if not title and not link:
                continue
            
            paper_key = {
                "title": title,
                "link": link,
                "doi": row.get("doi") or f"https://scholar.google.com/scholar?q={quote_plus(title)}" if title else "",
            }
            
            # ALWAYS add to sent_keys to prevent re-sending, even if data is missing
            sent_keys.add(normalize_key(paper_key))
            
            # Only add to history list if we have a valid published date AND NOT in current feeds
            try:
                published = datetime.strptime(row.get("published", ""), "%Y-%m-%d").replace(tzinfo=timezone.utc)
            except ValueError:
                # Skip adding to history, but we already added to sent_keys above
                continue
            
            try:
                score = float(row.get("relevance", 0))
            except (TypeError, ValueError):
                score = 0.0
            
            # Only add to history list if NOT in current feeds (avoid re-scoring)
            if link not in exclude_links:
                paper = {
             "title": title,
             "summary": summary,
             "link": link,
                    "published": published,
                    "citations": 0,
             "authors": authors,
                    "doi": row.get("doi") or f"https://scholar.google.com/scholar?q={quote_plus(title)}",
                    "source": "history",
                    "score": score,
                }
                ensure_summary_text(paper)
                history.append(paper)
    
    logger.info("Loaded %d previously sent papers from history, %d available for re-scoring", 
                len(sent_keys), len(history))
    return history, sent_keys

def detect_trending_topics(papers: List[dict], now: datetime) -> List[str]:
    """Identify top bigram/trigram trends from the last 90 days."""
    cutoff = now - timedelta(days=90)
    texts = [
        f"{p['title']} {p.get('summary', '')}"
        for p in papers
        if p["published"] >= cutoff
    ]
    if not texts:
        return []
    vectorizer = CountVectorizer(ngram_range=(2, 3), stop_words="english", min_df=3)
    try:
        X = vectorizer.fit_transform(texts)
    except ValueError:
        return []
    counts = X.sum(axis=0).A1
    vocab = vectorizer.get_feature_names_out()
    phrases_with_counts = sorted(zip(vocab, counts), key=lambda x: x[1], reverse=True)
    keyword_set = set(k.lower() for k in ALL_KEYWORDS)
    trending = []
    for phrase, count in phrases_with_counts:
        if phrase.lower() in keyword_set:
            continue
        if not re.search(r"[a-z]", phrase):
            continue
        if len(trending) >= 5:
            break
        trending.append(f"{phrase} ({int(count)} hits)")
    return trending

def cluster_weekly_sections(papers: List[dict]) -> List[Tuple[str, List[dict]]]:
    """Group papers by keyword cluster for the weekly mode."""
    clusters: Dict[str, List[dict]] = defaultdict(list)
    for paper in papers:
        text = f"{paper['title']} {paper.get('summary', '')}".lower()
        best_group = "general"
        best_hits = 0
        for group, phrases in KEYWORD_GROUPS.items():
            hits = sum(phrase.lower() in text for phrase in phrases)
            if hits > best_hits:
                best_group = group
                best_hits = hits
        clusters[best_group].append(paper)
    sections = []
    for group, items in clusters.items():
        sections.append((group.replace("_", " ").title(), sorted(items, key=lambda x: x["score"], reverse=True)[:10]))
    return sorted(sections, key=lambda s: len(s[1]), reverse=True)

def format_score_bar(score: float) -> str:
    return ""

def generate_discovery_links(paper: dict) -> str:
    return ""

def build_email_sections_html(sections: List[Tuple[str, List[dict]]],
                              weight_stats: Dict[str, float], mode: str,
                              daily_task: Optional[Dict[str, str]] = None) -> str:
    """Render the HTML email body with enhanced styling and metadata."""
    css = """
    <style>
      body { font-family: Arial, sans-serif; color:#1c2833; }
      h1 { color:#1a5276; }
      .section-title { margin-top:24px; border-bottom:2px solid #1a5276; padding-bottom:6px; }
      .footer { font-size:12px; color:#7b7d7d; margin-top:24px; }
      .daily-task { background:#fff3e0; padding:20px; margin:20px 0; border-left:5px solid #ff9800; border-radius:5px; }
      .daily-task h2 { color:#e65100; margin-top:0; }
      .daily-task .meta-row { display:flex; flex-wrap:wrap; gap:12px; font-size:13px; color:#6e2c00; margin-bottom:10px; }
      .daily-task .meta-row span { background:#ffe0b2; padding:6px 10px; border-radius:4px; }
      .daily-task .content { font-size:14px; line-height:1.6; background:#fff; padding:15px; border-radius:5px; box-shadow:0 1px 3px rgba(0,0,0,0.05); white-space:pre-wrap; }
      .daily-task pre { background:#263238; color:#eceff1; padding:12px; border-radius:6px; overflow-x:auto; font-size:13px; }
    </style>
    """

    total_papers = sum(len(items) for _, items in sections)
    all_scores = [paper.get("score", 0) for _, items in sections for paper in items]
    avg_score = sum(all_scores) / len(all_scores) if all_scores else 0.0

    section_descriptions = {
        "RF Systems & Nonlinear Phenomena": (
            "<em>Papers on nonlinear RF characterization, diagnostic techniques, harmonic radar, "
            "automotive radar, and 5G/6G hardware aligned with your core research.</em>"
        ),
        "Cultural Heritage & Conservation Science": (
            "<em>Papers on optical imaging, spectroscopy, pigment analysis, authentication, and "
            "conservation science for artworks.</em>"
        ),
        "Adjacent Opportunities": (
            "<em>Papers on commercial radar, climate monitoring, precision agriculture, autonomous "
            "systems, and other cross-domain opportunities.</em>"
        ),
    }

    body = [css, "<h1>Daily Paper Digest</h1>"]
    if mode == "weekly":
        body[1] = "<h1>Weekly Paper Digest</h1>"

    summary_banner = (
        "<div style='background:#e8f5e9; padding:15px; border-radius:5px; margin-bottom:20px'>"
        f"<strong>Today's Summary:</strong> {total_papers} papers (5 RF + 5 Heritage + 5 Adjacent) | "
        f"Avg relevance: {avg_score:.2f}"
        "</div>"
    )
    body.append(summary_banner)

    if daily_task:
        formatted_description = daily_task.get("description", "").strip()
        formatted_description = formatted_description.replace(
            "```python", "<pre><code class='language-python'>"
        ).replace("```", "</code></pre>")
        body.append(
            "<div class='daily-task'>"
            f"<h2>🎯 Today's Skill-Building Task: {daily_task.get('domain', 'Focus')}</h2>"
            "<div class='meta-row'>"
            f"<span><strong>Skill:</strong> {daily_task.get('skill', 'Practice')}</span>"
            f"<span><strong>Task:</strong> {daily_task.get('task', '')}</span>"
            f"<span><strong>Time:</strong> {daily_task.get('time', '30 minutes')}</span>"
            f"<span><strong>Level:</strong> {daily_task.get('difficulty', 'Intermediate')}</span>"
            "</div>"
            f"<div class='content'>{formatted_description}</div>"
            "</div>"
        )

    for label, items in sections:
        if not items:
            continue
        body.append(f"<h2 class='section-title'>{label}</h2>")
        body.append(
            f"<div style='color:#666; font-size:13px; margin-bottom:15px'>{section_descriptions.get(label, '')}</div>"
        )
        for paper in items:
            body.append(format_paper_html(paper))

    if weight_stats:
        top_weights = sorted(weight_stats.items(), key=lambda kv: kv[1], reverse=True)[:5]
        stats_str = ", ".join(f"{phrase}: {val:.2%}" for phrase, val in top_weights)
        body.append(f"<div class='footer'>Personalization signals from recent clicks: {stats_str}</div>")

    return "\n".join(body)

def log_papers(sections: List[Tuple[str, List[dict]]]) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    header = ["date", "section", "title", "published", "link", "relevance", "summary", "authors", "doi"]
    newfile = not os.path.exists(LOG_FILE)
    existing_keys = set()
    rows: List[Tuple[str, str, dict]] = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_keys.add((row.get("section", ""), normalize_key({"title": row.get("title",""), "link": row.get("link",""), "doi": row.get("doi", "")})))
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if newfile:
            writer.writerow(header)
        for label, items in sections:
            for it in items:
                key = (label, normalize_key(it))
                if key in existing_keys:
                    continue
                existing_keys.add(key)
                rows.append((label, it))
        for label, it in rows:
            doi = it.get("doi", "")
            # Clean DOI: extract bare DOI if it's a URL
            if doi and ("doi.org" in doi or doi.startswith("http")):
                doi_match = re.search(r"10\.\d+/[^\s?#]+", doi)
                if doi_match:
                    doi = doi_match.group(0)
            writer.writerow([
                today,
                label,
                it.get("title"),
                it.get("published", datetime.now(timezone.utc)).strftime("%Y-%m-%d"),
                it.get("link"),
                it.get("score"),
                short_summary(it.get("summary", "")),
                it.get("authors", ""),
                doi
            ])
    logger.info("Logged %d new papers.", len(rows))

def generate_rss_feed(max_items: int = 15) -> None:
    """
    Generate RSS 2.0 feed from recent papers for hyperimage web app consumption.
    
    Args:
        max_items: Maximum number of items to include in feed (default 15, ReadingFeed shows top 5)
    """
    if not os.path.exists(LOG_FILE):
        logger.warning("No log file found; skipping RSS feed generation")
        return
    
    try:
        import pandas as pd
    except ImportError:
        logger.warning("pandas not available; skipping RSS feed generation")
        return
    
    try:
        df = pd.read_csv(LOG_FILE)
        if df.empty:
            logger.warning("Log file is empty; skipping RSS feed generation")
            return
        
        # Get most recent papers, sorted by date (newest first)
        df = df.sort_values("date", ascending=False)
        
        # Use normalize_key for proper de-duplication (same as in main logic)
        seen_keys = set()
        keep_indices = []
        for idx, row in df.iterrows():
            paper_key = {
                "title": str(row.get("title", "")),
                "link": str(row.get("link", "")),
                "doi": str(row.get("doi", ""))
            }
            key = normalize_key(paper_key)
            if key not in seen_keys:
                seen_keys.add(key)
                keep_indices.append(idx)
        
        # Filter DataFrame to only keep deduplicated papers
        df_dedup = df.loc[keep_indices] if keep_indices else pd.DataFrame()
        
        # Limit to most recent items
        recent_papers = df_dedup.head(max_items)
        
        if recent_papers.empty:
            logger.warning("No papers after de-duplication; skipping RSS feed generation")
            return
        
        # Build RSS XML
        now = datetime.now(timezone.utc)
        rss_items = []
        
        for _, row in recent_papers.iterrows():
            title = html.escape(str(row.get("title", "Untitled")))
            link = html.escape(str(row.get("link", "")))
            description = html.escape(short_summary(str(row.get("summary", "")), 3))
            pub_date = row.get("published", "")
            author = html.escape(str(row.get("authors", ""))[:100])  # Limit author length
            category = html.escape(str(row.get("section", "")))
            
            # Format pubDate in RFC 822 format for RSS
            try:
                if pd.notna(pub_date) and pub_date:
                    pub_dt = datetime.strptime(str(pub_date), "%Y-%m-%d").replace(tzinfo=timezone.utc)
                else:
                    pub_dt = now
            except (ValueError, TypeError):
                pub_dt = now
            
            # RFC 822 format: "Wed, 02 Oct 2002 08:00:00 EST" or "Wed, 02 Oct 2002 13:00:00 +0000"
            # Python's %z gives +0000 format, but RSS prefers GMT for UTC
            if pub_dt.tzinfo == timezone.utc:
                pub_date_rfc822 = pub_dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
            else:
                pub_date_rfc822 = pub_dt.strftime("%a, %d %b %Y %H:%M:%S %z")
            
            # Build item XML
            item_xml = f"""    <item>
        <title>{title}</title>
        <link>{link}</link>
        <description>{description} | Score: {row.get('relevance', 0):.2f}</description>
        <pubDate>{pub_date_rfc822}</pubDate>
        <author>{author}</author>
        <category>{category}</category>
        <guid isPermaLink="true">{link}</guid>
    </item>"""
            rss_items.append(item_xml)
        
        # Build complete RSS feed
        rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>Daily Paper Digest</title>
        <link>https://github.com/ddrizzil/HyperImage</link>
        <description>Algorithmically selected papers from 20+ journal feeds, focused on RF systems, cultural heritage conservation, and adjacent opportunities.</description>
        <language>en-us</language>
        <lastBuildDate>{now.strftime("%a, %d %b %Y %H:%M:%S GMT")}</lastBuildDate>
        <atom:link href="https://raw.githubusercontent.com/ddrizzil/HyperImage/main/web/feed.xml" rel="self" type="application/rss+xml"/>
        <generator>Paper Digest Service</generator>
{chr(10).join(rss_items)}
    </channel>
</rss>"""
        
        # Write RSS feed to file in web directory for Next.js to serve
        rss_file = "web/feed.xml"
        os.makedirs("web", exist_ok=True)
        with open(rss_file, "w", encoding="utf-8") as f:
            f.write(rss_xml)
        
        logger.info("Generated RSS feed: %s (%d items)", rss_file, len(rss_items))
        
    except Exception as e:
        logger.error("Failed to generate RSS feed: %s", e)

def build_html_archive() -> None:
    try:
        import pandas as pd  # Lazy import to avoid dependency if not installed.
    except ImportError:
        logger.warning("pandas not available; skipping HTML archive generation")
        return
    if not os.path.exists(LOG_FILE):
        return
    try:
        df = pd.read_csv(LOG_FILE)
    except Exception as e:
        logger.error("Failed to read CSV for archive: %s", e)
        return
    df = df.sort_values(["date", "section"], ascending=[False, True])
    before = len(df)
    df = df.drop_duplicates(subset=["date", "section", "title", "link"], keep="first")
    after = len(df)
    if after != before:
        df.sort_values(["date", "section"], ascending=[False, True]).to_csv(LOG_FILE, index=False)
        logger.info("Deduplicated %d duplicate log rows.", before - after)
    html = [
        "<html><head><meta charset='utf-8'><title>Paper Archive</title>",
          "<style>body{font-family:sans-serif;padding:20px;}table{width:100%;border-collapse:collapse;}th,td{border:1px solid #ccc;padding:6px;}</style>",
        "</head><body><h1>📚 Paper Digest Archive</h1>"
    ]
    for date, g in df.groupby("date"):
        html.append(f"<h2>{date}</h2>")
        for section, sg in g.groupby("section"):
            html.append("<h3>{}</h3><table><tr><th>Title</th><th>Date</th><th>Rel.</th><th>Summary</th><th>Authors</th></tr>".format(section))
            for _, r in sg.iterrows():
                author_link = ""
                if pd.notna(r.authors) and r.authors:
                    first_author = r.authors.split(",")[0]
                    author_link = f"https://scholar.google.com/scholar?q={quote_plus(first_author)}"
                dive_link = f"https://scholar.google.com/scholar?q={quote_plus(r.title)}"
                html.append(
                    "<tr>"
                    f"<td><a href='{r.link}'>{r.title}</a><br>"
                            f"<a href='{dive_link}'>Dive deeper</a>"
                            + (f" | <a href='{author_link}'>Author page</a>" if author_link else "")
                    + "</td>"
                    f"<td>{r.published}</td><td>{r.relevance}</td><td>{r.summary}</td><td>{r.authors}</td>"
                    "</tr>"
                )
            html.append("</table>")
    html.append("</body></html>")
    with open("logs/archive.html", "w", encoding="utf-8") as f:
        f.write("\n".join(html))
    logger.info("Archive HTML updated.")

def email_digest(sections: List[Tuple[str, List[dict]]],
                 weight_stats: Dict[str, float], mode: str,
                 all_papers: List[dict]) -> None:
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    recipients = load_recipients()

    msg = MIMEMultipart("alternative")
    subject_prefix = "Weekly" if mode == "weekly" else "Daily"
    msg["Subject"] = f"📚 {subject_prefix} Paper Digest – {datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    msg["From"] = SENDER
    msg["To"] = ", ".join(recipients)

    daily_task = generate_daily_task(datetime.now(timezone.utc), all_papers)
    html_body = build_email_sections_html(sections, weight_stats, mode, daily_task)
    msg.attach(MIMEText(html_body, "html"))

    if not smtp_host:
        logger.warning("SMTP_HOST is not set; skipping email send.")
        return

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        if not smtp_user or not smtp_pass:
            logger.warning("SMTP credentials missing; skipping email send.")
            return
        server.login(smtp_user, smtp_pass)
        server.sendmail(SENDER, recipients, msg.as_string())
    logger.info("Email sent to %s", ", ".join(recipients))

def has_priority_topic(paper: dict) -> bool:
    text = f"{paper.get('title', '')} {paper.get('summary', '')}".lower()
    return any(keyword in text for keyword in PRIORITY_ML_KEYWORDS)


def classify_interest_group(paper: dict) -> str:
    text = f"{paper.get('title', '')} {paper.get('summary', '')}".lower()
    for group in ML_RF_GROUPS:
        for phrase in KEYWORD_GROUPS.get(group, []):
            if phrase.lower() in text:
                return "ml_rf"
    for group in HERITAGE_OPTICS_GROUPS:
        for phrase in KEYWORD_GROUPS.get(group, []):
            if phrase.lower() in text:
                return "heritage_optics"
    return "other"

def create_topic_based_sections(papers: List[dict], previously_sent_keys: Optional[set] = None) -> List[Tuple[str, List[dict]]]:
    """Build fixed-count topic sections (5 each) for RF, heritage, and adjacent topics."""
    prev_keys = previously_sent_keys or set()

    rf_papers: List[dict] = []
    heritage_papers: List[dict] = []
    adjacent_papers: List[dict] = []
    unrelated_papers: List[dict] = []

    # Strong art terms for validation (same as in classify_paper_topic)
    strong_art_terms_check = [
        # Core art terms (REQUIRED for heritage classification)
        r'\bart\b', r'\bartwork\b', r'\bartworks\b', 
        r'\bpainting\b', r'\bpaintings\b', 
        r'\bmuseum\b', r'\bmuseums\b',
        # Artist and artistic terms
        r'\bgallery\b', r'\bgalleries\b', r'\bartist\b', r'\bartistic\b', r'\bartists\b',
        r'\bcanvas\b', r'\bconservator\b', r'\bconservators\b',
        # Painting-specific terms
        r'\bpentimento\b', r'\bpentimenti\b',
        r'\bunderdrawing\b', r'\bunderdrawings\b',
        r'\bbrushstroke\b', r'\bbrushstrokes\b', r'\bbrush strokes\b', r'\bbrush stroke\b',
        # Authentication and art history
        r'\bforgery detection\b', r'\bartist attribution\b', r'\bdating artwork\b',
        r'\btechnical art history\b',
        # Conservation and restoration
        r'\bart conservation\b', r'\bart restoration\b', r'\bart authentication\b',
        # Imaging techniques with art context
        r'\boct painting\b', r'\bxrf painting\b', r'\braman painting\b',
        r'\bhyperspectral art\b', r'\bmultispectral art\b', r'\bphotoacoustic art\b',
        # Digital heritage
        r'\bvirtual museum\b', r'\bcomputational art history\b', r'\bdigital art history\b',
    ]
    
    art_context_phrases_check = [
        r'\bart conservation\b', r'\bart restoration\b', r'\bart authentication\b',
        r'\bart materials\b', r'\bpainting materials\b', r'\bart history\b',
        r'\bart science\b', r'\bart analysis\b', r'\bart imaging\b',
        r'\bmachine learning art\b', r'\bdeep learning art\b', r'\bcnn art\b',
        r'\bphotogrammetry art\b', r'\b3d reconstruction art\b',
    ]
    
    for paper in papers:
        key = normalize_key(paper)
        if key in prev_keys:
            continue
        category, adjusted_score, subcategories = classify_paper_topic(paper)
        paper['category'] = category
        paper['score'] = adjusted_score
        paper['subcategories'] = subcategories
        
        # CRITICAL SAFETY CHECK: If classified as heritage, verify it has strong art/painting context
        # This is a FINAL check - papers WITHOUT art/painting context CANNOT be heritage
        if category == 'cultural_heritage':
            text = f"{paper.get('title', '')} {paper.get('summary', '')}".lower()
            has_strong_art = any(re.search(pattern, text) for pattern in strong_art_terms_check)
            has_art_phrase = any(re.search(pattern, text) for pattern in art_context_phrases_check)
            # Check for explicit heritage context for standalone "art" (be very strict)
            has_explicit_heritage_for_art = any(re.search(pattern, text) for pattern in [
                r'\bcultural heritage\b', r'\bheritage conservation\b', r'\bart conservation\b',
                r'\bart restoration\b', r'\bart authentication\b', r'\bmuseum\b', r'\bgallery\b',
                r'\bartwork\b', r'\bpainting\b', r'\bpaintings\b', r'\bartist\b', r'\bartistic\b',
            ])
            has_standalone_art = bool(re.search(r'\bart\b', text))
            has_art = has_strong_art or has_art_phrase or (has_standalone_art and has_explicit_heritage_for_art)
            
            # ABSOLUTE REQUIREMENT: Must have art/painting context
            if not has_art:
                # Misclassified - CRITICAL ERROR: This should never happen if classify_paper_topic is working correctly
                logger.error(
                    "CRITICAL: Removing misclassified heritage paper (no art/painting context): %s (score=%.2f, subcategories=%s)",
                    paper.get('title', '')[:60], adjusted_score, paper.get('subcategories', [])
                )
                # Force reclassification - do NOT allow heritage classification without art/painting context
                category = 'adjacent' if adjusted_score >= 3.0 else 'unrelated'
                paper['category'] = category
                # Also reset heritage subcategories to prevent confusion
                paper['subcategories'] = []
            else:
                # Valid heritage paper - log it for verification
                logger.info(
                    "✓ Valid heritage paper (has art/painting context): %s (score=%.2f)",
                    paper.get('title', '')[:60], adjusted_score
                )
        
        if category == 'rf_systems':
            rf_papers.append(paper)
        elif category == 'cultural_heritage':
            heritage_papers.append(paper)
        elif category == 'adjacent':
            adjacent_papers.append(paper)
        else:
            unrelated_papers.append(paper)

    rf_papers.sort(key=lambda x: x.get('score', 0), reverse=True)
    heritage_papers.sort(key=lambda x: x.get('score', 0), reverse=True)
    adjacent_papers.sort(key=lambda x: x.get('score', 0), reverse=True)
    unrelated_papers.sort(key=lambda x: x.get('score', 0), reverse=True)

    selections = {
        'rf_systems': rf_papers[:5],
        'cultural_heritage': heritage_papers[:5],
        'adjacent': adjacent_papers[:5],
    }

    remaining = {
        'rf_systems': rf_papers[5:],
        'cultural_heritage': heritage_papers[5:],
        'adjacent': adjacent_papers[5:],
    }

    used_keys = {normalize_key(paper) for bucket in selections.values() for paper in bucket}

    fallback_pool = [
        p for p in (
            rf_papers[5:] +
            heritage_papers[5:] +
            adjacent_papers[5:] +
            unrelated_papers
        )
        if normalize_key(p) not in used_keys and normalize_key(p) not in prev_keys
    ]

    # REQUIRED: Art/painting context patterns for fallback (must have explicit art/painting mention)
    art_painting_patterns_fallback = [
        # Core art terms (REQUIRED)
        r'\bart\b', r'\bartwork\b', r'\bartworks\b', 
        r'\bpainting\b', r'\bpaintings\b', 
        r'\bmuseum\b', r'\bmuseums\b',
        # Artist and artistic terms
        r'\bgallery\b', r'\bgalleries\b', r'\bartist\b', r'\bartistic\b', r'\bartists\b',
        r'\bcanvas\b', r'\bconservator\b', r'\bconservators\b',
        # Painting-specific terms
        r'\bpentimento\b', r'\bpentimenti\b',
        r'\bunderdrawing\b', r'\bunderdrawings\b',
        r'\bbrushstroke\b', r'\bbrushstrokes\b', r'\bbrush strokes\b', r'\bbrush stroke\b',
        # Conservation and restoration
        r'\bart conservation\b', r'\bart restoration\b', r'\bart authentication\b',
        # Authentication and art history
        r'\bforgery detection\b', r'\bartist attribution\b', r'\bdating artwork\b',
        r'\btechnical art history\b', r'\bartist technique\b', r'\bpainting technique\b',
        # Materials
        r'\bart materials\b', r'\bpainting materials\b', r'\bpaint layer\b',
        r'\bpigment identification\b', r'\bpigment analysis\b', r'\bpigment degradation\b',
        r'\bvarnish characterization\b', r'\bbinding media\b',
        r'\bhistoric pigment\b', r'\btraditional pigment\b',
        # Imaging techniques with art context
        r'\boct painting\b', r'\bxrf painting\b', r'\braman painting\b',
        r'\bhyperspectral art\b', r'\bmultispectral art\b', r'\bphotoacoustic art\b',
        r'\bterahertz imaging art\b',
        # Digital heritage
        r'\bvirtual museum\b', r'\bcomputational art history\b', r'\bdigital art history\b',
        r'\bphotogrammetry art\b', r'\b3d reconstruction art\b',
        # ML with art context
        r'\bmachine learning art\b', r'\bdeep learning art\b', r'\bcnn art\b',
    ]

    for category in ('rf_systems', 'cultural_heritage', 'adjacent'):
        bucket = selections[category]
        while len(bucket) < 5 and remaining[category]:
            candidate = remaining[category].pop(0)
            key = normalize_key(candidate)
            if key in used_keys or key in prev_keys:
                continue
            bucket.append(candidate)
            used_keys.add(key)
        if category == 'cultural_heritage' and len(bucket) < 5:
            # REQUIRED: Only use fallback candidates that explicitly mention art/painting
            filtered = []
            for candidate in list(fallback_pool):
                key = normalize_key(candidate)
                if key in used_keys or key in prev_keys:
                    continue
                text = f"{candidate.get('title', '')} {candidate.get('summary', '')}".lower()
                # CRITICAL: MUST have explicit art/painting context (use regex for word boundaries)
                # This is the SAME check as in classify_paper_topic and the safety check above
                has_strong_art = any(re.search(pattern, text) for pattern in strong_art_terms_check)
                has_art_phrase = any(re.search(pattern, text) for pattern in art_context_phrases_check)
                has_explicit_heritage_for_art = any(re.search(pattern, text) for pattern in [
                    r'\bcultural heritage\b', r'\bheritage conservation\b', r'\bart conservation\b',
                    r'\bart restoration\b', r'\bart authentication\b', r'\bmuseum\b', r'\bgallery\b',
                    r'\bartwork\b', r'\bartworks\b', r'\bpainting\b', r'\bpaintings\b', 
                    r'\bartist\b', r'\bartistic\b', r'\bartists\b',
                    r'\bpentimento\b', r'\bpentimenti\b', r'\bunderdrawing\b', r'\bunderdrawings\b',
                    r'\bbrushstroke\b', r'\bbrushstrokes\b', r'\bbrush strokes\b', r'\bbrush stroke\b',
                ])
                has_standalone_art = bool(re.search(r'\bart\b', text))
                has_art_painting = has_strong_art or has_art_phrase or (has_standalone_art and has_explicit_heritage_for_art)
                
                if has_art_painting:
                    # Double-check it's not clearly non-heritage (weather, medical, etc.)
                    non_heritage_indicators = [
                        'weather radar', 'precipitation', 'atmospheric',
                        'thunderstorm', 'medical imaging', 'patient', 'clinical',
                        'water level monitoring', 'reservoir monitoring',
                        'soil moisture', 'crop monitoring', 'agricultural',
                        'remote sensing satellite', 'glacier monitoring',
                    ]
                    has_non_heritage = any(ind in text for ind in non_heritage_indicators)
                    if not has_non_heritage:
                        logger.debug(
                            "Fallback candidate for heritage (has art/painting context): %s",
                            candidate.get('title', '')[:60]
                        )
                        filtered.append(candidate)
                else:
                    # CRITICAL: Do NOT add papers without art/painting context to heritage section
                    logger.debug(
                        "Skipping fallback candidate for heritage (no art/painting context): %s",
                        candidate.get('title', '')[:60]
                    )
            # Sort by score and take highest scoring ones
            filtered.sort(key=lambda x: x.get('score', 0), reverse=True)
            for candidate in filtered:
                if len(bucket) >= 5:
                    break
                if candidate not in fallback_pool:
                    continue
                fallback_pool.remove(candidate)
                key = normalize_key(candidate)
                if key in used_keys or key in prev_keys:
                    continue
                candidate['category'] = 'cultural_heritage'
                bucket.append(candidate)
                used_keys.add(key)
        
        # For cultural_heritage: DO NOT use generic fallback - only accept art/painting papers
        # It's better to have fewer papers than to include non-art papers
        if category == 'cultural_heritage':
            # Skip generic fallback - we've already tried art/painting-specific fallback above
            pass
        else:
            # For RF and Adjacent: use generic fallback if needed
            while len(bucket) < 5 and fallback_pool:
                candidate = fallback_pool.pop(0)
                key = normalize_key(candidate)
                if key in used_keys or key in prev_keys:
                    continue
                bucket.append(candidate)
                used_keys.add(key)
                candidate['category'] = category

    logger.info(
        "Paper distribution: RF=%d, Heritage=%d, Adjacent=%d",
        len(rf_papers), len(heritage_papers), len(adjacent_papers)
    )
    logger.info(
        "Selected for email: RF=%d, Heritage=%d, Adjacent=%d",
        len(selections['rf_systems']),
        len(selections['cultural_heritage']),
        len(selections['adjacent'])
    )

    for category, label in [
        ('rf_systems', 'RF Systems & Nonlinear Phenomena'),
        ('cultural_heritage', 'Cultural Heritage & Conservation Science'),
        ('adjacent', 'Adjacent Opportunities'),
    ]:
        if len(selections[category]) < 5:
            logger.warning("Only found %d papers for %s (wanted 5).", len(selections[category]), label)

    return [
        ("RF Systems & Nonlinear Phenomena", selections['rf_systems'][:5]),
        ("Cultural Heritage & Conservation Science", selections['cultural_heritage'][:5]),
        ("Adjacent Opportunities", selections['adjacent'][:5]),
    ]

# ---------------- RESET & AUDIT FUNCTIONS ----------------
def reset_all_state(confirm: bool = False) -> None:
    """
    Reset all state files and caches for fresh deployment.
    
    Clears:
    - CSV log file (logs/paper_digest_log.csv)
    - Click history (config/clicks.txt)
    - HTML archive (logs/archive.html)
    - Citation cache (in-memory)
    
    Args:
        confirm: If True, actually performs reset. If False, just logs what would be reset.
    """
    files_to_remove = [
        LOG_FILE,
        PERSONALIZATION_FILE,
        "logs/archive.html",
    ]
    
    files_removed = []
    files_missing = []
    
    for filepath in files_to_remove:
        if os.path.exists(filepath):
            if confirm:
                try:
                    os.remove(filepath)
                    files_removed.append(filepath)
                    logger.info("Removed: %s", filepath)
                except Exception as e:
                    logger.error("Failed to remove %s: %s", filepath, e)
            else:
                files_removed.append(filepath)
                logger.info("Would remove: %s", filepath)
        else:
            files_missing.append(filepath)
    
    # Clear citation cache
    cache_size = len(CITATION_CACHE)
    if confirm:
        CITATION_CACHE.clear()
        logger.info("Cleared citation cache (%d entries)", cache_size)
    else:
        logger.info("Would clear citation cache (%d entries)", cache_size)
    
    # Ensure directories exist after reset
    if confirm:
        os.makedirs("logs", exist_ok=True)
        os.makedirs("config", exist_ok=True)
        ensure_file(PERSONALIZATION_FILE)
        logger.info("Recreated directory structure")
    
    if confirm:
        logger.info("✓ Reset complete: removed %d files, cleared cache", len(files_removed))
    else:
        logger.info("DRY RUN: Would remove %d files (%d missing), clear cache", 
                   len(files_removed), len(files_missing))
        if files_removed:
            logger.warning("To actually reset, call: reset_all_state(confirm=True)")

def audit_system() -> Dict[str, any]:  # type: ignore
    """
    Comprehensive audit of the system state.
    
    Returns:
        Dictionary with audit results including file sizes, cache stats, deduplication issues, etc.
    """
    audit_results = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "files": {},
        "cache": {},
        "deduplication": {},
        "errors": [],
    }
    
    # Check file sizes and line counts
    files_to_check = [
        ("log_file", LOG_FILE),
        ("click_history", PERSONALIZATION_FILE),
        ("archive_html", "logs/archive.html"),
    ]
    
    for name, filepath in files_to_check:
        file_info = {
            "exists": os.path.exists(filepath),
            "size_bytes": 0,
            "line_count": 0,
        }
        if file_info["exists"]:
            try:
                file_info["size_bytes"] = os.path.getsize(filepath)
                if filepath.endswith(".csv") or filepath.endswith(".txt"):
                    with open(filepath, encoding="utf-8") as f:
                        file_info["line_count"] = sum(1 for _ in f)
            except Exception as e:
                audit_results["errors"].append(f"Error checking {filepath}: {e}")
        audit_results["files"][name] = file_info
    
    # Check CSV for duplicates
    if os.path.exists(LOG_FILE):
        try:
            import pandas as pd
            df = pd.read_csv(LOG_FILE)
            total_rows = len(df)
            unique_rows = len(df.drop_duplicates(subset=["date", "section", "title", "link"]))
            duplicates = total_rows - unique_rows
            
            audit_results["deduplication"] = {
                "total_rows": total_rows,
                "unique_rows": unique_rows,
                "duplicates": duplicates,
                "duplicate_percentage": round(100 * duplicates / total_rows, 2) if total_rows > 0 else 0,
            }
            
            # Check for missing DOIs in CSV
            if "doi" in df.columns:
                missing_doi_count = df["doi"].isna().sum() + (df["doi"] == "").sum()
                audit_results["deduplication"]["missing_doi_count"] = int(missing_doi_count)
                audit_results["deduplication"]["missing_doi_percentage"] = round(
                    100 * missing_doi_count / total_rows, 2
                ) if total_rows > 0 else 0
        except Exception as e:
            audit_results["errors"].append(f"Error auditing CSV: {e}")
    
    # Citation cache stats
    audit_results["cache"] = {
        "citation_cache_size": len(CITATION_CACHE),
        "citation_cache_keys": list(CITATION_CACHE.keys())[:10] if CITATION_CACHE else [],
    }
    
    # Check for semantic model
    audit_results["model"] = {
        "semantic_model_loaded": SEMANTIC_MODEL is not None,
        "embedding_available": RESEARCH_EMBEDDING is not None,
    }
    
    # Check click history
    try:
        clicks = load_click_history()
        audit_results["personalization"] = {
            "click_count": len(clicks),
            "sample_clicks": clicks[:5] if clicks else [],
        }
    except Exception as e:
        audit_results["errors"].append(f"Error loading click history: {e}")
    
    return audit_results

def print_audit_results(results: Dict[str, any]) -> None:
    """Pretty print audit results."""
    print("\n" + "="*70)
    print("SYSTEM AUDIT REPORT")
    print("="*70)
    print(f"Timestamp: {results['timestamp']}\n")
    
    print("--- FILES ---")
    for name, info in results["files"].items():
        status = "✓" if info["exists"] else "✗"
        size_kb = info["size_bytes"] / 1024 if info["exists"] else 0
        print(f"{status} {name:20s} | Exists: {info['exists']:5s} | "
              f"Size: {size_kb:8.1f} KB | Lines: {info['line_count']:6d}")
    
    print("\n--- DEDUPLICATION ---")
    dedup = results.get("deduplication", {})
    if dedup:
        print(f"Total rows:        {dedup.get('total_rows', 0):6d}")
        print(f"Unique rows:       {dedup.get('unique_rows', 0):6d}")
        print(f"Duplicates:        {dedup.get('duplicates', 0):6d} "
              f"({dedup.get('duplicate_percentage', 0):.2f}%)")
        if "missing_doi_count" in dedup:
            print(f"Missing DOIs:       {dedup.get('missing_doi_count', 0):6d} "
                  f"({dedup.get('missing_doi_percentage', 0):.2f}%)")
    
    print("\n--- CACHE ---")
    cache = results.get("cache", {})
    print(f"Citation cache:    {cache.get('citation_cache_size', 0):6d} entries")
    
    print("\n--- MODEL ---")
    model = results.get("model", {})
    print(f"Semantic model:    {'✓ Loaded' if model.get('semantic_model_loaded') else '✗ Not loaded'}")
    print(f"Embedding:         {'✓ Available' if model.get('embedding_available') else '✗ Not available'}")
    
    print("\n--- PERSONALIZATION ---")
    pers = results.get("personalization", {})
    print(f"Click history:     {pers.get('click_count', 0):6d} clicks")
    
    if results.get("errors"):
        print("\n--- ERRORS ---")
        for error in results["errors"]:
            print(f"✗ {error}")
    
    print("\n" + "="*70)

# ---------------- MAIN PROCESS ----------------
def run_once() -> None:
    now = datetime.now(timezone.utc)
    clicked_titles = load_click_history()
    learned_weights, weight_stats = update_keyword_weights(clicked_titles)

    papers: List[dict] = []
    seen_links = set()

    for url in FEEDS:
        for entry in parse_feed(url):
            title, summary = entry.get("title", ""), entry.get("summary", "")
            link = entry.get("link", "")
            if link and link in seen_links:
                continue
            raw_authors = entry.get("authors", [])
            if isinstance(raw_authors, list):
                authors = ", ".join([a.get("name", "") for a in raw_authors])
            else:
                authors = str(raw_authors)
            pub_date = extract_pub_date(entry)
            if not pub_date:
                continue
            doi = entry.get("doi") if isinstance(entry, dict) and entry.get("doi") else f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"
            paper = {
                "title": title,
                "summary": summary,
                "link": link,
                "published": pub_date,
                "citations": None,  # to be filled
                "authors": authors,
                "doi": doi,
                "source": "feed"
            }
            if link:
                seen_links.add(link)
            enrich_with_citations(paper)
            ensure_summary_text(paper)
            paper["score"] = enhanced_score(paper, now, learned_weights)
            papers.append(paper)

    history_papers, sent_history_keys = load_history_papers(seen_links)
    all_papers = papers + history_papers
    seen_keys = {normalize_key(p) for p in all_papers}

    # Evaluate scores for history entries using current weights.
    for paper in history_papers:
        if paper.get("score") in (None, 0):
            paper["score"] = enhanced_score(paper, now, learned_weights)

    all_papers = [p for p in all_papers if p.get("published")]
    ensure_scores(all_papers, now, learned_weights)

    # Prefer papers not previously emailed
    ranked_papers = sorted(all_papers, key=lambda x: x.get("score", 0), reverse=True)
    candidate_papers: List[dict] = []
    seen_candidate_keys: set = set()
    filtered_count = 0
    for paper in ranked_papers:
        key = normalize_key(paper)
        if key in seen_candidate_keys:
            continue
        seen_candidate_keys.add(key)
        if key in sent_history_keys:
            filtered_count += 1
            continue
        candidate_papers.append(paper)
    
    logger.info(
        "Paper filtering: total=%d, previously_sent=%d, filtered=%d, candidates=%d",
        len(ranked_papers), len(sent_history_keys), filtered_count, len(candidate_papers)
    )

    sections = create_topic_based_sections(candidate_papers, sent_history_keys)

    # Log section status
    for label, items in sections:
        if len(items) < 5:
            logger.warning("Section '%s' has only %d papers (wanted 5). Total candidates: %d", 
                         label, len(items), len(candidate_papers))
        else:
            logger.info("Section '%s' has %d papers", label, len(items))

    # Ensure unique entries per section
    dedup_sections: List[Tuple[str, List[dict]]] = []
    seen_section_keys = set()
    for label, items in sections:
        unique_items: List[dict] = []
        for paper in items:
            key = (label, normalize_key(paper))
            if key in seen_section_keys:
                continue
            seen_section_keys.add(key)
            unique_items.append(paper)
        dedup_sections.append((label, unique_items))

    if DIGEST_MODE == "weekly":
        dedup_sections = cluster_weekly_sections(ranked_papers)

    counts = {label: len(items) for label, items in dedup_sections}
    logger.info(
        "Paper pools – total:%d rf:%d heritage:%d adjacent:%d",
        len(ranked_papers),
        counts.get("RF Systems & Nonlinear Phenomena", 0),
        counts.get("Cultural Heritage & Conservation Science", 0),
        counts.get("Adjacent Opportunities", 0),
    )

    log_papers(dedup_sections)
    build_html_archive()
    generate_rss_feed(max_items=15)  # Generate RSS feed for hyperimage web app
    email_digest(dedup_sections, weight_stats, DIGEST_MODE, ranked_papers)

def format_paper_html(paper: dict) -> str:
    """Render a single paper entry with badges and discovery links."""
    score = paper.get("score", 0)
    citations = paper.get("citations", 0) or 0
    source = paper.get("source", "feed").upper()
    subcategories = paper.get("subcategories", []) or []

    if score >= 7:
        border_color = "#4CAF50"
    elif score >= 5:
        border_color = "#2196F3"
    else:
        border_color = "#FF9800"

    subcat_html = ""
    if subcategories:
        readable_labels = {
            'nonlinear_rf': 'Nonlinear RF',
            'rf_diagnostics': 'RF Diagnostics',
            'harmonic_radar': 'Harmonic Radar',
            'automotive_radar': 'Automotive Radar',
            '5g_6g_hardware': '5G/6G Hardware',
            'rf_measurement': 'RF Measurement',
            'rf_signal_processing': 'RF Signal Processing',
            'power_amplifiers': 'Power Amplifiers',
            'gpr': 'Ground Penetrating Radar',
            'optical_imaging': 'Optical Imaging',
            'spectroscopy_analysis': 'Spectroscopy',
            'paint_analysis': 'Paint Analysis',
            'conservation_science': 'Conservation',
            'authentication': 'Authentication',
            'materials_art': 'Art Materials',
            'advanced_imaging': 'Advanced Imaging',
            '3d_heritage': '3D Heritage',
            'microscopy': 'Microscopy',
            'harmonic_applications': 'Harmonic Applications',
            'climate_monitoring': 'Climate Monitoring',
            'commercial_rf': 'Commercial RF',
            'autonomous_vehicles': 'Autonomous Vehicles',
            'precision_agriculture': 'Precision Agriculture',
            'ml_applications': 'Machine Learning',
            'disaster_response': 'Disaster Response',
            'sar_satellite': 'SAR/Satellite',
            'pedagogy_architecture': 'Pedagogy/Architecture',
            'advanced_dsp': 'Advanced DSP',
        }
        top_subcat = subcategories[0][0]
        label = readable_labels.get(top_subcat, top_subcat.replace('_', ' ').title())
        subcat_html = (
            "<span style='background:#e1f5fe; padding:2px 8px; border-radius:3px; margin-right:8px;"
            " font-size:11px'>" + label + "</span>"
        )

    title = paper.get("title", "Untitled")
    link = paper.get("link") or paper.get("doi") or ""
    published = paper.get("published") or datetime.now(timezone.utc)
    authors = paper.get("authors") or ""
    summary = short_summary(paper.get("summary", "No abstract available."), 2 if score < 7 else 3)

    doi_link = paper.get("doi") or ""
    doi_href = doi_link if doi_link.startswith("http") else (f"https://doi.org/{doi_link}" if doi_link else "")
    scholar_link = f"https://scholar.google.com/scholar?q={quote_plus(title)}"
    semantic_link = f"https://www.semanticscholar.org/search?q={quote_plus(title)}"
    connected_link = f"https://www.connectedpapers.com/search?q={quote_plus(title)}"

    citation_html = f"<span style='margin-right:12px'>📚 {citations} citations</span>" if citations else ""
    authors_html = (
        f"<div style='color:#555; font-size:13px; margin-bottom:8px; font-style:italic'>{authors[:150]}{'...' if len(authors) > 150 else ''}</div>"
        if authors else ""
    )

    return f"""
    <div style='margin-bottom:20px; padding:15px; border-left:4px solid {border_color}; background:#f9f9f9'>
        <div style='font-size:17px; font-weight:bold; margin-bottom:5px'>
            <a href='{link}' style='color:#1a0dab; text-decoration:none'>{title}</a>
        </div>
        <div style='color:#666; font-size:12px; margin-bottom:10px'>
            <span style='background:#e8f4f8; padding:2px 6px; border-radius:3px; margin-right:8px'>{source}</span>
            {subcat_html}
            <span style='margin-right:12px'>📅 {published.strftime('%Y-%m-%d')}</span>
            <span style='margin-right:12px'>⭐ Score: {score:.2f}</span>
            {citation_html}
        </div>
        {authors_html}
        <div style='font-size:14px; line-height:1.6; color:#333'>
            {summary}
        </div>
        <div style='margin-top:10px; font-size:12px'>
            {f"<a href='{doi_href}' style='margin-right:12px'>📄 DOI</a>" if doi_href else ''}
            <a href='{link}' style='margin-right:12px'>🔗 Publisher</a>
            <a href='{scholar_link}' style='margin-right:12px'>🔍 Scholar</a>
            <a href='{semantic_link}' style='margin-right:12px'>🧠 Semantic Scholar</a>
            <a href='{connected_link}'>🕸️ Connected Papers</a>
        </div>
    </div>
    """

if __name__ == "__main__":
    import sys
    
    # Support command-line arguments for reset and audit
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "reset":
            confirm = len(sys.argv) > 2 and sys.argv[2].lower() in ("yes", "y", "confirm", "true")
            if not confirm:
                print("DRY RUN MODE - Use 'python paper_digest_service.py reset confirm' to actually reset")
                print()
            reset_all_state(confirm=confirm)
            if confirm:
                print("\n✓ System reset complete. Ready for fresh deployment.")
            sys.exit(0)
        
        elif command == "audit":
            results = audit_system()
            print_audit_results(results)
            sys.exit(0)
        
        elif command == "help" or command == "--help" or command == "-h":
            print("Usage: python paper_digest_service.py [command]")
            print()
            print("Commands:")
            print("  (no args)  - Run the daily digest service")
            print("  reset      - Show what would be reset (dry run)")
            print("  reset confirm - Actually reset all state files and caches")
            print("  audit      - Run system audit and show results")
            print("  help       - Show this help message")
            sys.exit(0)
        
        else:
            print(f"Unknown command: {command}")
            print("Use 'python paper_digest_service.py help' for usage information")
            sys.exit(1)
    
    # Default: run the digest service
    run_once()
