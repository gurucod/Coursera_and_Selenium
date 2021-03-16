def sum(a, b):
    if a == 0:
        return print(b)
    sum(a - 1, b + 1)


a = int(input())
b = int(input())
if a > b:
    (a, b) = (b, a)
sum(a, b)
