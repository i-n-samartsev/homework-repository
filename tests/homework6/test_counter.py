from homework6.counter import instances_counter


@instances_counter
class A:
    """Class A docstring"""
    def __init__(self, a):
        self.a = a


@instances_counter
class B:
    """Class B docstring"""
    def __init__(self, b):
        self.b = b


instance, _, _ = A(1000), A(2000), A(3000)


def test_instances_counter_correct_counting_of_instances_from_class():
    assert A.get_created_instances() == 3


def test_instances_counter_correct_counting_of_instances_from_instance():
    assert instance.get_created_instances() == 3


def test_instances_counter_correct_counting_of_instances_from_unused_class():
    assert B.get_created_instances() == 0


def test_instances_counter_correct_reset_of_instances():
    assert A.reset_instances_counter() == 3


def test_instances_counter_correct_counting_of_instances_after_reset():
    assert A.get_created_instances() == 0


def test_instances_counter_saving_attributes():
    assert instance.a == 1000


def test_instances_counter_saving_docstring():
    assert A.__doc__ == 'Class A docstring'
