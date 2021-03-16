s = input()
if len(s) == 1:
    print(s)
else:
    print(s[0] + s[1:-1].replace('', '*') + s[-1])
