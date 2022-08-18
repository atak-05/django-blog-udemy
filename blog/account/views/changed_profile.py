from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import changedProfileForm



@login_required(login_url='/')
def changeProfile(request):
    if request.method =='POST':
       form = changedProfileForm(request.POST, request.FILES, instance = request.user)
       if form.is_valid():
           form.save()
           messages.success(request,  'Your Profile changed with success!')
       
    else:
       form  = changedProfileForm(instance = request.user)

    return render (request, 'pages/change_profile.html', context={
        'form' : form
    })