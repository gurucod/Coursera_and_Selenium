a = int(input())
b = int(input())
n = int(input())
price = (a * 100 + b) * n
rub = price // 100
coin = price % 100
print(rub, coin)
