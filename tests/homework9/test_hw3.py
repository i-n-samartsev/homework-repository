import shutil
from tempfile import NamedTemporaryFile, mkdtemp

from pytest import fixture

from homework9.hw3 import universal_file_counter


@fixture
def temp_test_dir():
    external_directory = mkdtemp()

    with NamedTemporaryFile(dir=external_directory, delete=False,
                            suffix='.txt', mode='w') as file:
        file.write('1 2\n3 4\n')
    with NamedTemporaryFile(dir=external_directory, delete=False,
                            suffix='.doc', mode='w') as file:
        file.write('0 0\n0 0\n')

    internal_directory = mkdtemp(dir=external_directory)

    with NamedTemporaryFile(dir=internal_directory, delete=False,
                            suffix='.txt', mode='w') as file:
        file.write('5 6\n7 8\n')
    with NamedTemporaryFile(dir=internal_directory, delete=False,
                            suffix='.txt', mode='w') as file:
        file.write('9 10\n11 12\n')

    try:
        yield external_directory
    finally:
        shutil.rmtree(external_directory)


def test_universal_file_counter_with_tokenizer(temp_test_dir):
    assert universal_file_counter(temp_test_dir, '.txt', str.split) == 12


def test_universal_file_counter_without_tokenizer(temp_test_dir):
    assert universal_file_counter(temp_test_dir, '.txt') == 6
