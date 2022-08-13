import imp
from django.urls import path
from blog_app.view import contact
from blog_app.view import home

urlpatterns = [
    path('',home),
    path('contact/', contact)
]
