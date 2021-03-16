n = int(input())
now = 0
aft = 0
while n != 0:
    if n >= now:
        aft = now
        now = n
    elif aft < n < now:
        aft = n
    n = int(input())
print(aft)
