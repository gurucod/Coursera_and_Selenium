n = int(input())
now = n
maxI = 0
i = 1
while n != 0:
    n = int(input())
    if n > now or n < now:
        now = n
        i = 1
    elif n == now:
        i += 1
    if maxI < i:
        maxI = i
print(maxI)
