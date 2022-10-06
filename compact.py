def compact(lst):
    
    print([itm for itm in lst if itm])


compact([0, 1, 2, '', [], False, (), None, 'All done'])
        # [1, 2, 'All done']
