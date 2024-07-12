from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Home")

def contato(request):
    return HttpResponse("Contato")

def my_view(request):
    return HttpResponse("Hello world")
