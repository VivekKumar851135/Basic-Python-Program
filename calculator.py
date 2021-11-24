a=input("Enter first number ")
b=input("Enter second number ")
print("Enter your choice: ")
print("1: addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
choice=input()
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
if(choice==1):
    print(add(a,b))
elif(choice==2):
    print(sub(a,b))
elif(choice==3):
    print(multiply(a,b))
elif(choice==4):
    print(divide(a,b))
else:
    print("Give valid choice")