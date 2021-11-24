a=input("Enter a number ")
sum=0
if(a<0):
    raise KeyboardInterrupt("Please enter positive no.")
else:
    for i in range(0,a+1):
        sum+=i
    print("Sum of natural number is {}".format(sum))