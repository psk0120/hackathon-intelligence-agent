from scraper import get_devpost_hackathons
from analyzer import analyze_hackathon
from agent import process_result
from database import already_seen, remember

import json
import time


def main():

    print("\n🚀 Hackathon Intelligence Agent Starting...\n")

    # STEP 1 — Discover hackathons
    links = get_devpost_hackathons()
    print(f"✅ Found {len(links)} hackathons\n")

    results = []

    # prevent free-tier quota burn
    TEST_LIMIT = 2

    # STEP 2 — Analyze + Filter
    for i, link in enumerate(links[:TEST_LIMIT], start=1):

        print(f"\n🔎 [{i}/{TEST_LIMIT}] Checking:", link)

        # Skip already analyzed hackathons
        if already_seen(link):
            print("⏭ Already analyzed")
            continue

        # SAFE GEMINI CALL
        try:
            analysis = analyze_hackathon(link)

        except Exception as e:
            print("⚠️ Gemini failed:", e)
            continue

        # Process + technical filtering
        result = process_result(link, analysis)

        if result is None:
            print("❌ Non-technical event skipped")
            continue

        print("✅ Technical hackathon saved")

        results.append(result)

        remember(link)

        # avoid rate limits
        time.sleep(10)

    # STEP 3 — Save structured intelligence
    with open("filtered_hackathons.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n🏆 Technical hackathons saved → filtered_hackathons.json")
    print("🤖 Agent finished.\n")


if __name__ == "__main__":
    main()