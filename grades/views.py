from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def login_view(request):
    messages = {}
    if request.method =='POST':
        user_parameter = request.POST.get('user','')
        password_parameter = request.POST.get('password','')
        user = authenticate(username=user_parameter, password=password_parameter)
        if not user:
            messages['message'] = "Usuario y/o password incorrecto."


    return render(request, 'login.html', messages)





def grades_form(request):
    return render(request, 'grades_form.html', {})


def grades_submit(request):
    return None
