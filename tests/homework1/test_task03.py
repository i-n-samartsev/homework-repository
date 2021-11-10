from homework1.task03 import find_maximum_and_minimum


def test_1_find_maximum_and_minimum():

    with open('testing_file.txt', mode='w') as file:
        file.write('1 20 3 44 -5' '\n' '12 0 100 1')

    assert find_maximum_and_minimum(file_name='testing_file.txt') == (-5, 100)


def test_2_find_maximum_and_minimum():

    with open('testing_file.txt', mode='w') as file:
        file.write('0 0 0 0 0' '\n' '0 0 0 0')

    assert find_maximum_and_minimum(file_name='testing_file.txt') == (0, 0)
