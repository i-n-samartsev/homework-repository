# Generated by Django 4.0.1 on 2022-01-10 19:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
                ('deadline', models.DurationField()),
                ('created', models.DateTimeField(default=django.utils.
                                                 timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('solution', models.CharField(max_length=30)),
                ('created', models.DateTimeField(default=django.utils.
                                                 timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.
                                             deletion.CASCADE,
                                             to='university.student')),
                ('homework', models.ForeignKey(on_delete=django.db.models.
                                               deletion.CASCADE,
                                               to='university.homework')),
            ],
        ),
    ]
