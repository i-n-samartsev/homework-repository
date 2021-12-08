from homework7.hw1 import find_occurrences


def test_find_occurrences_with_all_basic_structures():
    example_tree = {
        'first': ['RED', 100],
        True: {'simple_key': ['list', 'RED']},
        False: {'abc': 'cde',
                'jhl': 'RED',
                'complex_key': {'key1': 'value1',
                                10: 'RED',
                                20: {'set', 'RED', True}
                                }
                },
        ('tuple', 'key', 'RED'): 'RED',
    }
    assert find_occurrences(example_tree, 'RED') == 7


def test_find_occurrences_with_empty_tree():
    example_tree = {}
    assert find_occurrences(example_tree, 'RED') == 0
