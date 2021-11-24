import sys


a=input("Enter two number:- ")
b=input()
lcm=[]
lcm1=[]
lcm2=[]
for i in range(1,a):
    if(a%i==0):
        lcm.append(i)
for j in range(1,b):
    if(b%j==0):
        lcm1.append(j)
print(sys.getsizeof(lcm))
if(sys.getsizeof(lcm)>sys.getsizeof(lcm2)):
    size=len(lcm2)
elif(sys.getsizeof(lcm)<sys.getsizeof(lcm2)):
    size=len(lcm)
else:
    size=len(lcm)
for l in range()
for k in range(0,size):
    if(lcm[k]==lcm1[k]):
        lcm2.append(lcm[k])

print(lcm)
print(lcm1)
print(lcm2)
