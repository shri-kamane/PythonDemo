from openai import OpenAI
from dotenv import load_dotenv
import json
import os
load_dotenv()
###Define function####
def calculator(expression:str)->str:
    try:
        return str(round(eval(expression), 2))
    except:
        return "Invalid expression"
def is_prime(number:int)->bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
####tool description
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
####Agent Loop###
def run_agent(user_question:str):
    message = [
        {
            "role": "system",
            "content": "You are a helpful math assistant."
        },
        {
            "role": "user",
            "content": user_question
        }
    ]
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=message,
        tools=tools,    
        max_tokens=200,
        temperature=0.7
    )
    message_response = response.choices[0].message
    if message_response.tool_calls:
        print(message_response.tool_calls)
        print("\n")
        tool_name = message_response.tool_calls[0].function.name
        print(f"Tool called: {tool_name}")
        tool_input = json.loads(message_response.tool_calls[0].function.arguments)
        if tool_name == "calculator":
            result = calculator(tool_input["expression"])
            return f"Calculator Result: {result}"
        elif tool_name == "is_prime":
            result = is_prime(tool_input["number"])
            return f"Is Prime: {result}"
        
    else:
        print("No tool was called.")
        return f"AI Response: {message_response}"
print(run_agent("Calculate 2 percent  of 50."))