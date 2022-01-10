from django.db import models
from django.utils import timezone


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Homework(models.Model):
    text = models.CharField(max_length=30)
    deadline = models.DurationField()
    created = models.DateTimeField(default=timezone.now)


class HomeworkResult(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=30)
    created = models.DateTimeField(default=timezone.now)

# Create your models here.
