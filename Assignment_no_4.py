"""students mangement student using dictionary 
requirement = roll, marks , name input 
store value in dictionary"""

print("Welcome to Student Management System!")

students = []

n = int(input("Enter The No of Student You Want To Insert : "))
for i in range (n):
    student = {}
    student['Name'] = input("Enter the Student : ")
    student['Roll No'] = int(input("Enter Roll No : "))
    student['Marks'] = int(input("Enter Marks : "))
    students.append(student)

print(students)

