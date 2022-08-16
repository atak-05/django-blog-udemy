import email
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=False, max_length=100)
    name_lastname = forms.CharField(max_length=25)
    message = forms.CharField(widget = forms.Textarea)
    
    
    