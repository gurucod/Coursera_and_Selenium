a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = 0
y = 0
delT = a * d - c * b
if abs(delT) != 0:
    dlx = e * d - f * b
    dly = a * f - c * e
    x = dlx / delT
    y = dly / delT
print(x, y)
