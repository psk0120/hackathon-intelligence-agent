from google import genai

client = genai.Client(api_key="AIzaSyBJleWt6FZ6AWL3I4I4VSEtetKQGiQQShA")

def analyze_hackathon(url):

    prompt = f"""
You are a Hackathon Intelligence Agent.

Analyze this hackathon page:
{url}

Return JSON:

{{
"name":"",
"organizer":"",
"themes":"",
"deadline":"",
"mode":"",
"prize":"",
"why_join":""
}}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text