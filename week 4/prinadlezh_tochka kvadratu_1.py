def isPositionSqare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


if isPositionSqare(float(input()), float(input())):
    print('YES')
else:
    print('NO')
