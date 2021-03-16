n = int(input())
i = 0
nMax = 1
while n != 0:
    if n == nMax:
        i += 1
    elif n > nMax:
        nMax = n
        i = 1
    n = int(input())
print(i)
