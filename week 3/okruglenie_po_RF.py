import math
n = float(input())
if n % 1 == 0.5:
    print(math.ceil(n))
elif n % 1 > 0.5:
    print(math.ceil(n))
else:
    print(math.floor(n))
