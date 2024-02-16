from typing import List

from functions import func1, func2, func3, func4, func5


def route(func: int):
    nums: List[int] = [int(value) for value in input().split()]
    if func == 1:
        func1.func(nums)
    elif func == 2:
        func2.func(nums)
    elif func == 3:
        print(func3.func(nums))
    elif func == 4:
        a, b = map(int, input().split())
        print(func4.func(nums, a, b))
    elif func == 5:
        print(func5.func(nums))
    else:
        print("no such function")


if __name__ == "__main__":
    func = int(input("choose function: "))
    route(func)
