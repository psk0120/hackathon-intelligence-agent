import json
import os

DB_FILE = "memory.json"
SEEN_FILE = "seen.txt"


# =============================
# MEMORY SYSTEM
# =============================

def load_all_hackathons():
    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_hackathon(data):
    hackathons = load_all_hackathons()
    hackathons.append(data)

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(hackathons, f, indent=2, ensure_ascii=False)


# =============================
# SEEN TRACKER
# =============================

def already_seen(link):
    if not os.path.exists(SEEN_FILE):
        return False

    with open(SEEN_FILE, "r") as f:
        return link in f.read().splitlines()


def remember(link):
    with open(SEEN_FILE, "a") as f:
        f.write(link + "\n")