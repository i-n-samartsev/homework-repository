from homework2.hw2 import major_and_minor_elem


def test_major_and_minor_elem_on_varied_data():
    major_and_minor = major_and_minor_elem([2, 2, 1, 1, 1, 2, 2])
    assert major_and_minor.major_elem == 2
    assert major_and_minor.minor_elem == 1


def test_major_and_minor_elem_on_homogeneous_data():
    major_and_minor = major_and_minor_elem([0, 0, 0, 0])
    assert major_and_minor.major_elem == 0
    assert major_and_minor.minor_elem == 0
