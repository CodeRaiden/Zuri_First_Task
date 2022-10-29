# first we will import admin from the django.cotrib library
from django.contrib import admin
# then we will also import the Student class from the models.py file
from .models import Student

# then we register the different tables we want to show up in our admin panel
admin.site.register(Student)