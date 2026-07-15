import json
json_data = {
    "name" : "Shrirudra",
    "RollNO" : 12,
    "address" : "pune" ,
    "Array" : {"+" : "add" , "-" : "sub" , "*" : "mul" ,"/" : "div"},
    "is_student" : True
}

py_data  =[{"subject" : "maths", "marks" : 89 },
    {"subject" : "science", "marks" : 83 },
    {"subject" : "geometry", "marks" : 85 },
    {"subject" : "history", "marks" : 78 },
    {"subject" : "geography", "marks" : 80 }
]

json_str = json.dumps(json_data)
python_dic = json.loads(json_str)

print(type(json_str)) #json.dumps() = used to convert data of pyhton file into the json file
print(type(python_dic)) #json.load() = used to convert data of json file into the python file

with open ("C:\\Users\\Shrirudra\\Internship Codes\\python_json.json","r") as file:
    data = json.load(file)

print(data)
print(type(data))

with open ("C:\\Users\\Shrirudra\\Internship Codes\\python_json.json","w") as file:
    json.dump(py_data,file)
