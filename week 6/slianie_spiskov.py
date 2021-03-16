def merge(a, b):
    a.extend(b)
    for j in range(0, len(a) - 1):
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))
