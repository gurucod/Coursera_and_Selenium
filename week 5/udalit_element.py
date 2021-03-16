a = list(map(int, input().split()))
k = int(input())


for i in range(k, len(a) - 1):
    a[k] = a[k + 1]
    k += 1
a.pop()
print(*a)
