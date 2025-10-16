from django.shortcuts import render
from django.http import HttpResponse
from .models import Band

def hello(request):
    bands=Band.objects.all()
    return render(request, 'listings/hello.html')

def about(request):
    return HttpResponse("Hello, world. You're at the about index.")
