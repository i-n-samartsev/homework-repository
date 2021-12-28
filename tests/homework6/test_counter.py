from pytest import fixture

from homework6.counter import instances_counter


@instances_counter
class Fruit:
    """It is a fruit"""
    def __init__(self, color):
        self.color = color


class Apple(Fruit):
    """It is an apple"""


@fixture(scope='module')
def fruit():
    return Fruit(None)


@fixture(scope='module')
def apple():
    _, _ = Apple('green'), Apple('yellow')
    return Apple('red')


def test_instances_counter_before_instances_creation():
    assert Fruit.get_created_instances() == 0
    assert Apple.get_created_instances() == 0


def test_instances_counter_get_from_instance(fruit):
    assert fruit.get_created_instances() == 1


def test_instances_counter_get_from_class():
    assert Fruit.get_created_instances() == 1


def test_instances_counter_get_from_inheritor_instance(apple):
    assert apple.get_created_instances() == 3


def test_instances_counter_get_from_inheritor_class():
    assert Apple.get_created_instances() == 3


def test_instances_counter_correct_reset_of_instances(apple):
    assert apple.reset_instances_counter() == 3


def test_instances_counter_correct_counting_of_instances_after_reset():
    assert Apple.get_created_instances() == 0


def test_instances_counter_saving_attributes(apple):
    assert apple.color == 'red'


def test_instances_counter_saving_docstring(apple):
    assert apple.__doc__ == 'It is an apple'


def test_instances_counter_get_from_parent_after_inheritor_reset(fruit):
    assert fruit.get_created_instances() == 1
