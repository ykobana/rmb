from . import views
from django.conf.urls import url
from django.contrib.auth.views import TemplateView

app_name = 'create'

urlpatterns = [
    url(r'^graffiti', TemplateView.as_view(template_name='create/graffiti.html'), name='graffiti'),
    url(r'^upload_graffiti', views.upload_graffiti, name='upload_graffiti'),
]