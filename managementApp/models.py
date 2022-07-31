from django.db import models
from django.urls import reverse
from datetime import datetime

class Student(models.Model):
    firstName = models.CharField("First name", max_length=50)
    lastName = models.CharField("Last name", max_length=50)
    group = models.CharField("Group", max_length=50)
    course = models.IntegerField("Course", max_length=50)
    email = models.EmailField("E-mail", max_length=50)
    queryDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.firstName

class Document(models.Model):
    title = models.CharField("Document title", max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="student")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('documentDetail', args=[self.pk])
