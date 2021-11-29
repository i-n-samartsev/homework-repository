from homework1.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum_on_a_varied_data():

    with open('test_file.txt', mode='w') as file:
        file.write('1 20 3 44 -5' '\n' '12 0 100 1')

    values = find_maximum_and_minimum('test_file.txt')
    assert values.min == -5 and values.max == 100


def test_2_find_maximum_and_minimum_on_a_monotonous_data():

    with open('test_file.txt', mode='w') as file:
        file.write('0 0 0 0 0' '\n' '0 0 0 0')

    values = find_maximum_and_minimum('test_file.txt')
    assert values.min == 0 and values.max == 0


def test_2_find_maximum_and_minimum_on_a_file_with_empty_lines():

    with open('test_file.txt', mode='w') as file:
        file.write('1 2 3 \n \n \n 1 -1 \n -10 10 ')

    values = find_maximum_and_minimum('test_file.txt')
    assert values.min == -10 and values.max == 10
