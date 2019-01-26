# Create your views here.
from django.shortcuts import render


def index(request):
    response = {
        'names': ["Alice", "Bob", "Chap"]
    }
    return render(request, 'chat/index.html', response)
