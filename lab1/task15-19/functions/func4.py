from typing import List


def func(nums: List[int], a: int, b: int) -> int:

    curr_sum: int = 0

    for num in nums:
        if a < num < b:
            curr_sum += num

    return curr_sum


