s = input()
pos = s.find('f')
i = 0
while pos != -1:
    i += 1
    if i == 2:
        print(pos)
    pos = s.find('f', pos + 1)
if i == 1:
    print(-1)
if i == 0:
    print(-2)
