name = "Cage"
age = 28

#     format
print("My name is {}. I\'m {}".format("Petr", 40))
print("My name is {1}. I\'m {0}".format("Petr", 40))
print("My name is {}. I\'m {}".format(name, age))
print("My name is {name}. I\'m {age}".format(name=name, age=age))

#   f-strings
print(f"My name is {name}. I\'m {age}")
print(f'My name is {name}. I\'m {age + 5}')
#print('5 + 2 = {}'.format(5 + 2))     при помощи format
print(f'5 + 2 = {5 + 2}')

#                       Работа со строками
s = 'Py' 'Thon'
r = 'wdwa'
print(s, r, end=' ')
print(s)
s = 'Answer'
print(s[::-2])

print("Price: %.3f , Name brand: %s" % (40, "Samsung"))

#                       Условия if

x = 0
if not x:
    print("OK")
else:
    print("NO")

# Тернарный оператор или то же что и выше но короче

x = 1
res = 'OK' if x else 'No'
print(res)

# или можно так

print('OK' if x else 'No')
