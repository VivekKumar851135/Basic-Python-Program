a=input("Enter a number\n")
b=[]
k=0
c=0
for i in range(4):
    b.append(a%10)
    a=a/10
    
for j in range(4):
    if(b[j]==0 or b[j]==1):
      c
    else:
       k=k+1
if(k>=1):
    print("not binary")
else:
    print("binary")
