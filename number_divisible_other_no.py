a=input("Enter a number:- ")
for i in range(1,a):
    if(a%i==0):
        print("{0} is divisible by {1} ".format(a,i))