now = int(input())
newNow = now
while now != 0:
    now = int(input())
    if now > 0 and now > newNow:
        newNow = now
print(newNow)
