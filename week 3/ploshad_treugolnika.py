a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if abs(int(s) - float(s)) < 10e-6:
    print(int(s))
else:
    print('{0:.6f}'.format(s))
