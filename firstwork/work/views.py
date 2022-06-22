from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    st = Student.objects.all()
 
    return render(request, "home.html", {'student': st})

def registration(request):

    return render(request, "student_register.html")

def login(request):
    return render(request, 'login.html')