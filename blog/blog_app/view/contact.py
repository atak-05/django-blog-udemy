from django.shortcuts import render, redirect
from blog_app.forms import ContactForm
from blog_app.models import ContactModel



def contact(request):
    form = ContactForm()
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactModel()
            contact.email = form.cleaned_data['email']
            contact.name_lastname = form.cleaned_data['name_lastname']
            contact.message = form.cleaned_data['message']
            contact.save()
            return redirect('home')
        else:
            print('not valid')    
        
    context = {
        'form': form 
    }
    return render (request,'pages/contact.html',context=context)