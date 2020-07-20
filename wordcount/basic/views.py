from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Hello world!')

def eggs(request):
    return HttpResponse('<h1>I like to eat eggs</h1>')
