from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100,blank=False)
    logo = models.ImageField(max_length=100,blank=False)
    def __str__(self):
        return f"Name: {self.name}"