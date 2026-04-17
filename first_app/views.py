from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello <a href="/about">World</a>')
def about(request):
    return HttpResponse('<h1> This is the About page!</h1>')