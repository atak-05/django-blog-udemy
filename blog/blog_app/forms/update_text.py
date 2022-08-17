from socket import fromshare
from tkinter import E
from django import forms
from blog_app.models import TextModel

class UpdateTextForm(forms.ModelForm):
    
    class Meta:
        model = TextModel
        exclude = ('author','slug')