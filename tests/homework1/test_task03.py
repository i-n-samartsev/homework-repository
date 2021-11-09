from homework1.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum():

    with open('testing_file.txt', mode='w') as file:
        print('1 20 3 44 -5', '12 0 100 1', sep='\n', file=file)

    assert find_maximum_and_minimum(file_name='testing_file.txt') == (-5, 100)

    with open('testing_file.txt', mode='w') as file:
        print('0 0 0 0 0', '0 0 0 0', sep='\n', file=file)

    assert find_maximum_and_minimum(file_name='testing_file.txt') == (0, 0)
