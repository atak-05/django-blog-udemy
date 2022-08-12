from distutils.command.upload import upload
from enum import unique
from statistics import mode
from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField
from blog_app.models import CategoryModel
from blog_app.abstract_models import DateAbstractModel

# ck editor import edilecek!


class TextModel(DateAbstractModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='text_image')
    context = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='text')
    author = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='text_author')

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        db_table = 'Text'

    def __str__(self):
        return self.title
