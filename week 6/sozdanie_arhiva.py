h = list(map(int, input().split()))
N = []
for i in range(h[1]):
    N.append(int(input()))
N.sort()
count = 0
mem = 0
for i in range(len(N)):
    mem += N[i]
    if mem <= h[0]:
        count += 1
print(count)
