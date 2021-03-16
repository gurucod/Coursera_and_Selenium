flag = ('+___ ', ('|', '/ '), '|__\\ ', '|    ')
m = 1
n = int(input())
for i in range(len(flag)):
    if i == 1:
        for j in range(1, n + 1):
            print(flag[1][0], m, ' ', flag[1][1], sep='', end='')
            m += 1
        print()
    else:
        print(flag[i] * n)
