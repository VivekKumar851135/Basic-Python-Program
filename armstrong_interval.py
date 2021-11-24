a=input("Enter the first interval= ")
f=input("Enter the Second interval= ")
if(a==0 or f==0):
    raise KeyboardInterrupt("Please enter non zero interval")
    

for j in range(a,f):
    c=0
    g=j
    for i in range(0,g):
        if(g==0):
            break
        b=g%10
        c+=b*b*b
        g=g/10
    if(j==c):
        print("{0} Armstrong Number".format(j)) 
        
  