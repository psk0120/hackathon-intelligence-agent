import json
from database import save_hackathon

"""
Hackathon Intelligence Agent Core
Filters technical hackathons + structures data
"""

TECH_KEYWORDS = [
    "ai",
    "machine learning",
    "software",
    "developer",
    "engineering",
    "cybersecurity",
    "hardware",
    "robotics",
    "blockchain",
    "data",
    "startup",
    "programming",
    "hackathon",
    "tech"
]


def is_technical_event(analysis_text: str):
    """
    Detect if hackathon is technical.
    """
    if not analysis_text:
        return False

    text = analysis_text.lower()

    for keyword in TECH_KEYWORDS:
        if keyword in text:
            return True

    return False


def process_result(link, analysis):
    """
    Convert AI output into structured intelligence.
    Returns None if event is non-technical.
    """

    if analysis is None:
        return None

    # --- Technical filtering ---
    if not is_technical_event(str(analysis)):
        return None

    # --- Structured extraction ---
    data = {
        "url": link,
        "title": analysis.get("title"),
        "registration_link": analysis.get("registration_link"),
        "mode": analysis.get("mode"),
        "deadline": analysis.get("deadline"),
        "prize_pool": analysis.get("prize_pool"),
        "tags": analysis.get("tags"),
    }

    return data