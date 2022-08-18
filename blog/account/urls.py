from unicodedata import name
from django.urls import path
from account.views import exit, changePassword,changeProfile



urlpatterns = [ 
    path('exit', exit , name= 'exit'),
    path('change-password',changePassword, name='change_password' ),
    path('change-profile',changeProfile, name='change_profile' ),
               ]
