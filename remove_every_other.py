def remove_every_other(lst):
    count = 0
    new_lst = []
    for num in lst:
        if count%2 == 0:
            new_lst.append(num) 
        count += 1 
    print(new_lst)
    """Return a new list of other item.
    """
lst = [1, 2, 3, 4, 5]

remove_every_other(lst)
        #[1, 3, 5]


print(lst)
        #[1, 2, 3, 4, 5]

