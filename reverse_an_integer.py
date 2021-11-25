a=input("Enter a number")
b=[]
j=0

reverse=0
for i in range(100):
    if(a%10!=0):
        b.append(a%10)
        a=a/10
        ++j
    else:
        break
for k in range(len(b)):
    reverse=reverse+b[k]*pow(10,len(b)-k-1)
print(reverse)  





