from django.shortcuts import render
from django.http import HttpResponse

def index_view(request) :
    return render(request, 'website/index.html')

def about_view(request) :
    return render(request, 'website/about.html')

def contact_view(request) :
    return render(request, 'website/contact.html')

def elements(request) :
    return render(request, 'website/elements.html')

def signup(request) :
    return render(request, 'website/index1.html')



# Create your views here.
