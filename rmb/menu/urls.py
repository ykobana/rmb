from django.conf.urls import url
from . import views
from django.urls import include

app_name = 'menu'

urlpatterns = [
    url(r'^main', views.main, name='menu'),
    url(r'^create', include('create.urls'), name='create'),
    url(r'^get_chat_list', views.get_chat_list, name='get_chat_list'),
    url(r'^post_chat_message', views.post_chat_message, name='post_chat_message'),
]
