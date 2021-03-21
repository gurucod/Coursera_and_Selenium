def decor1(func):
    def text_submit():
        print("Начало обёртки")
        func()
        print("Конец обёртки")
    return text_submit

@decor1
def hello():
    print("Hello my dear guest")


# test = decor1(hello)
# test()
# тут аналог того что делает добавление к функции @decor1

hello()
