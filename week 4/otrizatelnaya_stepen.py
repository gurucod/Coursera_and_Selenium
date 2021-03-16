def power(a, n):
    i = 1
    res = a
    if n == 0:
        return 1
    if n > 0:
        while i < n:
            res *= a
            i += 1
        return res
    else:
        while i > n:
            res = res * 1 / a
            i -= 1
        return res


a = float(input())
n = int(input())
print(power(a, n))
