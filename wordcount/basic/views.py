from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {"welcome":"Halo selamat datang di Depok"})

def eggs(request):
    return HttpResponse('<h1>I like to eat eggs</h1>')
