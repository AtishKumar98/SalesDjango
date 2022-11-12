
# from tkinter import CASCADE
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No Bio')
    avatar = models.ImageField(upload_to = 'avatars',default= 'NOPIC.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Profile of {self.user.username}"