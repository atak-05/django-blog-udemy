from dataclasses import field
from socket import fromshare
from statistics import mode
from django import forms
from blog_app.models import CommentModel

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment',)