def is_palindrome(phrase):
    phrase = ''.join(phrase.upper().split(' '))
    print(list(phrase) == list(phrase)[::-1])

is_palindrome('tacocat')
        # True

is_palindrome('noon')
        # True

is_palindrome('robert')
        # False


is_palindrome('taco cat')
        # True

is_palindrome('Noon')
        # True

