from homework2.hw2 import major_and_minor_elem


def test_1_major_and_minor_elem():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_2_major_and_minor_elem():
    assert major_and_minor_elem([0, 0, 0, 0]) == (0, 0)
