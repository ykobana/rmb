from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'app/login.html'


def index(request):
    return HttpResponse("Hello, world.")