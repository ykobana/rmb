from django.conf.urls import url
from django.contrib.auth.views import TemplateView
from . import views
from django.urls import include

app_name = 'menu'
urlpatterns = [
    url('', views.main, name='menu'),
    url(r'^create', include('create.urls'), name='create'),
]
