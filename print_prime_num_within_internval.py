a=input("Enter two number for printing prime number with in internval ")
b=input()
if(a==b or a==1):
    print("Please Provide valid Input")
else:
    for i in range(a,b):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(str(i)+" is a prime number")