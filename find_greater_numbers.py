def find_greater_numbers(nums):
    ind =0 
    count = 0
    for n1 in nums:
        ind += 1
        for n2 in nums[ind:]:
            if n1 < n2:
                count += 1 
    
    print(count)
        
find_greater_numbers([1, 2, 3])
        # 3

find_greater_numbers([6, 1, 2, 7])
        # 4

find_greater_numbers([5, 4, 3, 2, 1])
        # 0

find_greater_numbers([])
        # 0
