# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    response = {
        'names': ["Alice", "Bob", "Chap"]
    }
    return render(request, 'chat/index.html', response)
