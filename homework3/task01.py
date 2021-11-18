from typing import Callable


def cache(func: Callable) -> Callable:
    saved_data = {}

    def helper(*args):
        if args in saved_data.keys():
            return saved_data[args]
        else:
            val_func = func(*args)
            saved_data.update([(args, val_func)])
            return val_func

    return helper
