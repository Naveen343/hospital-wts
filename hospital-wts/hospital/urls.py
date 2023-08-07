from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    path('appointments/', views.appointments_list, name='appointments_list'),
]
