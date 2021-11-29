import functools

from homework5.save_original_info import print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_print_result():
    without_print = custom_sum.__original_func

    assert (
        custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
        and custom_sum(1, 2, 3, 4) == 10
        and custom_sum.__doc__
        == "This function can sum any objects which have __add___"
        and custom_sum.__name__ == "custom_sum"
        and without_print(1, 2, 3, 4) == 10
    )
