a = int(input())
b = int(input())
c = a % b
k = (c + b - 1) // b
print(k * 'NO', (0 ** k) * 'YES', sep='')
