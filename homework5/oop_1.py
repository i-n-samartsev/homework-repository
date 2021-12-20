"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
import random


class Homework:
    def __init__(self, text, num_of_days, help_from_teacher=0):
        self.text = text
        self.deadline = datetime.timedelta(num_of_days)
        self.created = datetime.datetime.now()
        self.help_from_teacher = help_from_teacher

    def is_active(self):
        return self.created + self.deadline > datetime.date.today()


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework, help_from_teacher=1, teach_help=False):
        """Chance of passing without the help of a teacher 90 percent"""
        if homework.created + homework.deadline <= datetime.datetime.now():
            print("You are late")
            return None
        elif teach_help or random.random() < 0.9:
            homework.help_from_teacher = help_from_teacher
            return homework
        else:
            print("You didn't pass")
            return None


class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, num_of_days):
        return Homework(text, num_of_days)
