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
from collections import defaultdict
from datetime import datetime, timedelta


class NotAHomeworkError(ValueError):
    """Exception for invalid passed Homework object"""
    def __init__(self, message='You gave not a Homework object!'):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class DeadlineError(ValueError):
    """Exception for expired Homework"""

    def __init__(self, message='You are late!'):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class Homework:
    """
        Student's homework with text and deadline.
        Deadline - number of days to complete.
    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.today()

    def is_active(self) -> bool:
        """
            Checks that the homework is not expired.
        """
        return self.created + self.deadline > datetime.today()

    def __str__(self):
        return f'{self.text}'


class HomeworkResult:
    """
        Result of student's homework.
    """
    def __init__(self, author, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise NotAHomeworkError
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.today()

    def __str__(self):
        return f'{self.author} - {self.homework} - {self.solution}'


class Person:
    """Base class for people"""
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):

    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        if not homework.is_active():
            raise DeadlineError
        else:
            return HomeworkResult(self, homework, solution)


class Teacher(Person):
    """
        All inheritors should have class attribute:
        homework_done = defaultdict(set)
    """
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_res: HomeworkResult) -> bool:
        homework = homework_res.homework
        solution = homework_res.solution
        if len(solution) > 5:
            cls.homework_done[homework].add(solution)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None):
        if homework:
            cls.homework_done.pop(homework, None)
        else:
            cls.homework_done.clear()
