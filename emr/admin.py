from django.contrib import admin
from .models import Department, Employee, Patient, Appointment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'department', 'designation', ]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'age', 'gender', ]


@admin.register(Appointment)
class ApppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'visitor_name', 'date_time']

