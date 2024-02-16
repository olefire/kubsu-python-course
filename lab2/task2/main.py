from typing import Set, List, Dict


def solve() -> int:
    def find_emphasis(word: str) -> int:
        emp_count: int = 0
        index: int = 0
        for i in range(len(word)):
            if word[i].isupper():
                emp_count += 1
                index = i
        if emp_count == 0 or emp_count > 1:
            return -1
        return index

    emphasises: Dict[str, set[int]] = dict()
    n: int = int(input())

    for _ in range(n):
        word = input()
        index = find_emphasis(word)
        lower_word = word.lower()
        if lower_word not in emphasises:
            emphasises[lower_word] = set()
        emphasises[lower_word].add(index)

    text: List[str] = input().split()
    mistakes: int = 0
    for word in text:
        lower_word = word.lower()
        emphasis_index = find_emphasis(word)
        if emphasis_index == -1:
            mistakes += 1
        elif lower_word in emphasises and emphasis_index not in emphasises[lower_word]:
            mistakes += 1

    return mistakes


print(solve())

# 4
# cAnnot
# cannOt
# fOund
# pAge
# thE pAge cAnnot be found