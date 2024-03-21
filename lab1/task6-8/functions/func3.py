def find_min_integer():
    text = input("input text.txt here: ")

    current_num = 0
    is_positive = 1
    min_integer = 2 ** 63 - 1

    for i in range(len(text)):
        if text[i] == "-" and i + 1 != len(text) and text[i+1].isdigit():
            is_positive = -1

        if text[i].isdigit():
            current_num = current_num * 10 + int(text[i])

        elif current_num:
            if current_num * is_positive < min_integer:
                min_integer = current_num * is_positive
            current_num = 0
            is_positive = 1

    if current_num:
        if current_num * is_positive < min_integer:
            min_integer = current_num * is_positive

    print(min_integer)
