from math import sqrt


def max_prime_division(x: int):
    def is_prime(num: int):
        if num == 2:
            return True
        if num == 1:
            return False
        for i in range(3, int(sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    max_prime_division = -1
    for i in range(int(sqrt(x)), 0, -1):
        if x % i == 0 and is_prime(i):
            max_prime_division = i
            break
    return max_prime_division


# x = int(input())
# print("максимальный простой делитель числа", max_prime_division(x))
# print(max_prime_division(5 * 11 * 17 * 19 * 29 * 37)) 37
