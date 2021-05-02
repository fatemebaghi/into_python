def prog1(a,b):
  """ (int,int)-> list
You can use this function to find even numbers between two numbers.
Please pay attention that a must be bigger than b .

>>> prog1(12,26)
[14, 16, 18, 20, 22, 24] 
  """
  num=[]
  for m in range(a,b):
        if (m%2)==0 and m!=a and m!=b :
            num.append(m)
  print(num)

       
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))    
print(prog1(a,b))        
