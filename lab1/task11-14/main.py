from typing import List, Set

from functions import func1, func2, func3, func4


def route(func: int):
    string: str = input()
    str_list: List[str] = []
    while string != "":
        str_list.append(string)
        string = input()

    if func == 1:
        str_list.sort(key=func1.sort_func)
        print("Sorted list: ", str_list)

    elif func == 2:
        set_alphabet: Set[str] = set()
        alphabet: str = input()
        for a in alphabet:
            set_alphabet.add(a)
        sorted_func = func2.func(set_alphabet, str_list)
        print("Sorted list: ", sorted_func)

    elif func == 3:
        str_list.sort(key=lambda x: func3.sort_func(x))
        print("Sorted list: ", str_list)

    elif func == 4:
        str_list.sort(key=func4.sort_func)
    else:
        print("no such function")


if __name__ == "__main__":
    func = int(input("choose function: "))
    route(func)
