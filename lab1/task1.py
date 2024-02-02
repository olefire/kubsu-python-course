from math import sqrt


def maxPrimeDivision(x: int):
    def isPrime(num: int):
        divsCount = 0
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                divsCount += 1
            if divsCount > 0:
                return False
        return True

    maxPrimeDivision = -1
    for i in range(x-1, 0, -1):
         if x % i == 0 and isPrime(i):
             maxPrimeDivision = i
             break
    return maxPrimeDivision

print(maxPrimeDivision(5*11*17*19*29))