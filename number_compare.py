def number_compare(a, b):
    print('Numbers are equal' if a == b else 'First is greater' if a>b else 'Second is greater')
    """Report on whether a>b, b>a, or b==a
        """
number_compare(1, 1)
       # 'Numbers are equal'
        
number_compare(-1, 1)
        #'Second is greater'
        
number_compare(1, -2)
        #'First is greater'
