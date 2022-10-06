def repeat(phrase, num):
    print(phrase*num if type(num) == int and num >= 0 else 'None')
    """Return phrase, repeated num times.
    """
repeat('*', 3)
       # '***'

repeat('abc', 2)
       # 'abcabc'

repeat('abc', 0)
      #  ''

    #Ignore illegal values of num and return None:

repeat('abc', -1)
        #None

repeat('abc', 'nope')
        #None

