def min_max_keys(d):
   keys = [key for key in d.keys()]
   keys.sort()
   print((keys[0], keys[-1]))

min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        # (1, 10)
        
min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
       # ('apple', 'cherry')
