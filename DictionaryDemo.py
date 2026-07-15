students = {"John": 85, "Alice": 92, "Bob": 78}
print(students)
#Accessing values
print(students['John'])

#Insert Value and new key
students['Mahesh']=90
print(students)

#Update Value and Key
students['Alice']=45
print(students)

#pop method
students.pop('Alice')
print(students)

#Loop through dictionary

for key in students:
    print(key)

for val in students.values():
    print(val)

for key, val in students.items():
    if val < 80:
        print(key,val)

