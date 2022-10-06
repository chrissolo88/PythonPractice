def sum_pairs(nums, goal):
    pair = ()
    for ind in range(len(nums)):
        for num in nums[:ind+1]:
            for num2 in nums[:ind+1]:
                if num + num2 == goal:
                    pair = (num,num2)
                    break
            if pair != ():
                break
        if pair != ():
            break
    print(pair)
    """Return tuple of first pair of nums that sum to goal.
    """

sum_pairs([1, 2, 2, 10], 4)
       # (2, 2)

sum_pairs([4, 2, 10, 5, 1], 6)
       # (4, 2)

sum_pairs([5, 1, 4, 8, 3, 2], 7)
      #  (4, 3)

sum_pairs([11, 20, 4, 2, 1, 5], 100)
     #   ()

