s = input()
s1 = s.find('h')
s2 = s.rfind('h')+1
print(s[:s1] + s[s2:])
