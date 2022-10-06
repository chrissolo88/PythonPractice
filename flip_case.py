def flip_case(phrase, to_swap):
    swapped = [char.upper() if char == to_swap.lower() else char.lower() if char == to_swap.upper() else char for char in list(phrase)]
    print(''.join(swapped))
 
flip_case('Aaaahhh', 'a')
        # 'aAAAhhh'
flip_case('Aaaahhh', 'A')
        # 'aAAAhhh'
flip_case('Aaaahhh', 'h')
        # 'AaaaHHH'


