from homework5.save_original_info import custom_sum


def test_custom_wraps_correct_function_work(capsys):
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert custom_sum(1, 2, 3, 4) == 10
    captured = capsys.readouterr()
    assert captured.out == '[1, 2, 3, 4, 5]\n10\n'


def test_custom_wraps_saving_attributes():
    doc = 'This function can sum any objects which have __add__'
    assert custom_sum.__doc__ == doc
    assert custom_sum.__name__ == 'custom_sum'


def test_custom_wraps_without_printing(capsys):
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert captured.out == ''
