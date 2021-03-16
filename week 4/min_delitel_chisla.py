import math


def MinDivision(n):
    i = 2
    while n % i != 0:
        i += 1
        if i > math.sqrt(n):
            return n
    return i


print(MinDivision(int(input())))
