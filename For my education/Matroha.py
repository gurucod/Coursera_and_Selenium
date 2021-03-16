def matro(n):
    if n == 1:
        print('matroha', n)
    else:
        print('Вверх матро', n)
        matro(n - 1)
        print('Низ Матро', n)


matro(int(input()))
