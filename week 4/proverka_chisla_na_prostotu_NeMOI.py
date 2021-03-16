from math import sqrt


def isPrime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'


n = int(input())
print(isPrime(n))
