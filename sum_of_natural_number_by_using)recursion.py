a=input("Enter a number ")
def sum_of_interger(a):
    if(a==1):
        return 1
    else:
        return a+sum_of_interger(a-1)
print("sum of interger:- {}".format(sum_of_interger(a)))
