def notify(hackathon, decision):

    if decision == "APPLY":
        print(f"🔥 APPLY NOW → {hackathon['url']}")

    elif decision == "WATCH":
        print(f"👀 Keep Watching → {hackathon['url']}")