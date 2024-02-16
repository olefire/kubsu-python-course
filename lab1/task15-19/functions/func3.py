from typing import List


def func(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] * nums[i + 1] > 0:
            return False
    return True


