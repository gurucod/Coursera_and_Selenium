def st(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return st(a * a, n // 2)
    else:
        return a * st(a, n - 1)


a = float(input())
n = int(input())
print(st(a, n))
