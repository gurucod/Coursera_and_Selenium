p = int(input())
x = int(input())
y = int(input())
s = x * 100 + y
pr = (s * (1 + p / 100)) + 10 ** -9
r = pr // 100
c = pr % 100
print(int(r), int(c))
