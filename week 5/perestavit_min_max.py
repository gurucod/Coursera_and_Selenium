a = list(map(int, input().split()))

x = min(a)
y = max(a)

for i in range(len(a)):
    if a[i] == x:
        a[i] = y
    elif a[i] == y:
        a[i] = x
print(*a)
