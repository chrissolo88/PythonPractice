def includes(collection, sought, start=None):
    
    if type(collection) is dict:
        print(sought in collection.values())
    elif type(collection) is list or type(collection) is tuple:
        print(sought in collection) if start == None else print(sought in collection[start:])
    elif type(collection) is set:
        print(sought in collection)
    elif type(collection) is str:
        print(sought in list(collection)) if start == None else print(sought in list(collection)[start:])
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.
    """
includes([1, 2, 3], 1)
        # True

includes([1, 2, 3], 1, 2)
        # False

includes("hello", "o")
        # True

includes(('Elmo', 5, 'red'), 'red', 1)
        # True

includes({1, 2, 3}, 1)
        # True

includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        # True

includes({"apple": "red", "berry": "blue"}, "blue")
        # True