a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if c <= a:
        (a, c) = (c, a)
    if c <= b:
        (b, c) = (c, b)
    if c ** 2 == a ** 2 + b ** 2:
        print('rectangular')
    elif c ** 2 > a ** 2 + b ** 2:
        print('obtuse')
    elif c ** 2 < a ** 2 + b ** 2:
        print('acute')
else:
    print('impossible')
