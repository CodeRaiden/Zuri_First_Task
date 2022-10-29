from unittest.util import _MAX_LENGTH
from django.db import models

# our student class will inherit from the models.Model base class
class Student(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=1000)