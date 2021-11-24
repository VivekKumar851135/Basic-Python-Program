a=input("Enter a number: ")
b=a
def factorial(a):
    if(a==1):
        return 1
    else:
        return a*factorial(a-1)
print("factorial of {0} is {1}".format(b,factorial(a)))