x = "some_text"
y = "some1"


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert y in x, \
        f"expected '{substring}' to be substring of '{full_string}'"
    #проверка того что подстрока входит в строку


test_substring(x, y)
