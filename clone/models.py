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
    likes = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE,blank=True, null=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, blank = True, null=True)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

class Like(models.Model):
    like= models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_liked = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.like)

class Comment(models.Model):
    message= models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)

    def add_comment(self):
        self.save()

    class Meta:
        ordering = ['created_on']

    def get_post_comments(cls, image_id):
        comments = cls.objects.filter(image_id=image_id)
        return comments

    @classmethod
    def get_comments(cls):
        comments=cls.objects.all()
        return comments