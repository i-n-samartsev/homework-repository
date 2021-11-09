from homework0.task03 import find_maximum_and_minimum


def test_regular_case():
    """Testing regular example"""
    assert find_maximum_and_minimum(
        "tests/homework0/" "files_task03/test_file.txt"
    ) == (
        -100,
        6,
    )


def test_empty_case():
    """Testing empty example"""
    assert find_maximum_and_minimum(
        "tests/homework0/" "files_task03/empty_file.txt"
    ) == (None, None)


def test_non_existent_file_case():
    """Testing non existent example"""
    assert find_maximum_and_minimum(
        "tests/homework0/" "files_task03/some_file.txt"
    ) == (None, None)
