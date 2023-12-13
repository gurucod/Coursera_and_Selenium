import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False




# Задание: пропуск тестов. Параметр, который в случае неожиданного прохождения теста, помеченного как xfail,
# отметит в отчете этот тест как упавший. Пометьте таким образом первый тест из этого тестового набора.