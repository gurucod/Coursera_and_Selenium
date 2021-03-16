a = int(input())
b = int(input())
c1 = a // b
c2 = b // a
rez = (a * c1 + b * c2) // (c1 + c2)
print(rez)
