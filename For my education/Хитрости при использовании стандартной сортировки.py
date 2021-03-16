from random import randint

a = [randint(0, 10) for i in range(10)]
print(a)
a.sort()
print(a)
a.sort(reverse = True)
"""Сортирует в обратном порядке"""
print(a)


b = ['abc', 'de', 'd', 'ad']
b.sort()
print(b)

b.sort(key = len)
"""Сортирует по длине слов"""
print(b)

b.sort(key = len, reverse=True)
"""Сортирует по длине слов, и в развернутом виде"""
print(b)

c = [2, 3, -4, 5, -3, -2]
"""Сортировка по модулю"""
c.sort(key = abs)
print(c)

d = [10, 82, 45, 21, 58]
"""Функция суммирует цифры числа (тут например 1+0, 8+2...) и сортировка происходит по сумме цифр"""
def f(x):
    return x % 10 + x // 10
d.sort(key=f)
print(d)

d = [10, 82, 45, 21, 58]
"""То же самое что выше но упрощенный вариант - так можно записывать короткую функцию"""
d.sort(key = lambda x: x % 10 + x // 10)
print(d)

e = [10, 82, 45, 21, 58]
"""Сортирует по последней цифре"""
e.sort(key= lambda x: str(x)[-1])
print(e)