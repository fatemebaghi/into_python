def func1(a):
    '''
    str -> list
    
    The program receives one or more English sentences and separates the sentence
    components and returns them in a list.

    
    >>> a='Hello . Nice to meet you.'
    >>> func1(a)
    ['Hello', '.', 'Nice', 'to', 'meet', 'you.']
    
    '''
    
    b=a.split()
    return b

a=input("Enter a sentence in english : ")
print(func1(a))


