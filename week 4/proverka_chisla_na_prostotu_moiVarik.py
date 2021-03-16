from math import sqrt


def isPrime(n):
    i = 2
    if n == 2:
        return 'YES'
    while n % i != 0:
        i += 1
        if i > sqrt(n):
            return 'YES'
    return 'NO'


print(isPrime(int(input())))
