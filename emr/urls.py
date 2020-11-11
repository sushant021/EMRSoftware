from django.urls import path, include
from emr import views

urlpatterns = [
    path('home/', views.home, name='home'),

    # authentication
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # patient_crud
    path('patients/', views.list_patients, name='list_patients'),
    path('search-patient/', views.search_patients, name='search_patient'),
    path('patient/add/', views.add_patient, name='add_patient'),
    path('patient/<int:id>/', views.view_patient, name='view_patient'),
    path('patient/delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('patient/update/<int:id>/', views.update_patient, name='update_patient'),

    # appointment_crud
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointment/add/', views.add_appointment, name='add_appointment'),
    path('appointment/<int:id>/', views.view_appointment, name='view_appointment'),
    path('appointment/delete/<int:id>/',
         views.delete_appointment, name='delete_appointment'),
    path('appointment/update/<int:id>/',
         views.update_appointment, name='update_appointment'),






]
