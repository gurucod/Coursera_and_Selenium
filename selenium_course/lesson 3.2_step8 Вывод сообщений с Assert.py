expected_result = 11
actual_result = 15


def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    text = actual_result
    assert text == expected_result, \
        f"expected {expected_result}, got {actual_result}"


test_input_text(expected_result, actual_result)
