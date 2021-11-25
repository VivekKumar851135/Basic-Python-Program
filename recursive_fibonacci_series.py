def my_function(a,b):
    if(len(str(b))==5):
        exit()
    else:
        c=a+b
        a=b
        b=c
        print(str(b))
        my_function(a,b)
print("0")
print("1")
my_function(0,1)
