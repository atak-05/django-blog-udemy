from re import template
from unicodedata import name
from django.urls import path
from account.forms import sign_in_user
from account.views import exit, changePassword,changeProfile, sign_In_User ,ProfileDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path("login", auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
        ), name="login"),           
    path('exit', exit , name= 'exit'),
    path('change-password',changePassword, name='change_password' ),
    path('change-profile',changeProfile, name='change_profile' ),
    path('sign-in_user',sign_In_User, name='sign_in_user' ),
    path('user/<str:username>', ProfileDetailView.as_view(), name='profil')
 ]
