def find_the_duplicate(nums):
    duplicate = [num for ind, num in enumerate(nums) if nums[ind:].count(num) > 1]
    print(duplicate[0])  if len(duplicate) > 0 else print('None')


find_the_duplicate([1, 2, 1, 4, 3, 12])
        # 1

find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        # 9

find_the_duplicate([2, 1, 3, 4]) 
        # is None
        # True

