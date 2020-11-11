from django import forms
from django.forms import ModelForm
from .models import Patient, Appointment
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'username-field', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'password-field', 'placeholder': 'Password'}))


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentForm(ModelForm):
    date_time = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )

    class Meta:
        model = Appointment
        fields = ['visitor_name', 'description', 'date_time', ]
