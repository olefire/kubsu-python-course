def sort_by_length():
    strings = []
    count_of_strings = int(input("input count of strings: "))
    for i in range(count_of_strings):
        string = input("input string: ")
        strings.append(string)

    sorted_strings = sorted(strings, key=len)

    print("Упорядоченный по длине список строк: ", sorted_strings)


sort_by_length()