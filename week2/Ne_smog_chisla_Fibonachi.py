a = 1
b = 1
i = 0
n = int(input())
while i < n - 2:
    "действия n - 2 раз, так как первые два элемента уже учтены"
    c = a + b
    a = b
    b = c
    i += 1
print(b)
