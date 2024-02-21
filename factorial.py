x= int(input("enter the value of n"))
def factorial(x):
    
    return 1 if (x==1 or x==0) else x * factorial(x-1)

print ("factorail of x is ", factorial(x) )
    