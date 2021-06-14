def st(a):
    '''
    float -> int

    The program receives a decimal number _as a float_  and rounds it down
    without the basic Python functions.
    In other words, it deletes the section after the audit.


    >>> a=677.876999
    >>> func3(a)
    677
    
    '''
    
    b="{}".format(a)
    return b
    
def func3(a):
    e=0
    c=st(a)
    d=c.index('.')
    num={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    for i in range(d):
           for j in c[i]:
           	e=e*10+num[j]
           	       	
    return e
a=677.876999
print(func3(a))
