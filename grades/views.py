from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from grades.models import Student


def login_view(request):
    messages = {}
    if request.method == 'POST':
        user_parameter = request.POST.get('user', '')
        password_parameter = request.POST.get('password', '')

        user = authenticate(username=user_parameter, password=password_parameter)
        if not user:
            messages['message'] = "Usuario y/o password incorrecto."
        else:
            login(request, user)
            return redirect('/students')

    return render(request, 'login.html', messages)


def logout_view(request):
    logout(request)
    return redirect("/")


def show_student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def grades_form(request, student_id):
    return render(request, 'grades_form.html', {})


def grades_submit(request):
    return None
