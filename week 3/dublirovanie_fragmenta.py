s = input()
g1 = s.find('h')
g2 = s.rfind('h')
g3 = s[g1+1:g2]
print(s[:g2] + g3 + s[g2:])
