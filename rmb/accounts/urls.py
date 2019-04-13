from django.conf.urls import url
from django.contrib.auth.views import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registration/$', TemplateView.as_view(template_name='accounts/registration.html'), name='registration'),
    url(r'^auth$', views.auth, name='auth'),
    url(r'^register$', views.register, name='register'),
]
