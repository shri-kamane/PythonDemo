from openai import OpenAI
from dotenv import load_dotenv
import re
import os
load_dotenv()

topic = input("Enter Topic : ")
Role = input("enter role system (blogger,story-writer,researcher)? : ")
audience = input("Entre the type of Audience (beginer,Expert,pro,noob)? : ")
tone = input("Enter User Tone Preference (simple,friendly,strict)? : ")
System_prompt = f'''write on this {topic} as excellent perfrom on this {Role} 
                having this type of {audience} use this {tone} give onlly 300 words as simple fromat to topic
'''

client = OpenAI(
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("API_KEY_GROK")
)

responce = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
            {"role" : "system" , "content" : System_prompt}],
    max_tokens=300,
    temperature=0.7
)

result = responce.choices[0].message.content
print(result)
