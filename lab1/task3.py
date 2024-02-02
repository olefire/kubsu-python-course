from math import sqrt


def fin_nod_of_max_odd_division(x: int, y: int):
    def is_prime(num: int):
        divs_count = 0
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                divs_count += 1
            if divs_count > 0:
                return False
        return True

    def find_max_odd_division(number: int):
        max_prime_division = -1
        xsqrt = int(sqrt(x))
        for i in range(xsqrt + (xsqrt % 2 - 1), 0, -2):
            if x % i == 0 and not is_prime(i):
                max_prime_division = i
                break
        return max_prime_division

    def find_nod(x: int, y: int):
        if y == 0:
            return x
        else:
            return find_nod(y, x % y)

    divX = find_max_odd_division(x)
    divY = find_max_odd_division(y)

    nod = find_nod(x, y)

    return nod


x = int(input("x: "))
y = int(input("y: "))

print("НОД максимального нечетного непростого делителя", fin_nod_of_max_odd_division(x, y))

# print(fin_nod_of_max_odd_division(1*3*6*8, 3*7*12*5)) 36
