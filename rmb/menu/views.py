# Create your views here.
from django.shortcuts import render
#from django.http import HttpResponse


def main(request):
#    return HttpResponse("You're looking at question!!")
    return render(request, 'menu/menu.html', {})
