from django.contrib import admin
from grades.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(QualificationHeader)
admin.site.register(Qualification)
