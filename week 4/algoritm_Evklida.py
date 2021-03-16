def gcd(a, b):
    if a == 0 or b == 0:
        return print(a + b)
    if a >= b:
        gcd(b, a % b)
    else:
        gcd(a, b % a)


a = int(input())
b = int(input())
gcd(a, b)
