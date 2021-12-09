from homework2.hw4 import cache


def test_cache_with_one_function_with_args():
    @cache
    def func(a, b):
        return (a ** b) ** 2
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    assert val_1 is val_2


def test_cache_with_two_functions_with_args():
    @cache
    def func_1(a, b):
        return (a ** b) ** 2

    @cache
    def func_2(a, b):
        return (a ** b) ** 2

    some = 100, 200
    val_1 = func_1(*some)
    val_2 = func_2(*some)
    assert val_1 is not val_2


def test_cache_with_args_and_kwargs():
    @cache
    def func(a, *, b):
        return (a ** b) ** 2
    val_1 = func(100, b=200)
    val_2 = func(100, b=200)
    assert val_1 is val_2


def test_cache_with_unhashable_objects():
    @cache
    def func(a, *, b):
        return a * b
    val_1 = func(100, b=[200])
    val_2 = func(100, b=[200])
    assert val_1 is val_2


def test_cache_with_call_with_parameter_replacement():
    @cache
    def func(a, b):
        return (a ** b) ** 2
    val_1 = func(a=100, b=200)
    val_2 = func(b=200, a=100)
    assert val_1 is val_2
