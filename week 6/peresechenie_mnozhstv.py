def intersection(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if a[i] == b[j]:
                res.append(a[i])
            i += 1
        else:
            j += 1
    return res


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*intersection(a, b))
