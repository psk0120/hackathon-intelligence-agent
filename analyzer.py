import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")
print("API KEY LOADED:", API_KEY[:8])

client = genai.Client(api_key=API_KEY)


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
Return:
REJECTED

If technical, extract ONLY:

Hackathon Name:
Registration Link:
Mode (Online / Offline / Hybrid):
Registration Deadline:
Prize Pool (Total + Breakdown):

Return clean structured data.
"""
    print("PROMPT LENGTH:", len(prompt))
    print(type(prompt))

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    ]
)

    return response.text