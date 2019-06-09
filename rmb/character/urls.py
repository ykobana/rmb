from . import views
from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import TemplateView

app_name = 'character'

urlpatterns = [
    url(r'^graffiti', TemplateView.as_view(template_name='character/graffiti.html'), name='graffiti'),
    url(r'^upload_graffiti', views.create, name='upload_graffiti'),
    path('<int:character_id>/delete/', views.delete, name='delete'),
]