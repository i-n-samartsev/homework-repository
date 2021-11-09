from homework2.hw3 import combinations


def test_combinations():
    assert combinations([1, 2], [3, 4]) == [[1, 3],
                                            [1, 4],
                                            [2, 3],
                                            [2, 4],
                                            ]
    assert combinations([1, 2], [0], [3, 4]) == [
        [1, 0, 3],
        [1, 0, 4],
        [2, 0, 3],
        [2, 0, 4],
        ]
