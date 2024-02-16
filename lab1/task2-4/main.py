from functioins import func3, func1, func2


def route(func: int):
    if func == 1:
        func1.mix_words()
    elif func == 2:
        func2.find_count_of_words_with_even_count_of_letters()
    elif func == 3:
        func3.organize_flag()
    else:
        print("no such function")


if __name__ == "__main__":
    func = int(input("choose function: "))
    route(func)
