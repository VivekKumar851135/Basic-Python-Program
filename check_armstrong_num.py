a=input("Enter the numbers= ")
e=a
c=0
for i in range(0,a):
    if(a==0):
        break
    b=a%10
    c+=b*b*b
    a=a/10
    
if(e==c):
    print("{0} Armstrong Number".format(e))
else:
   print("{0} is not armstrong Number".format(e))

  