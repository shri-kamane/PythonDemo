
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



while True:
    a = int(input("Enter No 1 : "))
    b = int(input("Enter No 2 : "))
    op = input("Enter Operator from this(+,-,*,/) : ")
    
    if op not in ["+","-","*","/"]:
        print("Operator is invalid")
    elif op == "+":
            print("Result : ",add(a,b))
    elif op == "-":
            print("Result : ",sub(a,b))
    elif op == "*":
            print("Result : ",mul(a,b))
    elif op == "/" :
            print("Result : ",div(a,b))
    Agian = input("Do you want to continue (yes/no): ")
    if Agian.lower() != "yes":
         break
    