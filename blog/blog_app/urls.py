import imp
from unicodedata import name
from django.urls import path
from blog_app.view import contact
from blog_app.view import home,category

urlpatterns = [
    path('',home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name = 'category' )
]
