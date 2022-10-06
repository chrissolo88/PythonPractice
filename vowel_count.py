def vowel_count(phrase):
    vowels = ['a','e','i','o', 'u']
    phrase_lst = list(phrase.lower())
    print({vow:phrase_lst.count(vow) for vow in vowels if vow in phrase_lst})
    """Return frequency map of vowels, case-insensitive.
    """
vowel_count('rithm school')
        #{'i': 1, 'o': 2}
        
vowel_count('HOW ARE YOU? i am great!') 
        #{'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
