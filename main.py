from scraper import get_devpost_hackathons
from analyzer import analyze_hackathon
import json


def main():
    # STEP 1 — discover hackathons
    links = get_devpost_hackathons()
    print(f"Found {len(links)} hackathons")

    results = []

    # STEP 2 — analyze each hackathon
    for link in links[:5]:   # limit for testing
        print("\nAnalyzing:", link)

        result = analyze_hackathon(link)

        print(result)

        results.append(result)

    # STEP 3 — save intelligence
    with open("hackathons.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()