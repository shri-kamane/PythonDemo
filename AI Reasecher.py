
from openai import OpenAI
from dotenv import load_dotenv
import re
import os

load_dotenv()

""" AI Reascher """

print ("fill this info first for your perfection of your answer.")

system_role = input("Enter the role of ai : ")
ai_Audience = input("Enter the Audience of ai : ")
topic = input("Enter Topic of Todays Discusion : ")
tone = input("Enter tone of ai explanation : "  )
format = input("Enter the format : ")
length = input("Enter the length of answer (lines) ? ")

user_query = input("Enter the Query ? ")
System_Prompt = f'''imagine you are this role { system_role} person worjing on reacher of this topic {topic} having 10+ years of experience and your audience is this type {ai_Audience} you use this tone {tone} for the answer for give answer in this format {format} give in this length {length}'''



message = [{
            "role":"system",
            "content" : System_Prompt },
            {
                "role" : "user",
                "content" : user_query
            }
        ]

client = OpenAI(
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("OPENAI_API_KEY")
)

responce = client.chat.completions.create(
    model = "llama-3.1-8b-instant",
    messages = message,
    max_tokens=200,
    temperature=0.7
)

print(responce.choices[0].message.content)




"""
Tools Dicriptions 
"""

"""



tools = [
    { 
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "A simple calculator that evaluates mathematical expressions",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "is_prime",
        "description": "Check if a number is prime",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "integer",
                    "description": "The number to check"
                }
            },
            "required": ["number"]
        }
    }
    }
]
"""