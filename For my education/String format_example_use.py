name = "Cage"
age = 28

#     format
print("My name is {}. I\'m {}".format("Petr", 40))
print("My name is {1}. I\'m {0}".format("Petr", 40))
print("My name is {}. I\'m {}".format(name, age))
print("My name is {name}. I\'m {age}".format(name=name, age=age))

#   f-strings
print(f"My name is {name}. I\'m {age}")
print(f'My name is {name}. I\'m {age+5}')
print('5 + 2 = {}'.format(5 + 2))