from distutils.command.upload import upload
from enum import unique
from statistics import mode
from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField
from blog_app.models import CategoryModel
from django.contrib.auth.models import User

#ck editor import edilecek!
class TextModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to= 'text_image')
    context = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from= 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='text')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='text_author')
    
    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        db_table = 'Text'  

    def __str__(self):
        return self.title
        
        