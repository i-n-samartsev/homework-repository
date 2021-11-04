from homework0.task02 import check_fibonacci


def test_positive_case():
    """Testing that actual fibonacci sequence gives True"""
    assert check_fibonacci(
        [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
        ]
    )


def test_negative_case():
    """Testing that not a fibonacci sequence gives False"""
    assert not check_fibonacci(
        [
            0,
            1,
            1,
            2,
            3,
            6,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
        ]
    )


def test_first_numbers_case():
    """Testing that not a fibonacci sequence gives False"""
    assert not check_fibonacci(
        [
            1,
            0,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
        ]
    )


def test_empty_case():
    """Testing that empty sequence gives False"""
    assert not check_fibonacci([])


def test_len1_positive_case():
    """Testing that a fibonacci sequence with length == 1 gives True"""
    assert check_fibonacci([0])


def test_len1_negative_case():
    """Testing that not a fibonacci sequence with length == 1 gives False"""
    assert not check_fibonacci([1])


def test_negative_sequence_case():
    """Testing that a negative fibonacci sequence gives True"""
    assert check_fibonacci([-8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8])
