from django.conf.urls import url
from . import views
from django.urls import include

app_name = 'menu'

urlpatterns = [
    url(r'^main', views.main, name='main'),
    url(r'^create', include('create.urls'), name='create'),
    url(r'^chat_message', views.chat_message, name='chat_message'),
]
