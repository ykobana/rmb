from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'
urlpatterns = [
#    path('', views.index, name='login'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^registration/$', LoginView.as_view(template_name='accounts/registration.html'), name='registration'),
    url(r'^authenticate$', views.authenticate, name='authenticate'),
    url(r'^register$', views.register, name='register'),
]
