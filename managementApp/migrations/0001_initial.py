# Generated by Django 3.1 on 2022-07-17 20:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50, verbose_name='First name')),
                ('lastName', models.CharField(max_length=50, verbose_name='Last name')),
                ('group', models.CharField(max_length=50, verbose_name='Group')),
                ('course', models.IntegerField(max_length=50, verbose_name='Course')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('queryDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Document title')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managementApp.student', verbose_name='student')),
            ],
        ),
    ]