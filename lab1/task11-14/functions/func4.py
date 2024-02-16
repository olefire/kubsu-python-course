def calculate_average_weight(string: str):
    weigh = 0
    for i in range(len(string) - 2):
        tr_weight = calculate_weigh(string[i:i + 3])
        weigh += tr_weight
    average_weight = weigh / (len(string) - 2)
    return average_weight


def calculate_weigh(string: str):
    weight = 0
    for char in string:
        weight += ord(char)
    return weight


def sort_func(string: str):
    first_weight = calculate_average_weight(string[0])
    current_string_weight = calculate_average_weight(string)
    deviation = (first_weight - current_string_weight) ** 2
    return deviation


