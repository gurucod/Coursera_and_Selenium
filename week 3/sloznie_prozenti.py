p = float(input())
x = float(input())
y = float(input())
k = float(input())
su = x * 100 + y
while k > 0:
    su = int((su * (1 + p/100)) + (5 * 10 ** -6))
    k -= 1
r = su // 100
c = su % 100
print(int(r), int(c))
