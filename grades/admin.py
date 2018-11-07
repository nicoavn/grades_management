from django.contrib import admin
from grades.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(CourseConfiguration)
admin.site.register(StudentSubject)
# admin.site.register(QualificationHeader)
admin.site.register(Qualification)

