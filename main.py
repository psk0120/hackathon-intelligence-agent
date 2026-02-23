from scraper import get_devpost_hackathons
from analyzer import analyze_hackathon
import json
import time


def main():

    print("\n🚀 Hackathon Intelligence Agent Starting...\n")

    # STEP 1 — discover hackathons
    links = get_devpost_hackathons()
    print(f"✅ Found {len(links)} hackathons\n")

    results = []

    # VERY IMPORTANT FOR FREE TIER
    TEST_LIMIT = 2

    for i, link in enumerate(links[:TEST_LIMIT], start=1):

        print(f"\n🔎 [{i}/{TEST_LIMIT}] Analyzing:", link)

        try:
            result = analyze_hackathon(link)

            print("✅ Analysis Complete\n")

            results.append({
                "url": link,
                "analysis": result
            })

        except Exception as e:
            print("❌ Analysis failed:", e)

        # Prevent Gemini rate limit
        print("⏳ Waiting 5 seconds to avoid rate limits...\n")
        time.sleep(5)

    # STEP 3 — save intelligence
    with open("hackathons.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n💾 Intelligence saved → hackathons.json")
    print("🏁 Agent finished successfully.\n")


if __name__ == "__main__":
    main()