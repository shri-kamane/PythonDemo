import requests

req = {
    "title" : "hello",
    "body" : "fine",
    "user" : 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts',json= req)
print(response.json())