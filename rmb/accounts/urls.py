from django.conf.urls import url
from django.contrib.auth.views import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registration/$', TemplateView.as_view(template_name='accounts/registration.html'), name='registration'),
    url(r'^authenticate$', views.authenticate, name='authenticate'),
    url(r'^register$', views.register, name='register'),
]
