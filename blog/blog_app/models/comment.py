from statistics import mode
from turtle import update
from venv import create
from django.db import models
from django.contrib.auth.models import User
from blog_app.models import TextModel


class CommentModel(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    text = models.ForeignKey(TextModel, on_delete=models.CASCADE, related_name ='comments')
    comment = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
            