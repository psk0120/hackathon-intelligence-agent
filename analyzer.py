import os
import json
from dotenv import load_dotenv
from google import genai

# ================================
# LOAD ENVIRONMENT
# ================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

print("API KEY LOADED:", API_KEY[:8])

# ✅ Correct Gemini client
client = genai.Client(api_key=API_KEY)


# ================================
# HACKATHON ANALYZER
# ================================

def analyze_hackathon(url: str):

    prompt = f"""
You are an autonomous Hackathon Intelligence Agent.

Analyze this event page:

{url}

FIRST:
Determine if this is a TECHNICAL hackathon.

Include ONLY:
- AI
- Software
- Engineering
- Cybersecurity
- Hardware
- Innovation
- Startup building

Reject:
- Business case competitions
- Marketing contests
- Quizzes
- Non-technical events

If NOT technical:
Return exactly:
REJECTED

If technical, extract ONLY:

Hackathon Name
Registration Link
Mode (Online / Offline / Hybrid)
Registration Deadline
Prize Pool (total + breakdown)

Return STRICT JSON:

{{
"title": "",
"registration_link": "",
"mode": "",
"deadline": "",
"prize_pool": "",
"tags": []
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        text = response.text.strip()

        # --------------------------------
        # Reject non-technical events
        # --------------------------------
        if "REJECTED" in text.upper():
            return None

        # --------------------------------
        # Parse JSON safely
        # --------------------------------
        start = text.find("{")
        end = text.rfind("}") + 1

        json_text = text[start:end]

        data = json.loads(json_text)

        return data

    except Exception as e:
        print("⚠️ Gemini failed:", e)
        return None