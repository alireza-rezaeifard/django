
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name = 'home'),
    path('about', about_view, name = 'about'),
    path('contact', contact_view, name = 'contact'),
    path('elements', elements, name = 'elements'),
    path('signup', signup, name = 'signup'),
    path('dashboard/', dashboard, name='dash'),

]
