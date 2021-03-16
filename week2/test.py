a = list(map(int, input().split()))
print(a)
num = 0
indx = 0
for i in a:
    if i >= num:
        num = i
        indx = a.index(num)
print(num, indx)
