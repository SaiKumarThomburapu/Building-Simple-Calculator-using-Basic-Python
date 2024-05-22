# SIMPLE CALCULATOR
# we define function for each operator
print("Operations are:'+','-','*','/'")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Zero Division Error"
    else:
        return a/b
num1=float(input("Enter the first value:"))
num2=float(input("Enter the second value:"))

# Chossing the  Operation
choice=str(input("Enter the operation : "))
if choice in ('+','-','*','/'):
    if choice=='+':
        print("Addition of two numbers is",add(num1,num2))
    elif choice=='-':
        print("Subtraction of two numbers is",sub(num1,num2))
    elif choice=='*':
        print("Multiplication of two numbers is",mul(num1,num2))
    elif choice=='/':
        print("Division of two numbers is",div(num1,num2))
else:
    print("Invalid Operation")

