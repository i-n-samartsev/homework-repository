import pytest

from homework5.oop_1 import Student, Teacher


@pytest.fixture
def teacher():
    return Teacher('Daniil', 'Shadrin')


@pytest.fixture
def student():
    return Student('Roman', 'Petrov')


@pytest.fixture
def expired_homework(teacher):
    return teacher.create_homework('Expired', 0)


@pytest.fixture
def active_homework(teacher):
    return teacher.create_homework('Create 2 classes', 5)


def test_oop_1_teacher_attributes_are_properly_created(teacher):
    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Shadrin'


def test_oop_1_student_attributes_are_properly_created(student):
    assert student.first_name == 'Roman'
    assert student.last_name == 'Petrov'


def test_oop_1_homework_attributes_are_properly_created(expired_homework):
    assert expired_homework.deadline.days == 0
    assert expired_homework.text == 'Expired'


def test_oop_1_homework_is_active_return_true(active_homework):
    assert active_homework.is_active() is True


def test_oop_1_homework_is_active_return_false(expired_homework):
    assert expired_homework.is_active() is False


def test_oop_1_student_do_active_homework(student, active_homework, capsys):
    assert student.do_homework(active_homework) is active_homework


def test_oop_1_student_do_expired_homework(student, expired_homework, capsys):
    assert student.do_homework(expired_homework) is None
    captured = capsys.readouterr()
    assert captured.out == 'You are late\n'
