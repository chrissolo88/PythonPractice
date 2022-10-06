def multiple_letter_count(phrase):
    lst = list(phrase)
    count = {char:lst.count(char) for char in set(lst)}
    print(count)
    """Return dict of {ltr: frequency} from phrase."""

multiple_letter_count('yay')
       # {'y': 2, 'a': 1}

multiple_letter_count('Yay')
       # {'Y': 1, 'a': 1, 'y': 1}
