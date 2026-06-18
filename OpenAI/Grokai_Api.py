from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client = OpenAI (
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROK_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{
        "role" : "system" , "content" : "hey I am best tutor for poytechinc student"},
        {
         "role" : "user" , "content" : "Explain The Concept of API?"
        }],
    max_tokens=400,
    temperature=0.5
)

print(response.choices[0].message.content)
print("token used: ", response.usage.total_tokens)
