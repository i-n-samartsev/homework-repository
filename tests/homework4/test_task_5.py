from homework4.task_5_optional import fizzbuzz


def test_fizzbuzz_return_correct_sequence():
    assert list(fizzbuzz(5)) == ['1', '2', 'Fizz', '4', 'Buzz']


def test_fizzbuzz_return_fizzbuzz_element():
    assert list(fizzbuzz(20))[14] == 'FizzBuzz'
