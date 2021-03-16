n = int(input())
a = list(map(int, input().split()))[:n]
x = int(input())
b = []

for i in range(n):
    b.append(abs(a[i] - x))
print(a[b.index(min(b))])
