from homework7.hw1 import example_tree, find_occurrences


def test_find_occurrences():
    assert find_occurrences(example_tree, 'RED') == 6
