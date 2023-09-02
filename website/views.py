from django.shortcuts import render
from django.http import HttpResponse

def index_view(request) :
    return render(request, 'home_page/index.html')

def about_view(request) :
    return render(request, 'about_page/about.html')

def contact_view(request) :
    return render(request, 'contact_page/contact.html')

# Create your views here.
