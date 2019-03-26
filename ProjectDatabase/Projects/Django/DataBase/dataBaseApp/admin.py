from django.contrib import admin
from .models import Doctor, Patient, Test, Worker, Report, CashMemo
# Register your models here.


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'designation', 'address']
    lis_per_page = 20


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'test_price']
    list_editable = ['test_price']
    lis_per_page = 20


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_gender', 'patient_age',
                    'test_name', 'ref_by', 'address', 'speciman_type']
    list_editable = ['patient_gender', 'patient_age']
    list_filter = ['ref_by', 'test_name']
    list_per_page = 30


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'address']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'ref_by', 'tests', 'worker']
    list_filter = ['ref_by', 'worker']
    list_per_page = 30


@admin.register(CashMemo)
class CashMemoAdmin(admin.ModelAdmin):
    list_display = ['bill_no', 'patient']
