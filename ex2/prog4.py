
def prog4(a):
 """ (int) -> list

With this function you can find the divisor( Counter ) of the desired number
And see them from small to large.

>>>prog4(36)
[1, 2, 3, 4, 6, 9, 12, 18, 36]

"""
 n=[]
 for i in range(1,a+1):
        if a%i==0:
            n.append(i)
 print(n)

a=int(input("Enter a number greater than one :"))
print(prog4(a))
