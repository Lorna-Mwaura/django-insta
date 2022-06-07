from tkinter import CASCADE
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    caption =  models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name = 'created_at', on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ForeignKey(User, related_name='liked_by', on_delete=CASCADE,blank=True, null=True)
    comments = models.ForeignKey('Comment', on_delete=CASCADE, blank = True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField()