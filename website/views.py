from django.shortcuts import render
from django.http import HttpResponse
from website.forms import NameForm
def index_view(request) :
    return render(request, 'website/index.html')

def about_view(request) :
    return render(request, 'website/about.html')

def contact_view(request) :
    if request.method == 'POST' :
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name, email, subject, message)

    
    return render(request, 'website/contact.html')

def elements(request) :
    return render(request, 'website/elements.html')

def signup(request) :
    return render(request, 'website/index1.html')

def dashboard(request) :
    return render(request, 'website/dashboard.html')



# Create your views here.
