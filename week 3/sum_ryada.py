n = int(input())
i = 1
r = 0
while n >= i:
    r = r + (1 / n ** 2)
    n -= 1
print(r)
