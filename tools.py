from openai import OpenAI
from dotenv import load_dotenv
import json
import os
load_dotenv()
###Define function####
def calculator(exp:str)->str:
    try:
        return str(round(eval(exp), 2))
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
    "type" : "function",
    "function" : {
        "name" : "calculator",
        "discription" : "calucation of the given using simple evel function",
        "parameters" : {
            "type" : "object" ,
            "properties" : {
                "exp" : {
                    "type" : "string",
                    "discription" : "expression which on the performing the opearations"
                }
            },
            "required" : ["exp"]
        }
     }
}
,{
    "type" : "function",
    "function" : {
        "name" : "oddevenchecker",
        "discription" : "cheker for given is it odd or even",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "number" : {
                    "type" : "string",
                    "discription" : "to take number from user"
                }
            },
            "required" : ["number"]
        }
    }
}]

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
            result = calculator(tool_input["exp"])
            return f"Calculator Result: {result}"
        elif tool_name == "is_prime":
            result = is_prime(tool_input["number"])
            return f"Is Prime: {result}"
        
    else:
        print("No tool was called.")
        return f"AI Response: {message_response}"
print(run_agent("Calculate 2 percent  of 50."))