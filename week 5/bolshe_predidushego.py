a = list(map(int, input().split()))
k = a[0]
for i in a:
    if i > k:
        print(i, end=' ')
    k = i
