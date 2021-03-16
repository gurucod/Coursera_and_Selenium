def isPositionSqare(x, y):
    return abs(x) + abs(y) <= 1


if isPositionSqare(float(input()), float(input())):
    print('YES')
else:
    print('NO')
