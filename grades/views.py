from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request,'login.html',{})


def grades_form(request):
    return None


def grades_submit(request):
    return None
