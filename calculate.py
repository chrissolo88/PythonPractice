def calculate(operation, a, b, make_int=False, message='The result is'):
    oper = {'add': a+b, 'subtract': a-b, 'divide': a/b, 'multiply': a*b}
    num = oper.get(operation, 'None')
    msg = num if num == 'None' else f'{message} {int(num)}' if make_int == True else f'{message} {num}'
    print(msg)

calculate('add', 2.5, 4)
        # 'The result is 6.5'

calculate('subtract', 4, 1.5, make_int=True)
        # 'The result is 2'

calculate('multiply', 1.5, 2)
        # 'The result is 3.0'

calculate('divide', 10, 4, message='I got')
        # 'I got 2.5'

    # If a valid operation isn't provided, return None.

calculate('foo', 2, 3)
        

