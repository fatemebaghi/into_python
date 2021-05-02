def prog3(a):
    """ (int) -> bool

You can recognize prime numbers with this function.
And find out if the number you want is prime or not.

>>> prog3(11)
True
>>> prog3(18)
False

"""
    while True :
        for i in range (2, a):
            if (a % i) == 0 :
                return False
                break
        if (a % i) != 0:
            return True
            break

      
a=int(input("Enter a number greater than one :"))
print(prog3(a))
