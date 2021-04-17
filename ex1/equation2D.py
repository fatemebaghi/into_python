def Delta(a,b,c):
    return ((b**2)-(4*a*c))

def equation2D(a,b,c):
    if Delta(a,b,c) < 0 :
        return print("This function has no answer")
    elif Delta(a,b,c) == 0 :
        x = -b/(2*a)
        return print("This function has an answer. The answer is {}.".format(x))
    elif Delta(a,b,c) > 0 :
        x1 = (-b +(Delta(a,b,c)**2))/(a*2)
        x2 = (-b -(Delta(a,b,c)**2))/(a*2)
        return print("This function has two answers. The answers are {} and {}.".format(x1,x2)) 
a=int(input("Enter a coefficient X**2' :"))    
b=int(input("Enter b 'coefficient X' :"))
c=int(input("Enter c 'the intercept' :"))    
print(equation2D(a,b,c))
