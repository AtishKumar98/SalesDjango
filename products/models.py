from email.policy import default
from django.db import models
from .models import *

# Create your models here.
class Product(models.Model):
    name  = models.CharField(max_length=100, blank=False)
    image  = models.ImageField(default='nopic.jpg')
    price  = models.FloatField(help_text='in INR ')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"