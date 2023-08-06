from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
]
