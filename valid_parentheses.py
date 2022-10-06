def valid_parentheses(parens):
    parens_list = list(parens)
    print(parens_list.count('(')==parens_list.count(')')) if parens_list[0] == '(' and parens_list[-1] == ')' else print('False')
    """Are the parentheses validly balanced?
    """
valid_parentheses("()")
        #True

valid_parentheses("()()")
        #True

valid_parentheses("(()())")
        #True

valid_parentheses(")()")
       # False

valid_parentheses("())")
       # False

valid_parentheses("((())")
       # False

valid_parentheses(")()(")
        #False
