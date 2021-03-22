print('Введите значение Time Stamp:')
time_stamp = int(input())
print('Укажите сколько дней необходимо отмотать "назад"')
day = int(input())
if day > 0:
    res = time_stamp - (86400 * day)
    print('Результат который нужно ввставить в БД:')
    print(res)
else:
    print("Вы ввели некоректное кол-во дней. Укажите значение больше '0'")
