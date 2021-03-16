a = list(map(int, input().split()))


def isAscending(a):
    i = 1
    while i < len(a):
        i += 1
    return i


print(isAscending(a))
