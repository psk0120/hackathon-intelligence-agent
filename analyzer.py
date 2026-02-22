import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key safely
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def analyze_hackathon(url: str):
    prompt = f"""
Analyze this hackathon and extract structured information:

{url}

Return JSON only.
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text