from openai import OpenAI
from dotenv import load_dotenv
import json
import os
import re
import requests
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

### Tools / Functions defined devloper not by any LLM ###
def oddevenchecker(number:int):
    if(number%2==0):
        return f"5{number} is even"
    else :
        return f"{number} is odd"

def weather(lati : int,longi : int,curent_wea : bool):
    url="https://api.open-meteo.com/v1/forecast"
    params = {'latitude': lati, 'longitude': longi, 'current_weather': curent_wea}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return(f"Current temperature of pune:" , data['current_weather']['temperature'])

### tool discrption json ###
tool = [ 
            {
        "type" : "function",
        "function" : {
            "name" : "oddevenchecker",
            "description" : "cheker for given is it odd or even",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "number" : {
                        "type" : "integer",
                        "description" : "to take number from user"
                    }
                },
                "required" : ["number"]
            }
        }
    },{
        "type" : "function",
        "function" : {
            "name" : "weather",
            "description" : "weather prediction on given longitude and latitude",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "lati" : {
                        "type" : "number",
                        "description" : "taking latitude from the user"},
                    "longi" : {
                        "type" : "number",
                        "description" : "taking lomgitude from the user"
                        },
                    "curent_wea" : {
                        "type" : "boolean",
                        "description" : "taking permition from the user ( true/false )"
                    }
                },
                "required" : ["lati","longi","curent_wea"]
            }
        }
    }
]
#### Agent to decide that tool are inside or not in operatioon ####
def run_agent(user_query):
    message = [{
        "role" : "system",
        "content" : "Act like You are helpful guide "
    },{
        "role" : "user",
        "content" : user_query
    }]
    response = client.chat.completions.create(
       model="llama-3.1-8b-instant",
       messages=message,
       tools=tool,
       max_tokens = 400,
       temperature= 0.5
       )
    message_responce = response.choices[0].message
    if message_responce.tool_calls:
        tool_name = message_responce.tool_calls[0].function.name
        print(f"tool called : {tool_name}")
        tool_input = json.loads(message_responce.tool_calls[0].function.arguments)
        
        if tool_name == "oddevenchecker":
            result = oddevenchecker(tool_input["number"])
            return f"Odd or Even Result : {result}"
        elif tool_name == "weather":
            result = weather(tool_input["lati"],tool_input["longi"],tool_input["curent_wea"])
            return f"Weather is in you city it {result}"
    else : 
        print("nothing is called")
        return f"AI Responce : {message_responce}"
    
print(run_agent("4 is odd or even"))
print(run_agent("todays weather in pune here's 'latitude': 18.5204, 'longitude': 73.8567"))

