def list_check(lst):
    lst_chk = [type(itm) is list for itm in lst]
    print(all(lst_chk))

list_check([[1], [2, 3]])
        # True

list_check([[1], "nope"])
        # False

