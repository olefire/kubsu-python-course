from typing import List


def func(nums: List[int]) -> int:
    count = 0
    curr_sum = 0

    for num in nums:
        if num > curr_sum:
            count += 1
        curr_sum += num

    return count

