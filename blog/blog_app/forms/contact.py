import email
from tkinter import Label
from django import forms
from blog_app.models import ContactModel
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ("name_lastname","email","message")


    
    