from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

# Create your views here.
from grades.models import *


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
    student = Student.objects.get(pk=student_id)

    student_subjects = student.studentsubject_set.all()

    ss = StudentSubject()
    ss.qualification_set.first()

    context = {
        'student': student,
        'student_subjects': student_subjects,
        # 'qualifications': Qualification.objects.all(),
    }
    return render(request, 'grades_form.html', context)


def save_qualification(request, student_id):

    for key in request.POST:
        if key[0:16] == 'student-subject-':
            ss_index = int(key[16:])

            working_ss = StudentSubject.objects.get(pk=ss_index)
            working_qualification = working_ss.qualification_set.first()

            if working_qualification is None:
                working_qualification = Qualification()
                working_qualification.student_subject = working_ss

            working_qualification.p1_partial1 = request.POST.get('ss-' + str(ss_index) + '-AGO-SEPT-OCT', '')
            working_qualification.p1_partial2 = request.POST.get('ss-' + str(ss_index) + '-NOV-DIC-ENE', '')
            working_qualification.p1_partial3 = request.POST.get('ss-' + str(ss_index) + '-FEB-MAR', '')
            working_qualification.p1_partial4 = request.POST.get('ss-' + str(ss_index) + '-ABRIL-MAYO-JUNIO', '')
            working_qualification.p1_cf = request.POST.get('ss-' + str(ss_index) + '-C-F', '')
            working_qualification.p1_aa_percent = request.POST.get('ss-' + str(ss_index) + '-percent-A-A', '')
            working_qualification.p2_pcp_percent = request.POST.get('ss-' + str(ss_index) + '-50-percent-P-C-P', '')
            working_qualification.p2_cpc = request.POST.get('ss-' + str(ss_index) + '-C-P-C', '')
            working_qualification.p2_cpc_percent = request.POST.get('ss-' + str(ss_index) + '-50-percent-C-P-C', '')
            working_qualification.p2_cc = request.POST.get('ss-' + str(ss_index) + '-C-C', '')
            working_qualification.p3_pcp_percent = request.POST.get('ss-' + str(ss_index) + '-30-percent-P-C-P', '')
            working_qualification.p3_cpex = request.POST.get('ss-' + str(ss_index) + '-C-P-EX', '')
            working_qualification.p3_cpex_percent = request.POST.get('ss-' + str(ss_index) + '-70-percent-C-P-EX', '')
            working_qualification.p3_cex = request.POST.get('ss-' + str(ss_index) + '-C-EX', '')

            a_r = request.POST.get('ss-' + str(ss_index) + '-a-r', False)
            if a_r:
                working_qualification.a = True if a_r == 'a' else False
                working_qualification.r = True if a_r == 'r' else False

            working_qualification.cap_1 = request.POST.get('ss-' + str(ss_index) + '-C-A-P-1', '')
            working_qualification.cap_2 = request.POST.get('ss-' + str(ss_index) + '-C-A-P-2', '')

            working_qualification.save()

    return redirect("/student/" + str(student_id))


def report_qualification(request, student_id):
    student = Student.objects.get(pk=student_id)

    student_subjects = student.studentsubject_set.all()

    ss = StudentSubject()
    ss.qualification_set.first()

    context = {
        'student': student,
        'student_subjects': student_subjects,
        # 'qualifications': Qualification.objects.all(),
    }
    return render(request, 'qualification_report.html', context)
