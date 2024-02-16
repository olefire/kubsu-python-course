from functions import func3, func1, func2


def route(func: int):
    if func == 1:
        func1.count_of_russian_letters()
    elif func == 2:
        func2.count_of_latin_lower_letters()
    elif func == 3:
        func3.find_min_integer()
    else:
        print("no such function")


if __name__ == "__main__":
    func = int(input("choose function: "))
    route(func)
