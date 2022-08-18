from unicodedata import name
from django.urls import path
from account.forms import sign_in_user
from account.views import exit, changePassword,changeProfile, sign_In_User


urlpatterns = [ 
    path('exit', exit , name= 'exit'),
    path('change-password',changePassword, name='change_password' ),
    path('change-profile',changeProfile, name='change_profile' ),
    path('sign-in_user',sign_In_User, name='sign_in_user' ),
 ]
