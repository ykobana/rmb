# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the log index.")
