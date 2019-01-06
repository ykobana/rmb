from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    url(r'^menu', views.main, name='menu'),
]
