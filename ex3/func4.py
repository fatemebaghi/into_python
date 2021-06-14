def func4(g):
    '''
    list -> list

    The program receives a list containing a number of ordered pairs in the tuple
    and simplifies the numbers for each tuple, then delivers a new list containing
    simplified ordered pairs.
    This program can be used to simplify the face and denominator of the deduction. 


    >>> g=[(14,7),(100,20),(20,100),(2,16),(4,36),(9,27)] 
    >>> func4(g)
    [(2.0, 1.0), (5.0, 1.0), (1.0, 5.0), (1.0, 8.0), (1.0, 9.0), (1.0, 3.0)]
    
    '''
    
    list1=[]
    for i in g:
        (x,y)=i
        while y and x!=0:
            if x>y:
                (x,y)=(y,x%y)
                b=(i[0]/x,i[1]/x)
                list1.append(tuple(b))
            if x<y:
                (y,x)=(x,y%x)
                b=(i[0]/y,i[1]/y)
                list1.append(tuple(b))
    return list1
             

g=[(14,7),(100,20),(20,100),(2,16),(4,36),(9,27)]    
print(func4(g))    
          


            
            
