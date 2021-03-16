a = int(input())
a1 = a // 1000
a2 = (a // 100) % 10
a3 = (a % 100) // 10
a4 = a % 10
h1 = a1 - a4
h2 = a2 - a3
h3 = (h1 ** 2) + (h2 ** 2)
k = 0 ** h3
print(k)
