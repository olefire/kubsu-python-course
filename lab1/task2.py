def maxProductNotDiv5(x: int):
    product = 1
    while x != 0:
        curDigit = x % 10
        x //= 10
        if curDigit % 5 != 0:
            product *= curDigit
    return product

print(maxProductNotDiv5(12375))