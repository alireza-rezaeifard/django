from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]