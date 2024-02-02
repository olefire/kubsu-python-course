from math import sqrt


def findNodOfMaxOddDivision(x: int, y: int):
    def isPrime(num: int):
        divsCount = 0
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                divsCount += 1
            if divsCount > 0:
                return False
        return True

    def findMaxOddDivision(number: int):
        maxPrimeDivision = -1
        xsqrt = int(sqrt(x))
        for i in range(xsqrt + (xsqrt % 2 - 1), 0, -2):
            if x % i == 0 and not isPrime(i):
                maxPrimeDivision = i
                break
        return maxPrimeDivision
    def findNOD(x: int, y: int):
        if y == 0:
            return x
        else:
            return findNOD(y, x % y)

    divX = findMaxOddDivision(x)
    divY = findMaxOddDivision(y)

    nod = findNOD(x, y)

    return nod


x = int(input())
y = int(input())

print(findNodOfMaxOddDivision(x, y))

# print(findNodOfMaxOddDivision(1*3*6, 3*7*12)) 18