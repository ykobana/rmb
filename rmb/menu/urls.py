from django.conf.urls import url
from . import views
from django.urls import include

app_name = 'menu'

urlpatterns = [
    url(r'^main', views.main, name='main'),
    url(r'^character', include('character.urls'), name='character'),
    url(r'^chat_message', views.chat_message, name='chat_message'),
]
