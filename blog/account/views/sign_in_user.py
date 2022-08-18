from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import signinUser
from django.contrib.auth import login, authenticate


def sign_In_User(request):
    if request.method =='POST':
        form = signinUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
       
    else:
       form = signinUser()

    return render (request, 'pages/sign_in_user.html', context={
        'form' : form
    })