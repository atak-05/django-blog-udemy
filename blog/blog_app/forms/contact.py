import email
from tkinter import Label
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=100)
    name_lastname = forms.CharField(label='Name Lastname' , max_length=25)
    message = forms.CharField(label = 'Message' ,widget = forms.Textarea)
    
    
    