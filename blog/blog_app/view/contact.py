from django.shortcuts import render, redirect
from blog_app.forms import ContactForm
from blog_app.models import ContactModel



def contact(request):
    form = ContactForm()
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('not valid')    
        
    context = {
        'form': form 
    }
    return render (request,'pages/contact.html',context=context)