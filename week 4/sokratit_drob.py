def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def reduceFraction(n, m):
    a = gcd(n, m)
    return int(n / a), int(m / a)


n = int(input())
m = int(input())
print(*reduceFraction(n, m))
