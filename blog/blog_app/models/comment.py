from statistics import mode
from turtle import update
from venv import create
from django.db import models
from django.contrib.auth.models import User
from blog_app.models import TextModel
from blog_app.abstract_models import DateAbstractModel


class CommentModel(models.Model):
    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    text = models.ForeignKey(TextModel, on_delete=models.CASCADE, related_name ='comments')
    comment = models.TextField()
    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        return self.writer.username
            