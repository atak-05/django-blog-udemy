import email
from tkinter import Label
from django import forms
from blog_app.models import ContactModel
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ("name_lastname","email","message")
        
    def send_email(self, message):
        send_mail(
            subject='İleşitim Formundan yeni mesaj var!',
            message= message,
            recipient_list=['gizem.cirikka@outlook.com'],
            fail_silently=False,
            from_email=None,
            
        )
    
    