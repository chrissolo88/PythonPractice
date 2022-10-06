def reverse_vowels(s):
    phrase_list = list(s)
    vowels= ['a','e','i','o','u']
    vowel_ind = [ind for ind,char in enumerate(phrase_list) if char in vowels]
    vowel_char = [char for ind,char in enumerate(phrase_list) if char in vowels]
    vowel_char.reverse()
    for ind, vow in enumerate(vowel_char):
        phrase_list[vowel_ind[ind]] = vow 
    print(''.join(phrase_list))
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.
    """
reverse_vowels("Hello!")
    #'Holle!'

reverse_vowels("Tomatoes")
    #'Temotaos'

reverse_vowels("Reverse Vowels In A String")
    #'RivArsI Vewols en e Streng'

reverse_vowels("aeiou")
    #'uoiea'

reverse_vowels("why try, shy fly?")
    #'why try, shy fly?''
