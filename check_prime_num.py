a=input("Enter a number= ")
if(a==1):
    print(str(a)+" is not prime number")
else:
    for i in range(2,a):
        if(a%i==0):
            print(str(a)+" is not prime number")
            break
    else:print(str(a)+" is  prime number")

