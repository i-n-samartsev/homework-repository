"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

>>> with Supressor(ZeroDivisionError):
...    1/0

"""

from contextlib import contextmanager


@contextmanager
def supressor(error):
    """Context manager, that suppresses passed exception"""
    try:
        yield
    except error:
        pass


class Supressor:
    """Context manager, that suppresses passed exception"""
    def __init__(self, error):
        self.error = error

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.error)
