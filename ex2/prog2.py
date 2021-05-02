def prog2(a,b):
     """ (int,int)-> list
You can use this function to find even numbers between two numbers.
In this function, it does not matter which a or b is bigger .

>>> prog1(12,26)
[14, 16, 18, 20, 22, 24]

>>> prog1(26,12)
[14, 16, 18, 20, 22, 24]

"""
     if b>a :
      num=[]
      for m in range(a,b):
            if (m%2)==0 and m!=a and m!=b :
                num.append(m)
      print(num)
     if a>b :
       print(prog2(b,a))
        
           
       
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))      
print(prog2(a,b))        



       
