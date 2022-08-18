from unicodedata import name
from django.urls import path
from account.views import exit, changePassword



urlpatterns = [ 
    path('exit', exit , name= 'exit'),
    path('change-password',changePassword, name='change_password' ),
               ]
