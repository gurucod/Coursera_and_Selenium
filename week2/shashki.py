v1 = int(input())
g1 = int(input())
v2 = int(input())
g2 = int(input())
if v1 + g1 < v2 + g2:
    if ((v1 + g1) % 2 == 0) and ((v2 + g2) % 2 == 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
