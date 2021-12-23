"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text, num_of_days):
        self.text = text
        self.deadline = datetime.timedelta(num_of_days)
        self.created = datetime.datetime.now()

    def is_active(self):
        """
            Checking a job for expiration.
            :rtype: bool
        """
        if self.created + self.deadline < datetime.datetime.now():
            return False
        else:
            return True


class HomeworkResult:
    def __init__(self, homework, solution, author):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")

        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()
        self.grade = 0


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    def do_homework(self, homework, solution):
        """
            Creates and returns a new HomeworkResult instance
            that will hold the Homework instance
            and solution specified when created.

            :param homework: Issued homework
            :type homework: Homework
            :param solution: Homework solution
            :type solution: str
            :rtype: HomeworkResult
        """
        if homework.created + homework.deadline > datetime.datetime.now():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError("You are late")

    def homework_request(self, homework_done, grade=5):
        """
            Return all instances of Homework that have
            a grade of grade and are authored by this student.

            :param homework_done: Dictionary of proven homework
            :type homework_done: defaultdict
            :param grade: Assessment with which we are looking for homework
            :type grade: int
            :rtype: List[Homework]
        """
        return [
            hw_result
            for hw_result in homework_done.values()
            if hw_result.author == self and hw_result.grade == grade
        ]


class Teacher(Person):
    homework_done = defaultdict(HomeworkResult)

    @staticmethod
    def create_homework(text, num_of_days):
        """
            Creates and return new Homework instance that will
            expire according to number of days specified when creating.

            :param text: Task text
            :type text: str
            :param num_of_days: Number of days to complete
            :type num_of_days: int
            :rtype: Homework
        """
        return Homework(text, num_of_days)

    @staticmethod
    def check_homework(homework_done, homework_result, grade=5):
        """
            Checking homework and returning the check result.

            :param homework_done: Dictionary of proven homework
            :type homework_done: defaultdict
            :param homework_result: Completed homework
            :type homework_result: HomeworkResult
            :param grade: The grade we give for homework
            :type grade: int
            :rtype: bool
        """
        if len(homework_result.solution) > 5:
            homework_result.grade = grade
            homework_done[homework_result.homework] = homework_result
            return True
        else:
            return False

    @staticmethod
    def reset_results(homework_done, homework=None):
        """
            Removing a checked homework.

            :param homework_done: Dictionary of proven homework
            :type homework_done: defaultdict
            :param homework: Issued homework
            :type homework: Homework
        """
        if homework:
            homework_done.pop(homework)
        else:
            homework_done.clear()
