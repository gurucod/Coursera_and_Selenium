s = input()
g1 = s.find('h')
g2 = s.rfind('h')
gg = s[g1+1:g2]
print(s[:g1+1] + gg.replace('h', 'H', ) + s[g2:])
