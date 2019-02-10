from django.conf.urls import url
from . import views
from django.urls import include

app_name = 'menu'

urlpatterns = [
    url(r'^main/$', views.main, name='menu'),
    url(r'^create', include('create.urls'), name='create'),
]
