def func2(a):
    '''
    str -> int
    str -> float

    The program receives a number typed in a string and
    delivers the same number as a float or int.

    >>> a='654'
    >>> func2(a) 
    654
    >>> a='654.98'
    >>> func2(a)
    654.98
    
    '''
 
    b=0
    d=len(a)-a.find('.')-1
    num={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    
    if '.' not in a:
        for c in a:
            b=b*10+num[c]
        return b
        
    else:
        for c in a:
            while c!='.':
                b=b*10+num[c]
                f=b*(10**(-d))
                break
        return f


a=input("Enter a number : ")
print(func2(a))

