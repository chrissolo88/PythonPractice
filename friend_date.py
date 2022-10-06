def friend_date(a, b):
    print("True") if set(a[2]) & set(b[2]) else print("False")
    
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

friend_date(elmo, sauron)
        # False

friend_date(sauron, gandalf)
        # True
