n = int(input())
for i in range(1, n + 1):
    print('+___' * n)
    print('|',i ,' /' * n, sep='')
    print('|__\\' * n)
    print('|   ' * n)
