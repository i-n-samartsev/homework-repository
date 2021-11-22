from homework4.task_4_doctest import fizzbuzz


def test_fizzbuzz_return_correct_sequence():
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']


def test_fizzbuzz_return_fizzbuzz_element():
    assert fizzbuzz(20)[14] == 'FizzBuzz'
