from django.db import models
from django.urls import reverse
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=254)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='employees')
    designation = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(auto_now_add=True, blank=True)
    address = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    contact_number = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse('view_employee', args=[self.id])


class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    full_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, blank=True)
    contact = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(blank=True)
    medical_history = models.TextField(blank=True)
    initial_diagnosis = models.TextField(blank=True)
    updated_diagnosis = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('view_patient', args=[self.id])


class Month(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, default='November')

    def __str__(self):
        return self.name


class Day(models.Model):
    number = models.IntegerField()
    month = models.ForeignKey(
        Month, on_delete=models.CASCADE, related_name='days', default=11)

    def __str__(self):
        return "%d %s" % (self.number, self.month)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    visitor_name = models.CharField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.visitor_name

    def get_absolute_url(self):
        return reverse('view_appointment', args=[self.id])
