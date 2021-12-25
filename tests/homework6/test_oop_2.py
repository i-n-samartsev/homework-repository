from collections import defaultdict

from pytest import fixture, raises

from homework6.oop_2 import (DeadlineError, HomeworkResult, NotAHomeworkError,
                             Student, Teacher)


@fixture(scope='module')
def opp_teacher():
    return Teacher('Daniil', 'Shadrin')


@fixture(scope='module')
def advanced_teacher():
    return Teacher('Aleksandr', 'Smetanin')


@fixture(scope='module')
def lazy_student():
    return Student('Roman', 'Petrov')


@fixture(scope='module')
def good_student():
    return Student('Lev', 'Sokolov')


@fixture(scope='module')
def oop_hw(opp_teacher):
    return opp_teacher.create_homework('Learn OOP', 1)


@fixture(scope='module')
def docs_hw(opp_teacher):
    return opp_teacher.create_homework('Read docs', 5)


@fixture(scope='module')
def expired_hw(advanced_teacher):
    return advanced_teacher.create_homework("You can't do it", 0)


@fixture(scope='module')
def good_do_oop(good_student, oop_hw):
    return good_student.do_homework(oop_hw, "I've done this hw")


@fixture(scope='module')
def good_do_docs(good_student, docs_hw):
    return good_student.do_homework(docs_hw, "I've done this hw too")


@fixture(scope='module')
def lazy_do_docs(lazy_student, docs_hw):
    return lazy_student.do_homework(docs_hw, 'bad')


def test_wrong_homework_for_homework_result_raises_exception(good_student):
    with raises(NotAHomeworkError):
        HomeworkResult(good_student, 'fff', 'Solution')


def test_doing_expired_homework_raises_exception(good_student, expired_hw):
    with raises(DeadlineError):
        good_student.do_homework(expired_hw, 'I have tried')


def test_storing_only_unique_homework_solutions(opp_teacher, advanced_teacher,
                                                good_do_oop, oop_hw):
    opp_teacher.check_homework(good_do_oop)
    advanced_teacher.check_homework(good_do_oop)
    assert len(Teacher.homework_done[oop_hw]) == 1


def test_badly_solved_homeworks_are_not_stored(opp_teacher, good_do_docs,
                                               lazy_do_docs, docs_hw):
    opp_teacher.check_homework(good_do_docs)
    opp_teacher.check_homework(lazy_do_docs)
    assert len(Teacher.homework_done[docs_hw]) == 1


def test_reset_homework_done():
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0


def test_homework_done_teacher_inheritance(good_do_oop):

    class ProTeacher(Teacher):
        homework_done = defaultdict(set)

    pro_teacher = ProTeacher('Name', 'Surname')

    pro_teacher.check_homework(good_do_oop)
    assert len(Teacher.homework_done) == 0
    assert len(ProTeacher.homework_done) == 1
