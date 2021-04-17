def P(A,B,C):
	return (A+B+C)/2
def s(A,B,C):
	p=P(A,B,C)
	return (p*(p-A)*(p-B)*(p-C))**0.5
def Area(A,B,C,D,E):

  if  D==0 :
        return s(A,B,C)
  elif  D != 0 :
        return s(A,B,E)+s(C,D,E)
A=int(input("Enter the first side 'A' :"))
B=int(input("Enter the second side 'B' :")) 
C=int(input("Enter the third side 'C' :"))  
D=int(input("Enter the fourth side 'D' :"))
E=int(input("Enter the diameter. and if D=0 Enter 0 :"))

print(Area(A,B,C,D,E))
