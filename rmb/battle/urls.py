from django.urls import path

from . import views

app_name = 'battle'

urlpatterns = [
    path('', views.index, name='index'),
]