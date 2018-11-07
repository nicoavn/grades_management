from django.http import HttpResponse
from django.shortcuts import render
from grades.models import *


# Create your views here.


def login_view(request):
    return render(request, 'login.html', {})


def grades_form(request):
    context = {
        'qualifications': Qualification.objects.all()
    }
    return render(request, 'grades_form.html', context)


def grades_submit(request):
    return None
