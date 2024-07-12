from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Matheus Stelzner',
    })

def contato(request):
    return render(request, 'recipes/contato.html')

def my_view(request):
    return HttpResponse("Hello world")
