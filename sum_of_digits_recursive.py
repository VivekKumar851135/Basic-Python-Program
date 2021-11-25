b=0
def my_function(a):
    global b
    if(a==0):
        return b
    else:
        
        b=b+a%10
        a=a/10
        return  my_function(a)
   
c=input("Enter a number\n")
f=my_function(c)
print(f)