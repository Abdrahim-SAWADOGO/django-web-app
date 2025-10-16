from django.shortcuts import render
from django.http import HttpResponse
from .models import Band
from .models import Listing

def band(request):
    bands=Band.objects.all()
    return render(request, 'listings/band.html',
                  {'bands': bands})

def about(request):
    listings=Listing.objects.all()
    return render(request, 'listings/listings.html',
                  {'listings': listings})

def home(request):
    return render(request, 'listings/home.html')