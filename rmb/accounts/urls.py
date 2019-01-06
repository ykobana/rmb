from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
#    path('', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^register/$', LoginView.as_view(template_name='accounts/register.html'), name='register'),
    url(r'^authenticate$', views.authenticate, name='authenticate'),
    url(r'^register$', views.register, name='register'),
]
