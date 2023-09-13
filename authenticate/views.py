from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard page
        return render(request, 'signup/signup.html', {'form': form})

