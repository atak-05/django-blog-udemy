from decimal import Clamped
import email
from email import message
from statistics import mode
from tabnanny import verbose
from django.db import models


class ContactModel(models.Model):
    email = models.EmailField(max_length=250)
    name_lastname=models.CharField(max_length=150)
    message = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    
    class  Meta:
        db_table = 'contact'
        verbose_name= 'contact'
        verbose_name_plural = 'contact'
        
    def __str__(self):
        return self.email    