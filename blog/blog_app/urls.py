import imp
from unicodedata import name
from django.urls import path
from blog_app.view import contact
from blog_app.view import home, category, my_text, detail,add_text,update_text,delete_text

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('mytext/', my_text, name='mytext'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-text/', add_text, name='add_text'),
    path('update-text/<slug:slug>', update_text ,name='update_text'),
    path('delete-text/<slug:slug>', delete_text ,name='delete_text'),
]
