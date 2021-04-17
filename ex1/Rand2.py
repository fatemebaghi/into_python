import random
def Rand2(a,b):
    x=random.randint(a,b)
    if x % 2==0:
        return x
    elif x % 2 !=0 and a<=x<b:
        return x+1
    else:
        return x-1
a=int(input("Enter the first number 'a' :"))
b=int(input("Enter the second number 'b' :"))
print(Rand2(a,b))
