import math
from typing import List


def sort_func(string: str) -> float:
    max_ascii_symbol: int = max(map(ord, string))
    diff_sum: int = 0
    for i in range(len(string) // 2):
        diff_sum += (max_ascii_symbol - (ord(string[i]) - ord(string[len(string) - 1 - i]))) ** 2
    return math.sqrt(diff_sum)


