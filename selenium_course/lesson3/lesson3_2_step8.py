def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
    except AssertionError:
        print("expected {}, got {}".format(expected_result, actual_result))

    # assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)

expected_result, actual_result = input("Введите ожидаемый результат и полученное значение:\n").split()
test_input_text(expected_result, actual_result)
