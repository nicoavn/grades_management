from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    order_number = models.IntegerField()


class Subject(models.Model):
    name = models.CharField(max_length=45)


class QualificationHeader(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    school_year = models.CharField(max_length=15)
    section = models.CharField(max_length=15)
    observation = models.CharField(max_length=15)

    final_situation_promoted = models.BooleanField()
    final_situation_promoted_with_pending = models.BooleanField()
    final_situation_promoted_with_reprobate = models.BooleanField()


class Qualification(models.Model):
    qualification_header = models.ForeignKey(QualificationHeader, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    p1_partial1 = models.CharField(max_length=15, null=True, blank=True)
    p1_partial2 = models.CharField(max_length=15, null=True, blank=True)
    p1_partial3 = models.CharField(max_length=15, null=True, blank=True)
    p1_partial4 = models.CharField(max_length=15, null=True, blank=True)
    p1_cf = models.CharField(max_length=15, null=True, blank=True)

    p1_aa_percent = models.CharField(max_length=15, null=True, blank=True)

    p2_pcp_percent = models.CharField(max_length=15, null=True, blank=True)
    p2_cpc = models.CharField(max_length=15, null=True, blank=True)
    p2_cpc_percent = models.CharField(max_length=15, null=True, blank=True)
    p2_cc = models.CharField(max_length=15, null=True, blank=True)

    p3_pcp_percent = models.CharField(max_length=15, null=True, blank=True)
    p3_cpex = models.CharField(max_length=15, null=True, blank=True)
    p3_cpex_percent = models.CharField(max_length=15, null=True, blank=True)
    p3_cex = models.CharField(max_length=15, null=True, blank=True)

    a = models.BooleanField()
    r = models.BooleanField()

    cap_1 = models.CharField(max_length=15, null=True, blank=True)
    cap_2 = models.CharField(max_length=15, null=True, blank=True)
