from typing import List, Dict


def sort_func(string: str) -> float:

    freq_of_chars: Dict[str, int] = dict()
    for char in string:
        if char not in freq_of_chars:
            freq_of_chars[char] = 0
        freq_of_chars[char] += 1

    max_count: int = 0
    for char in freq_of_chars:
        if freq_of_chars[char] > max_count:
            max_count = freq_of_chars[char]

    return max_count / len(string) - max_count / 26
