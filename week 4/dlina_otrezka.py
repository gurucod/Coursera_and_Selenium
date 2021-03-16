import math


def distance(x1, y1, x2, y2):
    xy = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 5)
    return xy


print(distance(float(input()), float(input()), float(input()), float(input())))
