a = list(map(int, input().split()))
b = []
if len(a) == 1:
    b = a
else:
    for i in range(len(a)-1):
        if i % 2 == 0:
            b.append(a[i+1])
            b.append(a[i])
        elif i == len(a)-2:
            b.append(a[-1])
print(*b)



#a = list(map(int, input().split()))
#for i in range(0, len(a) - 1, 2):
#    a[i], a[i+1] = a[i+1], a[i]
#print(*a) #решение не моё, но гораздо лучше моего
