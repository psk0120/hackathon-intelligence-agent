from scraper import get_devpost_hackathons
from analyzer import analyze_hackathon
from agent import process_result, rank_opportunities

import json
import time

from database import already_seen, remember
from decision import should_apply
from notifier import notify


def main():

    print("\n🚀 Hackathon Intelligence Agent Starting...\n")

    # STEP 1 — Discover hackathons
    links = get_devpost_hackathons()
    print(f"✅ Found {len(links)} hackathons\n")

    results = []

    # Limit during testing (prevents Gemini quota burn)
    TEST_LIMIT = 2

    # STEP 2 — Analyze + Decide
    for i, link in enumerate(links[:TEST_LIMIT], start=1):

        print(f"\n🔎 [{i}/{TEST_LIMIT}] Analyzing:", link)

        # Skip already analyzed
        if already_seen(link):
            print("⏭️ Already analyzed")
            continue

        try:
            # AI Analysis
            analysis = analyze_hackathon(link)

            # Agent processing
            result = process_result(link, analysis)

            # Decision engine
            decision = should_apply(result)

            # Notify user
            notify(result, decision)

            # Remember processed hackathon
            remember(link)

            results.append(result)

        except Exception as e:
            print("❌ Analysis failed:", e)

        # Prevent Gemini rate limits
        print("⏳ Waiting 5 seconds...")
        time.sleep(5)

    # STEP 3 — Rank Opportunities
    ranked = rank_opportunities()

    with open("ranked_hackathons.json", "w", encoding="utf-8") as f:
        json.dump(ranked, f, indent=2, ensure_ascii=False)

    print("\n🏆 Ranked opportunities saved.")
    print("🤖 Agent finished.\n")


if __name__ == "__main__":
    main()