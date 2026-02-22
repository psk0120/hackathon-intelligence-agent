from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": "Say AI connected successfully"}],
)

print(response.choices[0].message.content)