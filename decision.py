def should_apply(hackathon):

    score = hackathon.get("score", 0)

    if score >= 8:
        return "APPLY"

    elif score >= 6:
        return "WATCH"

    return "IGNORE"