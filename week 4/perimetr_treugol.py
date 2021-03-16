import math


def p(x1, y1, x2, y2, x3, y3):
    ab = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    bc = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    ac = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    res = round(abs(ab) + abs(bc) + abs(ac), 6)
    return res


print(p(float(input()), float(input()), float(input()), float(input()),
        float(input()), float(input())))
