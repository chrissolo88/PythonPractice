def list_manipulation(lst, command, location, value=None):
    indx = 0 if location == "beginning" else -1 if location == "end" else "None"
    if indx == "None":
        return print(indx)
    else:
        return lst.pop(indx) if command == "remove" else lst.insert(indx, value) if command == "add" and indx == 0 else lst.append(value) if command == "add"  else print("None")
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    # remove: remove item at beginning or end, and return item removed
"""
lst = [1, 2, 3]

list_manipulation(lst, 'remove', 'end')
        # 3

list_manipulation(lst, 'remove', 'beginning')
        # 1

print(lst)
        # [2]

    # add: add item at beginning/end, and return list

lst = [1, 2, 3]

list_manipulation(lst, 'add', 'beginning', 20)
        # [20, 1, 2, 3]

list_manipulation(lst, 'add', 'end', 30)
        # [20, 1, 2, 3, 30]

print(lst)
        # [20, 1, 2, 3, 30]

   # Invalid commands or locations should return None:

list_manipulation(lst, 'foo', 'end') is None
        # True

list_manipulation(lst, 'add', 'dunno') is None
        # True

