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
Extract structured hackathon information from this link.

URL: {url}

Return JSON with:
- name
- deadline
- prizes
- eligibility
- mode (online/offline)
- location

Return JSON only.
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