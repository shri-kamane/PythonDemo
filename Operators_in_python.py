
#Arithmatic Operators : 
age = int(input("Please Enter Your Age:"))
print("add ",age+1)
print("sub ",age-1)
print("mul ",age*2)
print("div ",age/2)
print("floordiv ",age//2)
print("mod ",age%2)
print("pow ",age**2)

#Conditional Operators :
if age == 18:
    print("You are eligible for voting")
if age != 18:
    print("You are not eligible for voting")
if age > 18: 
    print("You are eligible for voting")
if age < 18:
    print("You are not eligible for voting")
if age >= 18:
    print("You are eligible for voting")
if age <= 18:
    print("You are not eligible for voting")

#Logical Operators :

if age >= 18 and age <= 40:
    print("Your age is between of 18 and 40")

if age >= 40 or age >= 60:
    print("Your age is in between 40 and 60")

