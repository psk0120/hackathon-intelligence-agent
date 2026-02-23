from scraper import get_devpost_hackathons
from analyzer import analyze_hackathon
from agent import process_result, rank_opportunities
import json
import time


def main():

    print("\n🚀 Hackathon Intelligence Agent Starting...\n")

    links = get_devpost_hackathons()
    print(f"✅ Found {len(links)} hackathons\n")

    TEST_LIMIT = 2

    for i, link in enumerate(links[:TEST_LIMIT], start=1):

        print(f"\n🔎 [{i}/{TEST_LIMIT}] Analyzing:", link)

        try:
            analysis = analyze_hackathon(link)

            result = process_result(link, analysis)

            print(f"⭐ Score: {result['score']}")

        except Exception as e:
            print("❌ Analysis failed:", e)

        print("⏳ Waiting 5 seconds...")
        time.sleep(5)

    ranked = rank_opportunities()

    with open("ranked_hackathons.json", "w", encoding="utf-8") as f:
        json.dump(ranked, f, indent=2, ensure_ascii=False)

    print("\n🏆 Ranked opportunities saved.")
    print("🤖 Agent finished.\n")


if __name__ == "__main__":
    main()