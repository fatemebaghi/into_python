def P(A,B,C):
	return (A+B+C)/2
def s(A,B,C):
	p=P(A,B,C)
	return (p*(p-A)*(p-B)*(p-C))**0.5
    
def AreaX(A,B,C,D,E):
    
    if A == 0 :
        return s(B,C,D)
    elif B == 0 :
        return s(A,C,D)
    elif C == 0 :
        return s(A,B,D)
    elif D == 0 :
        return s(A,B,C)

    else:
        return s(A,B,E)+s(C,D,E)
    
A=int(input("Enter the first side :"))
B=int(input("Enter the second side :")) 
C=int(input("Enter the third side :"))  
D=int(input("Enter the fourth side :"))
E=int(input("Enter the diameter. and if it's a triagle Enter 0 :"))
print(AreaX(A,B,C,D,E))
