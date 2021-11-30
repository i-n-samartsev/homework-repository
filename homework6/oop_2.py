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
    text = ""
    deadline = None
    created = None

    def __init__(self, text, num_of_days):
        self.text = text
        self.deadline = datetime.timedelta(num_of_days)
        self.created = datetime.date.today()

    def is_active(self):
        if self.created + self.deadline < datetime.date.today():
            return False
        else:
            return True


class HomeworkResult:
    homework = None
    solution = ""
    author = None
    created = None

    def __init__(self, homework, solution, author):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")

        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.date.today()


class Person:
    last_name = ""
    first_name = ""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):

    def do_homework(self, homework: Homework, solution):
        if homework.created + homework.deadline > datetime.date.today():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError("You are late")


class Teacher(Person):
    homework_done = defaultdict(HomeworkResult)

    @staticmethod
    def create_homework(text, num_of_days):
        return Homework(text, num_of_days)

    @staticmethod
    def check_homework(homework_result):
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework] = homework_result
            return True
        else:
            return False

    @staticmethod
    def reset_results(homework=None):
        if homework:
            Teacher.homework_done.pop(homework)
        else:
            Teacher.homework_done.clear()
