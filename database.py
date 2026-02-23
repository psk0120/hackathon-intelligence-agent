import json
from pathlib import Path

DB_FILE = "memory.json"


def load_all_hackathons():
    if not Path(DB_FILE).exists():
        return []

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_hackathon(entry):
    data = load_all_hackathons()

    # avoid duplicates
    if any(x["url"] == entry["url"] for x in data):
        return

    data.append(entry)

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)