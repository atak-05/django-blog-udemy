import imp
from django.urls import path
from blog_app.view import contact
from blog_app.view import home

urlpatterns = [
    path('',home, name='home'),
    path('contact/', contact, name='contact')
]
