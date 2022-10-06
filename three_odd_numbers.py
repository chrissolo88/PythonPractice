def three_odd_numbers(nums):
    result = 'False'
    totals = [num + nums[ind+1] + nums[ind+2] for ind, num in enumerate(nums) if ind + 2 < len(nums)]
    for num in totals:
        if num%2!=0:
            result ='True'
            break
    print(result)
    """Is the sum of any 3 sequential numbers odd?"
    """
three_odd_numbers([1, 2, 3, 4, 5])
        #True

three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        #True

three_odd_numbers([5, 2, 1])
        #False
three_odd_numbers([1, 2, 3, 3, 2])
        #False

