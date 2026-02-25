def should_apply(result):

    tags = result.get("tags", [])
    prize = str(result.get("prize_pool", "")).lower()
    mode = str(result.get("mode", "")).lower()

    tech_keywords = [
        "ai",
        "cybersecurity",
        "software",
        "hardware",
        "engineering",
        "startup",
        "innovation",
    ]

    score = 0

    for tag in tags:
        if any(k in tag.lower() for k in tech_keywords):
            score += 2

    if "online" in mode:
        score += 1

    if "$" in prize or "usd" in prize:
        score += 1

    return "APPLY" if score >= 3 else "IGNORE"