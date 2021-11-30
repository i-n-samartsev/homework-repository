from homework5.oop_1 import Student, Teacher

teacher = Teacher('Daniil', 'Shadrin')
student = Student('Roman', 'Petrov')
expired_homework = teacher.create_homework('Learn functions', 0)
create_homework_too = teacher.create_homework
oop_homework = create_homework_too('create 2 simple classes', 5)


def test_oop_1_instance_attributes():
    assert teacher.last_name == 'Shadrin'
    assert student.first_name == 'Roman'


def test_oop_1_expired_homework():
    assert expired_homework.deadline.days == 0
    assert expired_homework.text == 'Learn functions'


def test_oop_1_method_using():
    assert student.do_homework(oop_homework)
    assert not student.do_homework(expired_homework)
