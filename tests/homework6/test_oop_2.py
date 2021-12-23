from collections import defaultdict

import pytest

from homework6.oop_2 import (DeadlineError, HomeworkResult, NotAHomeworkError,
                             Student, Teacher)

opp_teacher = Teacher('Daniil', 'Shadrin')
advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

lazy_student = Student('Roman', 'Petrov')
good_student = Student('Lev', 'Sokolov')

oop_hw = opp_teacher.create_homework('Learn OOP', 1)
docs_hw = opp_teacher.create_homework('Read docs', 5)
expired_hw = advanced_python_teacher.create_homework("You can't do it", 0)

good_do_oop = good_student.do_homework(oop_hw, 'I have done this hw')
good_do_docs = good_student.do_homework(docs_hw, 'I have done this hw too')
lazy_do_docs = lazy_student.do_homework(docs_hw, 'done')


def test_wrong_homework_for_homework_result_raises_exception():
    with pytest.raises(NotAHomeworkError):
        HomeworkResult(good_student, 'fff', 'Solution')


def test_doing_expired_homework_raises_exception():
    with pytest.raises(DeadlineError):
        good_student.do_homework(expired_hw, 'I have tried')


def test_storing_only_unique_homework_solutions():
    opp_teacher.check_homework(good_do_oop)
    advanced_python_teacher.check_homework(good_do_oop)
    assert len(Teacher.homework_done[oop_hw]) == 1


def test_badly_solved_homeworks_are_not_stored():
    opp_teacher.check_homework(good_do_docs)
    opp_teacher.check_homework(lazy_do_docs)
    assert len(Teacher.homework_done[docs_hw]) == 1


def test_reset_homework_done():
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0


def test_homework_done_teacher_inheritance():

    class ProTeacher(Teacher):
        homework_done = defaultdict(set)

    pro_teacher = ProTeacher('Name', 'Surname')

    pro_teacher.check_homework(good_do_oop)
    assert len(Teacher.homework_done) == 0
    assert len(ProTeacher.homework_done) == 1
