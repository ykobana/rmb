from django.conf.urls import url
from . import views

app_name = 'show'

urlpatterns = [
    url(r'^profile', views.profile, name='profile'),
    # TODO: 下をリソースID指定にする
    url(r'^delete_character', views.delete_character, name='delete_character')
]