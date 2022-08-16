import imp
from unicodedata import name
from django.urls import path
from blog_app.view import contact
from blog_app.view import home, category, my_text, detail

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('mytext/', my_text, name='mytext'),
    path('detail/<slug:slug>', detail, name='detail'),
]
