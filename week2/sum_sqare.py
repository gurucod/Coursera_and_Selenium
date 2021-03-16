n = int(input())
sumSq = 0
q = 0
i = 1
while n >= i:
    q = i ** 2
    i += 1
    sumSq += q
print(sumSq)
