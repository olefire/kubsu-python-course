from typing import Set, List, Dict


def func(alphabet: Set[str], strings: List[str]) -> int:
    def freq_in_strings(alphabet: Set[str], strings: List[str]):
        freq_of_chars: Dict[str, int] = {}
        for string in strings:
            for char in string:
                if char in alphabet:
                    if char not in freq_of_chars:
                        freq_of_chars[char] = 0
                    freq_of_chars[char] += 1

        return freq_of_chars

    freq_char_in_strings: Dict[str, int] = freq_in_strings(alphabet, strings)

    def sort_func(string: str) -> float:
        freq_of_chars: Dict[str, int] = {}
        for char in string:
            if char not in freq_of_chars:
                freq_of_chars[char] = 0
            freq_of_chars[char] += 1

        max_count = 0
        max_char = 0
        for char in freq_of_chars:
            if freq_of_chars[char] > max_count:
                max_count = freq_of_chars[char]
                max_char = char

        return max_count / len(string) - freq_char_in_strings[max_char] / 26

    strings.sort(key=sort_func)
