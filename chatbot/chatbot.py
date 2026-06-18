from openai import  OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROK_API_KEY")
)

message = [{'role':'system','content' : '''Yoy are best Tutor for the Engineering Student Answer also related user Qouation give 
keep answer in 300 word not so lenghty or so shortly simply lovely'''}]

while True:
    user_prompt = input("User Prompt : ")
    if not  user_prompt:
        continue

    if user_prompt.lower() in ['quit','bye']:
        break
    message.append({'role' : 'user','content' : user_prompt})
    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=message,
    max_tokens=400,
    temperature=0.5
    )
    reply = response.choices[0].message.content
    print(reply)
    message.append({'role':'assistant','content':reply})

