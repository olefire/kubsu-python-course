from typing import List


def func(nums: List[int]):
    def index_of_min(nums: List[int]) -> int:
        min_num: int = 2 ** 32 - 1
        index: int = 0
        for i in range(len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
                index = i
        return index

    index: int = index_of_min(nums)
    for i in range(index):
        print(nums[i])


