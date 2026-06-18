Name = input("Enter The Name Of The Student : ")
Math = int(input("Enter The Marks for Math :"))
Marathi = int(input("Enter The Marks for Marathi :"))
History = int(input("Enter The Marks for History :"))
Geography = int(input("Enter The Marks for Geography :"))
Science =  int(input("Enter The Marks for Science :"))

Percentage = (Math + Marathi + History +Geography + Science )/ 5
print(" ")

print("-----------------Report Card-------------------")
print("The Percentage of the ",Name,"is : ",Percentage)

if Percentage >= 90 and Percentage <= 100:
    print("Mr.",Name,"You Got Grade : A")
elif Percentage >= 75 and Percentage < 90:
    print("Mr.",Name,"You Got Grade : B")
elif Percentage >= 65 and Percentage < 75:
    print("Mr.",Name,"You Got Grade : C")
elif(Percentage >= 50 and Percentage < 65   ):
    print("Mr.",Name,"You Got Grade : D")
elif(Percentage >= 35 and Percentage < 50):
    print("Mr.",Name,"You Got Grade : E")
else:
    print("Mr.",Name,"You are Fail , Better Luck Next Time!")

print("-----------------------------------------------")