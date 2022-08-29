from django import forms
from blog_app.models import TextModel

class AddTextForm(forms.ModelForm):
    
    class Meta:
        model = TextModel
        exclude = ('author','slug')