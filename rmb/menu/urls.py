from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'menu'
urlpatterns = [
    url('', views.main, name='menu'),
]
