from homework3.task01 import cache


def test_cache_return_same_output_for_same_input():

    @cache(times=2)
    def some_func(*args):
        return sum(args)

    first_function_call = some_func(999, 999, 999)
    second_function_call = some_func(999, 999, 999)

    assert first_function_call is second_function_call


def test_cache_return_another_output_for_another_input():

    @cache(times=2)
    def some_func(*args):
        return sum(args)

    first_function_call = some_func(999, 999, 999)
    second_function_call = some_func(777, 777, 777)

    assert first_function_call is not second_function_call


def test_cache_return_another_output_for_same_input_after_times():

    @cache(times=2)
    def some_func(*args):
        return sum(args)

    _ = some_func(999, 999, 999)
    _ = some_func(999, 999, 999)
    third_function_call = some_func(999, 999, 999)
    forth_function_call = some_func(999, 999, 999)

    assert third_function_call is not forth_function_call


def test_cache_return_same_output_for_same_input_with_kwargs():

    @cache(times=2)
    def some_func(a, b=50):
        return a * b

    first_function_call = some_func(a=['qwerty'])
    second_function_call = some_func(a=['qwerty'])

    assert first_function_call is second_function_call


def test_cache_return_another_output_for_same_input_after_times_with_kwargs():

    @cache(times=2)
    def some_func(a, b=50):
        return a * b

    _ = some_func(a=['qwerty'])
    _ = some_func(a=['qwerty'])
    third_function_call = some_func(a=['qwerty'])
    forth_function_call = some_func(a=['qwerty'])

    assert third_function_call is not forth_function_call
