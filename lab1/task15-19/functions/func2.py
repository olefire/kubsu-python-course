def func(nums: list):
    index_of_min = nums.index(min(nums))

    for i in range(index_of_min + 1, len(nums)):
        print(nums[i])


