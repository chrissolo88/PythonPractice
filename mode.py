def mode(nums):
    count = {num:nums.count(num) for num in set(nums)}
    print([num for num in count.keys() if count[num] == max(count.values())][0])

mode([1, 2, 1])
        # 1

mode([2, 2, 3, 3, 2])
        # 2

