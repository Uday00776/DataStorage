from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='home'),
    path('employee/new/', views.create_employee, name='create_employee'),
    path('employees/', views.employee_list, name='employee_list'),
]
