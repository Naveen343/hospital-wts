from django.urls import path
from . import views

app_name = 'visitors'

urlpatterns = [

    path('', views.index, name='index'),
    
    #path('create_appointment/', views.create_appointment, name='create_appointment'),
]
