from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    # login
    path("login/", login_view, name="login"),
    # logout
    path("logout", logout_view, name="logout"),
    # registration / signup
    path("signup", signup_view, name="signup"),
]
