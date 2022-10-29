from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student
# we will need to import JsonResponse from django.http
from django.http import JsonResponse
# and then we import jason also
import json

# create our view
def json(request):
    # here we add an attribute called data which will be a list of all the object values of the Student model
    data = list(Student.objects.values())
    # then we will return a json represntation of the data list by including the safe=false in the jsonResponse parameter so as not to risk an error.
    return JsonResponse(data, safe=False)