from django.db import models

# Create your models here.

# Abstract Base Class Model inheritance
class ContaictInfo(models.Model):

    name = models.CharField(max_length = 64)
    email = models.EmailField()
    address = models.CharField(max_length = 256)

    class Meta:

        abstract = True

class Student(ContaictInfo):

    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContaictInfo):

    subject = models.CharField(max_length = 128)
    salary = models.FloatField()


# Multi-table inheritance
class ContaictInfo1(models.Model):

    name = models.CharField(max_length = 64)
    email = models.EmailField()
    address = models.CharField(max_length = 256)

class Student1(ContaictInfo1):

    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContaictInfo1):

    subject = models.CharField(max_length = 128)
    salary = models.FloatField()