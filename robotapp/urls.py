from django.urls import path
from . import views

app_name = 'robotapp'

urlpatterns = [
    path('', views.index, name='index'),     
]