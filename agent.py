import json
from database import save_hackathon, load_all_hackathons


def score_hackathon(analysis_text: str):
    """
    Simple intelligence scoring system.
    Later this becomes AI-driven.
    """

    score = 0

    keywords = {
        "ai": 3,
        "startup": 2,
        "funding": 4,
        "remote": 3,
        "international": 3,
        "prize": 2,
        "open source": 2,
        "travel": 1
    }

    text = analysis_text.lower()

    for k, v in keywords.items():
        if k in text:
            score += v

    return score


def process_result(url, analysis):
    score = score_hackathon(analysis)

    data = {
        "url": url,
        "analysis": analysis,
        "score": score
    }

    save_hackathon(data)

    return data


def rank_opportunities():
    hacks = load_all_hackathons()

    ranked = sorted(hacks, key=lambda x: x["score"], reverse=True)

    return ranked