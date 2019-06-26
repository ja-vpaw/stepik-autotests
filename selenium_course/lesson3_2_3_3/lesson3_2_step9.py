def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    try:
        assert substring in full_string
    except AssertionError:
        print("expected '{}' to be substring of '{}'".format(substring, full_string))
