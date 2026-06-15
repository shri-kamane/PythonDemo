
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0 or b == 0:
        return ("in both values one value is Zero")
    else:
        return a/b

print("Welcome TO Calculator!")
dict = {"+":add,"-":sub,"*":mul,"/":div}

while True:
    a = int(input("Enter No 1 : "))
    b = int(input("Enter No 2 : "))
    op = input("Enter Operator from this(+,-,*,/) : ")
        
    if op not in dict:
            print("invalid operator")
    Result = dict[op](a,b)
    print(Result)

    again = input("Do you want continue ? (yes/no): ")
    if again.lower() != "yes":
         break
    

    