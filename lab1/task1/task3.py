def max_product_not_div5(x: int):
    product = 1
    while x != 0:
        cur_digit = x % 10
        x //= 10
        if cur_digit % 5 != 0:
            product *= cur_digit
    return product


x = int(input())
print("произведение цифр числа, не делящихся на 5", max_product_not_div5(x))
# print(max_product_not_div5(12375)) 42
