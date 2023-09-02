from django.shortcuts import render
from django.http import HttpResponse

def home_view(request) :
    return HttpResponse('<h1>this is a home page view</h1>')

def about_view(request) :
    return HttpResponse('<h1>this is a about page view</h1>')

def contact_view(request) :
    return HttpResponse('<h1>this is a contact page view</h1>')

# Create your views here.
